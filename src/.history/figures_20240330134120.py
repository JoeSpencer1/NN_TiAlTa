import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

'''
df = pd.read_csv('../data/model/compare.csv', skiprows=1)
fig, ax = plt.subplots()
ax.plot(df['Depth (nm)'], df['Load (uN)'], linewidth=0.3, color='gray', zorder=1, label='Experimental results')
ax.plot(df['Depth0 (nm)'], df['Load0 (uN)'], linewidth=0.3, color='gray', zorder=1)
ax.plot(df['Depth2 (nm)'], df['Load2 (uN)'], linewidth=0.3, color='gray', zorder=1)
ax.plot(df['Depth3 (nm)'], df['Load3 (uN)'], color='gray', linewidth=0.3, zorder=1)
ax.plot(df['Depth4 (nm)'], df['Load4 (uN)'], color='gray', linewidth=0.3, zorder=1)
ax.plot(df['Depth5 (nm)'], df['Load5 (uN)'], color='gray', linewidth=0.3, zorder=1)
ax.plot(df['Depth6 (nm)'], df['Load6 (uN)'], color='gray', linewidth=0.3, zorder=1)
ax.plot(df['Depth7 (nm)'], df['Load7 (uN)'], color='gray', linewidth=0.3, zorder=1)
ax.plot(df['Depth8 (nm)'], df['Load8 (uN)'], color='gray', linewidth=0.3, zorder=1)
ax.plot(df['Depth9 (nm)'], df['Load9 (uN)'], color='gray', linewidth=0.3, zorder=1)
ax.plot(df['Depth10 (nm)'], df['Load10 (uN)'], color='gray', linewidth=0.3, zorder=1)
ax.plot(df['Depth11 (nm)'], df['Load11 (uN)'], color='gray', linewidth=0.3, zorder=1)
ax.plot(df['Depth12 (nm)'], df['Load12 (uN)'], color='gray', linewidth=0.3, zorder=1)
ax.plot(df['Depth13 (nm)'], df['Load13 (uN)'], color='gray', linewidth=0.3, zorder=1)
ax.plot(df['Depth14 (nm)'], df['Load14 (uN)'], color='gray', linewidth=0.3, zorder=1)
ax.plot(df['Depth15 (nm)'], df['Load15 (uN)'], color='gray', linewidth=0.3, zorder=1)
ax.plot(df['Depth16 (nm)'], df['Load16 (uN)'], color='gray', linewidth=0.3, zorder=1)
ax.plot(df['Depth17 (nm)'], df['Load17 (uN)'], color='gray', linewidth=0.3, zorder=1)
ax.plot(df['Depth18 (nm)'], df['Load18 (uN)'], color='gray', linewidth=0.3, zorder=1)
ax.plot(df['Depth19 (nm)'], df['Load19 (uN)'], color='gray', linewidth=0.3, zorder=1)
ax.plot(df['Depth20 (nm)'], df['Load20 (uN)'], color='gray', linewidth=0.3, zorder=1)
ax.plot(df['Depth21 (nm)'], df['Load21 (uN)'], color='gray', linewidth=0.3, zorder=1)
ax.plot(df['Depth22 (nm)'], df['Load22 (uN)'], color='gray', linewidth=0.3, zorder=1)
ax.plot(df['Depth23 (nm)'], df['Load23 (uN)'], color='gray', linewidth=0.3, zorder=1)
ax.plot(df['Depth24 (nm)'], df['Load24 (uN)'], color='gray', linewidth=0.3, zorder=1)
ax.scatter(df['hm (nm)'], df['F (uN)'], color='blue', marker='.', zorder=2, label='3D FEM simulation')
ax.scatter(df['Depth']*1000, df['Force'], color='red', marker='*', zorder=3, s = 10, label='2D FEM simulation')
ax.set_xlabel('Indenter depth (nm)')
ax.set_xlim([0, 275])
ax.set_ylabel('Load (μN)')
ax.set_ylim([0, 11000])
ax.grid(False)
leg = ax.legend()
plt.savefig('/Users/joe/Desktop/R2comp.pdf', dpi=800, bbox_inches="tight")
plt.show()
'''
'''
Bqx = [0.5, 0.25, 0.125]
Bqy = [4.0372711553219845e-09, 7.747377814928931e-10, 1.9368444537322373e-10]
Blx = [0.5, 0.25, 0.125]
Bly = [8.819859692027829e-10, 3.302762232738491e-10, 8.256905581846215e-11]
fx = [0.01, 1.5]
C70lx = [0.25, 0.125, 0.0625, 0.03125]
C70lx = [0.25, 0.125, 0.0625]
C70ly = [1.5246585249772645e-09, 4.582326181224469e-10, 1.2222572353786809e-10, 3.0556430884467364e-11]
C70ly = [1.5246585249772645e-09, 4.582326181224469e-10, 1.2222572353786809e-10]
C70qx = [0.25, 0.125, 0.0625]
C70qy = [1.3124579276878138e-09, 3.5390593493538945e-10, 8.847648373384798e-11]

def equation(x, y, eqx):
    l = len(x) - 1
    p = np.log10(y[l]/y[0])/np.log10(x[l]/x[0])
    C = 0
    for i in range(3):
        C += (1/3)*y[i]/(x[i]**p)
    print('C = ', C)
    print('p = ', p)
    eqy = [0, 0]
    for i in range(2):
        eqy[i] = C * eqx[i] ** p
    return eqy
Bfq = equation(Bqx, Bqy, fx)
Bfl = equation(Blx, Bly, fx)
f70l = equation(C70lx, C70ly, fx)
f70q = equation(C70qx, C70qy, fx)

fig, ax = plt.subplots()
ax.scatter(Blx, Bly, color='blue', marker='s', facecolor='none', label='Linear 3D: $||e||_{L_{2}}=0.0031h^{1.71}$')
ax.scatter(Bqx, Bqy, color='red', marker='^', facecolor='none', label='Qadratic 3D: $||e||_{L_{2}}=0.0177h^{2.19}$')
ax.scatter(C70lx, C70ly, color='gray', marker='o', label='Linear 2D: $||e||_{L_{2}}=0.0194h^{1.82}$')
ax.scatter(C70qx, C70qy, color='violet', marker='d', label='Qadratic 2D: $||e||_{L_{2}}=0.0197h^{1.95}$')
ax.plot(fx, Bfl, linestyle="--", color='blue')
ax.plot(fx, Bfq, linestyle="--", color='red')
ax.plot(fx, f70l, linestyle="--", color='gray')
ax.plot(fx, f70q, linestyle="--", color='violet')
ax.plot()
ax.set_xlabel('Element length (μm)')
ax.set_xscale('log')
ax.set_xlim([0.04, 0.8])
ax.set_ylabel('L$_{2}$ error')
ax.set_yscale('log')
ax.set_ylim([8*10.0**-12, 0.6*10.0**-8])
ax.grid(False)
leg = ax.legend(loc='lower right')
leg.set_title('Element order')
plt.savefig('/Users/joe/Desktop/linqd2D.pdf', dpi=800, bbox_inches="tight")
plt.show()
'''
'''
# NN trained using only Exp data
n = [2, 3, 4, 5, 6, 8, 10, 15]
expσ = [1106.81, 69.63, 26.74, 26.09, 22.29, 14.31, 6.84, 4.44]
εexpσ = [1753.26, 55.26, 14.42, 11.69, 20.16, 8.48, 3.68, 2.4]
expE = [63.26, 54.73, 35.98, 10.44, 21.04, 3.82, 1.13, 2.68]
εexpE = [60.11, 54.11, 61.9, 8.32, 29.84, 1.83, 1.13, 1.77]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.errorbar(n, expσ, yerr = εexpσ, color = 'blue', label = "MAPE with experimental training data")
ax1.set_yscale('log')
ax1.set_ylim([2, 3000])
ax1.set_xlim([-0.5, 16])
ax1.set_xticks([0, 5, 10, 15])
ax1.set_yticks([2, 5, 20, 200, 2000])
ax1.set_yticklabels([2, 5, 20, 200, 2000])
ax1.legend()
ax1.set_ylabel("MAPE (%)")
ax1.set_xlabel("Experimental training data size")
ax1.annotate("A: $\sigma_{y}$", xy=(0.05, 0.95), xycoords="axes fraction",
              fontsize=12, ha="center",
              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))

ax2.errorbar(n, expE, yerr = εexpE, color = 'blue')
ax2.set_yscale('log')
ax2.set_ylim([1, 150])
ax2.set_xlim([-0.5, 16])
ax2.set_xticks([0, 5, 10, 15])
ax2.set_yticks([1, 3, 10, 30,100])
ax2.set_yticklabels([1, 3, 10, 30,100])
ax2.legend()
ax2.set_ylabel("MAPE (%)")
ax2.set_xlabel("Experimental training data size")
plt.subplots_adjust(bottom=0.180)
fig.tight_layout()
ax2.annotate("B: $E_{r}$", xy=(0.05, 0.95), xycoords="axes fraction",
              fontsize=12, ha="center",
              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))
plt.savefig("/Users/Joe/Desktop/NN_graphs/NN_exp.pdf", dpi=800, bbox_inches="tight")
plt.show()
'''
'''
# NN trained using only 3D FEM data
n = [2, 3, 4, 5, 6, 8, 10, 15]
# Quad
quadσ = [186.66, 46.38, 28.6, 14.01, 9.74, 6.19, 3.22, 2.46]
εquadσ = [189.15, 56.01, 23.82, 7.84, 4.39, 5.08, 1.45, 2.53]
quadE = [345.4, 42.02, 14.72, 7.1, 4.34, 2.17, 2.59, 1.05]
εquadE = [507.45, 62.97, 18.38, 6.16, 3.04, 1.25, 1.69, 0.86]
# Linear
linσ = [1995.92, 48.35, 34.45, 22.19, 14.58, 6.71, 4.52, 2.86]
εlinσ = [5267.5, 33.75, 21.54, 15.88, 8.52, 3.58, 3.35, 2.67]
linE = [79.87, 36.83, 20.77, 8.3, 6.37, 3.6, 0.89, 1.6]
εlinE = [70.26, 42.85, 29.94, 6.17, 4.53, 5.16, 0.37, 2.09]
# Rough
roughσ = [214.67, 105.36, 30.22, 32.76, 19.03, 11.82, 8.21, 0.51]
εroughσ = [382.82, 74.29, 20.58, 23.93, 12.61, 14.24, 11.15, 0.56]
roughE = [117.55, 29.76, 21.78, 8.34, 5.86, 5.95, 2.4, 0.36]
εroughE = [129.98, 17.51, 15.83, 6.72, 4.59, 8.15, 5.36, 0.19]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.errorbar(n, quadσ, yerr = εquadσ, color = 'blue', label = "MAPE with quadratic 3D FEM training data")
ax1.errorbar(n, linσ, yerr = εlinσ, color = 'darkorange', linestyle = '--', label = "MAPE with linear 3D FEM training data")
ax1.errorbar(n, roughσ, yerr = εroughσ, color = 'red', linestyle = '-.', label = "MAPE with rough 3D FEM training data")
ax1.set_yscale('log')
ax1.set_ylim([0.5, 3000])
ax1.set_xlim([-0.5, 16])
ax1.set_xticks([0, 5, 10, 15])
ax1.set_yticks([1, 5, 20, 200, 2000])
ax1.set_yticklabels([1, 5, 20, 200, 2000])
ax1.legend()
ax1.set_ylabel("MAPE (%)")
ax1.set_xlabel("3D FEM training data size")
ax1.annotate("A: $\sigma_{y}$", xy=(0.05, 0.95), xycoords="axes fraction",
              fontsize=12, ha="center",
              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))

ax2.errorbar(n, quadE, yerr = εquadE, color = 'blue')
ax2.errorbar(n, linE, yerr = εlinE, color = 'darkorange', linestyle = '--')
ax2.errorbar(n, roughE, yerr = εroughE, color = 'red', linestyle = '-.')
ax2.set_yscale('log')
ax2.set_ylim([0.3, 400])
ax2.set_xlim([-0.5, 16])
ax2.set_xticks([0, 5, 10, 15])
ax2.set_yticks([1, 3, 8, 20, 200])
ax2.set_yticklabels([1, 3, 8, 20, 200])
ax2.legend()
ax2.set_ylabel("MAPE (%)")
ax2.set_xlabel("3D FEM training data size")
plt.subplots_adjust(bottom=0.180)
fig.tight_layout()
ax2.annotate("B: $E_{r}$", xy=(0.05, 0.95), xycoords="axes fraction",
              fontsize=12, ha="center",
              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))
plt.savefig("/Users/Joe/Desktop/NN_graphs/NN_3D.pdf", dpi=800, bbox_inches="tight")
plt.show()
'''
'''
# NN trained using only 2D FEM data
n = [2, 3, 4, 5, 6, 8, 10, 15]
# Quad
quadσ = [138.11, 43.18, 45.15, 25.09, 11.48, 4.66, 4.98, 1.4]
εquadσ = [105.82, 28.19, 39.35, 15.59, 8.58, 1.81, 3.01, 1.33]
quadE = [107.11, 84.02, 33.06, 24.34, 8.55, 3.16, 0.99, 0.58]
εquadE = [101.72, 144.88, 42.79, 34.47, 9.99, 3.55, 0.77, 0.63]
# Linear
linσ = [276.46, 137.41, 258.65, 149.91, 73.08, 65.71, 132.51, 36.05]
εlinσ = [159.96, 131, 469.07, 165.62, 46.38, 44.83, 110.42, 61.28]
linE = [5420.07, 175.19, 240.3, 67.63, 14.73, 47.28, 5.72, 15.84]
εlinE = [14794.34, 260.99, 620.91, 103.07, 17.36, 30.32, 4.18, 22.52]
# Rough
roughσ = [354.03, 79.83, 70, 38.13, 23.22, 14.63, 10.4, 2.08]
εroughσ = [838.61, 64.48, 99.67, 21.22, 12.49, 14.81, 5.42, 1.2]
roughE = [93.73, 46.15, 75.98, 24.53, 8.7, 5.57, 3.15, 3.64]
εroughE = [55.47, 24.75, 136.34, 21.07, 3.57, 3.84, 2.25, 3.17]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.errorbar(n, quadσ, yerr = εquadσ, color = 'blue', label = "MAPE with quadratic 2D FEM training data")
ax1.errorbar(n, linσ, yerr = εlinσ, color = 'darkorange', linestyle = '--', label = "MAPE with linear 2D FEM training data")
ax1.errorbar(n, roughσ, yerr = εroughσ, color = 'red', linestyle = '-.', label = "MAPE with rough 2D FEM training data")
ax1.set_yscale('log')
ax1.set_ylim([1, 2010])
ax1.set_xlim([-0.5, 16])
ax1.set_xticks([0, 5, 10, 15])
ax1.set_yticks([1, 3, 10, 100, 1000])
ax1.set_yticklabels([1, 3, 20, 200, 2000])
ax1.legend()
ax1.set_ylabel("MAPE (%)")
ax1.set_xlabel("2D FEM training data size")
ax1.annotate("A: $\sigma_{y}$", xy=(0.05, 0.95), xycoords="axes fraction",
              fontsize=12, ha="center",
              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))

ax2.errorbar(n, quadE, yerr = εquadE, color = 'blue')
ax2.errorbar(n, linE, yerr = εlinE, color = 'darkorange', linestyle = '--')
ax2.errorbar(n, roughE, yerr = εroughE, color = 'red', linestyle = '-.')
ax2.set_yscale('log')
ax2.set_ylim([0.5, 5500])
ax2.set_xlim([-0.5, 16])
ax2.set_xticks([0, 5, 10, 15])
ax2.set_yticks([1, 5, 20, 200, 2000])
ax2.set_yticklabels([1, 5, 20, 200, 2000])
ax2.legend()
ax2.set_ylabel("MAPE (%)")
ax2.set_xlabel("2D FEM training data size")
plt.subplots_adjust(bottom=0.180)
fig.tight_layout()
ax2.annotate("B: $E_{r}$", xy=(0.05, 0.95), xycoords="axes fraction",
              fontsize=12, ha="center",
              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))
plt.savefig("/Users/Joe/Desktop/NN_graphs/NN_2D.pdf", dpi=800, bbox_inches="tight")
plt.show()
'''
'''
# NN trained using 3D FEM + exp data
n = [0, 1,2, 3, 4, 5, 6, 8, 10, 15]
# Quad
quadσ = [740.72, 252.74, 111.54, 90.05, 90.79, 32.03, 38.39, 23.28, 24.59, 8.57]
εquadσ = [404.34, 203.45, 66.79, 44.65, 94.55, 14.62, 24.99, 12.25, 23.08, 8.65]
quadE = [61.32, 52.72, 15.51, 14.08, 10.74, 8.83, 7.09, 6.64, 4.44, 1.7]
εquadE = [27.06, 39.16, 10.11, 6.88, 5.72, 4.42, 4.01, 3.69, 3.97, 3.21]
# Linear
linσ = [543.86, 128.53, 97.73, 35.13, 21.94, 15.6, 13.91, 4.88, 4.29, 2.25]
εlinσ = [303.57, 112.67, 107.49, 22.73, 14.82, 10.68, 12.13, 2.04, 2.66, 1.16]
linE = [138.04, 19.43, 17.34, 13.28, 6.33, 3.19, 2.37, 1.54, 0.61, 0.2]
εlinE = [52.77, 10.9, 17.39, 14.92, 10.78, 3.46, 1.51, 2.54, 0.39, 0.1]
# Rough
roughσ = [101.42, 44.69, 36.98, 20.33, 15.55, 7.81, 7.37, 4.67, 2.57, 2.05]
εroughσ = [33.53, 20.28, 21.55, 14.56, 13.14, 2.69, 4.22, 2.56, 0.82, 1.27]
roughE = [35.39, 3.56, 2.1, 1.52, 1.4, 0.9, 1.05, 0.54, 0.31, 0.21]
εroughE = [5.22, 1.37, 1.03, 0.71, 0.7, 0.27, 0.69, 0.19, 0.14, 0.12]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.errorbar(n, quadσ, yerr = εquadσ, color = 'blue', label = "MFNN trained with quadratic 3D FEM training data")
ax1.errorbar(n, linσ, yerr = εlinσ, color = 'darkorange', linestyle = '--', label = "MAPE with linear 3D FEM training data")
ax1.errorbar(n, roughσ, yerr = εroughσ, color = 'red', linestyle = '-.', label = "MAPE with rough 3D FEM training data")
ax1.set_yscale('log')
ax1.set_ylim([1, 2010])
ax1.set_xlim([-0.5, 16])
ax1.set_xticks([0, 5, 10, 15])
ax1.set_yticks([1, 3, 10, 100, 1000])
ax1.set_yticklabels([1, 3, 20, 200, 2000])
ax1.legend()
ax1.set_ylabel("MAPE (%)")
ax1.set_xlabel("Experimental training data size")
ax1.annotate("A: $\sigma_{y}$", xy=(0.05, 0.95), xycoords="axes fraction",
              fontsize=12, ha="center",
              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))

ax2.errorbar(n, quadE, yerr = εquadE, color = 'blue')
ax2.errorbar(n, linE, yerr = εlinE, color = 'darkorange', linestyle = '--')
ax2.errorbar(n, roughE, yerr = εroughE, color = 'red', linestyle = '-.')
ax2.set_yscale('log')
ax2.set_ylim([0.1, 200])
ax2.set_xlim([-0.5, 16])
ax2.set_xticks([0, 5, 10, 15])
ax2.set_yticks([1, 5, 20, 200])
ax2.set_yticklabels([1, 5, 20, 200])
ax2.legend()
ax2.set_ylabel("MAPE (%)")
ax2.set_xlabel("Experimental training data size")
plt.subplots_adjust(bottom=0.180)
fig.tight_layout()
ax2.annotate("B: $E_{r}$", xy=(0.05, 0.95), xycoords="axes fraction",
              fontsize=12, ha="center",
              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))
plt.savefig("/Users/Joe/Desktop/NN_graphs/MFNN_3Dexp.pdf", dpi=800, bbox_inches="tight")
plt.show()
'''

# NN trained using 2D FEM + exp data
n = [0, 1,2, 3, 4, 5, 6, 8, 10, 15]
# Quad
quadσ = [581.3, 339.88, 285.23, 150.08, 191.27, 122.55, 168.67, 89.58, 48.09, 24.95]
εquadσ = [158.29, 306.29, 158.49, 65.99, 90.44, 53.61, 116.04, 48.03, 24.65, 12.05]
quadE = [298.82, 64.09, 54.9, 53.03, 26.08, 26.25, 12.9, 10.98, 5.48, 2.82]
εquadE = [40.3, 57.51, 46.59, 24.41, 23.17, 16.96, 6.82, 5.51, 2.93, 4.43]
# Linear
linσ = [1466.83, 283.36, 240.21, 86.12, 62.09, 104.42, 28.63, 15.78, 18.84, 9.37]
εlinσ = [466.01, 184.79, 240.76, 85.69, 39.93, 121.31, 19.92, 10.14, 15.83, 6.07]
linE = [284.24, 122.93, 39.28, 7.33, 16.92, 8.45, 4.36, 2.09, 1.59, 1.37]
εlinE = [27.14, 68.5, 48.34, 5, 21.8, 9.25, 4.24, 3.26, 1.97, 3.2]
# Rough
roughσ = [2210.49, 434.87, 202.75, 125.6, 63.71, 48.32, 39.08, 27.1, 20.68, 12.65]
εroughσ = [497.72, 237.52, 133.06, 120, 24.73, 21.33, 15.24, 13.25, 10.21, 10.12]
roughE = [136.36, 64.29, 26.06, 14.32, 6.82, 8.78, 8.77, 3.06, 2.07, 1.34]
εroughE = [38.96, 38.14, 20.43, 10.47, 2.27, 6.67, 6.37, 2.05, 1.59, 1.62]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.errorbar(n, quadσ, yerr = εquadσ, color = 'blue', label = "MFNN trained with quadratic 2D FEM training data")
ax1.errorbar(n, linσ, yerr = εlinσ, color = 'darkorange', linestyle = '--', label = "MAPE with linear 2D FEM training data")
ax1.errorbar(n, roughσ, yerr = εroughσ, color = 'red', linestyle = '-.', label = "MAPE with rough 2D FEM training data")
ax1.set_yscale('log')
ax1.set_ylim([5, 3000])
ax1.set_xlim([-0.5, 16])
ax1.set_xticks([0, 5, 10, 15])
ax1.set_yticks([5, 20, 100, 1000])
ax1.set_yticklabels([5, 20, 100, 1000])
ax1.legend()
ax1.set_ylabel("MAPE (%)")
ax1.set_xlabel("Experimental training data size")
ax1.annotate("A: $\sigma_{y}$", xy=(0.05, 0.95), xycoords="axes fraction",
              fontsize=12, ha="center",
              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))

ax2.errorbar(n, quadE, yerr = εquadE, color = 'blue')
ax2.errorbar(n, linE, yerr = εlinE, color = 'darkorange', linestyle = '--')
ax2.errorbar(n, roughE, yerr = εroughE, color = 'red', linestyle = '-.')
ax2.set_yscale('log')
ax2.set_ylim([1, 350])
ax2.set_xlim([-0.5, 16])
ax2.set_xticks([0, 5, 10, 15])
ax2.set_yticks([1, 5, 20, 200])
ax2.set_yticklabels([1, 5, 20, 200])
ax2.legend()
ax2.set_ylabel("MAPE (%)")
ax2.set_xlabel("Experimental training data size")
plt.subplots_adjust(bottom=0.180)
fig.tight_layout()
ax2.annotate("B: $E_{r}$", xy=(0.05, 0.95), xycoords="axes fraction",
              fontsize=12, ha="center",
              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))
plt.savefig("/Users/Joe/Desktop/NN_graphs/MFNN_2Dexp.pdf", dpi=800, bbox_inches="tight")
plt.show()

