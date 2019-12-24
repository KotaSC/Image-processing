import numpy as np
import sys
args = sys.argv
import matplotlib.pyplot as plt
plt.style.use('seaborn-white')
from matplotlib import cycler

def multi_func(x, th, dim, grad, amin, amax, fth):

    condlist = [x < th , (x >= th) & (x < fth), x >= fth]
    funclist = [lambda a: amin, lambda a: grad*((a-th)**dim)+amin, lambda a: amax]

    return np.piecewise(x, condlist, funclist)

colors = cycler('color', ['#EE6666', '#3388BB', '#9988DD', '#EECC55', '#88BB44', '#FFBBBB'])
plt.rc('axes',  facecolor='#E6E6E6', edgecolor='black', axisbelow=True, grid=False, prop_cycle=colors)
plt.rc('grid',  color='w', linestyle='solid')
plt.rc('xtick', direction='in', color='black')
plt.rc('ytick', direction='in', color='black')
plt.rc('patch', edgecolor='#E6E6E6')
plt.rc('lines', linewidth=2)

plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams["xtick.major.size"] = 10
plt.rcParams["xtick.minor.size"] = 5
plt.rcParams["ytick.major.size"] = 10
plt.rcParams["ytick.minor.size"] = 5
plt.rcParams["font.size"]        = 18

plt.figure(figsize=(10, 8))
ax = plt.axes(facecolor='white')
ax.set_axisbelow(True)

ax.set_xlim([0.0, 1.0])
ax.set_ylim([0.0, 1.0])

plt.xticks([0.0, 0.2, 0.4, 0.6, 0.8, 1.0])
plt.yticks([0.2, 0.4, 0.6, 0.8, 1.0])


# ax.set_title(r"Realation between Feature value $\hat{F}^{(i)}$ and Function ${\rm g}(\hat{F}^{(i)})$", fontsize=20)
ax.set_xlabel(r"feature value $f$",         fontsize=22, color='black')
ax.set_ylabel(r"opacity ${\alpha( f)}$", fontsize=22, color='black')

a_max = 1.0
a_min = 0.2
fth   = 0.3
d     = 2.0
Fth   = 1.0

denom = Fth - fth
grad  = (a_max-a_min)/(denom**d)
x     = np.linspace(0.0, 1.0, 1000.0)

y = multi_func(x, fth, d, grad, a_min, a_max, Fth)

plt.plot(x,y, color='black')

plt.gca().yaxis.set_major_formatter(plt.FormatStrFormatter('%.1f'))
plt.gca().xaxis.set_major_formatter(plt.FormatStrFormatter('%.1f'))

fig_name = args[1]
plt.savefig(fig_name)

plt.show()