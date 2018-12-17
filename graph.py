import numpy as np
import sys
args = sys.argv
import matplotlib.pyplot as plt
plt.style.use('seaborn-white')
from matplotlib import cycler

def multi_func(x, th, dim, grad):

    condlist = [x <= th , (x > th) & (x <= 1)]
    funclist = [lambda a: 0, lambda a: grad*((a-th)**dim)]

    return np.piecewise(x, condlist, funclist)

colors = cycler('color', ['#EE6666', '#3388BB', '#9988DD', '#EECC55', '#88BB44', '#FFBBBB'])
plt.rc('axes', facecolor='#E6E6E6', edgecolor='none', axisbelow=True, grid=True, prop_cycle=colors)
plt.rc('grid', color='w', linestyle='solid')
plt.rc('xtick', direction='out', color='black')
plt.rc('ytick', direction='out', color='black')
plt.rc('patch', edgecolor='#E6E6E6')
plt.rc('lines', linewidth=2)

plt.figure(figsize=(10, 8))
ax = plt.axes(facecolor='#E6E6E6')
ax.set_axisbelow(True)

ax.set_xlim([0, 1])
ax.set_ylim([0, 1])

ax.set_title("Function used for feature extraction", fontsize=12)
ax.set_xlabel("Feature value F", fontsize=12, color='black')
ax.set_ylabel("Probability P", fontsize=12, color='black')

x = np.linspace(0, 1, 100)

th    = input('閾値を入力してください         >>')
ftMax = input('特徴量の最大値を入力してください >>')
dim   = input('関数の次元を入力してください    >>')
grad = 1.0/((1.0-float(th)/float(ftMax))**float(dim))

y = multi_func(x, float(th), float(dim), grad)

plt.plot(x,y)

fig_name = args[1]
plt.savefig(fig_name)

plt.show()