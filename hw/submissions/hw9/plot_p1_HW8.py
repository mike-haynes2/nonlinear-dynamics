import math as m
import numpy as np

import matplotlib.pyplot as plt



def F(x):
    return np.piecewise(x, [x <= -1., (x>-1.) & (x<1.), x >= 1.], [lambda x: x+2, lambda x: -x, lambda x: x-2])


def sys(x,y, mu=1.):
    return (mu * (y - F(x))),(-x/mu)



l = 4.
xmin = -l
xmax = l
ymin = -l
ymax = l


res = 0.01

Xarr = np.arange(start=xmin,stop=xmax,step=res)
Yarr = np.arange(start=ymin,stop=ymax,step=res)

X, Y = np.meshgrid(Xarr,Yarr)
dX, dY = sys(X,Y,mu=10.)
mag = np.sqrt(dX**2. + dY**2.)


fig, ax = plt.subplots(figsize=(10,7))
#NOTE: NEED matplotlib version 3.6.0 minimum in order to use the broken_streamlines keyword argument for the ax.streamplot() call. 
#I had to install in user space, so I uninstalled after completion [work desktop]
pp = ax.streamplot(X, Y, dX, dY, color=(mag), cmap = 'turbo', linewidth=0.9, density=1.4, broken_streamlines=False)
cbar = fig.colorbar(pp.lines)
cbar.set_label(r'${\sqrt{\dot{x}^2 + \dot{y}^2}}$')


plt.plot(Xarr, np.zeros_like(Xarr), color='red', lw=2, label=r'$x=0$')
plt.plot(Xarr, F(Xarr), color='blue', lw=2, label=r'$y=F(x)$')


xpl = np.arange(start=-3.,stop=-1.,step=0.1)
plt.plot(xpl,F(xpl), color='magenta', linestyle='dashed', label='Limit Cycle', lw=2)
xpl = np.arange(start=1.,stop=3.,step=0.1)
plt.plot(xpl,F(xpl), color='magenta', linestyle='dashed', lw=2)
xpl = np.arange(start=-1.,stop=3.,step=0.1)
plt.plot(xpl,np.ones_like(xpl), color='magenta', linestyle='dashed', lw=2)
plt.plot(xpl-2.*np.ones_like(xpl),-np.ones_like(xpl), color='magenta', linestyle='dashed', lw=2)


plt.xlabel(r'$x$')
plt.ylabel(r'$y$')

ax.set_xlim(xmin,xmax)
ax.set_ylim(ymin,ymax)
ax.grid()

plt.legend()

plt.title('Phase Portrait with Nullclines ($μ = 1$): 7.5.4 ')

#plt.show()

plt.savefig('limit_cycle_1c.png', dpi=285.)
plt.close()

