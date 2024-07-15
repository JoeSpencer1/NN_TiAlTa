import numpy as np
import pandas as pd
from scipy import optimize

def Pi1(Er_sigma33):
    x = np.log(Er_sigma33)
    return -1.131 * x ** 3 + 13.635 * x ** 2 - 30.594 * x + 29.267


def Pi2(Er_sigma33, n):
    x = np.log(Er_sigma33)
    return (
        (-1.40557 * n ** 3 + 0.77526 * n ** 2 + 0.1583 * n - 0.06831) * x ** 3
        + (17.93006 * n ** 3 - 9.22091 * n ** 2 - 2.37733 * n + 0.86295) * x ** 2
        + (-79.99715 * n ** 3 + 40.5562 * n ** 2 + 9.00157 * n - 2.54543) * x
        + 122.65069 * n ** 3
        - 63.88418 * n ** 2
        - 9.58936 * n
        + 6.20045
    )

def Pi4(hrhm):
    return 0.268536 * (0.9952495 - hrhm) ** 1.1142735

def Pitheta(theta, Er_sigma):
    Ersig = np.log(Er_sigma)
    t1 = (-2.3985e-5 * theta ** 3 + 6.0446e-4 * theta ** 2 +0.13243 * theta - 5.0950)
    t2 = (0.0014741 * theta ** 3 - 0.21502 * theta ** 2 + 10.4415 * theta - 169.8767)
    t3 = (-3.9124e-3 * theta ** 3 + 0.53332 * theta ** 2 - 23.2834 * theta + 329.7724)
    t4 = (2.6981e-3 * theta ** 3 - 0.29197 * theta ** 2 + 7.5761 * theta + 2.0165)
    return t1 * Ersig ** 3 + t2 * Ersig ** 2 + t3 * Ersig + t4

def epsilon_r(theta):
    return 2.397e-5 * theta ** 2 - 5.311e-3 * theta + 0.2884

def model_dao(C, dPdh, nu, Er, hm, hr, nu_i=0.0691, E_i=1143):
    C *= 1e9
    hm *= 1e-6
    hr *= 1e-6
    E_i *= 1e9
    Er *= 1e9
    sigma_33 = optimize.brentq(lambda x: Pi1(Er / x) - C / x, 1e8, 1e11)
    E = (1 - nu ** 2) / (1 / Er - (1 - nu_i ** 2) / E_i)
    try:
        n = optimize.brentq(
            lambda x: Pi2(Er / sigma_33, x) - dPdh / Er / hm, 0, 0.5
        )
    except ValueError:
        n = 0
    if n > 0:
        sigma_y = optimize.brentq(
            lambda x: (1 + E / x * 0.033) ** n - sigma_33 / x, 1e7, 1e10
        )
    else:
        sigma_y = sigma_33
    return sigma_y/1e9, n

def model_swa(C, dPdh, nu, Er, hm, hr, theta=70.3, nu_i=0.0691, E_i=1143, typ='b'):
    # This model is only valid with θ=70.3˚. Please refer to Chollacoop et al for more information.
    C *= 1e9
    E_i *= 1e9
    Er *= 1e9
    hm *= 1e-6
    hr *= 1e-6
    
    if typ == 'c':
        cstar = 1.1957  # Conical
    if typ == 'b':
        cstar = 1.2370  # Berkovich
    Pm = C * hm ** 2
    Am = (Pm * cstar / dPdh / Pi4(hr / hm)) ** 2
    Er = dPdh / cstar / Am ** 0.5
    sigma_33 = optimize.brentq(lambda x: Pi1(Er / x) - C / x, 1e7, 1e10)
    for l, r in [[1e7, 1e9], [1e9, 5e9], [5e9, 1e10]]:
        if (Pitheta(theta, Er / l) - C / l) * (
            Pitheta(theta, Er / r) - C / r
        ) < 0:
            sigma_r = optimize.brentq(
                lambda x: Pitheta(theta, Er / x) - C / x, l, r
            )
            break
    else:
        raise ValueError
    epsilon = epsilon_r(theta)
    E = (1 - nu ** 2) / (1 / Er - (1 - nu_i ** 2) / E_i)
    print(epsilon, ' ', sigma_33 - sigma_r)
    if (epsilon > 0.033 and sigma_33 < sigma_r) or (
        epsilon < 0.033 and sigma_33 > sigma_r
    ):
        sigma_y = optimize.brentq(
            lambda x: np.log(sigma_33 / x) / np.log(sigma_r / x)
            - np.log(1 + E / x * 0.033) / np.log(1 + E / x * epsilon),
            1e7,
            min(sigma_33, sigma_r),
        )
        n = np.log(sigma_33 / sigma_y) / np.log(1 + E / sigma_y * 0.033)
    else:
        n = 0
        sigma_y = (sigma_33 + sigma_r) / 2
    return E/1e9,Er/1e9, sigma_y/1e9, n




#print(model_old(204.8761345, 188141.7926, 0.25, 151, 0.220941158, 0.025171))
#print(model_new(204.8761345, 0.25, 151, 0.220941158))
filename = '../data/TI33_25.csv'
df = pd.read_csv(filename)
print('New')
for i in range(len(df)):
    if i not in [0, 23]: # Remove 2 indices that do not converge
        print(model_swa(df['C (GPa)'][i], df['dP/dh (N/m)'][i], df['nu'][i], df['E* (GPa)'][i], df['hmax(um)'][i], df['hr(um)'][i]))
print('Old')
for i in range(len(df)):
    if i not in [25]: # Remove 1 indices that do not converge
        print(i, model_dao(df['C (GPa)'][i], df['dP/dh (N/m)'][i], df['nu'][i], df['E* (GPa)'][i], df['hmax(um)'][i], df['hr(um)'][i]))


# Matlab(R) function to inversely recover material properties
# Copyright Christian Heinrich
function main_function()
# These are the four values that have to be entered by them experimentalist
# Example values for aluminium
h=10; # maximum indentation depth in micron
F6=1743440 # maximum loading force 60.0 degree indenter in mirco N
Su7=5135493 # initial unloading stiffness 70.3 degree indenter in micro N/micro m
F7=3332070 # maximum loading force 70.3 degree indenter
x0 = [100, 100e3, 0.1]; #initial guess
#coefficients for the non-dimensional functions
coeff_F6=[
-2.26367e-3,+5.70479e+1,+1.79838e-1, -2.12958e+3,+5.51884e+4, -6.51318e+5,
+5.13388e-8,+9.17537e-1,+6.19795e+2, -3.80206e+1, -5.88275e+4,+3.27898e+6,
-6.70223e+7, -1.02486e-4, -2.92575e+0, -1.99867e+3,+1.47611e+2,+1.67356e+5,
-9.15371e+6,+1.84290e+8,+2.91144e-4,+4.10818e+0,+2.07408e+3, -1.54721e+2,
-1.87635e+5,+1.06689e+7,-2.18065e+8,-3.82211e-4,-2.84731e-1,-1.78953e+2,
+1.38509e+1,+1.46633e+4,-7.91493e+5,+1.62369e+7,+3.02873e-5,]
coeff_F7=[
-6.12261e-2,+7.87874e+1,+3.31048e+0,-3.94470e+3,+1.33496e+5,-1.92058e+6,
+6.00416e-6,-.43092e+0,-9.98581e+2,+7.71022e+1,+4.76054e+4,-9.58699e+5,
-9.47438e+6,+2.00402e-4,+1.46421e+0,+7.98144e+2,-3.74903e+1,-2.07108e+4,
-2.99794e+6,+1.49407e+8,-3.79577e-4,+1.53383e+0,+7.41653e+1,-3.34441e+1,
-6.32584e+4,+8.77821e+6,-2.98936e+8,+1.75463e-4,+4.23333e-1,+2.95422e+2,
-1.91534e+1,-1.67611e+4,+5.28320e+5,-4.41803e+6,-5.82415e-5,]
coeff_S7=[
+4.34955e+0,-2.30482e+2,+5.61782e+0,+9.91949e+3,-1.25739e+5,-2.28101e+6,
+2.47650e-5,-2.48846e+1,-9.24054e+3,+8.54432e+2,+4.76044e+5,-1.98529e+7,
+3.69156e+8,+3.88344e-3,+7.09114e+1,+2.82049e+4,-2.54284e+3,-1.52109e+6,
+6.48387e+7,-1.20803e+9,-1.17274e-2,-8.21417e+1,-3.25830e+4,+2.93012e+3,
+1.74396e+6,-7.24071e+7,+1.31271e+9,+1.32455e-2,+5.18080e+0,+2.60302e+3,
-2.29315e+2,-1.23766e+5,+4.44699e+6,-7.21355e+7,-9.25320e-4,]
options=optimset(‘Display’, ‘iter’, ‘MaxFunEvals’, 500,000,
‘MaxIter’, 30000, ‘NonlEqnAlgorithm’, ‘gn’);
[x,fval] = fsolve(@(x) NLSystem(x,coeff_F6,coeff_S7,coeff_F7,F6,Su7,F7,h),x0);
#E=x(1),Y=x(2),n=x(3)
disp(x);
end
function F=NLSystem(x,coeff_F6,coeff_S7,coeff_F7,F6,Su7,F7,h)
#non-linear equations that need to be solved
F(1)= h.ˆ2.*x(2).*pi_fun(coeff_F6,[x(1)/x(2);x(3)])-F6;
F(2)=2.*h .*x(2).*pi_fun(coeff_S7,[x(1)/x(2);x(3)])-Su7;
F(3)= h.ˆ2.*x(2).*pi_fun(coeff_F7,[x(1)/x(2);x(3)])-F7;
end
function F = pi_fun(a,data)
r=data(1,:);
n=data(2,:);
#shape of the non-dimensional pi-functions in terms of r=E/Y and n
F = (a( 1)+a( 2).*r+a( 3).*sqrt(r)+a( 4).*r.ˆ2+a( 5).*r.ˆ3+a( 6).*r.ˆ4+
a( 7)./r) +(a( 8)+a( 9).*r+a(10).*sqrt(r)+a(11).*r.ˆ2+a(12).*r.ˆ3+
a(13).*r.ˆ4+a(14)./r).*n+(a(15)+a(16).*r+a(17).*sqrt(r)+a(18).*r.ˆ2+
a(19).*r.ˆ3+a(20).*r.ˆ4+a(21)./r).*n.ˆ2 +(a(22)+a(23).*r+
a(24).*sqrt(r)+a(25).*r.ˆ2+a(26).*r.ˆ3+a(27).*r.ˆ4+a(28)./r).*n.ˆ3
+(a(29)+a(30).*r+a(31).*sqrt(r)+a(32).*r.ˆ2+a(33).*r.ˆ3+a(34).*r.ˆ4+
a(35)./r).*sqrt(n);
end