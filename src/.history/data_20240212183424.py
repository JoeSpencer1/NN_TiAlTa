from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import pandas as pd

class FEMData0(object):
    def __init__(self, yname, angles):
        self.yname = yname
        self.angles = angles

        self.X = None
        self.y = None

        if len(angles) == 1:
            self.read_1angle()
        elif len(angles) == 2:
            self.read_2angles()
        elif len(angles) == 4:
            self.read_4angles()

    def read_1angle(self):
        df = pd.read_csv("../data/FEM_{}deg.csv".format(self.angles[0]))
        df["E* (GPa)"] = EtoEstar(df["E (GPa)"])
        df["sy/E*"] = df["sy (GPa)"] / df["E* (GPa)"]
        df = df.loc[~((df["n"] > 0.3) & (df["sy/E*"] >= 0.03))]
        # df = df.loc[df["n"] <= 0.3]
        # Scale c* from Conical to Berkovich
        # df["dP/dh (N/m)"] *= 1.167 / 1.128
        # Add noise
        # sigma = 0.2
        # df["E* (GPa)"] *= 1 + sigma * np.random.randn(len(df))
        # df["sy (GPa)"] *= 1 + sigma * np.random.randn(len(df))
        print(df.describe())

        self.X = df[["C (GPa)", "dP/dh (N/m)", "Wp/Wt"]].values
        if self.yname == "E*":
            self.y = df["E* (GPa)"].values[:, None]
        elif self.yname == "sigma_y":
            self.y = df["sy (GPa)"].values[:, None]
        elif self.yname.startswith("sigma_"):
            e_plastic = float(self.yname[6:])
            self.y = (
                df["sy (GPa)"]
                * (1 + e_plastic * df["E (GPa)"] / df["sy (GPa)"]) ** df["n"]
            ).values[:, None]

class FEM1(object):
    def __init__(self, yname, filename):
        self.yname = yname
        self.filename = filename

        self.X = None
        self.y = None
        self.read_1angle()


    def read_1angle(self):
        name = '../data/' + self.filename + '.csv'
        print('Name=', name)
        df = pd.read_csv(name)
        if self.filename != 'TI33_25':
            df["Estar (GPa)"] = EtoEstar(df["E (GPa)"])
        df["sy/Estar"] = df["sy (GPa)"] / df["Estar (GPa)"]
        if (self.filename == 'FEM_70deg'):
            df = df.loc[~((df["n"] > 0.3) & (df["sy/Estar"] >= 0.03))]
        # df = df.loc[df["n"] <= 0.3]
        # Scale c* from Conical to Berkovich
        # df["dP/dh (N/m)"] *= 1.167 / 1.128
        # Add noise
        # sigma = 0.2
        # df["E* (GPa)"] *= 1 + sigma * np.random.randn(len(df))
        # df["sy (GPa)"] *= 1 + sigma * np.random.randn(len(df))
        print(df.describe())

        self.X = df[["C (GPa)", "dP/dh (N/m)", "Wp/Wt"]].values
        if self.yname == "Estar":
            self.y = df["Estar (GPa)"].values[:, None]
        else:
            self.y = df["sy (GPa)"].values[:, None]





class FEMData(object):
    def __init__(self, yname):
        self.yname = yname
        #self.angles = angles
        #self.angles = ['../data/TI33_conical_30.csv', '../data/TI33_conical_45.csv', '../data/TI33_conical_60.csv']
        #self.angles = ['../data/TI33_conical_30_i.csv', '../data/TI33_conical_45_i.csv', '../data/TI33_conical_60_i.csv']
        #self.angles = ['../data/TI33_conical_30_i.csv']
        self.angles = ['../data/TI33_conical_30.csv']
        #self.angles = ['../data/TI33_conical_30_i.csv', '../data/TI33_conical_30.csv']
        #self.angles = ['../data/FEM_70deg.csv']
        print('Size: '+str(len(self.angles)))

        self.X = None
        self.y = None

        self.read_angles()
        '''
        if len(angles) == 1:
            self.read_1angle()
        elif len(angles) == 2:
            self.read_2angles()
        elif len(angles) == 3:
            self.read_3angles()'''

    def read_angles(self):
        df_list = []
        for angle in self.angles:
            df_list.append(pd.read_csv(angle))
            print(df_list[-1].describe())

        df = pd.concat(df_list, ignore_index=True)

        self.X = df[[
                'C (GPa)',
                'dP/dh (N/m)',
                'Wp/Wt'
            ]].values
        if self.yname == 'Estar':
            self.y = EtoEr(df['E (GPa)'].values, df['nu'].values)[:, None]
        elif self.yname == 'sigma_y':
            self.y = df['sy (GPa)'].values[:, None]

class ExpData(object):
    def __init__(self, temp, yname):
        filename = '../data/' + temp + '.csv'
        self.filename = filename
        self.yname = yname

        self.X = None
        self.y = None

        self.read()

    def read(self):
        df = pd.read_csv(self.filename)

        #
        # Scale dP/dh from 3N to hm = 0.2um

# This is for Al alloys
#        df['dP/dh (N/m)'] *= 0.2 * (df['C (GPa)'] / 3) ** 0.5 * 10 ** (-1.5)

        
        # Scale dP/dh from Pm to hm = 0.2um
        # df['dP/dh (N/m)'] *= 0.2 * (df['C (GPa)'] / df['Pm (N)']) ** 0.5 * 10 ** (-1.5)
        # Scale dP/dh from hm to hm = 0.2um 

# This is for Ti alloys
#        df['dP/dh (N/m)'] *= 0.2 / df['hm (um)']
# This is for the Yanbo's Ti alloys
        df['dP/dh (N/m)'] *= 0.2 * 1000 / df['hmax(nm)']

        # Scale c* from Berkovich to Conical
#        df['dP/dh (N/m)'] *= 1.128 / 1.167
        #

        print(df.describe())

# I just commented this line for my own work.
        self.X = df[['C (GPa)', 'dP/dh (N/m)', 'Wp/Wt']].values
        if self.yname == 'Estar':
            self.y = df['Estar (GPa)'].values[:, None]
        if self.yname.startswith('E_'):
            self.y = df[self.yname].values[:, None]
        elif self.yname == 'sigma_y':
            self.y = df['sy (GPa)'].values[:, None]
        elif self.yname.startswith('sigma_'):
            e_plastic = self.yname[6:]
            self.y = df['s' + e_plastic + ' (GPa)'].values[:, None]

class ExpDataT(object):
    def __init__(self, temp, yname):
        filename = '../data/' + temp + '.csv'
        self.filename = filename
        self.yname = yname

        self.X = None
        self.y = None

        self.read()

    def read(self):
        df = pd.read_csv(self.filename)

        #
        # Scale dP/dh from 3N to hm = 0.2um

# This is for Al alloys
#        df['dP/dh (N/m)'] *= 0.2 * (df['C (GPa)'] / 3) ** 0.5 * 10 ** (-1.5)

        
        # Scale dP/dh from Pm to hm = 0.2um
        # df['dP/dh (N/m)'] *= 0.2 * (df['C (GPa)'] / df['Pm (N)']) ** 0.5 * 10 ** (-1.5)
        # Scale dP/dh from hm to hm = 0.2um 

# This is for Ti alloys
#        df['dP/dh (N/m)'] *= 0.2 / df['hm (um)']
# This is for the Yanbo's Ti alloys
        df['dP/dh (N/m)'] *= 0.2 * 1000 / df['hmax(nm)']

        # Scale c* from Berkovich to Conical
#        df['dP/dh (N/m)'] *= 1.128 / 1.167
        #

        print(df.describe())

# I just commented this line for my own work.
        self.X = df[['C (GPa)', 'dP/dh (N/m)', 'Wp/Wt', 'T (C)']].values
        if self.yname == 'Estar':
            self.y = df['Estar (GPa)'].values[:, None]
        if self.yname.startswith('E_'):
            self.y = df[self.yname].values[:, None]
        elif self.yname == 'sigma_y':
            self.y = df['sy (GPa)'].values[:, None]
        elif self.yname.startswith('sigma_'):
            e_plastic = self.yname[6:]
            self.y = df['s' + e_plastic + ' (GPa)'].values[:, None]


class BerkovichData(object):
    def __init__(self, yname, scale_c=False):
        self.yname = yname
        self.scale_c = scale_c

        self.X = None
        self.y = None

        self.read()

    def read(self):
        #df = pd.read_csv('../data/Berkovich.csv')
        df = pd.read_csv('../data/TI33_Berkovich.csv')
        if self.scale_c:
            df['dP/dh (N/m)'] *= 1.128 / 1.167
        print(df.describe())

        self.X = df[['C (GPa)', 'dP/dh (N/m)', 'Wp/Wt']].values
        if self.yname == 'Estar':
            self.y = EtoEr(df['E (GPa)'].values, df['nu'].values)[:, None]
        elif self.yname == 'sigma_y':
            self.y = df['sy (GPa)'].values[:, None]
        elif self.yname == 'n':
            self.y = df['n'].values[:, None]
        elif self.yname.startswith('sigma_'):
            e_plastic = float(self.yname[6:])
            self.y = (
                df['sy (GPa)']
                * (1 + e_plastic * df['E (GPa)'] / df['sy (GPa)']) ** df['n']
            ).values[:, None]


def EtoEr(E, nu):
    nu_i, E_i = 0.0691, 1143
    return 1 / ((1 - nu ** 2) / E + (1 - nu_i ** 2) / E_i)

def EtoEstar(E):
    nu = 0.3
    nu_i, E_i = 0.07, 1100
    return 1 / ((1 - nu ** 2) / E + (1 - nu_i ** 2) / E_i)