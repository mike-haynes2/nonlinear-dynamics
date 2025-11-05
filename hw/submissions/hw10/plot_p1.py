import math as m
import numpy as np

import matplotlib.pyplot as plt



def sys(r,th,u):
    return (r*(u-np.sin(r))), (np.ones_like(th))




l = 4.
xmin = -l
xmax = l
ymin = -l
ymax = l


res = 0.01

Rarr = np.arange(start=0.,stop=8.,step=0.02)
THarr = np.arange(start=0.,stop=2.*np.pi,step=0.01)
T, R = np.meshgrid(THarr,Rarr)
dR, dT = sys(R,T,u=-0.5)
mag = np.sqrt((dR**2.)+(dT**2.))

print(np.shape(R))
print(np.shape(T))


fig, ax = plt.subplots(1, 1, figsize=(10,7), subplot_kw={'projection': 'polar'},
                        layout='constrained')
#NOTE: NEED matplotlib version 3.6.0 minimum in order to use the broken_streamlines keyword argument for the ax.streamplot() call. 
#I had to install in user space, so I uninstalled after completion [work desktop]
pp = ax.streamplot(T, R, dT, dR, color=(mag), cmap = 'turbo', linewidth=0.9, density=1.4, broken_streamlines=False)
cbar = fig.colorbar(pp.lines)
cbar.set_label(r'${\sqrt{\dot{x}^2 + \dot{y}^2}}$')

# trapping region stuff
# circleI = plt.Circle((0,0),(1./np.sqrt(2)), color='r',fill=False,zorder=1000)
# circleO = plt.Circle((0,0),(1.), color='r',fill=False,zorder=1000)
# ax.add_patch(circleI)
# ax.add_patch(circleO)

ax.set_rmax(8)
ax.set_rmin(0)

ax.set_rticks([1., 2., 3., 4., 5., 6., 7.])  # Fewer radial ticks
ax.set_rlabel_position(-22.5)  # Move radial labels away from plotted line

# ax.set_xlim(xmin,xmax)
# ax.set_ylim(ymin,ymax)
ax.grid()

plt.title(r'Global Homoclinic Bifurcation: $μ = -\frac{1}{2}$')

#plt.show()

plt.savefig('phase_portrait_1_munp5.png', dpi=290.)
plt.close()

