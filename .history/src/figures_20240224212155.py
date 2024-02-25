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
'''
'''
Bqx = [0.5, 0.25, 0.125]
Bqy = [0.05743, 0.03417, 0.00854]
Blx = [0.25, 0.125, 0.0625]
Bly = [0.16434, 0.14397, 0.03599]
Bfx = [0.01, 1.5]
C30x = [0.050, 0.025, 0.0125]
C30y = [0.00193, 0.00029, 0.00007]
C45x = [0.100, 0.050, 0.025, 0.0125]
C45y = [0.10706, 0.01024, 0.00738, 0.00185]
C60x = [0.050, 0.025, 0.0125]
C60y = [0.01087, 0.00156, 0.00039]
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
ax.scatter(C30x, C30y, color='blue', marker='s', label='30˚: $||e||_{L_{2}}=2.30h^{2.36}$')
ax.scatter(C45x, C45y, color='red', marker='o', facecolor='none', label='45˚: $||e||_{L_{2}}=14.42h^{2.40}$')
ax.scatter(C60x, C60y, color='black', marker='x', label='60˚: $||e||_{L_{2}}=9.60h^{1.95}$')
ax.plot(Cfx, Cf30, linestyle="--", color='blue')
ax.plot(Cfx, Cf45, linestyle="--", color='red')
ax.plot(Cfx, Cf60, linestyle="--", color='black')
ax.set_xlabel('Element length (μm)')
ax.set_xscale('log')
ax.set_xlim([0.006, 0.2])
ax.set_ylabel('L$_{2}$ error')
ax.set_yscale('log')
ax.set_ylim([0.00003, 0.4])
ax.grid(False)
leg = ax.legend(loc='lower right')
leg.set_title('Conical half-angle')
plt.savefig('/Users/joe/Desktop/figure3.jpeg', dpi=800, bbox_inches="tight")
plt.show()

fig, ax = plt.subplots()
ax.scatter(Blx, Bly, color='blue', marker='s', label='Linear: $||e||_{L_{2}}=0.75h^{1.10}$')
ax.scatter(Bqx, Bqy, color='red', marker='o', facecolor='none', label='Quadratic: $||e||_{L_{2}}=0.15h^{1.37}$')
ax.plot(Bfx, Bfl, linestyle="--", color='blue')
ax.plot(Bfx, Bfq, linestyle="--", color='red')
ax.set_xlabel('Element length (μm)')
ax.set_xscale('log')
ax.set_xlim([0.03, 1])
ax.set_ylabel('L$_{2}$ error')
ax.set_yscale('log')
ax.set_ylim([0.001, 1])
ax.grid(False)
leg = ax.legend(loc='lower right')
leg.set_title('Element order')
plt.savefig('/Users/joe/Desktop/figure4.jpeg', dpi=800, bbox_inches="tight")
plt.show()
'''
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
'''
n = [0, 5, 10, 20]
threeσ = [376.0572733054678, 39.5938033843615, 41.8456251546561, 37.20982506131551]
εthreeσ = [196.86908836541178, 21.68148559652081, 28.00063811133066, 28.472024602496692]
threeE = [27.637875079481226, 1.8371707313939147, 0.9618014686986018, 0.6094185678582443]
εthreeE = [16.76186263408408, 0.7040937053244141, 0.5416984171832155, 0.1433441723448427]
FEAExpσ = [10340.612, 30.692963398804512, 17.966434316750032, 20.30981467660651]
εFEAExpσ = [4267.742, 24.432717466772974, 17.157632184190486, 15.24454689795884]
FEAExpE = [452.68634, 3.1407760620117187, 0.8857396979081005, 0.48970565795898435]
εFEAExpE = [60.762478, 2.1787414072193108, 0.20985072884833247, 0.24028577974579077]
BerExpσ = [3993.4524, 29.085435433129238, 7.699660556574902, 3.526308835701772]
εBerExpσ = [2809.7415, 11.931510220287686, 4.180595260183477, 4.05852053586458]
BerExpE = [43.70184, 5.2056050250404775, 2.3034492091128698, 0.5525932111238178]
εBerExpE = [31.433922, 2.364614922311323, 2.124353990665903, 0.8359455695302426]
FEABerσ = [16360.667, 224.50905550158168, 318.32331392100775, 411.2046768176986]
εFEABerσ = [10235.277, 105.82854182729396, 210.21371442021476, 242.1779691403267]
FEABerE = [462.53745, 50.763517706017744, 35.24591202986868, 35.340911950563125]
εFEABerE = [74.264534, 20.539216787616077, 17.80116783395519, 8.634077709953575]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.errorbar(n, threeσ, yerr = εthreeσ, color = 'blue', label = "All three")
ax1.errorbar(n, BerExpσ, yerr = εBerExpσ, color = 'green', label = "Berkovich/Exp")
ax1.errorbar(n, FEAExpσ, yerr = εFEAExpσ, color = 'grey', label = "FEA/Exp")
ax1.errorbar(n, FEABerσ, yerr = εFEABerσ, color = 'red', label = "FEA/Berkovich")
ax1.set_yscale('linear')
ax1.set_ylim([0, 1200])
ax1.set_xlim([-0.5, 21])
ax1.set_xticks([0, 5, 10, 15, 20])
ax1.set_yticks([0, 100, 200, 300, 400, 500, 1000])
ax1.set_yticklabels([0, 100, 200, 300, 400, 500, 1000])
ax1.legend()
ax1.set_ylabel("MAPE (%)")
ax1.set_xlabel("Experimental training data size")
ax1.annotate("A: $\sigma_{y}$", xy=(0.15, 0.95), xycoords="axes fraction",
              fontsize=12, ha="center",
              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))

ax2.errorbar(n, threeE, yerr = εthreeE, color = 'blue', label = "All three")
ax2.errorbar(n, BerExpE, yerr = εBerExpE, color = 'green', label = "Berkovich/Exp")
ax2.errorbar(n, FEAExpE, yerr = εFEAExpE, color = 'grey', label = "FEA/Exp")
ax2.errorbar(n, FEABerE, yerr = εFEABerE, color = 'red', label = "FEA/Berkovich")
ax2.set_yscale('linear')
ax2.set_ylim([0, 500])
ax2.set_xlim([-0.5, 21])
ax2.set_xticks([0, 5, 10, 15, 20])
ax2.set_yticks([0, 40, 100, 300])
ax2.set_yticklabels([0, 40, 100, 300])
ax2.legend()
ax2.set_ylabel("MAPE (%)")
ax2.set_xlabel("Experimental training data size")
plt.subplots_adjust(bottom=0.180)
fig.tight_layout()
ax2.annotate("B: $E_{r}$", xy=(0.15, 0.95), xycoords="axes fraction",
              fontsize=12, ha="center",
              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))
plt.savefig("/Users/Joe/Desktop/figure1.jpeg", dpi=800, bbox_inches="tight")
plt.show()
'''
'''
# 2D FEM plot
n_30 = [5, 10, 15, 20, 25, 30, 35, 40]
c30σ = [60.18876, 44.969826, 47.465202, 61.82657, 52.733135, 35.656128, 40.851677, 13.14303]
εc30σ = [41.206966, 27.921497, 38.5343, 68.33482, 49.83972, 44.069607, 53.421883, 3.7868276]
c30E = [6.7017927, 3.968275, 3.2684226, 3.115778, 3.8301284, 0.48159194, 0.44056806, 0.51108503]
εc30E = [3.8387244, 4.64504, 5.1517644, 5.197127, 6.792287, 0.16580099, 0.21634454, 0.27333787]
n_45 = [5, 10, 15, 20, 25, 30, 35, 40]
c45σ = [47.69543, 36.88656, 49.16212, 69.39226, 38.905285, 35.58552, 39.764732, 13.041214]
εc45σ = [34.60377, 26.898079, 48.949436, 79.412865, 36.342518, 43.10947, 52.700333, 3.8021903]
c45E = [6.8221407, 3.6736221, 2.6227307, 2.6362934, 3.6511178, 1.1328148, 1.0110619, 0.94891435]
εc45E = [4.168493, 4.141034, 3.486758, 3.2869203, 5.257216, 0.4206212, 0.40799123, 0.44324088]
n_60 = [5, 10, 15, 20, 25, 30, 35, 40]
c60σ = [56.82661, 59.390118, 43.545666, 62.64787, 57.540466, 34.09452, 37.99452, 12.12359]
εc60σ = [51.9622, 49.808273, 40.93228, 68.1315, 56.818974, 43.810177, 51.654713, 4.199802]
c60E = [2.2587574, 1.553577, 1.2308276, 1.1793786, 1.2517836, 0.40467867, 0.46838742, 0.4566309]
εc60E = [1.823878, 1.6410633, 1.4770961, 1.3812854, 1.595665, 0.15322132, 0.16536641, 0.18179524]
n_70 = [5, 10, 15, 20, 25, 30, 35, 40]
c70σ = [62.534313, 46.959476, 44.965855, 42.311863, 67.861046, 46.759636, 47.27385, 16.88904]
εc70σ = [35.405556, 31.7435, 53.33709, 35.76007, 59.417057, 41.19558, 48.47632, 5.148048]
c70E = [2.8892665, 2.4597995, 2.64531, 2.3275874, 1.7165909, 1.1549096, 1.2989982, 1.1708868]
εc70E = [1.680209, 1.8020929, 2.3944137, 2.0285802, 1.329095, 0.542358, 0.5996636, 0.542196]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.errorbar(n_30, c30σ, yerr = εc30σ, color = 'blue', label = "30˚ (n$_{tr}$=58)")
ax1.errorbar(n_45, c45σ, yerr = εc45σ, color = 'green', label = "45˚ (n$_{tr}$=58)")
ax1.errorbar(n_60, c60σ, yerr = εc60σ, color = 'grey', label = "60˚ (n$_{tr}$=58)")
ax1.errorbar(n_70, c70σ, yerr = εc70σ, color = 'red', label = "70.3˚ (n$_{tr}$=58)")
ax1.set_yscale('linear')
ax1.set_ylim([0, 120])
ax1.set_xlim([-0.5, 41])
ax1.set_xticks([0, 10, 20, 30, 40])
ax1.set_yticks([0, 20, 40, 60, 80, 100])
ax1.set_yticklabels([0, 20, 40, 60, 80, 100])
ax1.legend()
ax1.set_ylabel("MAPE (%)")
ax1.set_xlabel("2D FEM training data size")
ax1.annotate("A: $\sigma_{y}$", xy=(0.15, 0.95), xycoords="axes fraction",
              fontsize=12, ha="center",
              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))

ax2.errorbar(n_30, c30E, yerr = εc30E, color = 'blue', label = "30˚")
ax2.errorbar(n_45, c45E, yerr = εc45E, color = 'green', label = "45˚")
ax2.errorbar(n_60, c60E, yerr = εc60E, color = 'grey', label = "60˚")
ax2.errorbar(n_70, c70E, yerr = εc70E, color = 'red', label = "70.3˚")
ax2.set_yscale('linear')
ax2.set_ylim([0, 12])
ax2.set_xlim([-0.5, 41])
ax2.set_xticks([0, 10, 20, 30, 40])
ax2.set_yticks([2, 4, 6, 8, 10])
ax2.set_yticklabels([2, 4, 6, 8, 10])
ax2.legend()
ax2.set_ylabel("MAPE (%)")
ax2.set_xlabel("2D FEM training data size")
plt.subplots_adjust(bottom=0.180)
fig.tight_layout()
ax2.annotate("B: $E_{r}$", xy=(0.15, 0.95), xycoords="axes fraction",
              fontsize=12, ha="center",
              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))
plt.savefig("/Users/Joe/Desktop/figure1.jpeg", dpi=800, bbox_inches="tight")
plt.show()
''''''

# 3D FEM plot
r_x = [1, 2, 3, 4, 5, 6, 8, 10]
r_σ = [31.167276, 24.943111, 20.253149, 15.603119, 11.571823, 14.716022, 25.289545, 10.5968075]
εr_σ = [27.557905, 26.2535, 26.97568, 15.423944, 10.414749, 16.37767, 40.68997, 13.132583]
r_E = [25.682007, 16.355625, 14.56958, 6.826603, 4.200863, 2.6998656, 2.2280948, 2.012631]
εr_E = [8.459303, 10.0506, 10.471922, 7.449751, 6.624577, 3.3484201, 2.7749627, 1.8120223]
s_x = [1, 2, 3, 4, 5, 10, 15, 20]
s_σ = [36.33727, 16.587528, 32.654137, 26.998251, 21.507994, 6.641703, 11.909295, 27.69657]
εs_σ = [31.16571, 8.561503, 43.09252, 28.568037, 24.293598, 6.7919755, 10.9536705, 18.105864]
s_E = [33.29425, 14.667213, 12.1152315, 8.055034, 4.9854064, 3.2479203, 2.2900672, 2.1973984]
εs_E = [12.97419, 13.794886, 9.608465, 9.460078, 2.1073222, 2.6266623, 1.3813006, 1.1200465]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.errorbar(r_x, r_σ, yerr = εr_σ, color = 'blue', label = "Rough (n$_{tr}$=11)")
ax1.errorbar(s_x, s_σ, yerr = εs_σ, color = 'green', label = "Refined (n$_{tr}$=26)")
ax1.set_yscale('linear')
ax1.set_ylim([0, 20])
ax1.set_xlim([-0.5, 21])
ax1.set_xticks([0, 5, 10, 15, 20])
ax1.set_yticks([0, 20, 40, 60])
ax1.set_yticklabels([0, 20, 40, 60])
ax1.legend()
ax1.set_ylabel("MAPE (%)")
ax1.set_xlabel("3D FEM training data size")
ax1.annotate("A: $\sigma_{y}$", xy=(0.15, 0.95), xycoords="axes fraction",
              fontsize=12, ha="center",
              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))

ax2.errorbar(r_x, r_E, yerr = εr_E, color = 'blue', label = "Rough")
ax2.errorbar(s_x, s_E, yerr = εs_E, color = 'green', label = "Refined")
ax2.set_yscale('linear')
ax2.set_ylim([0, 50])
ax2.set_xlim([-0.5, 21])
ax2.set_xticks([0, 5, 10, 15, 20])
ax2.set_yticks([10, 20, 30, 40, 50])
ax2.set_yticklabels([10, 20, 30, 40, 50])
ax2.legend()
ax2.set_ylabel("MAPE (%)")
ax2.set_xlabel("3D FEM training data size")
plt.subplots_adjust(bottom=0.180)
fig.tight_layout()
ax2.annotate("B: $E_{r}$", xy=(0.15, 0.95), xycoords="axes fraction",
              fontsize=12, ha="center",
              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))
plt.savefig("/Users/Joe/Desktop/figure2.jpeg", dpi=800, bbox_inches="tight")
plt.show()
'''
'''
# Exp data
ex_x = [2, 4, 6, 8, 10, 12, 14, 16]
ex_σ = [17.503685, 26.466599, 21.911015, 22.106192, 45.090057, 28.716232, 48.521652, 36.83198]
εex_σ = [13.739083, 14.606619, 10.539335, 9.395743, 32.86384, 21.917978, 35.697067, 26.285158]
ex_E = [7.4552474, 5.515073, 4.4371285, 4.143283, 4.210283, 4.4349427, 3.7818809, 3.8236954]
εex_E = [1.4885967, 2.467008, 1.3652551, 1.0471737, 1.6728787, 1.4284903, 1.4719386, 1.6564999]
# 3D data
s_x = [1, 2, 3, 4, 5, 10, 15, 20]
s_σ = [36.33727, 16.587528, 32.654137, 26.998251, 21.507994, 6.641703, 11.909295, 27.69657]
εs_σ = [31.16571, 8.561503, 43.09252, 28.568037, 24.293598, 6.7919755, 10.9536705, 18.105864]
s_E = [33.29425, 14.667213, 12.1152315, 8.055034, 4.9854064, 3.2479203, 2.2900672, 2.1973984]
εs_E = [12.97419, 13.794886, 9.608465, 9.460078, 2.1073222, 2.6266623, 1.3813006, 1.1200465]
# 2D data
n_70 = [5, 10, 15, 20, 25, 30, 35, 40]
c70σ = [62.534313, 46.959476, 44.965855, 42.311863, 67.861046, 46.759636, 47.27385, 16.88904]
εc70σ = [35.405556, 31.7435, 53.33709, 35.76007, 59.417057, 41.19558, 48.47632, 5.148048]
c70E = [2.8892665, 2.4597995, 2.64531, 2.3275874, 1.7165909, 1.1549096, 1.2989982, 1.1708868]
εc70E = [1.680209, 1.8020929, 2.3944137, 2.0285802, 1.329095, 0.542358, 0.5996636, 0.542196]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.errorbar(n_70, c70σ, yerr = εc70σ, color = 'green', label = "2D FEM (70.3˚)")
ax1.errorbar(s_x, s_σ, yerr = εs_σ, color = 'red', label = "3D FEM")
ax1.errorbar(ex_x, ex_σ, yerr = εex_σ, color = 'blue', label = "Experiment")
ax1.set_yscale('linear')
ax1.set_ylim([0, 120])
ax1.set_xlim([-0.5, 41])
ax1.set_xticks([0, 10, 20, 30, 40])
ax1.set_yticks([0, 20, 40, 60, 80, 100])
ax1.set_yticklabels([0, 20, 40, 60, 80, 100])
ax1.legend()
ax1.set_ylabel("MAPE (%)")
ax1.set_xlabel("Experimental training data size")
ax1.annotate("A: $\sigma_{y}$", xy=(0.15, 0.95), xycoords="axes fraction",
              fontsize=12, ha="center",
              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))

ax2.errorbar(n_70, c70E, yerr = εc70E, color = 'green', label = "2D FEM (n$_{tr}$=58)")
ax2.errorbar(s_x, s_E, yerr = εs_E, color = 'red', label = "3D FEM (n$_{tr}$=26)")
ax2.errorbar(ex_x, ex_E, yerr = εex_E, color = 'blue', label = "Experiment (n$_{tr}$=25)")
ax2.set_yscale('linear')
ax2.set_ylim([0, 12])
ax2.set_xlim([-0.5, 41])
ax2.set_xticks([0, 10, 20, 30, 40])
ax2.set_yticks([2, 4, 6, 8, 10])
ax2.set_yticklabels([2, 4, 6, 8, 10])
ax2.legend()
ax2.set_ylabel("MAPE (%)")
ax2.set_xlabel("Experimental training data size")
plt.subplots_adjust(bottom=0.180)
fig.tight_layout()
ax2.annotate("B: $E_{r}$", xy=(0.15, 0.95), xycoords="axes fraction",
              fontsize=12, ha="center",
              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))
plt.savefig("/Users/Joe/Desktop/trainingsources.jpeg", dpi=800, bbox_inches="tight")
plt.show()


categories = ['Physical', 'Fine 3D FEM', 'Rough 3D FEM', '2D FEM (70.3˚)']
σvalues = [45.090057, 70.12297, 82.563194, 58.66543]
σerrors = [32.86384, 22.982897, 28.687885, 19.887922]
Evalues = [4.210283, 3.5263298, 5.338781, 9.962336]
Eerrors = [1.6728787, 2.66636, 3.444265, 0.95166034]

colors = ['darkred', 'green', 'gray', 'blue']
bar_width = 0.15
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.bar(categories, σvalues, yerr=σerrors, capsize=4, color=colors)
ax1.set_yticks([0, 25, 50, 75, 100])
ax1.set_yticklabels([0, 25, 50, 75, 100])
ax1.set_xlabel('Trainind data type')
ax1.tick_params(axis='x', labelsize=8)
ax1.set_ylabel('MAPE (%)')
plt.subplots_adjust(bottom=0.18)
ax1.annotate("A: $\sigma_{y}$", xy=(0.15, 0.95), xycoords="axes fraction",
              fontsize=12, ha="center",
              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))
ax2.bar(categories, Evalues, yerr=Eerrors, capsize=4, color=colors)
ax2.set_yticks([0, 2, 4, 6, 8, 10])
ax2.tick_params(axis='x', labelsize=8)
ax2.set_yticklabels([0, 2, 4, 6, 8, 10])
ax2.set_xlabel('Trainind data type')
ax2.set_ylabel('MAPE (%)')
plt.subplots_adjust(bottom=0.18)
ax2.annotate("B: $E_{r}$", xy=(0.15, 0.95), xycoords="axes fraction",
              fontsize=12, ha="center",
              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))
plt.savefig("/Users/Joe/Desktop/trainingerrors.jpeg", dpi=800, bbox_inches="tight")
plt.show()
'''
'''
# Lu's data, digitized fig. 2 from paper
n_lu = [10, 20, 30, 40, 50, 60, 70, 80]
luσ = [126.59981, 74.7933, 49.3204, 48.40326, 43.34291, 38.5812, 40.6214, 39.11309]
εluσ = [126.59981-126.0069, 74.7933-41.0649, 49.3204-41.6276, 48.40326-37.45651, 43.34291-37.13045, 38.5812-32.6623, 40.6214-33.2250, 39.11309-31.12437]
luE = [14.31427, 6.67098, 6.20802, 5.507686, 4.74777, 4.4628, 4.3559, 4.54563]
εluE = [14.31427-7.84565, 6.67098-4.890341, 6.20802-4.902166, 5.507686-4.32074, 4.74777-4.5697, 4.4628-3.9287, 4.3559-3.88121, 4.54563-3.71499]
# My version of lu's 70.3˚ FEM data
n_me = [10, 20, 30, 40, 50, 60, 70, 80]
meσ = [129.715, 74.073235, 52.414314, 41.575752, 49.87278, 38.934593, 39.65153, 40.450726]
εmeσ = [77.584915, 27.026743, 13.707746, 5.507115, 9.828185, 6.028146, 6.7208185, 8.7345]
meE = [13.2443695, 8.132007, 6.264584, 5.5313954, 4.8793535, 4.9000173, 4.4977903, 4.7119946]
εmeE = [3.303954, 3.1866722, 1.7214556, 0.9339477, 0.63589025, 0.47832343, 0.6403632, 1.3723232]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.errorbar(n_me, meσ, yerr = εmeσ, linestyle = '--', color = 'red', label = "My replication")
ax1.errorbar(n_lu, luσ, yerr = εluσ, color = 'green', label = "Lu's NN (70.3˚)")
ax1.set_yscale('linear')
ax1.set_ylim([0, 150])
ax1.set_xlim([-0.5, 90])
ax1.set_xticks([0, 20, 40, 60, 80])
ax1.set_yticks([0, 20, 40, 60, 80, 100])
ax1.set_yticklabels([0, 20, 40, 60, 80, 100])
ax1.legend()
ax1.set_ylabel("MAPE (%)")
ax1.set_xlabel("2D FEM training data size")
ax1.annotate("A: $\sigma_{y}$", xy=(0.05, 0.95), xycoords="axes fraction",
              fontsize=12, ha="center",
              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))

ax2.errorbar(n_me, meE, yerr = εmeE, linestyle = '--', color = 'red', label = "My replication")
ax2.errorbar(n_lu, luE, yerr = εluE, color = 'green', label = "Lu's NN (n$_{tr}$=100)")
ax2.set_yscale('linear')
ax2.set_ylim([0, 16])
ax2.set_xlim([-0.5, 90])
ax2.set_xticks([0, 20, 40, 60, 80])
ax2.set_yticks([2, 4, 6, 8, 10])
ax2.set_yticklabels([2, 4, 6, 8, 10])
ax2.legend()
ax2.set_ylabel("MAPE (%)")
ax2.set_xlabel("2D FEM training data size")
plt.subplots_adjust(bottom=0.180)
fig.tight_layout()
ax2.annotate("B: $E_{r}$", xy=(0.05, 0.95), xycoords="axes fraction",
              fontsize=12, ha="center",
              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))
plt.savefig("/Users/Joe/Desktop/NN_graphs/lu2D.jpeg", dpi=800, bbox_inches="tight")
plt.show()


# Lu's 3D data
n_lu3 = [4, 6, 8, 10, 12]
lu3σ = [330.301, 241, 199.8, 54.2, 44.5]
εlu3σ = [330.301-302, 241-96.8, 199.8-98.7, 54.2, 44.5-6.39]
lu3E = [72.177, 41.554, 18.941, 10.971, 8.524]
εlu3E = [72.177-50.076, 41.554-8.404, 18.941-0, 10.971-3.511, 8.524-2.998]
# My version of Lu's 3D data
n_Br = [4, 6, 8, 10, 12]
Brσ = [409.73468, 178.92538, 226.17464, 73.83698, 58.871986]
εBrσ = [483.11395, 216.85849, 348.76566, 93.503784, 43.765083]
BrE = [72.62585, 34.406578, 16.770884, 13.474498, 8.293661]
εBrE = [58.778774, 40.89992, 6.265485, 9.39406, 5.6520896]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.errorbar(n_Br, Brσ, yerr = εBrσ, linestyle = '--', color = 'red', label = "My replication")
ax1.errorbar(n_lu3, lu3σ, yerr = εlu3σ, color = 'green', label = "Lu's NN (3D FEM)")
ax1.set_yscale('linear')
ax1.set_ylim([0, 800])
ax1.set_xlim([0, 13])
ax1.set_xticks([0, 3, 6, 9, 12])
ax1.set_yticks([0, 100, 200, 300, 400, 500, 600, 700, 800])
ax1.set_yticklabels([0, 100, 200, 300, 400, 500, 600, 700, 800])
ax1.legend()
ax1.set_ylabel("MAPE (%)")
ax1.set_xlabel("3D FEM training data size")
ax1.annotate("A: $\sigma_{y}$", xy=(0.05, 0.95), xycoords="axes fraction",
              fontsize=12, ha="center",
              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))

ax2.errorbar(n_Br, BrE, yerr = εBrE, linestyle = '--', color = 'red', label = "My replication")
ax2.errorbar(n_lu3, lu3E, yerr = εlu3E, color = 'green', label = "Lu's NN (n$_{tr}$=14)")
ax2.set_yscale('linear')
ax2.set_ylim([0, 150])
ax2.set_xlim([-0.5, 15])
ax2.set_xticks([0, 3, 6, 9, 12, 15])
ax2.set_yticks([0, 30, 60, 90, 120, 150])
ax2.set_yticklabels([0, 30, 60, 90, 120, 150])
ax2.legend()
ax2.set_ylabel("MAPE (%)")
ax2.set_xlabel("3D FEM training data size")
plt.subplots_adjust(bottom=0.180)
fig.tight_layout()
ax2.annotate("B: $E_{r}$", xy=(0.05, 0.95), xycoords="axes fraction",
              fontsize=12, ha="center",
              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))
plt.savefig("/Users/Joe/Desktop/NN_graphs/lu3D.jpeg", dpi=800, bbox_inches="tight")
plt.show()


# Lu's experimental data
n_Ex = [3, 6, 9, 12, 15, 18, 21]
Exσ = [105.38621, 37.710663, 23.844566, 16.386522, 15.827128, 12.619016, 10.768929]
εExσ = [39.772045, 16.506422, 8.401395, 5.692606, 8.074784, 4.6316137, 4.239168]
ExE = [53.26761, 25.274721, 10.545181, 6.2623787, 4.5989795, 3.6774323, 2.4038455]
εExE = [21.008629, 13.292065, 3.9533153, 4.338378, 2.1332085, 1.5747724, 1.2042903]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.errorbar(n_Ex, Exσ, yerr = εExσ, color = 'green', label = "Indentations on B3090")
ax1.set_yscale('linear')
ax1.set_ylim([0, 150])
ax1.set_xlim([-0.5, 24])
ax1.set_xticks([0, 3, 6, 9, 12, 15, 18, 21])
ax1.set_yticks([0, 30, 60, 90, 120, 150])
ax1.set_yticklabels([0, 30, 60, 90, 120, 150])
ax1.legend()
ax1.set_ylabel("MAPE (%)")
ax1.set_xlabel("Experimental training data size")
ax1.annotate("A: $\sigma_{y}$", xy=(0.05, 0.95), xycoords="axes fraction",
              fontsize=12, ha="center",
              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))

ax2.errorbar(n_Ex, ExE, yerr = εExE, color = 'green', label = "B3090 data (n$_{tr}$=144)")
ax2.set_yscale('linear')
ax2.set_ylim([0, 80])
ax2.set_xlim([-0.5, 24])
ax2.set_xticks([0, 3, 6, 9, 12, 15, 18, 21])
ax2.set_yticks([0, 20, 40, 60, 80])
ax2.set_yticklabels([0, 20, 40, 60, 80])
ax2.legend()
ax2.set_ylabel("MAPE (%)")
ax2.set_xlabel("Experimental training data size")
plt.subplots_adjust(bottom=0.180)
fig.tight_layout()
ax2.annotate("B: $E_{r}$", xy=(0.05, 0.95), xycoords="axes fraction",
              fontsize=12, ha="center",
              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))
plt.savefig("/Users/Joe/Desktop/NN_graphs/luexp.jpeg", dpi=800, bbox_inches="tight")
plt.show()


# Lu's MINN with all 3 data
n_lua = [0, 1, 2, 3, 4, 5, 6, 8, 10, 20]
meluσ = [96.79690387, 28.58358372, 9.24876582, 5.11659125, 4.20444411, 3.50299734, 3.23702025, 2.95160297, 2.63655563, 1.30540101]
εmeluσ = [11.25956148, 22.34089011, 7.71808326, 1.93115789, 1.07910404, 0.68240353, 0.69103869, 0.66872058, 0.41617703, 0.30860011]
meluE = [18.6240671, 13.07091517, 7.31385745, 4.43640207, 3.11487904, 2.34980973, 2.40618551, 2.15384257, 1.90070402, 1.42353008]
εmeluE = [2.33293523, 3.11706244, 3.33082938, 2.44876053, 1.52205441, 0.35729243, 0.2885574, 0.57204409, 0.47060894, 0.2238147]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.errorbar(n_lua, meluσ, yerr = εmeluσ, color = 'green', label = "Lu's indentations on B3090")
ax1.set_yscale('log')
ax1.set_ylim([1, 120])
ax1.set_xlim([-0.5, 21])
ax1.set_xticks([0, 5, 10, 15, 20])
ax1.set_yticks([1, 5, 10, 20, 40, 80, 120])
ax1.set_yticklabels([1, 5, 10, 20, 40, 80, 120])
ax1.legend()
ax1.set_ylabel("MAPE (%)")
ax1.set_xlabel("Experimental training data size")
ax1.annotate("A: $\sigma_{y}$", xy=(0.05, 0.95), xycoords="axes fraction",
              fontsize=12, ha="center",
              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))

ax2.errorbar(n_lua, meluE, yerr = εmeluE, color = 'green', label = "Lu's data (n$_{tr}$=144)")
ax2.set_yscale('log')
ax2.set_ylim([0, 20])
ax2.set_xlim([-0.5, 21])
ax2.set_xticks([0, 5, 10, 15, 20])
ax2.set_yticks([1, 2, 4, 8, 16])
ax2.set_yticklabels([1, 2, 4, 8, 16])
ax2.legend()
ax2.set_ylabel("MAPE (%)")
ax2.set_xlabel("Experimental training data size")
plt.subplots_adjust(bottom=0.180)
fig.tight_layout()
ax2.annotate("B: $E_{r}$", xy=(0.05, 0.95), xycoords="axes fraction",
              fontsize=12, ha="center",
              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))
plt.savefig("/Users/Joe/Desktop/NN_graphs/luMINN.jpeg", dpi=800, bbox_inches="tight")
plt.show()


# Lu's MINN with 2D+exp
n_lub = [1, 2, 3, 4, 5, 8, 10, 20]
luFEMσ = [34.76187049381707, 15.666057266762687, 6.996018572793789, 5.247694673209859, 4.675818271982714, 2.8224066143898994, 1.7193101447336872, 1.1601397290108126]
εluFEMσ = [10.740497950208871, 11.320466708732308, 3.6585756140059877, 2.428309380448281, 1.830393016684322, 0.7991033526928624, 0.5419118098670546, 0.6601813023072108]
luFEME = [6.277749365665346, 1.8816316858388151, 1.6219183265376143, 1.557228150514812, 1.2657623943780592, 1.123555123730203, 1.1112026038692304, 0.9507400282322637]
εluFEME = [6.320663598962627, 0.5880917816388127, 0.5585803534905526, 0.4803461648995692, 0.47507417407693564, 0.1597705074954198, 0.1597705074954198, 0.0680595017707608]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.errorbar(n_lub, luFEMσ, yerr = εluFEMσ, color = 'green', label = "Lu's indentations on B3090")
ax1.set_yscale('log')
ax1.set_ylim([1, 120])
ax1.set_xlim([-0.5, 21])
ax1.set_xticks([0, 5, 10, 15, 20])
ax1.set_yticks([1, 5, 10, 20, 40, 80, 120])
ax1.set_yticklabels([1, 5, 10, 20, 40, 80, 120])
ax1.legend()
ax1.set_ylabel("MAPE (%)")
ax1.set_xlabel("Experimental training data size")
ax1.annotate("A: $\sigma_{y}$", xy=(0.05, 0.95), xycoords="axes fraction",
              fontsize=12, ha="center",
              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))

ax2.errorbar(n_lub, luFEME, yerr = εluFEME, color = 'green', label = "Lu's data (n$_{tr}$=144)")
ax2.set_yscale('log')
ax2.set_ylim([0, 20])
ax2.set_xlim([-0.5, 21])
ax2.set_xticks([0, 5, 10, 15, 20])
ax2.set_yticks([1, 2, 4, 8, 16])
ax2.set_yticklabels([1, 2, 4, 8, 16])
ax2.legend()
ax2.set_ylabel("MAPE (%)")
ax2.set_xlabel("Experimental training data size")
plt.subplots_adjust(bottom=0.180)
fig.tight_layout()
ax2.annotate("B: $E_{r}$", xy=(0.05, 0.95), xycoords="axes fraction",
              fontsize=12, ha="center",
              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))
plt.savefig("/Users/Joe/Desktop/NN_graphs/lu2Dexp.jpeg", dpi=800, bbox_inches="tight")
plt.show()


# Lu's MINN with 2D+exp
n_luc = [1, 2, 3, 4, 5, 8, 10, 20]
luBerσ = [34.46453051282312, 14.430444813050446, 4.12398763020509, 3.5314341279625197, 3.0907205609813806, 2.2920436100804644, 1.6357738399610426, 1.2500409733864575]
εluBerσ = [22.360254865142583, 16.21183822544672, 2.0996833241547526, 1.9046035329593554, 1.8479607014761543, 0.49586585507229414, 0.3743748266099369, 0.36509353711279496]
luBerE = [4.628239397540119, 2.168147958579157, 1.8880737007128954, 1.8663205341038818, 1.611583831030046, 1.4588801771554758, 1.2661804874699487, 1.1079451346891076]
εluBerE = [3.9533561705442333, 0.5840393763292222, 0.6678048947524333, 0.5832767462508341, 0.45644151049291987, 0.44005901074087317, 0.3163713164786633, 0.07301838539300094]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.errorbar(n_luc, luBerσ, yerr = εluBerσ, color = 'green', label = "Lu's indentations on B3090")
ax1.set_yscale('log')
ax1.set_ylim([1, 120])
ax1.set_xlim([-0.5, 21])
ax1.set_xticks([0, 5, 10, 15, 20])
ax1.set_yticks([1, 5, 10, 20, 40, 80, 120])
ax1.set_yticklabels([1, 5, 10, 20, 40, 80, 120])
ax1.legend()
ax1.set_ylabel("MAPE (%)")
ax1.set_xlabel("Experimental training data size")
ax1.annotate("A: $\sigma_{y}$", xy=(0.05, 0.95), xycoords="axes fraction",
              fontsize=12, ha="center",
              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))

ax2.errorbar(n_luc, luBerE, yerr = εluBerE, color = 'green', label = "Lu's data (n$_{tr}$=144)")
ax2.set_yscale('log')
ax2.set_ylim([0, 20])
ax2.set_xlim([-0.5, 21])
ax2.set_xticks([0, 5, 10, 15, 20])
ax2.set_yticks([1, 2, 4, 8, 16])
ax2.set_yticklabels([1, 2, 4, 8, 16])
ax2.legend()
ax2.set_ylabel("MAPE (%)")
ax2.set_xlabel("Experimental training data size")
plt.subplots_adjust(bottom=0.180)
fig.tight_layout()
ax2.annotate("B: $E_{r}$", xy=(0.05, 0.95), xycoords="axes fraction",
              fontsize=12, ha="center",
              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))
plt.savefig("/Users/Joe/Desktop/NN_graphs/lu3Dexp.jpeg", dpi=800, bbox_inches="tight")
plt.show()
'''
'''
# My 70˚ data
n_a70 = [1, 2, 3, 4, 5, 6, 8, 10, 20]
a70σ = [61.162453, 3489.3862, 821.8509, 532.2977, 147.7874, 176.04375, 71.907486, 63.648335, 75.27569]
εa70σ = [4.3460784, 6518.8833, 896.3369, 616.8876, 95.840645, 127.86598, 82.1405, 56.214767, 106.56933]
a70E = [101.40326, 8090.0415, 991.31445, 569.72626, 326.1167, 248.37798, 125.59302, 66.22455, 33.23458]
εa70E = [6.8939376, 11720.051, 967.50916, 418.35547, 210.22432, 222.88261, 149.71326, 96.903496, 62.391518]
# rough 60˚ data
n_a60 = [1, 2, 3, 4, 5, 6, 8, 10, 20]
a60σ = [56.781788, 4200.5493, 526.8063, 380.36502, 168.2655, 169.8977, 91.55192, 64.54789, 38.680275]
εa60σ = [14.402582, 6976.8125, 519.221, 427.14392, 118.69308, 173.34337, 77.45191, 49.358387, 53.730602]
a60E = [101.397995, 3208.438, 849.90106, 569.96576, 340.64316, 264.78888, 152.801, 58.766777, 15.701685]
εa60E = [6.884638, 4754.098, 982.3889, 391.58392, 315.78214, 248.18668, 204.57101, 64.27664, 17.199352]
# fine 60˚ data
n_b60 = [1, 2, 3, 4, 5, 6, 8, 10]
b60σ = [364.34982, 311.10785, 448.8676, 374.02963, 370.30548, 372.08267, 380.42862, 253.73442]
εb60σ = [182.62218, 359.38074, 293.00198, 226.41072, 362.5988, 353.68384, 241.37292, 143.58322]
b60E = [235.99861, 205.91263, 382.17416, 264.4173, 265.08725, 275.69626, 214.23703, 197.72269]
εb60E = [168.32405, 180.41512, 306.19788, 182.81075, 200.02649, 210.8948, 143.58408, 181.44707]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.errorbar(n_a70, a70σ, yerr = εa70σ, linestyle = '--', color = 'red', label = "70.3˚")
ax1.errorbar(n_a60, a60σ, yerr = εa60σ, color = 'green', label = "fine mesh 60˚")
ax1.errorbar(n_b60, b60σ, yerr = εb60σ, linestyle = ':', color = 'black', label = "coarse mesh 60˚")
ax1.set_yscale('log')
ax1.set_ylim([1, 10000])
ax1.set_xlim([-0.5, 21])
ax1.set_xticks([0, 5, 10, 15, 20])
ax1.set_yticks([1, 100, 1000, 10000])
ax1.set_yticklabels([1, 100, 1000, 10000])
ax1.legend()
ax1.set_ylabel("MAPE (%)")
ax1.set_xlabel("2D FEM training data size")
ax1.annotate("A: $\sigma_{y}$", xy=(0.05, 0.95), xycoords="axes fraction",
              fontsize=12, ha="center",
              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))

ax2.errorbar(n_a70, a70E, yerr = εa70E, linestyle = '--', color = 'red', label = "70.3˚ (n$_{tr}$=58)")
ax2.errorbar(n_a60, a60E, yerr = εa60E, color = 'green', label = "60˚ (n$_{tr}$=58)")
ax2.errorbar(n_b60, b60E, yerr = εb60E, linestyle = ':', color = 'black', label = "coarse 60˚ (n$_{tr}$=17)")
ax2.set_yscale('log')
ax2.set_ylim([1, 10000])
ax2.set_xlim([-0.5, 21])
ax2.set_xticks([0, 5, 10, 15, 20])
ax2.set_yticks([1, 100, 1000, 10000])
ax2.set_yticklabels([1, 100, 1000, 10000])
ax2.legend()
ax2.set_ylabel("MAPE (%)")
ax2.set_xlabel("2D FEM training data size")
plt.subplots_adjust(bottom=0.180)
fig.tight_layout()
ax2.annotate("B: $E_{r}$", xy=(0.05, 0.95), xycoords="axes fraction",
              fontsize=12, ha="center",
              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))
plt.savefig("/Users/Joe/Desktop/NN_graphs/my2D.jpeg", dpi=800, bbox_inches="tight")
plt.show()


# My fine 3D data
n_me3 = [2, 3, 4, 5, 6, 8, 10, 20]
me3σ = [306.434, 129.54672, 34.51094, 16.30294, 11.011082, 12.529177, 4.876452, 2.347382]
εme3σ = [462.04684, 301.2473, 38.2321, 8.546992, 6.949768, 8.489592, 1.5463201, 1.5109531]
me3E = [414.90146, 44.883656, 25.77123, 6.2397795, 4.729158, 3.1615417, 1.646418, 1.073872]
εme3E = [679.3465, 52.76924, 34.00265, 4.2889166, 3.1390753, 2.3401568, 1.1024133, 0.42710212]
# My coarse 3D data
n_mr = [1, 2, 3, 4, 5, 6, 8, 10]
mrσ = [185.68034, 222.84956, 155.66293, 236.7647, 216.00008, 148.31773, 247.38887, 237.3854]
εmrσ = [94.66578, 213.69847, 112.16351, 132.68126, 83.09273, 182.30406, 100.73442, 136.23886]
mrE = [136.1349, 145.74281, 147.60287, 102.889626, 115.88994, 120.746544, 132.4818, 155.18082]
εmrE = [44.878254, 61.073906, 62.129875, 59.65944, 60.001347, 50.15582, 48.955044, 42.35498]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.errorbar(n_me3, me3σ, yerr = εme3σ, linestyle = '--', color = 'red', label = "TiAlTa 3D FEM")
ax1.errorbar(n_mr, mrσ, yerr = εmrσ, color = 'green', label = "Rough mesh")
ax1.set_yscale('linear')
ax1.set_ylim([0, 800])
ax1.set_xlim([0, 13])
ax1.set_xticks([0, 3, 6, 9, 12])
ax1.set_yticks([0, 200, 400, 600, 800])
ax1.set_yticklabels([0, 200, 400, 600, 800])
ax1.legend()
ax1.set_ylabel("MAPE (%)")
ax1.set_xlabel("3D FEM training data size")
ax1.annotate("A: $\sigma_{y}$", xy=(0.05, 0.95), xycoords="axes fraction",
              fontsize=12, ha="center",
              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))

ax2.errorbar(n_me3, me3E, yerr = εme3E, linestyle = '--', color = 'red', label = "33% TiAlTa (n$_{tr}$=26)")
ax2.errorbar(n_mr, mrE, yerr = εmrE, color = 'green', label = "Rough (n$_{tr}$=11)")
ax2.set_yscale('linear')
ax2.set_ylim([0, 200])
ax2.set_xlim([-0.5, 15])
ax2.set_xticks([0, 3, 6, 9, 12, 15])
ax2.set_yticks([0, 50, 100, 150, 200])
ax2.set_yticklabels([0, 50, 100, 150, 200])
ax2.legend()
ax2.set_ylabel("MAPE (%)")
ax2.set_xlabel("3D FEM training data size")
plt.subplots_adjust(bottom=0.180)
fig.tight_layout()
ax2.annotate("B: $E_{r}$", xy=(0.05, 0.95), xycoords="axes fraction",
              fontsize=12, ha="center",
              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))
plt.savefig("/Users/Joe/Desktop/NN_graphs/TiAlTa3D.jpeg", dpi=800, bbox_inches="tight")
plt.show()


# My experimental data
n_Ex = [2, 3, 4, 5, 6, 8, 10, 20]
Exσ = [861.10126, 82.19835, 50.26911, 40.918686, 23.89855, 16.746403, 14.455053, 6.0831113]
εExσ = [1933.915, 40.28174, 22.32007, 16.531126, 14.91269, 10.046402, 15.16982, 2.1733255]
ExE = [174.80925, 33.25544, 21.027987, 16.96242, 10.253847, 6.8848433, 3.7717087, 1.7349592]
εExE = [276.84796, 21.188744, 16.89436, 12.064427, 6.9805694, 7.832006, 2.0475862, 0.8986498]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.errorbar(n_Ex, Exσ, yerr = εExσ, color = 'green', label = "Indentations on 33% TiAlTa")
ax1.set_yscale('linear')
ax1.set_ylim([0, 150])
ax1.set_xlim([-0.5, 20])
ax1.set_xticks([0, 5, 10, 15, 20])
ax1.set_yticks([0, 30, 60, 90, 120, 150])
ax1.set_yticklabels([0, 30, 60, 90, 120, 150])
ax1.legend()
ax1.set_ylabel("MAPE (%)")
ax1.set_xlabel("Experimental training data size")
ax1.annotate("A: $\sigma_{y}$", xy=(0.05, 0.95), xycoords="axes fraction",
              fontsize=12, ha="center",
              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))

ax2.errorbar(n_Ex, ExE, yerr = εExE, color = 'green', label = "TiAlTa data (n$_{tr}$=144)")
ax2.set_yscale('linear')
ax2.set_ylim([0, 80])
ax2.set_xlim([-0.5, 20])
ax2.set_xticks([0, 5, 10, 15, 20])
ax2.set_yticks([0, 20, 40, 60, 80])
ax2.set_yticklabels([0, 20, 40, 60, 80])
ax2.legend()
ax2.set_ylabel("MAPE (%)")
ax2.set_xlabel("Experimental training data size")
plt.subplots_adjust(bottom=0.180)
fig.tight_layout()
ax2.annotate("B: $E_{r}$", xy=(0.05, 0.95), xycoords="axes fraction",
              fontsize=12, ha="center",
              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))
plt.savefig("/Users/Joe/Desktop/NN_graphs/TiAlTaexp.jpeg", dpi=800, bbox_inches="tight")
plt.show()


# My MINN with all 3 data
n_MFa = [0, 1, 2, 3, 4, 5, 6, 8, 10, 20]
MFσ = [127.48970342, 95.18143722, 64.80104188, 36.19212082, 25.03781424, 15.82539208, 10.80078742, 7.46391443, 4.72507616, 1.01443709]
εMFσ = [24.53927427, 49.95136498, 48.40308968, 16.72142493, 21.51747504, 7.83671192, 2.85249597, 2.49897764, 1.90289354, 0.7769228]
MFE = [15.49784865, 12.78939787, 9.78318706, 6.0482391, 5.23448426, 4.27339502, 3.70077137, 3.01875205, 2.59431586, 1.41630972]
εMFE = [2.17359148, 4.35156782, 4.68156232, 2.24705721, 2.15758203, 0.92218672, 0.99049607, 0.73373167, 0.6901903, 0.36744165]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.errorbar(n_MFa, MFσ, yerr = εMFσ, color = 'green', label = "MINN with 33% TiAlTa")
ax1.set_yscale('log')
ax1.set_ylim([1, 120])
ax1.set_xlim([-0.5, 21])
ax1.set_xticks([0, 5, 10, 15, 20])
ax1.set_yticks([1, 5, 10, 20, 40, 80, 120])
ax1.set_yticklabels([1, 5, 10, 20, 40, 80, 120])
ax1.legend()
ax1.set_ylabel("MAPE (%)")
ax1.set_xlabel("Experimental training data size")
ax1.annotate("A: $\sigma_{y}$", xy=(0.05, 0.95), xycoords="axes fraction",
              fontsize=12, ha="center",
              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))

ax2.errorbar(n_MFa, MFE, yerr = εMFE, color = 'green', label = "Room temperature (n$_{tr}$=25)")
ax2.set_yscale('log')
ax2.set_ylim([0, 20])
ax2.set_xlim([-0.5, 21])
ax2.set_xticks([0, 5, 10, 15, 20])
ax2.set_yticks([1, 2, 4, 8, 16])
ax2.set_yticklabels([1, 2, 4, 8, 16])
ax2.legend()
ax2.set_ylabel("MAPE (%)")
ax2.set_xlabel("Experimental training data size")
plt.subplots_adjust(bottom=0.180)
fig.tight_layout()
ax2.annotate("B: $E_{r}$", xy=(0.05, 0.95), xycoords="axes fraction",
              fontsize=12, ha="center",
              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))
plt.savefig("/Users/Joe/Desktop/NN_graphs/TiAlTaMINN.jpeg", dpi=800, bbox_inches="tight")
plt.show()


# Lu's MINN with 2D+exp
n_2Db = [0, 1, 2, 3, 4, 5, 6, 7, 10, 20]
FEMσ = [188.76663, 154.20173428824592, 78.3082464897411, 41.47165045244181, 41.614586426585284, 24.020951814410918, 16.01009668015799, 12.963233176568654, 11.690476587977276, 3.756761872624776]
εFEMσ = [73.153694, 79.92413546007766, 62.730172245965115, 29.708274889841665, 47.47260623203874, 14.345424254023872, 4.786572368712445, 4.71760099220327, 3.6348027296795666, 3.1225136080466225]
FEME = [21.675121, 11.911197628891259, 11.71247997327582, 8.260459261077441, 5.495338105318839, 4.5959625244140625, 2.8897191414872694, 2.197175867417279, 1.4655314663000272, 0.6900146885922082]
εFEME = [2.4844365, 2.8615605474781947, 4.785541171473919, 3.228362235728788, 3.749041890960514, 3.321718063210472, 2.616692039808479, 1.8572451334679358, 0.7337463152562037, 0.2807680475152868]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.errorbar(n_2Db, FEMσ, yerr = εFEMσ, color = 'green', label = "2D FEM and physical indentation")
ax1.set_yscale('log')
ax1.set_ylim([1, 120])
ax1.set_xlim([-0.5, 21])
ax1.set_xticks([0, 5, 10, 15, 20])
ax1.set_yticks([1, 5, 10, 20, 40, 80, 120])
ax1.set_yticklabels([1, 5, 10, 20, 40, 80, 120])
ax1.legend()
ax1.set_ylabel("MAPE (%)")
ax1.set_xlabel("Experimental training data size")
ax1.annotate("A: $\sigma_{y}$", xy=(0.05, 0.95), xycoords="axes fraction",
              fontsize=12, ha="center",
              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))

ax2.errorbar(n_2Db, FEME, yerr = εFEME, color = 'green', label = "33% TiAlTa data (n$_{tr}$=25)")
ax2.set_yscale('log')
ax2.set_ylim([0, 20])
ax2.set_xlim([-0.5, 21])
ax2.set_xticks([0, 5, 10, 15, 20])
ax2.set_yticks([1, 2, 4, 8, 16])
ax2.set_yticklabels([1, 2, 4, 8, 16])
ax2.legend()
ax2.set_ylabel("MAPE (%)")
ax2.set_xlabel("Experimental training data size")
plt.subplots_adjust(bottom=0.180)
fig.tight_layout()
ax2.annotate("B: $E_{r}$", xy=(0.05, 0.95), xycoords="axes fraction",
              fontsize=12, ha="center",
              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))
plt.savefig("/Users/Joe/Desktop/NN_graphs/TiAlTa2Dexp.jpeg", dpi=800, bbox_inches="tight")
plt.show()


# Lu's MINN with 2D+exp
n_mec = [0, 1, 2, 3, 4, 5, 6, 7, 10, 20]
meBerσ = [576.5542, 247.22847294621542, 264.3965775960634, 55.529762281335465, 73.56101125957497, 39.706774422292966, 31.63647519555663, 29.333391616967116, 17.63436378197498, 11.49995381860848]
εmeBerσ = [446.05533, 183.4383555933049, 301.76505621329704, 24.501826960402603, 55.563140776760854, 14.042678593951647, 11.365757092762063, 10.17128621708138, 7.817827789945134, 14.059263603295284]
meBerE = [154.48647, 34.83283826133661, 39.56390138391568, 17.887449469862943, 13.728113637532207, 9.579535848216008, 9.906173009951688, 8.388153775926716, 3.5162076782761957, 2.646672499807258]
εmeBerE = [80.628624, 20.70156720054496, 42.47677824178318, 4.85255655659031, 6.576843079788938, 3.0702997131931067, 3.987283246851966, 5.579911914815005, 2.173199879706948, 3.9085836345128535]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.errorbar(n_mec, meBerσ, yerr = εmeBerσ, color = 'green', label = "Lu's indentations on B3090")
ax1.set_yscale('log')
ax1.set_ylim([1, 1000])
ax1.set_xlim([-0.5, 21])
ax1.set_xticks([0, 5, 10, 15, 20])
ax1.set_yticks([1, 10, 100, 1000])
ax1.set_yticklabels([1, 10, 100, 1000])
ax1.legend()
ax1.set_ylabel("MAPE (%)")
ax1.set_xlabel("Experimental training data size")
ax1.annotate("A: $\sigma_{y}$", xy=(0.05, 0.95), xycoords="axes fraction",
              fontsize=12, ha="center",
              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))

ax2.errorbar(n_mec, meBerE, yerr = εmeBerE, color = 'green', label = "Lu's data (n$_{tr}$=144)")
ax2.set_yscale('log')
ax2.set_ylim([0, 200])
ax2.set_xlim([-0.5, 21])
ax2.set_xticks([0, 5, 10, 15, 20])
ax2.set_yticks([1, 10, 100, 200])
ax2.set_yticklabels([1, 10, 100, 200])
ax2.legend()
ax2.set_ylabel("MAPE (%)")
ax2.set_xlabel("Experimental training data size")
plt.subplots_adjust(bottom=0.180)
fig.tight_layout()
ax2.annotate("B: $E_{r}$", xy=(0.05, 0.95), xycoords="axes fraction",
              fontsize=12, ha="center",
              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))
plt.savefig("/Users/Joe/Desktop/NN_graphs/TiAlTa3Dexp.jpeg", dpi=800, bbox_inches="tight")
plt.show()
'''

categories = ['Physical', '3D FEM', 'Rough 3D', '2D FEM (4∠)', '2D FEM (70.3˚)']
σvalues = [10.319227, 4.2227707, 13.366486, 63.699486, 59.360664]
σerrors = [3.7665966, 1.2720577, 13.127058, 39.098995, 73.83362]
Evalues = [3.4535072, 2.0597403, 1.2027538, 56.905693, 100.09694]
Eerrors = [1.8956615, 1.129313, 1.8326986, 45.235996, 112.177414]

colors = ['darkred', 'green', 'gray', 'blue']
bar_width = 0.15
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.bar(categories, σvalues, yerr=σerrors, capsize=4, color=colors)
ax1.set_yticks([0, 25, 50, 75, 100, 125])
ax1.set_yticklabels([0, 25, 50, 75, 100, 125])
ax1.set_ylim([0, 150])
ax1.set_xlabel('Trainind data type')
ax1.tick_params(axis='x', labelsize=7)
ax1.set_ylabel('MAPE (%)')
plt.subplots_adjust(bottom=0.18)
ax1.annotate("A: $\sigma_{y}$", xy=(0.15, 0.95), xycoords="axes fraction",
              fontsize=12, ha="center",
              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))
ax2.bar(categories, Evalues, yerr=Eerrors, capsize=4, color=colors)
ax2.set_yticks([0, 25, 50, 75, 100, 125])
ax2.tick_params(axis='x', labelsize=7)
ax2.set_yticklabels([0, 25, 50, 75, 100, 125])
ax1.set_ylim([0, 150])
ax2.set_xlabel('Trainind data type')
ax2.set_ylabel('MAPE (%)')
plt.subplots_adjust(bottom=0.18)
ax2.annotate("B: $E_{r}$", xy=(0.15, 0.95), xycoords="axes fraction",
              fontsize=12, ha="center",
              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))
plt.savefig("/Users/Joe/Desktop/trainingerrors.jpeg", dpi=800, bbox_inches="tight")
plt.show()