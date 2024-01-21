from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import itertools

import numpy as np
from sklearn.svm import SVR
from sklearn.model_selection import KFold, LeaveOneOut, RepeatedKFold, ShuffleSplit

import deepxde as dde
from data import BerkovichDataT, ExpDataT, FEMDataT, ModelData
import tensorflow as tf
tf.config.run_functions_eagerly(False)
from tensorflow.keras import layers, models
import os

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


def nn(data, lay=9, wid=32):
    layer_size = [data.train_x.shape[1]] + [wid] * lay + [1]
    activation = "selu"
    initializer = "LeCun normal"
    regularization = ["l2", 0.01]

    loss = "MAPE"
    optimizer = "adam"
    if data.train_x.shape[1] == 4:
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

'''
This attempt to reproduce the nn in tensorflow does not quite produce the correct results yet.
'''
def nntf(data, lay=9, wid=32):
    model = models.Sequential()
    model.add(layers.InputLayer(input_shape=(data.train_x.shape[1],)))
    for _ in range(lay):
        model.add(layers.Dense(wid, activation='selu', kernel_initializer='lecun_normal', kernel_regularizer=tf.keras.regularizers.l2(0.01)))
    model.add(layers.Dense(1))
    model.compile(optimizer='adam', loss='mean_absolute_percentage_error', metrics=['mae'])
    history = model.fit(data.train_x, data.train_y, epochs=30000, verbose=1)
    mape = model.evaluate(data.test_x, data.test_y, verbose=0)[1]
    return mape

def mfnn(data, lay = 2):
    x_dim, y_dim = 4, 1
    activation = "selu"
    initializer = "LeCun normal"
    regularization = ["l2", 0.01]
    net = dde.maps.MfNN(
        [x_dim] + [128] * lay + [y_dim],
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
    losshistory, train_state = model.train(epochs=30000)

    dde.saveplot(losshistory, train_state, issave=True, isplot=False)
    return (
        train_state.best_metrics[1],
        train_state.best_metrics[3],
        train_state.best_y[1],
    )

def validation_one(yname, trnames, tstname, type, train_size, lay=9, wid=32, angles=[]):
    
    data = []
    if type == 'FEM':
        data = FEMDataT(yname, angles)
    if type == 'Berk':
        data = BerkovichDataT(yname)
    if type == 'Exp':
        data = ExpDataT(trnames[0], yname)
    print(data)
    tdata = ExpDataT(tstname, yname)
    mape = []

    for i in range(0, len(trnames)):
        if train_size[i] == 80:
            kf = RepeatedKFold(n_splits=5, n_repeats=2, random_state=0)
        elif train_size[i] == 90:
            kf = KFold(n_splits=10, shuffle=True, random_state=0)
        else:
            kf = ShuffleSplit(
                n_splits=10, test_size=len(data.X) - train_size[i], random_state=0
            )

        iter = 0
        for train_index, test_index in kf.split(data.X):
            iter += 1
            print('\nCross-validation iteration: {}'.format(iter))

            print(data.X)
            X_train, X_test = data.X[train_index], tdata.X[test_index]
            y_train, y_test = data.y[train_index], tdata.y[test_index]

            data1 = dde.data.DataSet(
                X_train=X_train, y_train=y_train, X_test=X_test, y_test=y_test
            )

            mape.append(dde.utils.apply(nn, (data1, lay, wid, )))
            #mape.append(dde.utils.apply(nntf, (data1, lay, wid, )))

    stsize = ''
    for digit in train_size:
        stsize += str(digit) + ' '
    print(mape)
    print(yname, 'validation_one ', trnames, ' ', tstname, ' ', str(train_size), ' ', np.mean(mape), ' ', np.std(mape))
    with open('Output.txt', 'a') as f:
        f.write('validation_one [' + ' '.join(map(str, trnames)) + '] ' +  tstname + ' ' + yname + ' ' + str(lay) + ' ' + str(wid) + ' [' + stsize + '] ' + str(np.mean(mape, axis=0)) + ' ' + str(np.std(mape, axis=0)) + '\n')

def validation_two(yname, tsize_1, tsize_2, train1_name, train2_name, test_name):
    data_test = ExpDataT('../data/TI33_' + test_name + '.csv')
    data_train1 = FEMDataT('../data/TI33_' + train1_name + '.csv')

    ape = []
    y = []
    kf = ShuffleSplit(n_splits=10, train_size=tsize_1, random_state=0)
    for train_index, _ in kf.split(data_train1.X)

def validation_joe(yname, tsize_1, tsize_2, train1_name, train2_name, test_name):
    
    dataFEM = FEMData(yname, [70])
    dataBerkovich = BerkovichData(yname)
    data_train1 = ExpData('../data/' + train1_name + '.csv', yname)
    data_train2 = ExpData('../data/' + train2_name + '.csv', yname)
    data_test = ExpData('../data/' + test_name + '.csv', yname)
    
    ape = []
    y = []
    
    kf = ShuffleSplit(n_splits=10, train_size=tsize_1, random_state=0)
    
    if tsize_1 > 0:
        for train_index, _ in kf.split(data_train1.X):
            print("\nIteration: {}".format(len(ape)))
            print(train_index)
            data = dde.data.MfDataSet(
                X_lo_train=dataFEM.X,
                X_hi_train=np.vstack((dataBerkovich.X, data_train1.X[train_index])),
                y_lo_train=dataFEM.y,
                y_hi_train=np.vstack((dataBerkovich.y, data_train1.y[train_index])),
                X_hi_test=data_test.X,
                y_hi_test=data_test.y,
                standardize=True
            )
            res = dde.utils.apply(mfnn, (data,))
            ape.append(res[:2])
            y.append(res[2])
    else:
        for train_index in range(10):
            print("\nIteration: {}".format(train_index))
            print(train_index)
            data = dde.data.MfDataSet(
                X_lo_train=dataFEM.X,
                X_hi_train=dataBerkovich.X,
                y_lo_train=dataFEM.y,
                y_hi_train=dataBerkovich.y,
                X_hi_test=data_test.X,
                y_hi_test=data_test.y,
                standardize=True
            )
            res = dde.utils.apply(mfnn, (data,))
            ape.append(res[:2])
            y.append(res[2])
 
    num = 5
    y_res = [res[0]]
    y_data = np.vstack((dataBerkovich.y, data_train1.y[train_index]))
    X_data = np.vstack((dataBerkovich.X, data_train1.X[train_index]))
    find_index = np.argmax(y_data > y_res)
    X_res = X_data[find_index]
    y_res = np.repeat([y_res], num, axis = 0)
    X_res = np.repeat([X_res], num, axis = 0)

    kf = ShuffleSplit(n_splits=10, train_size=tsize_2, random_state=0)

    if tsize_2 > 0:
        for train_index, _ in kf.split(data_train2.X):
            print("\nIteration: {}".format(len(ape)))
            print(train_index)
            data = dde.data.MfDataSet(
                X_lo_train=dataBerkovich.X,
                X_hi_train=np.vstack((X_res, data_train2.X[train_index])),
                y_lo_train=dataBerkovich.y,
                y_hi_train=np.vstack((y_res, data_train2.y[train_index])),
                X_hi_test=data_test.X,
                y_hi_test=data_test.y,
                standardize=True
            )
            res = dde.utils.apply(mfnn, (data,))
            ape.append(res[:2])
            y.append(res[2])
    else:
        y_res = np.vstack((y_res, y_res))
        X_res = np.vstack((X_res, X_res))
        print('dataBerkovich.X: ', dataBerkovich.X)
        print('X_res: ', X_res)
        print('dataBerkovich.y: ', dataBerkovich.y)
        print('y_res: ', y_res)
        print('data_test.X: ', data_test.X)
        print('data_test.y: ', data_test.y)
        for train_index in range(10):
            print("\nIteration: {}".format(train_index))
            print(train_index)
            data = dde.data.MfDataSet(
                X_lo_train=dataBerkovich.X,
                X_hi_train=X_res,
                y_lo_train=dataBerkovich.y,
                y_hi_train=y_res,
                X_hi_test=data_test.X,
                y_hi_test=data_test.y,
                standardize=True
            )
            res = dde.utils.apply(mfnn, (data,))
            ape.append(res[:2])
            y.append(res[2])

def main(argument=None):
    if argument != None:
        exec(argument)
    return

if __name__ == "__main__":
    main()