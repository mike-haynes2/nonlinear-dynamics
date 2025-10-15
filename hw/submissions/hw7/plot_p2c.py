import math as m
import numpy as np

import matplotlib.pyplot as plt



def sys(x,y):
    ee = np.exp(x**2. + y**2.)
    return (-2.*x*ee), (-2.*y*ee)




l = 2.
xmin = -l
xmax = l
ymin = -l
ymax = l


res = 0.01

Xarr = np.arange(start=xmin,stop=xmax,step=res)
Yarr = np.arange(start=ymin,stop=ymax,step=res)

X, Y = np.meshgrid(Xarr,Yarr)
dX, dY = sys(X,Y)
mag = np.sqrt(dX**2. + dY**2.)


fig, ax = plt.subplots(figsize=(10,7))
#NOTE: NEED matplotlib version 3.6.0 minimum in order to use the broken_streamlines keyword argument for the ax.streamplot() call. 
#I had to install in user space, so I uninstalled after completion [work desktop]
pp = ax.streamplot(X, Y, dX, dY, color=np.log(mag), cmap = 'turbo', linewidth=0.9, density=1.4, broken_streamlines=False)
cbar = fig.colorbar(pp.lines)
cbar.set_label(r'$\log{\sqrt{\dot{x}^2 + \dot{y}^2}}$')

plt.xlabel(r'$x$')
plt.ylabel(r'$y$')

ax.set_xlim(xmin,xmax)
ax.set_ylim(ymin,ymax)
ax.grid()

plt.title('Phase Portrait: 7.2.9(c) ')

#plt.show()

plt.savefig('phase_portrait_2c.png', dpi=290.)
plt.close()


const_vals = np.arange(11)

def calcVc(x,val):
    yp = np.sqrt(np.log(val)- x**2.)
    ym = np.flip(-yp)
    y = np.concatenate((ym,yp))
    return y


xs = np.arange(start=0.,stop=xmax,step=res)


fig, ax = plt.subplots(figsize=(10,7))

for val in const_vals:
    ys = calcVc(xs,val)
    ax.plot(Xarr,ys,label='V = '+str(val))

ax.set_xlabel('x')
ax.set_ylabel('y')

plt.grid()
plt.legend()
#plt.show()
plt.savefig('iso_V_2c.png', dpi=260.)
