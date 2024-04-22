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
expσ = []
εexpσ = []
expE = []
εexpE = []

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

''''''
# NN trained using only 3D FEM data
n = [2, 3, 4, 5, 6, 8, 10, 15]
# Quad
quadσ = []
εquadσ = []
quadE = []
εquadE = []
# Linear
linσ = []
εlinσ = []
linE = []
εlinE = []
# Rough quad
rqσ = []
εrqσ = []
rqE = []
εrqE = []
# Rough linear
rlσ = []
εrlσ = []
rlE = []
εrlE = []

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.errorbar(n, quadσ, yerr = εquadσ, color = 'blue', label = "MAPE with quadratic 3D FEM training data")
ax1.errorbar(n, linσ, yerr = εlinσ, color = 'darkorange', linestyle = '--', label = "MAPE with linear 3D FEM training data")
ax1.errorbar(n, rqσ, yerr = εrqσ, color = 'red', linestyle = '-.', label = "MAPE with rough quadratic 3D FEM training data")
ax1.errorbar(n, rlσ, yerr = εrlσ, color = 'green', linestyle = ':', label = "MAPE with rough linear 3D FEM training data")
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
ax2.errorbar(n, rqE, yerr = εrqE, color = 'red', linestyle = '-.')
ax2.errorbar(n, rlE, yerr = εrlE, color = 'green', linestyle = ':')
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

''''''
# NN trained using only 2D FEM data
n = [2, 3, 4, 5, 6, 8, 10, 15]
# Quad
quadσ = []
εquadσ = []
quadE = []
εquadE = []
# Linear
linσ = []
εlinσ = []
linE = []
εlinE = []
# Rough quadratic
rqσ = []
εrqσ = []
rqE = []
εrqE = []
# Rough linear
rlσ = []
εrlσ = []
rlE = []
εrlE = []

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.errorbar(n, quadσ, yerr = εquadσ, color = 'blue', label = "MAPE with quadratic 2D FEM training data")
ax1.errorbar(n, linσ, yerr = εlinσ, color = 'darkorange', linestyle = '--', label = "MAPE with linear 2D FEM training data")
ax1.errorbar(n, rqσ, yerr = εrqσ, color = 'red', linestyle = '-.', label = "MAPE with rough quadratic 2D FEM training data")
ax1.errorbar(n, rlσ, yerr = εrlσ, color = 'green', linestyle = ':', label = "MAPE with rough linear 2D FEM training data")
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
ax2.errorbar(n, rqE, yerr = εrqE, color = 'red', linestyle = '-.')
ax2.errorbar(n, rlE, yerr = εrlE, color = 'green', linestyle = ':')
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

''''''
# NN trained using 3D FEM + exp data
n = [0, 1,2, 3, 4, 5, 6, 8, 10, 15]
# Quad
quadσ = []
εquadσ = []
quadE = []
εquadE = []
# Linear
linσ = []
εlinσ = []
linE = []
εlinE = []
# Rough quadratic
rqσ = []
εrqσ = []
rqE = []
εrqE = []
# Rough linear
rlσ = []
εrlσ = []
rlE = []
εrlE = []

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.errorbar(n, quadσ, yerr = εquadσ, color = 'blue', label = "MFNN trained with quadratic 3D FEM training data")
ax1.errorbar(n, linσ, yerr = εlinσ, color = 'darkorange', linestyle = '--', label = "MAPE with linear 3D FEM training data")
ax1.errorbar(n, rqσ, yerr = εrqσ, color = 'red', linestyle = '-.', label = "MAPE with rough quadratic 3D FEM training data")
ax1.errorbar(n, rlσ, yerr = εrlσ, color = 'green', linestyle = ':', label = "MAPE with rough linear 3D FEM training data")
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
ax2.errorbar(n, rqE, yerr = εrqE, color = 'red', linestyle = '-.')
ax2.errorbar(n, rlE, yerr = εrlE, color = 'green', linestyle = ':')
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

''''''
# NN trained using 2D FEM + exp data
n = [0, 1,2, 3, 4, 5, 6, 8, 10, 15]
# Quad
quadσ = []
εquadσ = []
quadE = []
εquadE = []
# Linear
linσ = []
εlinσ = []
linE = []
εlinE = []
# Rough quadratic
rqσ = []
εrqσ = []
rqE = []
εrqE = []
# Rough linear
rlσ = []
εrlσ = []
rlE = []
εrlE = []

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.errorbar(n, quadσ, yerr = εquadσ, color = 'blue', label = "MFNN trained with quadratic 2D FEM training data")
ax1.errorbar(n, linσ, yerr = εlinσ, color = 'darkorange', linestyle = '--', label = "MAPE with linear 2D FEM training data")
ax1.errorbar(n, rqσ, yerr = εrqσ, color = 'red', linestyle = '-.', label = "MAPE with rough quadratic 2D FEM training data")
ax1.errorbar(n, rlσ, yerr = εrlσ, color = 'green', linestyle = ':', label = "MAPE with rough linear 2D FEM training data")
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
ax2.errorbar(n, rqE, yerr = εrqE, color = 'red', linestyle = '-.')
ax2.errorbar(n, rlE, yerr = εrlE, color = 'green', linestyle = ':')
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

''''''
# NN trained using 2D FEM + 3D FEM + exp data
n = [1, 2, 3, 4, 5, 6, 8, 10, 15]
# Quad hi
quadσ = []
εquadσ = []
quadE = []
εquadE = []
# Linear hi
linσ = []
εlinσ = []
linE = []
εlinE = []
# Rough quadratic hi
rqσ = []
εrqσ = []
rqE = []
εrqE = []
# Rough linear hi
rlσ = []
εrlσ = []
rlE = []
εrlE = []

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.errorbar(n, quadσ, yerr = εquadσ, color = 'blue', label = "MFNN with quadratic FEM training data")
ax1.errorbar(n, linσ, yerr = εlinσ, color = 'darkorange', linestyle = '--', label = "MAPE with linear FEM training data")
ax1.errorbar(n, rqσ, yerr = εrqσ, color = 'red', linestyle = '-.', label = "MAPE with rough quadratic FEM training data")
ax1.errorbar(n, rlσ, yerr = εrlσ, color = 'green', linestyle = ':', label = "MAPE with rough linear FEM training data")
ax1.set_yscale('log')
ax1.set_ylim([3, 500])
ax1.set_xlim([-0.5, 16])
ax1.set_xticks([0, 5, 10, 15])
ax1.set_yticks([5, 20, 100, 200, 500])
ax1.set_yticklabels([5, 20, 100, 200, 500])
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
ax2.set_ylim([0.5, 200])
ax2.set_xlim([-0.5, 16])
ax2.set_xticks([0, 5, 10, 15])
ax2.set_yticks([1, 5, 20, 50, 200])
ax2.set_yticklabels([1, 5, 20, 50, 200])
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
quadσ = []
εquadσ = []
quadE = []
εquadE = []
# Linear lo
linσ = []
εlinσ = []
linE = []
εlinE = []
# Rough quadratic lo
rqσ = []
εrqσ = []
rqE = []
εrqE = []
# Rough linear lo
rlσ = []
εrlσ = []
rlE = []
εrlE = []

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.errorbar(n, quadσ, yerr = εquadσ, color = 'blue', label = "MFNN with quadratic FEM training data")
ax1.errorbar(n, linσ, yerr = εlinσ, color = 'darkorange', linestyle = '--', label = "MAPE with linear FEM training data")
ax1.errorbar(n, rqσ, yerr = εrqσ, color = 'red', linestyle = '-.', label = "MAPE with rough quadratic FEM training data")
ax1.errorbar(n, rlσ, yerr = εrlσ, color = 'green', linestyle = ':', label = "MAPE with rough linear FEM training data")
ax1.set_yscale('log')
ax1.set_ylim([3, 500])
ax1.set_xlim([-0.5, 16])
ax1.set_xticks([0, 5, 10, 15])
ax1.set_yticks([5, 20, 100, 200, 500])
ax1.set_yticklabels([5, 20, 100, 200, 500])
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
ax2.set_ylim([0.5, 200])
ax2.set_xlim([-0.5, 16])
ax2.set_xticks([0, 5, 10, 15])
ax2.set_yticks([1, 5, 20, 50, 200])
ax2.set_yticklabels([1, 5, 20, 50, 200])
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