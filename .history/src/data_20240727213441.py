from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import pandas as pd

class FileData(object):
    def __init__(self, filename, yname, new=False):
        
        self.filename = filename
        self.yname = yname
        self.new = new

        self.X = None
        self.y = None

        if type(self.filename) is tuple:
            for i in range(len(self.filename)):
                self.read(self.filename[i], self.new)

        else:
            self.read(self.filename, self.new)

    def read(self, name, new):
        df = pd.read_csv('../data/' + name + '.csv')

        # This is for Al alloys
        if 'Al7075' in name or 'Al6061' in name:
            df['dP/dh (N/m)'] *= 0.2 * (df['C (GPa)'] / 3) ** 0.5 * 10 ** (-1.5)
        # This is for Ti alloys
        if 'B3090' in name or 'B3067' in name:
            df['dP/dh (N/m)'] *= 0.2 / df['hmax(um)']
        # Scale TI33 to hm=0.2μm
        if 'TI33' in name or '2D' in name or '3D' in name:
            # For 25˚ case
            df['dP/dh (N/m)'] *= 0.2 / df['hmax(um)']
        # Scale from Conical to Berkovich with small deformations
        if 'FEM_70deg' in name:
            df['dP/dh (N/m)'] *= 1.167 / 1.128
        # Scale from Conical to Berkovich with large deformations (See Dao et al. 2001
        if '2D' in name:
            df['dP/dh (N/m)'] *= 1.2370 / 1.1957
        # Get Estar if none provided
        if 'FEM_70deg' in name or 'Berkovich' in name or 'conical' in name or '2D' in name or '3D' in name:
            df['Er (GPa)'] = EtoEr(df['E (GPa)'].values, df['nu'].values)[:, None]

        print(df.describe())

        if self.X is None:
            self.X = df[['C (GPa)', 'dP/dh (N/m)', 'Wp/Wt']].values
        else:
            self.X = np.vstack((self.X, df[['C (GPa)', 'dP/dh (N/m)', 'Wp/Wt']].values))
        if self.yname == 'Er':
            if self.y is None:
                self.y = df['Er (GPa)'].values[:, None]
            else:
                self.y = np.vstack((self.y, df['Er (GPa)'].values[:, None]))
        elif self.yname == 'sigma_y':
            if self.y is None:
                self.y = df['sy (GPa)'].values[:, None]
            else:
                self.y = np.vstack((self.y, df['sy (GPa)'].values[:, None]))
        elif self.yname == 'all':
            if new == False:
                if self.y is None:
                    #self.y = df['Er (GPa)', 'sy (GPa)', 'n'].values[:, None]
                    self.y = df[['Er (GPa)', 'sy (GPa)']].values
                else:
                    #self.y = np.vstack((self.y, df['Er (GPa)', 'sy (GPa)', 'n'].values[:, None]))
                    self.y = np.vstack(([self.y, df['Er (GPa)', 'sy (GPa)']].values))
            


    def pop(self, index):
        self.X = np.delete(self.X, index, axis=0)
        self.y = np.delete(self.y, index, axis=0)
    
    def push(self, index):
        self.X = np.append(index.X)
        self.y = np.append(index.y)
    
def EtoEr(E, nu):
    nu_i, E_i = 0.0691, 1143
    return 1 / ((1 - nu ** 2) / E + (1 - nu_i ** 2) / E_i)