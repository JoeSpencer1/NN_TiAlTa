import pandas as pd
import numpy as np

df = pd.read_excel('~/Desktop/Convergence/3D_lin.xlsx')
print(df)

x1, y1, z1 = df['X1 (m)'], df['Y1 (m)'], df['Z1 (m)']
x2, y2, z2 = df['X2 (m)'], df['Y2 (m)'], df['Z2 (m)']
x3, y3, z3 = df['X3 (m)'], df['Y3 (m)'], df['Z3 (m)']
D1, D2, D3 = df['D1 (m)'], df['D2 (m)'], df['D3 (m)']
df['e2'], df['e3'] = np.full((len(df['X1 (m)']),), 100), np.full((len(df['X1 (m)']),), 100)
df['pos2'], df['pos3'] = df['Node'], df['Node']

for i in range(len(x1)):
    if D1[i] != 'nan':
        for j in range(len(x2)):
            if abs(x2[j] - x1[i]) + abs(y2[j] - y1[i]) + abs(z2[j] - z1[i]) < df['e2'][j]:

