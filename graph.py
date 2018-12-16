import numpy as np
import matplotlib.pyplot as plt

th   = 0.3/1.0
dim  = 3.0
grad = 1.0/((1.0-th)**dim)


def multi_func(x):

    condlist = [x <= th , (x > th) & (x <= 1)]
    funclist = [lambda a: 0, lambda a: grad*((a-th)**dim)]

    return np.piecewise(x, condlist, funclist)

plt.figure(figsize=(10, 8))

plt.xlim([0,1])
plt.ylim([0,1])

plt.xlabel("Feature value F")
plt.ylabel("Probability P")

plt.grid(which='major',color='black',linestyle='-')

x = np.linspace(0, 1, 100)
y = multi_func(x)

plt.plot(x,y)

plt.savefig("nakajimake/graph/dim3.png")

plt.show()