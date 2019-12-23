# coding: utf-8
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
plt.style.use('seaborn-white')
from matplotlib import cycler


# colors = cycler('color', ['#EE6666', '#3388BB', '#9988DD', '#EECC55', '#88BB44', '#FFBBBB'])
# plt.rc('axes', facecolor='#E6E6E6', edgecolor='none', axisbelow=True, grid=True, prop_cycle=colors)
# plt.rc('grid', color='w', linestyle='solid')
# plt.rc('xtick', direction='out', color='None')
# plt.rc('ytick', direction='out', color='None')
# plt.rc('patch', edgecolor='#E6E6E6')
# plt.rc('lines', linewidth=2)

colors = cycler('color', ['#EE6666', '#3388BB', '#9988DD', '#EECC55', '#88BB44', '#FFBBBB'])
plt.rc('axes',  facecolor='white', edgecolor='black', axisbelow=True, grid=False, prop_cycle=colors)
plt.rc('grid',  color='w', linestyle='solid')
plt.rc('xtick', direction='in', color='None')
plt.rc('ytick', direction='in', color='None')
plt.rc('patch', edgecolor='#E6E6E6')
plt.rc('lines', linewidth=2)

n = np.linspace(-5.0, 5.0, 10000)

p = []
for i in range(len(n)):
    p.append(norm.pdf(x=n[i], loc=0, scale=1))

m    = max(p)
fwhm = m * 0.5

plt.figure(figsize=(10, 8))

plt.quiver(5000, fwhm , 1150, 0, angles='xy', scale_units='xy', scale=1, width=0.006)
plt.quiver(5020, fwhm , -1160, 0, angles='xy', scale_units='xy', scale=1, width=0.006)

plt.text( 4550, fwhm-0.015, "Half Width", fontsize=12 )

plt.xlim( [0, 10000] )
plt.ylim( [0, m+0.05] )

plt.plot( p, color='black' )

plt.plot( 5000, m, 'o', color='black' )
plt.text( 1400, m-0.005, r"$f_{max}$", fontsize=15 )
plt.text( 1400, fwhm-0.005, r"$\frac{f_{max}}{2}$", fontsize=18 )

plt.plot( 3810, fwhm, 'o', color='black' )
plt.plot( 6170, fwhm, 'o', color='black' )

p = plt.hlines([m], 2000, 5000, "black", linestyles='dashed')
p = plt.hlines([fwhm], 2000, 3810, "black", linestyles='dashed')

plt.xlabel("Feature region width", fontsize=22, color='black')
plt.ylabel("Pixel Value", fontsize=22, color='black')

plt.savefig("hw.png")

plt.show()