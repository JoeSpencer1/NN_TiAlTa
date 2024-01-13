from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import pandas as pd

class FEMData(object):
    def __init__(self, yname):
        self.yname = yname
        #self.angles = angles

        self.X = None
        self.y = None

        self.read_3angles()
        '''
        if len(angles) == 1:
            self.read_1angle()
        elif len(angles) == 2:
            self.read_2angles()
        elif len(angles) == 3:
            self.read_3angles()'''

    def read_3angles(self):
        df1 = pd.read_csv('../data/TI33_conical_30.csv')
        df2 = pd.read_csv('../data/TI33_conical_45.csv')
        df3 = pd.read_csv('../data/TI33_conical_60.csv')
        df = (
            df3.set_index('Case')
            .join(df2.set_index('Case'), how='inner', rsuffix='_45')
            .join(df3.set_index('Case'), how='inner', rsuffix='_60')
        )
        print(df.describe())

        self.X = df[
            [
                'C (GPa)',
                'dP/dh (N/m)',
                'Wp/Wt'
            ]
        ].values
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
