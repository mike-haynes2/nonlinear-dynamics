import math as m
import numpy as np

import matplotlib.pyplot as plt



def sys(t1,t2,w1,w2):
    return (w1 + (np.sin(t1) * np.cos(t2))), (w2+(np.sin(t2)*np.cos(t1)))





l = 4.
xmin = -l
xmax = l
ymin = -l
ymax = l


res = 0.05

Xarr = np.arange(start=xmin,stop=xmax,step=res)
Yarr = np.arange(start=ymin,stop=ymax,step=res)

X, Y = np.meshgrid(Xarr,Yarr)




dX, dY = sys(X,Y, w1=1.,w2=1.)
mag = np.sqrt(dX**2. + dY**2.)


fig, ax = plt.subplots(figsize=(10,7))
#NOTE: NEED matplotlib version 3.6.0 minimum in order to use the broken_streamlines keyword argument for the ax.streamplot() call. 
#I had to install in user space, so I uninstalled after completion [work desktop]
pp = ax.streamplot(X, Y, dX, dY, color=(mag), cmap = 'turbo', linewidth=0.9, density=1.4, broken_streamlines=False)
cbar = fig.colorbar(pp.lines)
cbar.set_label(r'${\sqrt{\dot{x}^2 + \dot{y}^2}}$')

# trapping region stuff
# circleI = plt.Circle((0,0),(1./np.sqrt(2)), color='r',fill=False,zorder=1000)
# circleO = plt.Circle((0,0),(1.), color='r',fill=False,zorder=1000)
# ax.add_patch(circleI)
# ax.add_patch(circleO)

plt.xlabel(r'$\theta_1$')
plt.ylabel(r'$\theta_2$')

ax.set_xlim(xmin,xmax)
ax.set_ylim(ymin,ymax)
ax.grid()

plt.title(r'Oscillator Death System $\omega_1=\omega_2=\frac{1}{2}$')

#plt.show()

plt.savefig('phase_portrait_p4_p5p5_zoomed.png', dpi=290.)
plt.close()

