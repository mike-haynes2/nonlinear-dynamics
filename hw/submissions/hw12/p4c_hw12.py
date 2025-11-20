import math as m
import numpy as np
from scipy import constants
import matplotlib.pyplot as plt



def f(x,r):
    return (r*np.exp(x))

Xarr = np.arange(start=-2.,stop=5.,step=0.01)


xn = []
xn2 = []
ns = []

x0 = -1.5
eps = 0.05
rc = 1./m.e
r1 = rc - eps
r2 = rc + eps
N = 100

xn.append(x0)
xn2.append(x0)

for i in range(N):
    xnew1 = f(xn[i],r=r1)
    xnew2 = f(xn2[i],r=r2)
    xn.append(xnew1)
    xn2.append(xnew2)
    ns.append(i)
ns.append(N)


fig,ax = plt.subplots(2)

ax[0].plot(ns,xn,color='magenta',lw=1.3)

ax[1].plot(ns,xn2,color='magenta',lw=1.3)

ax[1].set_xlabel('$n$')
ax[0].set_ylabel('$x_n$')
ax[1].set_ylabel('$x_n$')

ax[0].set_title('$r=r_c - 0.05$')
ax[1].set_title('$r=r_c + 0.05$')


fig.suptitle('Timeseries for $f(x_n)$')

ax[0].grid()
ax[1].grid()
fig.tight_layout()

#plt.show()

plt.savefig('p4c.png', dpi=295.)