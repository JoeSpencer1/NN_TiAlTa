from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import itertools

import numpy as np
from sklearn.svm import SVR
from sklearn.model_selection import KFold, LeaveOneOut, RepeatedKFold, ShuffleSplit

import deepxde as dde
from data import FileData
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

def t2s(names):
    if type(names) is str:
        return names
    else:
        return '[' + ','.join(names) + ']'

def nn(data, lay, wid):
    #lay, wid = 2, 32
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

def mfnn(data, lay, wid, wei):
    #lay, wid = 2, 128
    #wei = 0.5
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
    model.set_weights = [1 - wei, wei]
    losshistory, train_state = model.train(epochs=30000)

    dde.saveplot(losshistory, train_state, issave=True, isplot=False)
    return (
        train_state.best_metrics[1],
        train_state.best_metrics[3],
        train_state.best_y[1],
    )

def validation_one(yname, train_size, testname, trainname, lay=2, wid=32):
    datatrain = FileData(trainname, yname)
    datatest = FileData(testname, yname)
    
    kf = ShuffleSplit(
        n_splits=10, train_size=train_size, random_state=0
    )
    train_set = kf.split(datatrain.X)
    
    mape = []
    iter = 0
    for train_index, test_index in train_set:
        iter += 1
        print("\nCross-validation iteration: {}".format(iter))
        if trainname == testname:
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
            X_train=X_train, y_train=y_train, X_test=X_test, y_test=y_test, standardize=True
        )

        mape.append(dde.utils.apply(nn, (data,lay,wid,)))

    print(mape)
    print(yname, train_size, np.mean(mape), np.std(mape))
    with open('output.txt', 'a') as f:
        f.write('validation_one ' + yname + ' ' + str(train_size) + ' ' + str(np.mean(mape)) + ' ' + str(np.std(mape)) + ' ' + t2s(testname) + ' ' + t2s(trainname) + '\n')

def validation_two(yname, train_size, testname, trainhigh, trainlow, lay=2, wid=128, wei=0.5):
    datalow = FileData(trainlow, yname)
    datahigh = FileData(trainhigh, yname)
    datatest = FileData(testname, yname)

    mape = []
    iter = 0

    kf = ShuffleSplit(
        n_splits=10, train_size=train_size, random_state=0
    )

    if train_size == 0:
        for train_index, test_index in kf.split(datatest.X):
            data = dde.data.DataSet(
                X_train=datalow.X, y_train=datalow.y, X_test=datatest.X, y_test=datatest.y, standardize=True
            )
            mape.append(dde.utils.apply(nn, (data,lay,wid)))

    else:
        for train_index, test_index in kf.split(datahigh.X):
            iter += 1
            print("\nIteration: {}".format(iter), flush=True)
            train_index = train_index % len(datahigh.X)
            test_index = test_index % len(datatest.X)

            data = dde.data.MfDataSet(
                X_lo_train=datalow.X,
                X_hi_train=datahigh.X[train_index],
                y_lo_train=datalow.y,
                y_hi_train=datahigh.y[train_index],
                X_hi_test=datatest.X[test_index],
                y_hi_test=datatest.y[test_index],
                standardize=True
            )
            mape.append(dde.utils.apply(mfnn, (data,lay,wid,wei,))[0])

    with open('Output.txt', 'a') as f:
        f.write('validation_two ' + yname + ' ' + str(train_size) + ' ' + str(np.mean(mape, axis=0)) + ' ' + str(np.std(mape, axis=0)) + ' ' + t2s(testname) + ' ' + t2s(trainhigh) + ' ' + t2s(trainlow) + '\n')
    print(mape)
    print(yname, "validation_two ", t2s(trainlow), ' ', t2s(trainhigh), ' ', train_size, ' ', np.mean(mape), np.std(mape))

def validation_three(yname, train_size, testname, trainexp, trainhigh, trainlow, lay=2, wid=128, wei=0.5):
    datalow = FileData(trainlow, yname)
    datahigh = FileData(trainhigh, yname)
    dataexp = FileData(trainexp, yname)
    datatest = FileData(testname, yname)

    ape = []
    y = []

    if train_size == 0:
        for iter in range(10):
            print("\nIteration: {}".format(iter))
            data = dde.data.MfDataSet(
                X_lo_train=datalow.X,
                X_hi_train=datahigh.X,
                y_lo_train=datalow.y,
                y_hi_train=datahigh.y,
                X_hi_test=datatest.X,
                y_hi_test=datatest.y,
                standardize=True
            )
            res = dde.utils.apply(mfnn, (data,lay,wid,wei,))
            ape.append(res[:2])
            y.append(res[2])
    else:
        kf = ShuffleSplit(n_splits=10, train_size=train_size, random_state=0)
        for train_index, _ in kf.split(dataexp.X):
            print("\nIteration: {}".format(len(ape)))
            data = dde.data.MfDataSet(
                X_lo_train=datalow.X,
                X_hi_train=np.vstack((datahigh.X, dataexp.X[train_index])),
                y_lo_train=datalow.y,
                y_hi_train=np.vstack((datahigh.y, dataexp.y[train_index])),
                X_hi_test=datatest.X,
                y_hi_test=datatest.y,
                standardize=True
            )
            res = dde.utils.apply(mfnn, (data,lay,wid,wei,))
            ape.append(res[:2])
            y.append(res[2])

    print(yname, "validation_exp_cross2", train_size, np.mean(ape, axis=0), np.std(ape, axis=0))
    with open('output.txt', 'a') as f:
        f.write('validation_three ' + yname + ' ' + str(train_size) + ' ' + str(np.mean(ape, axis=0)[0]) + ' ' + str(np.std(ape, axis=0)[0]) + ' ' + t2s(testname) + ' ' + t2s(trainexp) + ' ' + t2s(trainhigh) + ' ' + t2s(trainlow) + '\n')
    print("Saved to ", yname, ".dat.")
    np.savetxt(yname + ".dat", np.hstack(y).T)  

def main(argument=None):
    if argument != None:
        exec(argument)
    return

if __name__ == "__main__":
    main()