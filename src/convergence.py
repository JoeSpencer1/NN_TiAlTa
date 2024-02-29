import pandas as pd
import numpy as np

# linear case
df = pd.read_excel('../data/conv/3D_lin.xlsx')
print(df)

x1, y1, z1 = df['X1 (m)'], df['Y1 (m)'], df['Z1 (m)']
x2, y2, z2 = df['X2 (m)'], df['Y2 (m)'], df['Z2 (m)']
x3, y3, z3 = df['X3 (m)'], df['Y3 (m)'], df['Z3 (m)']
D1, D2, D3 = df['D1 (m)'], df['D2 (m)'], df['D3 (m)']
df['r2'], df['r3'] = np.full((len(df['X1 (m)']),), 100), np.full((len(df['X1 (m)']),), 100)
df['err2'], df['err3'] = df['X1 (m)'], df['X1 (m)']
'''
for i in range(len(x1)):
    if np.isnan(D1[i]):
        break
    for j in range(len(x2)):
        if np.isnan(D2[j]):
            break
        if abs(x2[j] - x1[i]) + abs(y2[j] - y1[i]) + abs(z2[j] - z1[i]) < df['r2'][i]:
            df['r2'][i] = abs(x2[j] - x1[i]) + abs(y2[j] - y1[i]) + abs(z2[j] - z1[i])
            df['err2'][i] = D2[j]
    for j in range(len(x3)):
        if np.isnan(D3[j]):
            break
        if abs(x3[j] - x1[i]) + abs(y3[j] - y1[i]) + abs(z3[j] - z1[i]) < df['r3'][i]:
            df['r3'][i] = abs(x3[j] - x1[i]) + abs(y3[j] - y1[i]) + abs(z3[j] - z1[i])
            df['err3'][i] = D3[j]
    print(i, ' ', D2[i], ' ', D3[i])
e1 = 0
e2 = 0
e3 = 0

leng = 0
for i in range(len(x1)):
    if np.isnan(D1[i]):
        leng = float(i)
        break
    sol = (4 * df['err3'][i] - df['err2'][i]) / 3
    e1 += (sol - D1[i]) ** 2
    e2 += (sol - df['err2'][i]) ** 2
    e3 += (sol - df['err3'][i]) ** 2
    
e1 = np.sqrt(e1 / leng)
e2 = np.sqrt(e2 / leng)
e3 = np.sqrt(e3 / leng)
maxh = 0.5
print('\ne1=', e1)
print('e2=', e2)
print('e3=', e3)
print('p=', np.log(e1/e3)/np.log(4))
print('C=', e1 / maxh ** (np.log(e1/e3)/np.log(4)))
'''
# Quadratic case
df = pd.read_excel('../data/conv/3D_qua.xlsx')
print(df)

x1, y1, z1 = df['X1 (m)'], df['Y1 (m)'], df['Z1 (m)']
x2, y2, z2 = df['X2 (m)'], df['Y2 (m)'], df['Z2 (m)']
x3, y3, z3 = df['X3 (m)'], df['Y3 (m)'], df['Z3 (m)']
D1, D2, D3 = df['D1 (m)'], df['D2 (m)'], df['D3 (m)']
df['r2'], df['r3'] = np.full((len(df['X1 (m)']),), 100), np.full((len(df['X1 (m)']),), 100)
df['err2'], df['err3'] = df['X1 (m)'], df['X1 (m)']

for i in range(len(x1)):
    if np.isnan(D1[i]):
        break
    for j in range(len(x2)):
        if np.isnan(D2[j]):
            break
        if abs(x2[j] - x1[i]) + abs(y2[j] - y1[i]) + abs(z2[j] - z1[i]) < df['r2'][i]:
            df['r2'][i] = abs(x2[j] - x1[i]) + abs(y2[j] - y1[i]) + abs(z2[j] - z1[i])
            df['err2'][i] = D2[j]
    for j in range(len(x3)):
        if np.isnan(D3[j]):
            break
        if abs(x3[j] - x1[i]) + abs(y3[j] - y1[i]) + abs(z3[j] - z1[i]) < df['r3'][i]:
            df['r3'][i] = abs(x3[j] - x1[i]) + abs(y3[j] - y1[i]) + abs(z3[j] - z1[i])
            df['err3'][i] = D3[j]
    print(i, ' ', D2[i], ' ', D3[i])
e1 = 0
e2 = 0
e3 = 0

leng = 0
for i in range(len(x1)):
    if np.isnan(D1[i]):
        leng = float(i)
        break
    sol = (4 * df['err3'][i] - df['err2'][i]) / 3
    e1 += (sol - D1[i]) ** 2
    e2 += (sol - df['err2'][i]) ** 2
    e3 += (sol - df['err3'][i]) ** 2
    
e1 = np.sqrt(e1 / leng)
e2 = np.sqrt(e2 / leng)
e3 = np.sqrt(e3 / leng)
maxh = 0.5
print('\ne1=', e1)
print('e2=', e2)
print('e3=', e3)
print('p=', np.log(e1/e3)/np.log(4))
print('C=', e1 / maxh ** (np.log(e1/e3)/np.log(4)))
'''
# 30˚ case
df = pd.read_excel('../data/conv/2D_30.xlsx')
print(df)

x1, y1, z1 = df['X1 (m)'], df['Y1 (m)'], df['Z1 (m)']
x2, y2, z2 = df['X2 (m)'], df['Y2 (m)'], df['Z2 (m)']
x3, y3, z3 = df['X3 (m)'], df['Y3 (m)'], df['Z3 (m)']
D1, D2, D3 = df['D1 (m)'], df['D2 (m)'], df['D3 (m)']
df['r2'], df['r3'] = np.full((len(df['X1 (m)']),), 100), np.full((len(df['X1 (m)']),), 100)
df['err2'], df['err3'] = df['X1 (m)'], df['X1 (m)']

for i in range(len(x1)):
    if np.isnan(D1[i]):
        break
    for j in range(len(x2)):
        if np.isnan(D2[j]):
            break
        if abs(x2[j] - x1[i]) + abs(y2[j] - y1[i]) + abs(z2[j] - z1[i]) < df['r2'][i]:
            df['r2'][i] = abs(x2[j] - x1[i]) + abs(y2[j] - y1[i]) + abs(z2[j] - z1[i])
            df['err2'][i] = D2[j]
    for j in range(len(x3)):
        if np.isnan(D3[j]):
            break
        if abs(x3[j] - x1[i]) + abs(y3[j] - y1[i]) + abs(z3[j] - z1[i]) < df['r3'][i]:
            df['r3'][i] = abs(x3[j] - x1[i]) + abs(y3[j] - y1[i]) + abs(z3[j] - z1[i])
            df['err3'][i] = D3[j]
    print(i, ' ', D2[i], ' ', D3[i])
e1 = 0
e2 = 0
e3 = 0

leng = 0
for i in range(len(x1)):
    if np.isnan(D1[i]):
        leng = float(i)
        break
    sol = (4 * df['err3'][i] - df['err2'][i]) / 3
    e1 += (sol - D1[i]) ** 2
    e2 += (sol - df['err2'][i]) ** 2
    e3 += (sol - df['err3'][i]) ** 2
    
e1 = np.sqrt(e1 / leng)
e2 = np.sqrt(e2 / leng)
e3 = np.sqrt(e3 / leng)
maxh = 0.1
print('\ne1=', e1)
print('e2=', e2)
print('e3=', e3)
print('p=', np.log(e1/e3)/np.log(4))
print('C=', e1 / maxh ** (np.log(e1/e3)/np.log(4)))

# 45˚ case
df = pd.read_excel('../data/conv/2D_45.xlsx')
print(df)

x1, y1, z1 = df['X1 (m)'], df['Y1 (m)'], df['Z1 (m)']
x2, y2, z2 = df['X2 (m)'], df['Y2 (m)'], df['Z2 (m)']
x3, y3, z3 = df['X3 (m)'], df['Y3 (m)'], df['Z3 (m)']
D1, D2, D3 = df['D1 (m)'], df['D2 (m)'], df['D3 (m)']
df['r2'], df['r3'] = np.full((len(df['X1 (m)']),), 100), np.full((len(df['X1 (m)']),), 100)
df['err2'], df['err3'] = df['X1 (m)'], df['X1 (m)']

for i in range(len(x1)):
    if np.isnan(D1[i]):
        break
    for j in range(len(x2)):
        if np.isnan(D2[j]):
            break
        if abs(x2[j] - x1[i]) + abs(y2[j] - y1[i]) + abs(z2[j] - z1[i]) < df['r2'][i]:
            df['r2'][i] = abs(x2[j] - x1[i]) + abs(y2[j] - y1[i]) + abs(z2[j] - z1[i])
            df['err2'][i] = D2[j]
    for j in range(len(x3)):
        if np.isnan(D3[j]):
            break
        if abs(x3[j] - x1[i]) + abs(y3[j] - y1[i]) + abs(z3[j] - z1[i]) < df['r3'][i]:
            df['r3'][i] = abs(x3[j] - x1[i]) + abs(y3[j] - y1[i]) + abs(z3[j] - z1[i])
            df['err3'][i] = D3[j]
    print(i, ' ', D2[i], ' ', D3[i])
e1 = 0
e2 = 0
e3 = 0

leng = 0
for i in range(len(x1)):
    if np.isnan(D1[i]):
        leng = float(i)
        break
    sol = (4 * df['err3'][i] - df['err2'][i]) / 3
    e1 += (sol - D1[i]) ** 2
    e2 += (sol - df['err2'][i]) ** 2
    e3 += (sol - df['err3'][i]) ** 2
    
e1 = np.sqrt(e1 / leng)
e2 = np.sqrt(e2 / leng)
e3 = np.sqrt(e3 / leng) 
maxh = 0.1
print('\ne1=', e1)
print('e2=', e2)
print('e3=', e3)
print('p=', np.log(e1/e3)/np.log(4))
print('C=', e1 / maxh ** (np.log(e1/e3)/np.log(4)))

# 60˚ case
df = pd.read_excel('../data/conv/2D_60.xlsx')
print(df)

x1, y1, z1 = df['X1 (m)'], df['Y1 (m)'], df['Z1 (m)']
x2, y2, z2 = df['X2 (m)'], df['Y2 (m)'], df['Z2 (m)']
x3, y3, z3 = df['X3 (m)'], df['Y3 (m)'], df['Z3 (m)']
D1, D2, D3 = df['D1 (m)'], df['D2 (m)'], df['D3 (m)']
df['r2'], df['r3'] = np.full((len(df['X1 (m)']),), 100), np.full((len(df['X1 (m)']),), 100)
df['err2'], df['err3'] = df['X1 (m)'], df['X1 (m)']

for i in range(len(x1)):
    if np.isnan(D1[i]):
        break
    for j in range(len(x2)):
        if np.isnan(D2[j]):
            break
        if abs(x2[j] - x1[i]) + abs(y2[j] - y1[i]) + abs(z2[j] - z1[i]) < df['r2'][i]:
            df['r2'][i] = abs(x2[j] - x1[i]) + abs(y2[j] - y1[i]) + abs(z2[j] - z1[i])
            df['err2'][i] = D2[j]
    for j in range(len(x3)):
        if np.isnan(D3[j]):
            break
        if abs(x3[j] - x1[i]) + abs(y3[j] - y1[i]) + abs(z3[j] - z1[i]) < df['r3'][i]:
            df['r3'][i] = abs(x3[j] - x1[i]) + abs(y3[j] - y1[i]) + abs(z3[j] - z1[i])
            df['err3'][i] = D3[j]
    print(i, ' ', D2[i], ' ', D3[i])
e1 = 0
e2 = 0
e3 = 0

leng = 0
for i in range(len(x1)):
    if np.isnan(D1[i]):
        leng = float(i)
        break
    sol = (4 * df['err3'][i] - df['err2'][i]) / 3
    e1 += (sol - D1[i]) ** 2
    e2 += (sol - df['err2'][i]) ** 2
    e3 += (sol - df['err3'][i]) ** 2
    
e1 = np.sqrt(e1 / leng)
e2 = np.sqrt(e2 / leng)
e3 = np.sqrt(e3 / leng)
maxh = 0.1
print('\ne1=', e1)
print('e2=', e2)
print('e3=', e3)
print('p=', np.log(e1/e3)/np.log(4))
print('C=', e1 / maxh ** (np.log(e1/e3)/np.log(4)))
'''
# 70˚ case
df = pd.read_excel('../data/conv/2D_70.xlsx')
print(df)

x1, y1, z1 = df['X1 (m)'], df['Y1 (m)'], df['Z1 (m)']
x2, y2, z2 = df['X2 (m)'], df['Y2 (m)'], df['Z2 (m)']
x3, y3, z3 = df['X3 (m)'], df['Y3 (m)'], df['Z3 (m)']
D1, D2, D3 = df['D1 (m)'], df['D2 (m)'], df['D3 (m)']
df['r2'], df['r3'] = np.full((len(df['X1 (m)']),), 100), np.full((len(df['X1 (m)']),), 100)
df['err2'], df['err3'] = df['X1 (m)'], df['X1 (m)']

for i in range(len(x1)):
    if np.isnan(D1[i]):
        break
    for j in range(len(x2)):
        if np.isnan(D2[j]):
            break
        if abs(x2[j] - x1[i]) + abs(y2[j] - y1[i]) + abs(z2[j] - z1[i]) < df['r2'][i]:
            df['r2'][i] = abs(x2[j] - x1[i]) + abs(y2[j] - y1[i]) + abs(z2[j] - z1[i])
            df['err2'][i] = D2[j]
    for j in range(len(x3)):
        if np.isnan(D3[j]):
            break
        if abs(x3[j] - x1[i]) + abs(y3[j] - y1[i]) + abs(z3[j] - z1[i]) < df['r3'][i]:
            df['r3'][i] = abs(x3[j] - x1[i]) + abs(y3[j] - y1[i]) + abs(z3[j] - z1[i])
            df['err3'][i] = D3[j]
    print(i, ' ', D2[i], ' ', D3[i])
e1 = 0
e2 = 0
e3 = 0

leng = 0
for i in range(len(x1)):
    if np.isnan(D1[i]):
        leng = float(i)
        break
    sol = (4 * df['err3'][i] - df['err2'][i]) / 3
    e1 += (sol - D1[i]) ** 2
    e2 += (sol - df['err2'][i]) ** 2
    e3 += (sol - df['err3'][i]) ** 2
    
e1 = np.sqrt(e1 / leng)
e2 = np.sqrt(e2 / leng)
e3 = np.sqrt(e3 / leng)
maxh = 0.5
print('\ne1=', e1)
print('e2=', e2)
print('e3=', e3)
print('p=', np.log(e1/e3)/np.log(4))
print('C=', e1 / maxh ** (np.log(e1/e3)/np.log(4)))