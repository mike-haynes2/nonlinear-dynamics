import math as m
import numpy as np

import matplotlib.pyplot as plt



def sys(x,y,b):
    return (y), (-np.sin(x) - b*y)




l = 3.
xmin = -l
xmax = l
ymin = -l
ymax = l


res = 0.02

Xarr = np.arange(start=xmin,stop=xmax,step=res)
Yarr = np.arange(start=ymin,stop=ymax,step=res)

X, Y = np.meshgrid(Xarr,Yarr)



fig, ax = plt.subplots(3, figsize=(5,10))


for i,bidx in enumerate([1.,2.,3.]):
    dX, dY = sys(X,Y,b=bidx)
    mag = np.sqrt(dX**2. + dY**2.)


    
    #NOTE: NEED matplotlib version 3.6.0 minimum in order to use the broken_streamlines keyword argument for the ax.streamplot() call. 
    #I had to install in user space, so I uninstalled after completion [work desktop]
    pp = ax[i].streamplot(X, Y, dX, dY, color=mag, cmap = 'turbo', linewidth=0.9, density=1.4, broken_streamlines=False)
    cbar = fig.colorbar(pp.lines)
    cbar.set_label(r'$\sqrt{\dot{x}^2 + \dot{y}^2}$')

    ax[i].set_xlabel(r'$x$')
    ax[i].set_ylabel(r'$\dot{x}$')

    ax[i].set_xlim(xmin,xmax)
    ax[i].set_ylim(ymin,ymax)
    ax[i].grid()

    ax[i].set_title(f'$b=$ {bidx}')

fig.tight_layout()
#plt.show()

plt.savefig('phase_portrait_4.png', dpi=290.)
# plt.close()