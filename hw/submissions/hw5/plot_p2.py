import numpy as np
import math as m
import matplotlib.pyplot as plt



def gen_sys(x,y,a,b,c,d):
    xdot = a*x + b*y
    ydot = c*x + d*y
    return xdot, ydot




a= 1.
b = 0.
c = 0. 
d = 1.




l = 1.
xmin = -l
xmax = l
ymin = -l
ymax = l


res = 0.01

Xarr = np.arange(start=xmin,stop=xmax,step=res)
Yarr = np.arange(start=ymin,stop=ymax,step=res)

X, Y = np.meshgrid(Xarr,Yarr)
dX, dY = gen_sys(X,Y,a,b,c,d)
mag = np.sqrt(dX**2. + dY**2.)


fig, ax = plt.subplots(figsize=(10,7))
#NOTE: NEED matplotlib version 3.6.0 minimum in order to use the broken_streamlines keyword argument for the ax.streamplot() call. 
#I had to install in user space, so I uninstalled after completion [work desktop]
pp = ax.streamplot(X, Y, dX, dY, color=mag, cmap = 'turbo', linewidth=0.9, density=2.)
cbar = fig.colorbar(pp.lines)
cbar.set_label(r'$\sqrt{\dot{x}^2 + \dot{y}^2}$')

ax.set_xlim(xmin,xmax)
ax.set_ylim(ymin,ymax)
ax.grid()

plt.title('Phase Portrait')

plt.show()

# plt.savefig('VDP_phase_portrait_1.png', dpi=325.)
# plt.close()





