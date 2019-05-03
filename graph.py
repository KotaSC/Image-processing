import numpy as np
import sys
args = sys.argv
import matplotlib.pyplot as plt
plt.style.use('seaborn-white')
from matplotlib import cycler

def multi_func(x, th, dim, grad, fm):

    condlist = [x < th , (x >= th) & (x <= 1)]
    funclist = [lambda a: 0.0, lambda a: grad*((a-thr)**dim)]

    return np.piecewise(x, condlist, funclist)

colors = cycler('color', ['#EE6666', '#3388BB', '#9988DD', '#EECC55', '#88BB44', '#FFBBBB'])
plt.rc('axes',  facecolor='#E6E6E6', edgecolor='black', axisbelow=True, grid=False, prop_cycle=colors)
plt.rc('grid',  color='w', linestyle='solid')
plt.rc('xtick', direction='in', color='black')
plt.rc('ytick', direction='in', color='black')
plt.rc('patch', edgecolor='#E6E6E6')
plt.rc('lines', linewidth=2)

plt.rcParams["xtick.major.size"] = 10
plt.rcParams["xtick.minor.size"] = 5
plt.rcParams["ytick.major.size"] = 10
plt.rcParams["ytick.minor.size"] = 5
plt.rcParams["font.size"] = 14

plt.figure(figsize=(10, 8))
ax = plt.axes(facecolor='white')
ax.set_axisbelow(True)

ax.set_xlim([0, 1])
ax.set_ylim([0, 1])

plt.xticks([0.2, 0.4, 0.6, 0.8, 1.0])


# ax.set_title(r"Realation between Feature value $\hat{F}^{(i)}$ and Function ${\rm g}(\hat{F}^{(i)})$", fontsize=20)
ax.set_xlabel(r"Feature value $\hat{F}^{(i)}$", fontsize=20, color='black')
ax.set_ylabel(r"Function ${\rm g}(\hat{F}^{(i)})$", fontsize=20, color='black')

th    = input('閾値を入力してください         >>')
ftMax = input('特徴量の最大値を入力してください >>')
dim   = input('関数の次元を入力してください    >>')

thr   = float(th)/float(ftMax)
denom = 1.0 - thr
grad  = 1.0/(denom**float(dim))
x     = np.linspace(0, 1, 1000)

y = multi_func(x, float(thr), float(dim), grad, float(ftMax))

plt.plot(x,y, color='black')

fig_name = args[1]
plt.savefig(fig_name)

plt.show()