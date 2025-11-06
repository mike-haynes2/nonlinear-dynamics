import math as m
import numpy as np

import matplotlib.pyplot as plt



def sys(phi,theta,a,I):
    return (theta), (I - a * theta - np.sin(phi))





l = np.pi
xmin = -l
xmax = l
ymin = -l
ymax = l


res = 0.1

Xarr = np.arange(start=xmin,stop=xmax,step=res)
Yarr = np.arange(start=ymin,stop=ymax,step=res)

X, Y = np.meshgrid(Xarr,Yarr)

alphs = [0.1,2]
Ivals = [0.,0.5,1.,1.5,2]

fig, ax = plt.subplots(len(Ivals), len(alphs), figsize=(6.6,10))



for i, alpha in enumerate(alphs):
    for j, I in enumerate(Ivals):
        dX, dY = sys(X,Y, a=alpha,I=I)
        mag = np.sqrt(dX**2. + dY**2.)

        #NOTE: NEED matplotlib version 3.6.0 minimum in order to use the broken_streamlines keyword argument for the ax.streamplot() call. 
        #I had to install in user space, so I uninstalled after completion [work desktop]
        pp = ax[j,i].streamplot(X, Y, dX, dY, color=(mag), cmap = 'turbo', linewidth=0.9, density=1.4, broken_streamlines=False)
        cbar = fig.colorbar(pp.lines)
        if alpha == 2.:
            cbar.set_label(r'${\sqrt{\dot{x}^2 + \dot{y}^2}}$')
        if I == 0.:
            if alpha==0.1:
                ax[j,i].set_title(r'$\alpha=1/10$')
            else:
                ax[j,i].set_title(r'$\alpha=2$')
        if i == 0:
            ax[j,i].set_ylabel(r'$\dot \phi$')
        if I == 2.:
            ax[j,i].set_xlabel(r'$\phi$')
        
        ax[j,i].set_xlim(xmin,xmax)
        ax[j,i].set_ylim(ymin,ymax)
        ax[j,i].grid()

fig.suptitle(r'Driven pendulum: Comparison of Regimes')
fig.tight_layout()
#plt.show()

plt.savefig('phase_portrait_all_3.png', dpi=320.)
plt.close()

