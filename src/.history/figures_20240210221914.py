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


categories = ['Physical experiment', 'Fine 3D FEM', 'Rough 3D FEM', '2D FEM (70.3˚)']
σvalues = [45.090057, 70.12297, 82.563194, 58.66543]
σerrors = [32.86384, 22.982897, 28.687885, 19.887922]
Evalues = [4.210283, 3.5263298, 5.338781, 9.962336]
Eerrors = [1.6728787, 2.66636, 3.444265, 0.95166034]
colors = ['red', 'green', 'orange', 'blue']
bar_width = 0.15
bar_positions1 = np.arange(len(categories))
bar_positions2 = bar_positions1 + bar_width
bar_positions3 = bar_positions1 + bar_width * 2
bar_positions4 = bar_positions1 + bar_width * 3
fig, ax = plt.subplots()
ax.bar(bar_positions1, σvalues, yerr=σerrors, width=bar_width, label='Al7075-T651')
ax.set_xticks(bar_positions1 + bar_width*3/2)
ax.set_xticklabels(categories)
ax.set_yticks([0, 25, 50, 75, 100])
ax.set_yticklabels([0, 25, 50, 75, 100])
ax.set_xlabel('Trainind data type')
ax.set_ylabel('MAPE (%)')
ax.legend()
plt.subplots_adjust(bottom=0.18)
plt.savefig("figure16.png", dpi=800, bbox_inches="tight")
plt.show()