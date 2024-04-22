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
''''''
# NN trained using only Exp data
n = [2, 3, 4, 5, 6, 8, 10, 15]
expσ = [454.05, 71.77, 49.45, 25.61, 27.66, 12.97, 7.66, 2.95]
εexpσ = [712.66, 49.57, 42.9, 14.01, 11.68, 5.78, 3.54, 3.24]
expE = [410.65, 126.05, 22.35, 14.34, 4.76, 3.64, 1.77, 0.9]
εexpE = [1105.96, 263.65, 14.69, 6.97, 2.52, 2.01, 0.57, 0.95]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.errorbar(n, expσ, yerr = εexpσ, color = 'blue', label = "NN, experimental training data")
ax1.set_yscale('log')
ax1.set_ylim([1, 2000])
ax1.set_xlim([-0.5, 16])
ax1.set_xticks([0, 5, 10, 15])
ax1.set_yticks([1, 5, 20, 200, 2000])
ax1.set_yticklabels([1, 5, 20, 200, 2000])
ax1.legend()
ax1.set_ylabel("MAPE (%)")
ax1.set_xlabel("Experimental training data size")
ax1.annotate("A: $\sigma_{y}$", xy=(0.05, 0.95), xycoords="axes fraction",
              fontsize=12, ha="center",
              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))

ax2.errorbar(n, expE, yerr = εexpE, color = 'blue')
ax2.set_yscale('log')
ax2.set_ylim([0.5, 2000])
ax2.set_xlim([-0.5, 16])
ax2.set_xticks([0, 5, 10, 15])
ax2.set_yticks([1, 5, 20, 200, 2000])
ax2.set_yticklabels([1, 5, 20, 200, 2000])
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

''''''
# NN trained using only 3D FEM data
n = [2, 3, 4, 5, 6, 8, 10, 15]
# Quad
quadσ = [446.01, 78.58, 43.38, 92.26, 22.75, 10.05, 3.2, 2.76]
εquadσ = [674.86, 73.79, 29.23, 191.64, 19.98, 8.19, 1.72, 1.13]
quadE = [153.84, 46.81, 17.78, 9.39, 11.82, 4.2, 2.83, 1.11]
εquadE = [204.33, 40.51, 11.61, 9.9, 18.95, 3.84, 3.26, 0.92]
# Linear
linσ = [263.07, 136.04, 78.79, 31.6, 35.54, 15.67, 7.65, 4.87]
εlinσ = [320.99, 137.13, 55.85, 41.83, 45.52, 14.91, 6.73, 6.11]
linE = [201.58, 81.61, 36.67, 23.98, 9.4, 5.72, 2.66, 1.43]
εlinE = [166.62, 131.97, 51.13, 27.15, 10.02, 4.39, 1.76, 1.48]
# Rough quad
rqσ = [142.71, 74.53, 34.3, 28.01, 18.66, 7.73, 5.66, 3.89]
εrqσ = [94.42, 109.08, 29.02, 29.56, 15.26, 4.45, 6.47, 2.18]
rqE = [94.03, 126.64, 22.15, 8.25, 9.4, 3.32, 7.69, 0.73]
εrqE = [136.66, 326.68, 20.6, 7.18, 7.94, 2.76, 11.09, 0.52]
# Rough linear
rlσ = [339.8, 63.49, 27.3, 20.5, 13.02, 4.58, 3.98, 2.1]
εrlσ = [373.93, 38.56, 15.79, 13.91, 11.87, 2.76, 2.61, 1.25]
rlE = [163.99, 46.33, 18.12, 14.37, 8.08, 2.75, 3.2, 0.54]
εrlE = [165.07, 66.08, 19.43, 20.79, 13.91, 2.34, 2.11, 0.38]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.errorbar(n, quadσ, yerr = εquadσ, color = 'blue', label = "NN, quadratic 3D FEM training data")
ax1.errorbar(n, linσ, yerr = εlinσ, color = 'darkorange', linestyle = '--', label = "NN, linear 3D FEM")
ax1.errorbar(n, rqσ, yerr = εrqσ, color = 'red', linestyle = '-.', label = "NN, rough quadratic 3D FEM")
ax1.errorbar(n, rlσ, yerr = εrlσ, color = 'green', linestyle = ':', label = "NN, rough linear 3D FEM")
ax1.set_yscale('log')
ax1.set_ylim([0.5, 2000])
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
ax2.errorbar(n, rqE, yerr = εrqE, color = 'red', linestyle = '-.')
ax2.errorbar(n, rlE, yerr = εrlE, color = 'green', linestyle = ':')
ax2.set_yscale('log')
ax2.set_ylim([0.3, 400])
ax2.set_xlim([-0.5, 16])
ax2.set_xticks([0, 5, 10, 15])
ax2.set_yticks([1, 5, 20, 100, 400])
ax2.set_yticklabels([1, 5, 20, 100, 400])
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

''''''
# NN trained using only 2D FEM data
n = [2, 3, 4, 5, 6, 8, 10, 15]
# Quad
quadσ = [109.76, 47.89, 46.79, 38.21, 11.48, 16.78, 5.51, 1.4]
εquadσ = [91.8, 31.4, 37.23, 38.29, 7.64, 22.61, 2.71, 0.77]
quadE = [85.78, 43.17, 47.02, 21.88, 9.67, 4.68, 1.7, 0.76]
εquadE = [55.6, 34.09, 66.01, 25.56, 10.23, 8.88, 1.69, 1.04]
# Linear
linσ = [1633.42, 225.48, 191.84, 79.35, 118.2, 80.9, 104.55, 101.04]
εlinσ = [2284.04, 302.36, 274.23, 55.91, 84.98, 47.27, 79.21, 136.48]
linE = [349.65, 370.2, 250.86, 77.31, 31.56, 23.4, 7.37, 8.39]
εlinE = [343.99, 893.87, 614.8, 123.54, 43.18, 25.2, 4.13, 14.34]
# Rough quadratic
rqσ = [93.21, 31.84, 21.32, 15.24, 8.26, 5.15, 2.32, 0.54]
εrqσ = [66.1, 22.5, 15.99, 26.62, 13.35, 6.32, 2.06, 0.46]
rqE = [190.1, 40.48, 17.27, 9.16, 8.4, 3.1, 0.66, 0.3]
εrqE = [201.62, 60.1, 21.2, 18.23, 18.1, 2.39, 0.37, 0.25]
# Rough linear
rlσ = [109.07, 20.72, 24.49, 25.34, 7.48, 7.15, 0.86, 0.48]
εrlσ = [190.51, 21.75, 25.85, 46.21, 10.07, 9.02, 0.51, 0.66]
rlE = [145.15, 34.48, 10.35, 20.14, 2.93, 3.08, 0.46, 0.27]
εrlE = [159.4, 39.15, 14.58, 45.65, 2.31, 4, 0.24, 0.42]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.errorbar(n, quadσ, yerr = εquadσ, color = 'blue', label = "NN, quadratic 2D FEM training data")
ax1.errorbar(n, linσ, yerr = εlinσ, color = 'darkorange', linestyle = '--', label = "NN, linear 2D FEM")
ax1.errorbar(n, rqσ, yerr = εrqσ, color = 'red', linestyle = '-.', label = "NN, rough quadratic 2D FEM")
ax1.errorbar(n, rlσ, yerr = εrlσ, color = 'green', linestyle = ':', label = "NN, rough linear 2D FEM")
ax1.set_yscale('log')
ax1.set_ylim([0.3, 2000])
ax1.set_xlim([-0.5, 16])
ax1.set_xticks([0, 5, 10, 15])
ax1.set_yticks([1, 4, 40, 200, 2000])
ax1.set_yticklabels([1, 4, 40, 200, 2000])
ax1.legend()
ax1.set_ylabel("MAPE (%)")
ax1.set_xlabel("2D FEM training data size")
ax1.annotate("A: $\sigma_{y}$", xy=(0.05, 0.95), xycoords="axes fraction",
              fontsize=12, ha="center",
              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))

ax2.errorbar(n, quadE, yerr = εquadE, color = 'blue')
ax2.errorbar(n, linE, yerr = εlinE, color = 'darkorange', linestyle = '--')
ax2.errorbar(n, rqE, yerr = εrqE, color = 'red', linestyle = '-.')
ax2.errorbar(n, rlE, yerr = εrlE, color = 'green', linestyle = ':')
ax2.set_yscale('log')
ax2.set_ylim([0.2, 1000])
ax2.set_xlim([-0.5, 16])
ax2.set_xticks([0, 5, 10, 15])
ax2.set_yticks([1, 5, 20, 200, 2000])
ax2.set_yticklabels([1, 5, 20, 100, 1000])
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

''''''
# NN trained using 3D FEM + exp data
n = [1, 2, 3, 4, 5, 6, 8, 10, 15]
# Quad
quadσ = [1351.81, 452.26, 319.8, 177.61, 60.14, 46.42, 23.17, 15.56, 10.5]
εquadσ = [1072.1, 511.24, 442.56, 310.37, 44.82, 19.6, 12.36, 7.49, 8.69]
quadE = [51.58, 63.66, 79.89, 32.66, 11.93, 19.23, 9.25, 3.03, 0.99]
εquadE = [17.24, 45.07, 93.41, 21.8, 7.54, 29.84, 10.76, 1.95, 1.56]
# Linear
linσ = [36634.57, 708.92, 137.15, 59.39, 58.04, 49.06, 34.95, 7.95, 2.26]
εlinσ = [65961.55, 1199.85, 151.5, 50.03, 52.52, 50.9, 29.06, 4.53, 1.28]
linE = [491.49, 337.55, 76.81, 11.18, 12.07, 5.32, 2.32, 1.31, 0.71]
εlinE = [1047.59, 575.56, 97.39, 8.19, 15.69, 3.57, 1.41, 1.12, 0.46]
# Rough quadratic
rqσ = [973.17, 187.86, 98.51, 44.6, 23.13, 18.43, 13.11, 12.45, 3.17]
εrqσ = [913.21, 196.17, 128.93, 30.89, 12.48, 8.19, 5.92, 4, 1.26]
rqE = [726.8, 53.62, 35.26, 13.62, 4.73, 2.79, 2.13, 1.23, 0.78]
εrqE = [1996.38, 42.36, 50.84, 24.58, 2.59, 1.87, 1.73, 0.67, 0.27]
# Rough linear
rlσ = [2657.76, 66.44, 49.1, 34.98, 14.36, 7.57, 5.19, 3.86, 1.75]
εrlσ = [3730.08, 57.76, 60.19, 50.49, 8.66, 3.09, 4.66, 1.1, 1.06]
rlE = [178.95, 35.97, 11.05, 6, 4.32, 3.64, 1.88, 1.39, 0.4]
εrlE = [435.57, 45.93, 13.19, 7.08, 1.71, 2.71, 1.18, 1.11, 0.26]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.errorbar(n, quadσ, yerr = εquadσ, color = 'blue', label = "MFNN, quadratic 3D FEM + experiment")
ax1.errorbar(n, linσ, yerr = εlinσ, color = 'darkorange', linestyle = '--', label = "MFNN, linear 3D FEM + experiment")
ax1.errorbar(n, rqσ, yerr = εrqσ, color = 'red', linestyle = '-.', label = "MFNN, rough quadratic 3D FEM + experiment")
ax1.errorbar(n, rlσ, yerr = εrlσ, color = 'green', linestyle = ':', label = "MAPE, rough linear 3D FEM + experiment")
ax1.set_yscale('log')
ax1.set_ylim([1, 2000])
ax1.set_xlim([-0.5, 16])
ax1.set_xticks([0, 5, 10, 15])
ax1.set_yticks([1, 3, 20, 200, 2000])
ax1.set_yticklabels([1, 3, 20, 200, 2000])
ax1.legend()
ax1.set_ylabel("MAPE (%)")
ax1.set_xlabel("Experimental training data size")
ax1.annotate("A: $\sigma_{y}$", xy=(0.05, 0.95), xycoords="axes fraction",
              fontsize=12, ha="center",
              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))

ax2.errorbar(n, quadE, yerr = εquadE, color = 'blue')
ax2.errorbar(n, linE, yerr = εlinE, color = 'darkorange', linestyle = '--')
ax2.errorbar(n, rqE, yerr = εrqE, color = 'red', linestyle = '-.')
ax2.errorbar(n, rlE, yerr = εrlE, color = 'green', linestyle = ':')
ax2.set_yscale('log')
ax2.set_ylim([0.5, 400])
ax2.set_xlim([-0.5, 16])
ax2.set_xticks([0, 5, 10, 15])
ax2.set_yticks([1, 5, 20, 100, 400])
ax2.set_yticklabels([1, 5, 20, 100, 400])
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

''''''
# NN trained using 2D FEM + exp data
n = [1, 2, 3, 4, 5, 6, 8, 10, 15]
# Quad
quadσ = [36184.53, 1259.9, 419, 320.04, 189.93, 121.16, 71.58, 51.27, 31.79]
εquadσ = [66423.99, 1123.25, 312.95, 146.28, 113.76, 77.07, 29.23, 20.34, 23.96]
quadE = [497.91, 723.59, 96.18, 58.12, 15.87, 18.86, 9.63, 7.99, 3.19]
εquadE = [922.43, 1414.97, 114.58, 62.2, 8.22, 12.32, 9.22, 3.78, 1.92]
# Linear
linσ = [16184.69, 1381.04, 179.68, 136.8, 151.56, 62.47, 53.22, 23.73, 10.51]
εlinσ = [30905.79, 2243.39, 179.2, 172.37, 181.03, 35.03, 75.49, 16.61, 8.74]
linE = [147.68, 759.69, 73.81, 26.48, 8.68, 10.53, 2.84, 2.46, 1.19]
εlinE = [156.24, 945.02, 125.1, 36.81, 5.57, 7.8, 1.02, 1.68, 1.36]
# Rough quadratic
rqσ = [4407.64, 27.54, 11.08, 5.63, 2.84, 2.4, 1.58, 0.85, 0.73]
εrqσ = [4114.03, 18.8, 6.5, 5.16, 1.3, 1.43, 0.74, 0.36, 0.5]
rqE = [48.95, 6.7, 3.21, 1.34, 0.5, 0.68, 0.26, 0.13, 0.09]
εrqE = [32.54, 8.89, 2.61, 1.16, 0.35, 0.64, 0.18, 0.06, 0.06]
# Rough linear
rlσ = [29777.51, 19.85, 10.27, 3.22, 2.81, 2.78, 1.37, 1.12, 0.71]
εrlσ = [82262.28, 15.44, 14.15, 1.68, 1.1, 3.19, 0.84, 0.77, 0.64]
rlE = [60.04, 5, 1.91, 0.38, 0.44, 0.2, 0.14, 0.09, 0.06]
εrlE = [103.93, 5.09, 2.1, 0.17, 0.41, 0.11, 0.1, 0.05, 0.02]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.errorbar(n, quadσ, yerr = εquadσ, color = 'blue', label = "MFNN, quadratic 2D FEM + experiment")
ax1.errorbar(n, linσ, yerr = εlinσ, color = 'darkorange', linestyle = '--', label = "MFNN, linear 2D FEM + experiment")
ax1.errorbar(n, rqσ, yerr = εrqσ, color = 'red', linestyle = '-.', label = "MFNN, rought quadratic 2D FEM + experiment")
ax1.errorbar(n, rlσ, yerr = εrlσ, color = 'green', linestyle = ':', label = "MFNN, rough linear 2D FEM + experiment")
ax1.set_yscale('log')
ax1.set_ylim([0.5, 3000])
ax1.set_xlim([-0.5, 16])
ax1.set_xticks([0, 5, 10, 15])
ax1.set_yticks([1, 20, 200, 5000, 3000])
ax1.set_yticklabels([1, 20, 200, 5000, 3000])
ax1.legend()
ax1.set_ylabel("MAPE (%)")
ax1.set_xlabel("Experimental training data size")
ax1.annotate("A: $\sigma_{y}$", xy=(0.05, 0.95), xycoords="axes fraction",
              fontsize=12, ha="center",
              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))

ax2.errorbar(n, quadE, yerr = εquadE, color = 'blue')
ax2.errorbar(n, linE, yerr = εlinE, color = 'darkorange', linestyle = '--')
ax2.errorbar(n, rqE, yerr = εrqE, color = 'red', linestyle = '-.')
ax2.errorbar(n, rlE, yerr = εrlE, color = 'green', linestyle = ':')
ax2.set_yscale('log')
ax2.set_ylim([0.5, 1000])
ax2.set_xlim([-0.5, 16])
ax2.set_xticks([0, 5, 10, 15])
ax2.set_yticks([1, 5, 20, 100, 1000])
ax2.set_yticklabels([1, 5, 20, 100, 1000])
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

''''''
# NN trained using 2D FEM + 3D FEM + exp data
n = [1, 2, 3, 4, 5, 6, 8, 10, 15]
# Quad hi
quadσ = [43934.59, 1426.72, 478.59, 228.99, 169.88, 134.76, 92.12, 63.7, 21.94]
εquadσ = [121955.08, 1322.61, 446.62, 158.17, 90.84, 116.97, 73.74, 18.68, 5.01]
quadE = [1273.85, 313.26, 27.02, 20.79, 18.47, 20.26, 7.97, 6.8, 2.98]
εquadE = [2306.76, 397.27, 16.55, 9.3, 7.3, 20.55, 4.45, 4.21, 1.55]
# Linear hi
linσ = [4229.1, 360.61, 163.4, 129.94, 108.97, 33.36, 28.9, 22.49, 8.45]
εlinσ = [5101.53, 217.93, 134.17, 98.81, 134.96, 19.22, 14.2, 19.22, 3.88]
linE = [428.87, 108.84, 115.91, 27.23, 8.93, 10.6, 6.7, 3.41, 0.48]
εlinE = [523.46, 134.13, 206.01, 44.9, 6.66, 8.3, 6.1, 4.53, 0.32]
# Rough quadratic hi
rqσ = [10363.12, 28.96, 11.96, 3.72, 3.53, 1.7, 1.12, 0.87, 0.59]
εrqσ = [26058.97, 25.87, 9.2, 2.3, 3.03, 0.51, 0.59, 0.5, 0.3]
rqE = [178.51, 16.22, 1.71, 1.08, 0.43, 0.49, 0.32, 0.16, 0.08]
εrqE = [221.8, 22.46, 1.72, 0.65, 0.25, 0.53, 0.22, 0.08, 0.02]
# Rough linear hi
rlσ = [2187.96, 17.27, 7.75, 2.52, 3.52, 2.39, 1.09, 0.74, 0.53]
εrlσ = [1973.46, 12.4, 6.03, 0.96, 2.93, 2.36, 0.57, 0.42, 0.3]
rlE = [55.48, 3.28, 1.42, 0.43, 0.38, 0.35, 0.27, 0.11, 0.08]
εrlE = [40.21, 3.42, 1.34, 0.29, 0.21, 0.34, 0.25, 0.05, 0.04]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.errorbar(n, quadσ, yerr = εquadσ, color = 'blue', label = "MFNN, quadratic FEM 2D low + 3D high training")
ax1.errorbar(n, linσ, yerr = εlinσ, color = 'darkorange', linestyle = '--', label = "MFNN, linear FEM + experiment")
ax1.errorbar(n, rqσ, yerr = εrqσ, color = 'red', linestyle = '-.', label = "MFNN, rough quadratic FEM + experiment")
ax1.errorbar(n, rlσ, yerr = εrlσ, color = 'green', linestyle = ':', label = "MFNN, rough linear FEM + experiment")
ax1.set_yscale('log')
ax1.set_ylim([0.5, 1000])
ax1.set_xlim([-0.5, 16])
ax1.set_xticks([0, 5, 10, 15])
ax1.set_yticks([1, 5, 20, 100, 1000])
ax1.set_yticklabels([1, 5, 20, 100, 1000])
ax1.legend()
ax1.set_ylabel("MAPE (%)")
ax1.set_xlabel("Experimental training data size")
ax1.annotate("A: $\sigma_{y}$", xy=(0.05, 0.95), xycoords="axes fraction",
              fontsize=12, ha="center",
              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))

ax2.errorbar(n, quadE, yerr = εquadE, color = 'blue')
ax2.errorbar(n, linE, yerr = εlinE, color = 'darkorange', linestyle = '--')
ax2.errorbar(n, rqE, yerr = εrqE, color = 'red', linestyle = '-.')
ax2.errorbar(n, rlE, yerr = εrlE, color = 'green', linestyle = ':')
ax2.set_yscale('log')
ax2.set_ylim([0.5, 1000])
ax2.set_xlim([-0.5, 16])
ax2.set_xticks([0, 5, 10, 15])
ax2.set_yticks([1, 10, 50, 200, 1000])
ax2.set_yticklabels([1, 10, 50, 200, 1000])
ax2.legend()
ax2.set_ylabel("MAPE (%)")
ax2.set_xlabel("Experimental training data size")
plt.subplots_adjust(bottom=0.180)
fig.tight_layout()
ax2.annotate("B: $E_{r}$", xy=(0.05, 0.95), xycoords="axes fraction",
              fontsize=12, ha="center",
              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))
plt.savefig("/Users/Joe/Desktop/NN_graphs/MFNN_2D3Dexp_hi.pdf", dpi=800, bbox_inches="tight")
plt.show()


# NN trained using 2D FEM + 3D FEM + exp data
n = [1, 2, 3, 4, 5, 6, 8, 10, 15]
# Quad lo
quadσ = [1379.54, 161.92, 64.49, 74.03, 32.58, 32.72, 20.69, 11.22, 5.19]
εquadσ = [1934.59, 172.95, 29.88, 34.79, 11.55, 11.12, 6.97, 3.15, 0.92]
quadE = [240.18, 55.55, 38.79, 17.72, 9.4, 8.68, 3.24, 3.14, 0.97]
εquadE = [106.19, 51.93, 58.11, 26.48, 4.46, 7.3, 2.03, 1.25, 0.4]
# Linear lo
linσ = [1509.36, 237.77, 72.71, 59.4, 39.09, 20.95, 14.64, 12.39, 4.22]
εlinσ = [2204.52, 211.33, 47.31, 44.09, 28.53, 14.41, 7.36, 5.81, 1.1]
linE = [2061.41, 108.64, 14.23, 12.91, 6.95, 4.44, 3.1, 1.23, 0.64]
εlinE = [3495.15, 121.02, 10.8, 14.04, 4.83, 2.95, 2.22, 0.36, 0.19]
# Rough quadratic lo
rqσ = [74.01, 38.87, 10.55, 4.09, 3.23, 2.17, 1.23, 1.34, 0.83]
εrqσ = [96.68, 33.22, 9.61, 2.14, 3.65, 0.85, 0.66, 0.55, 0.35]
rqE = [17.23, 6.18, 5.14, 1.52, 0.25, 1.28, 0.55, 0.34, 0.1]
εrqE = [17.81, 4.51, 4.45, 1.24, 0.1, 1.48, 0.57, 0.39, 0.04]
# Rough linear lo
rlσ = [25.55, 17.36, 7.87, 4.09, 1.56, 1.75, 0.9, 0.8, 0.58]
εrlσ = [27.38, 13.39, 5.7, 3.8, 0.76, 1.52, 0.34, 0.3, 0.29]
rlE = [11.25, 2.3, 0.52, 0.57, 0.19, 0.27, 0.09, 0.07, 0.06]
εrlE = [11.62, 2.52, 0.22, 0.5, 0.16, 0.19, 0.08, 0.04, 0.03]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.errorbar(n, quadσ, yerr = εquadσ, color = 'blue', label = "MFNN, quadratic 2D & 3D FEM low training")
ax1.errorbar(n, linσ, yerr = εlinσ, color = 'darkorange', linestyle = '--', label = "MFNN, linear FEM training data")
ax1.errorbar(n, rqσ, yerr = εrqσ, color = 'red', linestyle = '-.', label = "MFNN, rough quadratic FEM training data")
ax1.errorbar(n, rlσ, yerr = εrlσ, color = 'green', linestyle = ':', label = "MFNN, rough linear FEM training data")
ax1.set_yscale('log')
ax1.set_ylim([0.5, 1000])
ax1.set_xlim([-0.5, 16])
ax1.set_xticks([0, 5, 10, 15])
ax1.set_yticks([1, 10, 50, 200, 1000])
ax1.set_yticklabels([1, 20, 50, 200, 1000])
ax1.legend()
ax1.set_ylabel("MAPE (%)")
ax1.set_xlabel("Experimental training data size")
ax1.annotate("A: $\sigma_{y}$", xy=(0.05, 0.95), xycoords="axes fraction",
              fontsize=12, ha="center",
              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))

ax2.errorbar(n, quadE, yerr = εquadE, color = 'blue')
ax2.errorbar(n, linE, yerr = εlinE, color = 'darkorange', linestyle = '--')
ax2.errorbar(n, rqE, yerr = εrqE, color = 'red', linestyle = '-.')
ax2.errorbar(n, rlE, yerr = εrlE, color = 'green', linestyle = ':')
ax2.set_yscale('log')
ax2.set_ylim([0.5, 1000])
ax2.set_xlim([-0.5, 16])
ax2.set_xticks([0, 5, 10, 15])
ax2.set_yticks([1, 5, 20, 100, 1000])
ax2.set_yticklabels([1, 5, 20, 100, 1000])
ax2.legend()
ax2.set_ylabel("MAPE (%)")
ax2.set_xlabel("Experimental training data size")
plt.subplots_adjust(bottom=0.180)
fig.tight_layout()
ax2.annotate("B: $E_{r}$", xy=(0.05, 0.95), xycoords="axes fraction",
              fontsize=12, ha="center",
              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))
plt.savefig("/Users/Joe/Desktop/NN_graphs/MFNN_2D3Dexp_lo.pdf", dpi=800, bbox_inches="tight")
plt.show()


# Comparison of different MFNNs
n = [1, 2, 3, 4, 5, 6, 8, 10, 15]
n_1 = [2, 3, 4, 5, 6, 8, 10, 15]
expσ = [454.05, 71.77, 49.45, 25.61, 27.66, 12.97, 7.66, 2.95]
εexpσ = [712.66, 49.57, 42.9, 14.01, 11.68, 5.78, 3.54, 3.24]
expE = [410.65, 126.05, 22.35, 14.34, 4.76, 3.64, 1.77, 0.9]
εexpE = [1105.96, 263.65, 14.69, 6.97, 2.52, 2.01, 0.57, 0.95]
# Quad 2
quad2σ = [1351.81, 452.26, 319.8, 177.61, 60.14, 46.42, 23.17, 15.56, 10.5]
εquad2σ = [1072.1, 511.24, 442.56, 310.37, 44.82, 19.6, 12.36, 7.49, 8.69]
quad2E = [51.58, 63.66, 79.89, 32.66, 11.93, 19.23, 9.25, 3.03, 0.99]
εquad2E = [17.24, 45.07, 93.41, 21.8, 7.54, 29.84, 10.76, 1.95, 1.56]
# Quad hi
quadσ = [43934.59, 1426.72, 478.59, 228.99, 169.88, 134.76, 92.12, 63.7, 21.94]
εquadσ = [121955.08, 1322.61, 446.62, 158.17, 90.84, 116.97, 73.74, 18.68, 5.01]
quadE = [1273.85, 313.26, 27.02, 20.79, 18.47, 20.26, 7.97, 6.8, 2.98]
εquadE = [2306.76, 397.27, 16.55, 9.3, 7.3, 20.55, 4.45, 4.21, 1.55]
# Quad lo
quadlσ = [1379.54, 161.92, 64.49, 74.03, 32.58, 32.72, 20.69, 11.22, 5.19]
εquadlσ = [1934.59, 172.95, 29.88, 34.79, 11.55, 11.12, 6.97, 3.15, 0.92]
quadlE = [240.18, 55.55, 38.79, 17.72, 9.4, 8.68, 3.24, 3.14, 0.97]
εquadlE = [106.19, 51.93, 58.11, 26.48, 4.46, 7.3, 2.03, 1.25, 0.4]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.errorbar(n, quadlσ, yerr = εquadlσ, color = 'blue', label = "MFNN, quadratic 2D & 3D FEM low training")
ax1.errorbar(n, quadσ, yerr = εquadσ, color = 'darkorange', linestyle = '--', label = "MFNN, quadratic 2D low + 3D FEM high")
ax1.errorbar(n, quad2σ, yerr = εquad2σ, color = 'red', linestyle = '-.', label = "MFNN, quadratic 3D low")
ax1.errorbar(n_1, expσ, yerr = εexpσ, color = 'green', linestyle = ':', label = "NN, experimental data")
ax1.set_yscale('log')
ax1.set_ylim([0.5, 1000])
ax1.set_xlim([-0.5, 16])
ax1.set_xticks([0, 5, 10, 15])
ax1.set_yticks([1, 10, 50, 200, 1000])
ax1.set_yticklabels([1, 20, 50, 200, 1000])
ax1.legend()
ax1.set_ylabel("MAPE (%)")
ax1.set_xlabel("Experimental training data size")
ax1.annotate("A: $\sigma_{y}$", xy=(0.05, 0.95), xycoords="axes fraction",
              fontsize=12, ha="center",
              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))

ax2.errorbar(n, quadlE, yerr = εquadlE, color = 'blue')
ax2.errorbar(n, quadE, yerr = εquadE, color = 'darkorange', linestyle = '--')
ax2.errorbar(n, quad2E, yerr = εquad2E, color = 'red', linestyle = '-.')
ax2.errorbar(n_1, expE, yerr = εexpE, color = 'green', linestyle = ':')
ax2.set_yscale('log')
ax2.set_ylim([0.5, 1000])
ax2.set_xlim([-0.5, 16])
ax2.set_xticks([0, 5, 10, 15])
ax2.set_yticks([1, 5, 20, 100, 1000])
ax2.set_yticklabels([1, 5, 20, 100, 1000])
ax2.legend()
ax2.set_ylabel("MAPE (%)")
ax2.set_xlabel("Experimental training data size")
plt.subplots_adjust(bottom=0.180)
fig.tight_layout()
ax2.annotate("B: $E_{r}$", xy=(0.05, 0.95), xycoords="axes fraction",
              fontsize=12, ha="center",
              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))
plt.savefig("/Users/Joe/Desktop/NN_graphs/NN_MFNN_compare_lo.pdf", dpi=800, bbox_inches="tight")
plt.show()
