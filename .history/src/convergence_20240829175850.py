import pandas as pd
import numpy as np

# 2D linear case
maxh = 0.5
df = pd.read_excel('../data/conv/3D_lin.xlsx')
print(df)

x1, y1, z1 = df['x1'], df['Y1 (m)'], df['Z1 (m)']
x2, y2, z2 = df['X2 (m)'], df['Y2 (m)'], df['Z2 (m)']
x3, y3, z3 = df['X3 (m)'], df['Y3 (m)'], df['Z3 (m)']
D1, D2, D3, D4 = df['D1 (m)'], df['D2 (m)'], df['D3 (m)'], df['D4 (m)']
df['r2'], df['r3'] = np.full((len(df['x1']),), 100), np.full((len(df['x1']),), 100)
df['err2'], df['err3'], df['err4'] = df['x1'], df['x1'], df['x1']

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
    for j in range(len(x4)):
        if np.isnan(D4[j]):
            break
        if abs(x4[j] - x1[i]) + abs(y4[j] - y1[i]) + abs(z4[j] - z1[i]) < df['r4'][i]:
            df['r4'][i] = abs(x4[j] - x1[i]) + abs(y4[j] - y1[i]) + abs(z4[j] - z1[i])
            df['err4'][i] = D4[j]
    print(i, ' ', D2[i], ' ', D3[i], ' ', D4[i])
e1 = 0
e2 = 0
e3 = 0
e4 = 0

leng = 0
for i in range(len(x1)):
    if np.isnan(D1[i]):
        leng = float(i)
        break
    # 20 total nodes in an element (8 * 2 + 4).
    # If it's on an edge, it will see a maximum of 1/2 as many elements. For linear shape functions, it will have equal weight.
    # ε = (∫(u-uh)^2)^0.5. Each body corner is used 8 times and each body edge is used 4 times.
    fac = maxh ** 3 / 8
    for axis in [x1, y1, z1]:
        if axis.equals(x1) or axis.equals(z1) and axis[i] in (-1.5, 1.5):
            fac /= 2
        if axis.equals(y1) and axis[i] in (-1.0, 0.0):
            fac /= 2
        if abs(axis[i] % maxh) > maxh / 4:
            fac /= 2

    sol = (4 * df['err3'][i] - df['err2'][i]) / 3
    e1 += fac * (sol - D1[i]) ** 2
    e2 += fac * (sol - df['err2'][i]) ** 2
    e3 += fac * (sol - df['err3'][i]) ** 2
    e4 += fac * (sol - df['err4'][i]) ** 2
    
e1 = np.sqrt(e1)
e2 = np.sqrt(e2)
e3 = np.sqrt(e3)
e4 = np.sqrt(e4)
print('\ne1=', e1)
print('e2=', e2)
print('e3=', e3)
print('e4=', e4)
print('p=', np.log(e1/e3)/np.log(4))
print('p1=', np.log(e1/e4)/np.log(8))
print('p2=', np.log(e2/e4)/np.log(4))
print('C=', np.average([e1/maxh**(np.log(e1/e4)/np.log(8)), e2/(maxh/2)**(np.log(e1/e4)), e3/(maxh/2)**(np.log(e1/e4)/np.log(8)), e4/maxh**(np.log(e1/e4)/np.log(8))]))




# # 3D linear case
# maxh = 0.5
# df = pd.read_excel('../data/conv/3D_lin.xlsx')
# print(df)

# x1, y1, z1 = df['X1 (m)'], df['Y1 (m)'], df['Z1 (m)']
# x2, y2, z2 = df['X2 (m)'], df['Y2 (m)'], df['Z2 (m)']
# x3, y3, z3 = df['X3 (m)'], df['Y3 (m)'], df['Z3 (m)']
# x4, y4, z4 = df['X4 (m)'], df['Y4 (m)'], df['Z4 (m)']
# D1, D2, D3, D4 = df['D1 (m)'], df['D2 (m)'], df['D3 (m)'], df['D4 (m)']
# df['r2'], df['r3'], df['r4'] = np.full((len(df['X1 (m)']),), 100), np.full((len(df['X1 (m)']),), 100), np.full((len(df['X1 (m)']),), 100)
# df['err2'], df['err3'], df['err4'] = df['X1 (m)'], df['X1 (m)'], df['X1 (m)']

# for i in range(len(x1)):
#     if np.isnan(D1[i]):
#         break
#     for j in range(len(x2)):
#         if np.isnan(D2[j]):
#             break
#         if abs(x2[j] - x1[i]) + abs(y2[j] - y1[i]) + abs(z2[j] - z1[i]) < df['r2'][i]:
#             df['r2'][i] = abs(x2[j] - x1[i]) + abs(y2[j] - y1[i]) + abs(z2[j] - z1[i])
#             df['err2'][i] = D2[j]
#     for j in range(len(x3)):
#         if np.isnan(D3[j]):
#             break
#         if abs(x3[j] - x1[i]) + abs(y3[j] - y1[i]) + abs(z3[j] - z1[i]) < df['r3'][i]:
#             df['r3'][i] = abs(x3[j] - x1[i]) + abs(y3[j] - y1[i]) + abs(z3[j] - z1[i])
#             df['err3'][i] = D3[j]
#     for j in range(len(x4)):
#         if np.isnan(D4[j]):
#             break
#         if abs(x4[j] - x1[i]) + abs(y4[j] - y1[i]) + abs(z4[j] - z1[i]) < df['r4'][i]:
#             df['r4'][i] = abs(x4[j] - x1[i]) + abs(y4[j] - y1[i]) + abs(z4[j] - z1[i])
#             df['err4'][i] = D4[j]
#     print(i, ' ', D2[i], ' ', D3[i], ' ', D4[i])
# e1 = 0
# e2 = 0
# e3 = 0
# e4 = 0

# leng = 0
# for i in range(len(x1)):
#     if np.isnan(D1[i]):
#         leng = float(i)
#         break
#     # 20 total nodes in an element (8 * 2 + 4).
#     # If it's on an edge, it will see a maximum of 1/2 as many elements. For linear shape functions, it will have equal weight.
#     # ε = (∫(u-uh)^2)^0.5. Each body corner is used 8 times and each body edge is used 4 times.
#     fac = maxh ** 3 / 8
#     for axis in [x1, y1, z1]:
#         if axis.equals(x1) or axis.equals(z1) and axis[i] in (-1.5, 1.5):
#             fac /= 2
#         if axis.equals(y1) and axis[i] in (-1.0, 0.0):
#             fac /= 2
#         if abs(axis[i] % maxh) > maxh / 4:
#             fac /= 2

#     sol = (4 * df['err3'][i] - df['err2'][i]) / 3
#     e1 += fac * (sol - D1[i]) ** 2
#     e2 += fac * (sol - df['err2'][i]) ** 2
#     e3 += fac * (sol - df['err3'][i]) ** 2
#     e4 += fac * (sol - df['err4'][i]) ** 2
    
# e1 = np.sqrt(e1)
# e2 = np.sqrt(e2)
# e3 = np.sqrt(e3)
# e4 = np.sqrt(e4)
# print('\ne1=', e1)
# print('e2=', e2)
# print('e3=', e3)
# print('e4=', e4)
# print('p=', np.log(e1/e3)/np.log(4))
# print('p1=', np.log(e1/e4)/np.log(8))
# print('p2=', np.log(e2/e4)/np.log(4))
# print('C=', np.average([e1/maxh**(np.log(e1/e4)/np.log(8)), e2/(maxh/2)**(np.log(e1/e4)), e3/(maxh/2)**(np.log(e1/e4)/np.log(8)), e4/maxh**(np.log(e1/e4)/np.log(8))]))


# # 3D Quadratic case
# maxh = 0.5
# df = pd.read_excel('../data/conv/3D_qua.xlsx')
# print(df)

# x1, y1, z1 = df['X1 (m)'], df['Y1 (m)'], df['Z1 (m)']
# x2, y2, z2 = df['X2 (m)'], df['Y2 (m)'], df['Z2 (m)']
# x3, y3, z3 = df['X3 (m)'], df['Y3 (m)'], df['Z3 (m)']
# D1, D2, D3 = df['D1 (m)'], df['D2 (m)'], df['D3 (m)']
# df['r2'], df['r3'] = np.full((len(df['X1 (m)']),), 100), np.full((len(df['X1 (m)']),), 100)
# df['err2'], df['err3'] = df['X1 (m)'], df['X1 (m)']

# for i in range(len(x1)):
#     if np.isnan(D1[i]):
#         break
#     for j in range(len(x2)):
#         if np.isnan(D2[j]):
#             break
#         if abs(x2[j] - x1[i]) + abs(y2[j] - y1[i]) + abs(z2[j] - z1[i]) < df['r2'][i]:
#             df['r2'][i] = abs(x2[j] - x1[i]) + abs(y2[j] - y1[i]) + abs(z2[j] - z1[i])
#             df['err2'][i] = D2[j]
#     for j in range(len(x3)):
#         if np.isnan(D3[j]):
#             break
#         if abs(x3[j] - x1[i]) + abs(y3[j] - y1[i]) + abs(z3[j] - z1[i]) < df['r3'][i]:
#             df['r3'][i] = abs(x3[j] - x1[i]) + abs(y3[j] - y1[i]) + abs(z3[j] - z1[i])
#             df['err3'][i] = D3[j]
#     print(i, ' ', D2[i], ' ', D3[i])
# e1 = 0
# e2 = 0
# e3 = 0

# leng = 0
# for i in range(len(x1)):
#     if np.isnan(D1[i]):
#         leng = float(i)
#         break
#     # 20 total nodes in an element (8 * 2 + 4). Middle nodes 4x4=16x weight and corners 3x8=24. Total 6x4x3=72
#     # ε = (∫(u-uh)^2)^0.5. Each body corner is used 8 times and each body edge is used 4 times.
#     fac = 24 * maxh ** 3 / 72
#     for axis in [x1, y1, z1]:
#         if axis[i] % maxh > maxh / 4:
#             fac *= 16/24
#         if axis.equals(x1) or axis.equals(z1) and axis[i] in (-1.5, 1.5):
#             fac /= 2
#         if axis.equals(y1) and axis[i] in (-1.0, 0.0):
#             fac /= 2

#     sol = (4 * df['err3'][i] - df['err2'][i]) / 3
#     e1 += fac * (sol - D1[i]) ** 2
#     e2 += fac * (sol - df['err2'][i]) ** 2
#     e3 += fac * (sol - df['err3'][i]) ** 2
    
# e1 = np.sqrt(e1)
# e2 = np.sqrt(e2)
# e3 = np.sqrt(e3)
# print('\ne1=', e1)
# print('e2=', e2)
# print('e3=', e3)
# print('p=', np.log(e1/e3)/np.log(4))
# print('C=', np.average([e1/maxh**(np.log(e1/e3)/np.log(4)), e2/(maxh/2)**(np.log(e1/e4)), e3/(maxh/2)**(np.log(e1/e4)/np.log(8))]))


# # 2D linear case
# maxh = 0.25
# df = pd.read_excel('../data/conv/2D_70_lin.xlsx')
# print(df)

# x1, y1, z1 = df['X1 (m)'], df['Y1 (m)'], df['Z1 (m)']
# x2, y2, z2 = df['X2 (m)'], df['Y2 (m)'], df['Z2 (m)']
# x3, y3, z3 = df['X3 (m)'], df['Y3 (m)'], df['Z3 (m)']
# x4, y4, z4 = df['X4 (m)'], df['Y4 (m)'], df['Z4 (m)']
# D1, D2, D3, D4 = df['D1 (m)'], df['D2 (m)'], df['D3 (m)'], df['D4 (m)']
# df['r2'], df['r3'], df['r4'] = np.full((len(df['X1 (m)']),), 100), np.full((len(df['X1 (m)']),), 100), np.full((len(df['X1 (m)']),), 100)
# df['err2'], df['err3'], df['err4'] = df['X1 (m)'], df['X1 (m)'], df['X1 (m)']

# for i in range(len(x1)):
#     if np.isnan(D1[i]):
#         break
#     for j in range(len(x2)):
#         if np.isnan(D2[j]):
#             break
#         if abs(x2[j] - x1[i]) + abs(y2[j] - y1[i]) + abs(z2[j] - z1[i]) < df['r2'][i]:
#             df['r2'][i] = abs(x2[j] - x1[i]) + abs(y2[j] - y1[i]) + abs(z2[j] - z1[i])
#             df['err2'][i] = D2[j]
#     for j in range(len(x3)):
#         if np.isnan(D3[j]):
#             break
#         if abs(x3[j] - x1[i]) + abs(y3[j] - y1[i]) + abs(z3[j] - z1[i]) < df['r3'][i]:
#             df['r3'][i] = abs(x3[j] - x1[i]) + abs(y3[j] - y1[i]) + abs(z3[j] - z1[i])
#             df['err3'][i] = D3[j]
#     for j in range(len(x4)):
#         if np.isnan(D4[j]):
#             break
#         if abs(x4[j] - x1[i]) + abs(y4[j] - y1[i]) + abs(z4[j] - z1[i]) < df['r4'][i]:
#             df['r4'][i] = abs(x4[j] - x1[i]) + abs(y4[j] - y1[i]) + abs(z4[j] - z1[i])
#             df['err4'][i] = D4[j]
#     print(i, ' ', D2[i], ' ', D3[i], ' ', D4[i])
# e1 = 0
# e2 = 0
# e3 = 0
# e4 = 0

# leng = 0
# for i in range(len(x1)):
#     if np.isnan(D1[i]):
#         leng = float(i)
#         break
#     # 8 total nodes in an element (4 + 4).
#     # ε = (∫(u-uh)^2)^0.5. Each body corner is used 8 times and each body edge is used 4 times.
#     fac = 8 * maxh ** 2 / 8
#     for axis in [x1, y1]:
#         if axis[i] % maxh != 0:
#             fac /= 2
#         if axis.equals(x1) and axis[i] in (0, 2):
#             fac /= 2
#         if axis.equals(y1) and axis[i] in (-4, 0):
#             fac /= 2

#     sol = (4 * df['err4'][i] - df['err3'][i]) / 3
#     e1 += fac * (sol - D1[i]) ** 2
#     e2 += fac * (sol - df['err2'][i]) ** 2
#     e3 += fac * (sol - df['err3'][i]) ** 2
#     e4 += fac * (sol - df['err4'][i]) ** 2
    
# e1 = np.sqrt(e1)
# e2 = np.sqrt(e2)
# e3 = np.sqrt(e3)
# e4 = np.sqrt(e4)
# print('\ne1=', e1)
# print('e2=', e2)
# print('e3=', e3)
# print('e4=', e4)
# print('p=', np.log(e1/e4)/np.log(8))
# print('p4=', np.log(e2/e4)/np.log(4))
# print('p3=', np.log(e1/e3)/np.log(4))
# print('C=', np.average([e1/maxh**(np.log(e1/e4)/np.log(8)), e2/(maxh/2)**(np.log(e1/e4)/np.log(8)), e3/(maxh/4)**(np.log(e1/e4)/np.log(8)), e4/(maxh/8)**(np.log(e1/e4)/np.log(8))]))


# # 2D Quadratic case
# maxh = 0.25
# df = pd.read_excel('../data/conv/2D_70_qua.xlsx')
# print(df)

# x1, y1, z1 = df['X1 (m)'], df['Y1 (m)'], df['Z1 (m)']
# x2, y2, z2 = df['X2 (m)'], df['Y2 (m)'], df['Z2 (m)']
# x3, y3, z3 = df['X3 (m)'], df['Y3 (m)'], df['Z3 (m)']
# x4, y4, z4 = df['X4 (m)'], df['Y4 (m)'], df['Z4 (m)']
# x5, y5, z5 = df['X5 (m)'], df['Y5 (m)'], df['Z5 (m)']
# D1, D2, D3, D4, D5 = df['D1 (m)'], df['D2 (m)'], df['D3 (m)'], df['D4 (m)'], df['D5 (m)']
# df['r2'], df['r3'], df['r4'], df['r5'] = np.full((len(df['X1 (m)']),), 100), np.full((len(df['X1 (m)']),), 100), np.full((len(df['X1 (m)']),), 100), np.full((len(df['X1 (m)']),), 100)
# df['err2'], df['err3'], df['err4'], df['err5'] = df['X1 (m)'], df['X1 (m)'], df['X1 (m)'], df['X1 (m)']

# for i in range(len(x1)):
#     if np.isnan(D1[i]):
#         break
#     for j in range(len(x2)):
#         if np.isnan(D2[j]):
#             break
#         if abs(x2[j] - x1[i]) + abs(y2[j] - y1[i]) + abs(z2[j] - z1[i]) < df['r2'][i]:
#             df['r2'][i] = abs(x2[j] - x1[i]) + abs(y2[j] - y1[i]) + abs(z2[j] - z1[i])
#             df['err2'][i] = D2[j]
#     for j in range(len(x3)):
#         if np.isnan(D3[j]):
#             break
#         if abs(x3[j] - x1[i]) + abs(y3[j] - y1[i]) + abs(z3[j] - z1[i]) < df['r3'][i]:
#             df['r3'][i] = abs(x3[j] - x1[i]) + abs(y3[j] - y1[i]) + abs(z3[j] - z1[i])
#             df['err3'][i] = D3[j]
#     for j in range(len(x4)):
#         if np.isnan(D4[j]):
#             break
#         if abs(x4[j] - x1[i]) + abs(y4[j] - y1[i]) + abs(z4[j] - z1[i]) < df['r4'][i]:
#             df['r4'][i] = abs(x4[j] - x1[i]) + abs(y4[j] - y1[i]) + abs(z4[j] - z1[i])
#             df['err4'][i] = D4[j]
#     for j in range(len(x5)):
#         if np.isnan(D5[j]):
#             break
#         if abs(x5[j] - x1[i]) + abs(y5[j] - y1[i]) + abs(z5[j] - z1[i]) < df['r5'][i]:
#             df['r5'][i] = abs(x5[j] - x1[i]) + abs(y5[j] - y1[i]) + abs(z5[j] - z1[i])
#             df['err5'][i] = D5[j]
#     print(i, ' ', D2[i], ' ', D3[i], ' ', D4[i], ' ', D5[i])
# e1 = 0
# e2 = 0
# e3 = 0
# e4 = 0
# e5 = 0

# leng = 0
# for i in range(len(x1)):
#     if np.isnan(D1[i]):
#         leng = float(i)
#         break
#     # 8 total nodes in an element (4 + 4). get 4x the value of corners, but corners are counted twice in an element and twice as many times. total of 4x4+2x4=24 values
#     # ε = (∫(u-uh)^2)^0.5. Each body corner is used 8 times and each body edge is used 4 times.
#     fac = 8 * maxh ** 2 / 24 # eacah corner node counted twice, can be on up to 4 elements, total of 24 nodes. Edge nodes are counted 4 times on 2 elements.
#     for axis in [x1, y1]:
#         if axis.equals(x1) and axis[i] in (0, 2):
#             fac /= 2
#         if axis.equals(y1) and axis[i] in (-4, 0):
#             fac /= 2

#     sol = (4 * df['err3'][i] - df['err2'][i]) / 3
#     e1 += fac * (sol - D1[i]) ** 2
#     e2 += fac * (sol - df['err2'][i]) ** 2
#     e3 += fac * (sol - df['err3'][i]) ** 2
#     e4 += fac * (sol - df['err4'][i]) ** 2
#     e5 += fac * (sol - df['err5'][i]) ** 2
    
# e1 = np.sqrt(e1)
# e2 = np.sqrt(e2)
# e3 = np.sqrt(e3)
# e4 = np.sqrt(e4)
# e5 = np.sqrt(e5)
# print('\ne1=', e1)
# print('e2=', e2)
# print('e3=', e3)
# print('e4=', e4)
# print('e5=', e5)
# print('p=', np.log(e1/e3)/np.log(4))
# print('C=', np.average([e1/maxh**(np.log(e1/e3)/np.log(4)), e2/(maxh/2)**(np.log(e1/e3)/np.log(4)), e3/(maxh/4)**(np.log(e1/e3)/np.log(4))]))
