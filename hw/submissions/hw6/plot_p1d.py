import math as m
import numpy as np

import matplotlib.pyplot as plt



def epi(x,y,k,l):
    return (-k*x*y), (k*x*y - l*y)




l = 5.
xmin = 0.
xmax = l
ymin = 0.
ymax = l


res = 0.01

Xarr = np.arange(start=xmin,stop=xmax,step=res)
Yarr = np.arange(start=ymin,stop=ymax,step=res)

X, Y = np.meshgrid(Xarr,Yarr)
dX, dY = epi(X,Y,k=1.,l=1.)
mag = np.sqrt(dX**2. + dY**2.)


fig, ax = plt.subplots(figsize=(10,7))
#NOTE: NEED matplotlib version 3.6.0 minimum in order to use the broken_streamlines keyword argument for the ax.streamplot() call. 
#I had to install in user space, so I uninstalled after completion [work desktop]
pp = ax.streamplot(X, Y, dX, dY, color=mag, cmap = 'turbo', linewidth=0.9, density=1.4, broken_streamlines=False)
cbar = fig.colorbar(pp.lines)
cbar.set_label(r'$\sqrt{\dot{x}^2 + \dot{y}^2}$')

ax.set_xlim(xmin,xmax)
ax.set_ylim(ymin,ymax)
ax.grid()

plt.title('Phase Portrait: Epidemic model')

plt.show()

#plt.savefig('epi_phase_portrait_1d.png', dpi=290.)
#plt.close()