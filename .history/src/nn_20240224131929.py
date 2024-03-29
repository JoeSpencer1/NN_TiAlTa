from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import itertools

import numpy as np
from sklearn.svm import SVR
from sklearn.model_selection import KFold, LeaveOneOut, RepeatedKFold, ShuffleSplit

import deepxde as dde
from data import BerkovichData, FEMData, ExpDataT, ExpData, Data1, FEMData0, FEMDataC, BerkovichDataC, ExpDataC, FEMData2, BerkovichData2, ExpData2, FileData
import tensorflow as tf
tf.config.run_functions_eagerly(False)
import os
import multiprocessing
#dde.backend.tf.Session()

global apeG, yG

def svm(data):
    clf = SVR(kernel="rbf")
    clf.fit(data.train_x, data.train_y[:, 0])
    y_pred = clf.predict(data.test_x)[:, None]
    return dde.metrics.get("MAPE")(data.test_y, y_pred)


def mfgp(data):
    from mfgp import LinearMFGP

    model = LinearMFGP(noise=0, n_optimization_restarts=5)
    model.train(data.X_lo_train, data.y_lo_train, data.X_hi_train, data.y_hi_train)
    _, _, y_pred, _ = model.predict(data.X_hi_test)
    return dde.metrics.get("MAPE")(data.y_hi_test, y_pred)


def nn(data, lay=2, wid=32):
    layer_size = [data.train_x.shape[1]] + [wid] * lay + [1]
    activation = "selu"
    initializer = "LeCun normal"
    regularization = ["l2", 0.01]

    loss = "MAPE"
    optimizer = "adam"
    if data.train_x.shape[1] == 3:
        lr = 0.0001
    else:
        lr = 0.001
    epochs = 30000
    net = dde.maps.FNN(
        layer_size, activation, initializer, regularization=regularization
    )
    model = dde.Model(data, net)
    model.compile(optimizer, lr=lr, loss=loss, metrics=["MAPE"])
    losshistory, train_state = model.train(epochs=epochs)
    dde.saveplot(losshistory, train_state, issave=True, isplot=False)
    return train_state.best_metrics[0]

def mfnn(data, lay=2, wid=128):
    x_dim, y_dim = 3, 1
    activation = "selu"
    initializer = "LeCun normal"
    regularization = ["l2", 0.01]
    net = dde.maps.MfNN(
        [x_dim] + [wid] * lay + [y_dim],
        [8] * lay + [y_dim],
        activation,
        initializer,
        regularization=regularization,
        residue=True,
        trainable_low_fidelity=True,
        trainable_high_fidelity=True,
    )

    model = dde.Model(data, net)
    model.compile("adam", lr=0.0001, loss="MAPE", metrics=["MAPE", "APE SD"])
    # Set weight of high-fidelity and low-fidelity data to 50%
    model.set_weights = [0.5, 0.5]
    losshistory, train_state = model.train(epochs=30000)

    dde.saveplot(losshistory, train_state, issave=True, isplot=False)
    return (
        train_state.best_metrics[1],
        train_state.best_metrics[3],
        train_state.best_y[1],
    )

def validation_one(yname, filename, testname, train_size):
    datatrain = FileData(filename, yname)
    datatest = FileData(testname, yname)
    
    if filename == testname:
        if train_size == 80:
            kf = RepeatedKFold(n_splits=5, n_repeats=2, random_state=0)
        elif train_size == 90:
            kf = KFold(n_splits=10, shuffle=True, random_state=0)
        else:
            kf = ShuffleSplit(
                n_splits=10, test_size=len(datatrain.X) - train_size, random_state=0
            )
        train_set = kf.split(datatrain.X)
    else:
        if len(datatrain.y) > len(datatest.y):
            kf = ShuffleSplit(
                n_splits=10, test_size=len(datatest.X) - train_size, random_state=0
            )
            train_set = kf.split(datatrain.X)
        else:
            kf = ShuffleSplit(
                n_splits=10, test_size=len(datatrain.X) - train_size, random_state=0
            )
            train_set = kf.split(datatest.X)
    
    mape = []
    iter = 0
    for train_index, test_index in train_set:
        iter += 1
        print("\nCross-validation iteration: {}".format(iter))

        if filename == testname:
            X_train, X_test = datatrain.X[train_index], datatrain.X[test_index]
            y_train, y_test = datatrain.y[train_index], datatrain.y[test_index]
        else:
            l_1 = len(datatest.y)
            l_2 = len(datatrain.y)
            if l_1 < l_2:
                t_i = test_index
                test_index = (t_i * l_1 / l_2).astype(int)
            else:
                t_i = train_index
                train_index = (t_i * l_2 / l_1).astype(int)
            X_train, X_test = datatrain.X[train_index], datatest.X[test_index]
            y_train, y_test = datatrain.y[train_index], datatest.y[test_index]

        data = dde.data.DataSet(
            #X_train=X_train, y_train=y_train, X_test=X_test, y_test=y_test
            X_train=X_train, y_train=y_train, X_test=X_test, y_test=y_test, standardize=True
        )

        mape.append(dde.utils.apply(nn, (data,)))

    print(mape)
    print(yname, train_size, np.mean(mape), np.std(mape))
    with open('output.txt', 'a') as f:
        f.write('validation_one ' + yname + ' ' + str(train_size) + ' ' + str(np.mean(mape)) + ' ' + str(np.std(mape)) +' ' + testname + ' ' + filename + '\n')

def validation_two(yname, train_size, dlow, dhigh, dexp):
    datalow = FileData(dlow, yname)
    datahigh = FileData(dhigh, yname)
    dataexp = FileData(dexp, yname)

    mape = []
    iter = 0

    kf = ShuffleSplit(
        n_splits=10, test_size=len(datahigh.X) - train_size, random_state=0
        #n_splits=10, train_size=train_size, random_state=0
    )

    if train_size == 0:
        for train_index, test_index in kf.split(datalow.X):
            data = dde.data.DataSet(
                X_train=datalow.X, y_train=datalow.y, X_test=dataexp.X, y_test=dataexp.y, standardize=True
            )
            mape.append(dde.utils.apply(nn, (data,)))

    else:
        for train_index, test_index in kf.split(datahigh.X):
            iter += 1
            print("\nCross-validation iteration: {}".format(iter), flush=True)

            data = dde.data.MfDataSet(
                X_lo_train=datalow.X,
                X_hi_train=datahigh.X[train_index],
                y_lo_train=datalow.y,
                y_hi_train=datahigh.y[train_index],
                X_hi_test=dataexp.X[test_index],
                y_hi_test=dataexp.y[test_index],
                standardize=True
            )
            mape.append(dde.utils.apply(mfnn, (data,))[0])
            #mape.append(dde.utils.apply(mfgp, (data,)))

    with open('Output.txt', 'a') as f:
        f.write("validation_two " + yname + ' ' + dlow + ' ' + dhigh + ' ' + dexp + ' ' + str(train_size) + ' ' + str(np.mean(mape, axis=0)) + ' ' + str(np.std(mape, axis=0)) + '\n')
    print(mape)
    print(yname, "validation_two ", dlow, ' ', dhigh, ' ', train_size, ' ', np.mean(mape), np.std(mape))

def validation_three(yname, train_size, datalo, datahi, data1, data2):
    '''
    datalow = FEMData2(yname, [70])
    dataBerkovich = BerkovichData2(yname)
    if data1 == "B30901":
        dataexp1 = ExpData2("../data/B30901.csv", yname)
    if data2 == "B30901":
        dataexp2 = ExpData2("../data/B30901.csv", yname)
    '''
    datalow = FileData(datalo, yname)
    dataBerkovich = FileData(datahi, yname)
    dataexp1 = FileData(data1, yname)
    dataexp2 = FileData(data2, yname)

    ape = []
    y = []

    if train_size == 0:
        for iter in range(10):
            print("\nIteration: {}".format(iter))
            data = dde.data.MfDataSet(
                X_lo_train=datalow.X,
                X_hi_train=dataBerkovich.X,
                y_lo_train=datalow.y,
                y_hi_train=dataBerkovich.y,
                X_hi_test=dataexp2.X,
                y_hi_test=dataexp2.y,
                standardize=True
            )
            res = dde.utils.apply(mfnn, (data,))
            ape.append(res[:2])
            y.append(res[2])
    else:
        kf = ShuffleSplit(n_splits=10, train_size=train_size, random_state=0)
        for train_index, _ in kf.split(dataexp1.X):
            print("\nIteration: {}".format(len(ape)))
            print(train_index)
            data = dde.data.MfDataSet(
                X_lo_train=datalow.X,
                X_hi_train=np.vstack((dataBerkovich.X, dataexp1.X[train_index])),
                y_lo_train=datalow.y,
                y_hi_train=np.vstack((dataBerkovich.y, dataexp1.y[train_index])),
                X_hi_test=dataexp2.X,
                y_hi_test=dataexp2.y,
                standardize=True
            )
            res = dde.utils.apply(mfnn, (data,))
            ape.append(res[:2])
            y.append(res[2])

    print(yname, "validation_exp_cross2", train_size, np.mean(ape, axis=0), np.std(ape, axis=0))
    with open('output.txt', 'a') as f:
        f.write("validation_three " + data1 + " " + datalo + " " + datahi + " " + data2 + " " + yname + " " + str(train_size) + str(np.mean(ape, axis=0)[0]) + " " + str(np.std(ape, axis=0)[0]) + '\n')
    print("Saved to ", yname, ".dat.")
    np.savetxt(yname + ".dat", np.hstack(y).T)  

def main(argument=None):
    if argument != None:
        exec(argument)
    return

if __name__ == "__main__":
    main()