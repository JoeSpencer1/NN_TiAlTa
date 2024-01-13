import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

'''
n = [1, 2, 3, 4, 5, 10, 20]
n1 = n
# 25˚C
Ti25E = [18.619205, 6.8593493, 6.0983825, 6.091887, 5.298505, 5.2244196, 3.6239312]
εTi25E = [1.6743975, 2.5646875, 1.9379541, 1.4813129, 1.9537387, 1.9212662, 2.01604]
Ti25σ = [34.068943, 18.617916, 43.272, 23.271488, 21.895184, 19.204937, 34.49958]
εTi25σ = [24.325975, 18.127224, 33.714092, 22.803173, 17.10482, 17.321714, 36.6192]
# 250˚C
Ti250E = [70.95709, 7.5985556, 8.114405, 1.6784289, 2.1151547, 1.8030748, 1.7651669]
εTi250E = [31.052818, 10.786752, 13.492649, 1.3040054, 1.0622171, 1.1414853, 1.182222]
Ti250σ = [261.21823, 25.825928, 49.60928, 17.916042, 17.266216, 16.254345, 47.430775]
εTi250σ = [270.2345, 23.495884, 65.91791, 15.266485, 21.114838, 16.953184, 59.20635]
# 500˚C/250˚C
Ti500E = [46.683464, 38.522774, 24.701038, 22.080563, 22.1474, 21.659185, 16.620623]
εTi500E = [6.765701, 10.513843, 11.301726, 10.384357, 9.72246, 11.2682905, 11.029994]
Ti500σ = [84.67531, 105.72215, 45.78838, 69.46997, 60.99529, 55.9422, 49.83204]
εTi500σ = [46.46603, 74.18298, 39.670254, 57.913757, 35.607227, 45.5547, 38.628445]
# 25˚C/250˚C
Ti25250E = [41.319565, 34.81656, 33.59124, 31.09554, 33.010456, 32.823563, 40.46569]
εTi25250E = [1.6541697, 6.365257, 4.6176863, 2.6873071, 3.4111104, 2.5400345, 8.93229]
Ti25250σ = [168.42062, 67.375565, 123.53137, 152.6323, 187.2847, 97.121, 52.3555]
εTi25250σ = [240.32188, 32.01899, 141.78886, 136.91542, 330.77194, 63.82302, 58.671406]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.errorbar(n, Ti25E, yerr = εTi25E, color = 'blue', label = "25˚C")
ax1.errorbar(n, Ti250E, yerr = εTi250E, color = 'red', label = "250˚C")
ax1.set_yscale('log')
ax1.set_ylim([0.5, 200])
ax1.set_xlim([0, 21])
ax1.set_xticks([0, 5, 10, 15, 20])
ax1.set_yticks([1, 3, 10, 30, 100])
ax1.set_yticklabels([1, 3, 10, 30, 100])
ax1.legend()
ax1.set_ylabel("MAPE (%)")
ax1.set_xlabel("Experimental training data size")
ax1.annotate("A: $E_{r}$", xy=(0.15, 0.95), xycoords="axes fraction",
              fontsize=12, ha="center",
              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))

ax2.errorbar(n1, Ti25σ, yerr = εTi25σ, color = 'blue', label = "25˚C")
ax2.errorbar(n1, Ti250σ, yerr = εTi250σ, color = 'red', label = "25˚C")
ax2.set_yscale('log')
ax2.set_ylim([10, 600])
ax2.set_xlim([-0.5, 21])
ax2.set_xticks([0, 5, 10, 15, 20])
ax2.set_yticks([10, 20, 50, 100, 200, 500])
ax2.set_yticklabels([10, 20, 50, 100, 200, 500])
ax2.legend()
ax2.set_ylabel("MAPE (%)")
ax2.set_xlabel("Experimental training data size")
plt.subplots_adjust(bottom=0.180)
fig.tight_layout()
ax2.annotate("B: $\sigma_{y}$", xy=(0.15, 0.95), xycoords="axes fraction",
              fontsize=12, ha="center",
              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))
plt.savefig("/Users/Joe/Desktop/figure1.jpeg", dpi=800, bbox_inches="tight")
plt.show()
'''
'''
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.errorbar(n, Ti25250E, yerr = εTi25250E, color = 'blue', label = "25˚C")
ax1.errorbar(n, Ti250E, yerr = εTi250E, color = 'red', label = "250˚C")
ax1.errorbar(n, Ti500E, yerr = εTi500E, color = 'black', label = "500˚C")
ax1.set_yscale('log')
ax1.set_ylim([0.5, 200])
ax1.set_xlim([0, 21])
ax1.set_xticks([0, 5, 10, 15, 20])
ax1.set_yticks([1, 3, 10, 30, 100])
ax1.set_yticklabels([1, 3, 10, 30, 100])
ax1.legend()
ax1.set_ylabel("MAPE (%)")
ax1.set_xlabel("Experimental training data size")
ax1.annotate("A: $E_{r}$ (250˚C)", xy=(0.15, 0.95), xycoords="axes fraction",
              fontsize=12, ha="center",
              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))

ax2.errorbar(n1, Ti25250σ, yerr = εTi25250σ, color = 'blue', label = "25˚C")
ax2.errorbar(n1, Ti250σ, yerr = εTi250σ, color = 'red', label = "250˚C")
ax2.errorbar(n1, Ti500σ, yerr = εTi500σ, color = 'black', label = "500˚C")
ax2.set_yscale('log')
ax2.set_ylim([10, 600])
ax2.set_xlim([-0.5, 21])
ax2.set_xticks([0, 5, 10, 15, 20])
ax2.set_yticks([10, 20, 50, 100, 200, 500])
ax2.set_yticklabels([10, 20, 50, 100, 200, 500])
ax2.legend()
ax2.set_ylabel("MAPE (%)")
ax2.set_xlabel("Experimental training data size")
plt.subplots_adjust(bottom=0.180)
fig.tight_layout()
ax2.annotate("B: $\sigma_{y}$ (250˚C)", xy=(0.15, 0.95), xycoords="axes fraction",
              fontsize=12, ha="center",
              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))
plt.savefig("/Users/Joe/Desktop/figure2.jpeg", dpi=800, bbox_inches="tight")
plt.show()
'''
'''
n = [1, 2, 3, 4, 5, 10, 20]
n1 = n
# 25˚C
Ti750E = [154.16795, 25.680262, 10.1573925, 7.744658, 5.137566, 2.6173031, 1.9064773]
εTi750E = [158.71921, 47.042423, 6.292157, 5.007044, 6.3082805, 1.3194628, 1.7983129]
Ti750σ = [537.51544, 187.94482, 16.950771, 38.089996, 26.567835, 22.038841, 34.741573]
εTi750σ = [822.8985, 455.4716, 22.714993, 39.45992, 35.60631, 25.618887, 42.27451]
# 250˚C
Ti25250500E = [44.90654, 41.499107, 39.673485, 39.662952, 38.275635, 44.390118, 45.897182]
εTi25250500E = [4.357474, 8.017073, 4.3895893, 5.539613, 4.685218, 15.8127165, 15.998017]
Ti25250500σ = [326.08405, 180.70842, 192.22061, 246.42114, 166.95808, 277.3227, 243.02325]
εTi25250500σ = [507.5874, 199.93362, 193.73439, 199.61105, 132.54443, 372.73825, 322.32126]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.errorbar(n, Ti25250500E, yerr = εTi25250500E, color = 'blue', label = "25$^{\circ}$C, 250$^{\circ}$C, 500$^{\circ}$C")
ax1.errorbar(n, Ti750E, yerr = εTi750E, color = 'red', label = "750˚C")
ax1.set_yscale('log')
ax1.set_ylim([0.5, 300])
ax1.set_xlim([0, 21])
ax1.set_xticks([0, 5, 10, 15, 20])
ax1.set_yticks([1, 3, 10, 30, 100])
ax1.set_yticklabels([1, 3, 10, 30, 100])
ax1.legend()
ax1.set_ylabel("MAPE (%)")
ax1.set_xlabel("Experimental training data size")
ax1.annotate("A: $E_{r}$ (750$^{\circ}$C)", xy=(0.15, 0.95), xycoords="axes fraction",
              fontsize=12, ha="center",
              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))

ax2.errorbar(n1, Ti25250500σ, yerr = εTi25250500σ, color = 'blue', label = "25$^{\circ}$C, 250$^{\circ}$C, 500$^{\circ}$C")
ax2.errorbar(n1, Ti750σ, yerr = εTi750σ, color = 'red', label = "750˚C")
ax2.set_yscale('log')
ax2.set_ylim([10, 1300])
ax2.set_xlim([-0.5, 21])
ax2.set_xticks([0, 5, 10, 15, 20])
ax2.set_yticks([10, 20, 50, 100, 200, 500])
ax2.set_yticklabels([10, 20, 50, 100, 200, 500])
ax2.legend()
ax2.set_ylabel("MAPE (%)")
ax2.set_xlabel("Experimental training data size")
plt.subplots_adjust(bottom=0.180)
fig.tight_layout()
ax2.annotate("B: $\sigma_{y}$ (750$^{\circ}$C)", xy=(0.15, 0.95), xycoords="axes fraction",
              fontsize=12, ha="center",
              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))
plt.savefig("/Users/Joe/Desktop/figure3.jpeg", dpi=800, bbox_inches="tight")
plt.show()
'''

Bqx = [0.125, 0.25, 0.5]
Bqy = [0.003352735, 0.013410939, 0.140242188]
Blx = [0.125, 0.25, 0.5]
Bly = [0.032266477, 0.12906591, 0.354190574]
Bfx = [0.01, 1.5]
C30x = [0.0125, 0.025, 0.05, 0.1]
C30y = [0.000446987, 0.001787949, 0.008582156, 0.037099946]
C45x = [0.0125, 0.025, 0.05]
C45y = [0.001166093, 0.004664373, 0.017291087]
C60x = [0.0125, 0.025, 0.05, 0.1]
C60y = [0.004029647, 0.016118587, 0.049746948, 0.17236334]
Cfx = [0.0001, 1]
def equation(x, y, eqx):
    l = len(x) - 1
    p = np.log10(y[l]/y[0])/np.log10(x[l]/x[0])
    C = 0
    for i in range(len(x)):
        C += y[i]/(len(x)*x[i]**p)
    print('C = ', C)
    print('p = ', p)
    eqy = [0, 0]
    for i in range(2):
        eqy[i] = C * eqx[i] ** p
    return eqy
Cf30 = equation(C30x, C30y, Cfx)
Cf45 = equation(C45x, C45y, Cfx)
Cf60 = equation(C60x, C60y, Cfx)
Bfq = equation(Bqx, Bqy, Bfx)
Bfl = equation(Blx, Bly, Bfx)

fig, ax = plt.subplots()
ax.scatter(C30x, C30y, color='blue', marker='s', label='30˚: $||e||_{L_{2}}=4.95h^{2.13}$')
ax.scatter(C45x, C45y, color='black', marker='o', facecolor='none', label='45˚: $||e||_{L_{2}}=5.87h^{1.95}$')
ax.scatter(C60x, C60y, color='red', marker='x', label='60˚: $||e||_{L_{2}}=11.03h^{1.81}$')
ax.plot(Cfx, Cf30, linestyle="--", color='blue')
ax.plot(Cfx, Cf45, linestyle="--", color='black')
ax.plot(Cfx, Cf60, linestyle="--", color='red')
ax.set_xlabel('Element length (μm)')
ax.set_xscale('log')
ax.set_xlim([0.006, 0.2])
ax.set_ylabel('L$_{2}$ error')
ax.set_yscale('log')
ax.set_ylim([0.0003, 0.7])
ax.grid(False)
leg = ax.legend(loc='lower right')
leg.set_title('Conical half-angle')
plt.savefig('/Users/joe/Desktop/figure3.jpeg', dpi=800, bbox_inches="tight")
plt.show()

fig, ax = plt.subplots()
ax.scatter(Blx, Bly, color='blue', marker='s', label='Linear: $||e||_{L_{2}}=1.17h^{1.73}$')
ax.scatter(Bqx, Bqy, color='black', marker='o', facecolor='none', label='Quadratic: $||e||_{L_{2}}=0.91h^{2.69}$')
ax.plot(Bfx, Bfl, linestyle="--", color='blue')
ax.plot(Bfx, Bfq, linestyle="--", color='black')
ax.set_xlabel('Element length (μm)')
ax.set_xscale('log')
ax.set_xlim([0.05, 1])
ax.set_ylabel('L$_{2}$ error')
ax.set_yscale('log')
ax.set_ylim([0.001, 1])
ax.grid(False)
leg = ax.legend(loc='lower right')
leg.set_title('Element order')
plt.savefig('/Users/joe/Desktop/figure4.jpeg', dpi=800, bbox_inches="tight")
plt.show()

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
ax.set_xlabel('Indenter depth (nm)')
ax.set_xlim([0, 275])
ax.set_ylabel('Load (μN)')
ax.set_ylim([0, 11000])
ax.grid(False)
leg = ax.legend()
plt.savefig('/Users/joe/Desktop/figure5.jpeg', dpi=800, bbox_inches="tight")
plt.show()
'''