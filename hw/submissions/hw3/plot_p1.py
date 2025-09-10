import numpy as np
from scipy import constants
import math as m
import matplotlib.pyplot as plt

from matplotlib.markers import MarkerStyle


def arrows_along(ax, range, dir):
    dir = 1. * np.sign(dir)
    start_vals = np.arange(start=range[0],stop=range[-1],step=1)
    if dir < 0:
        start_vals += np.ones_like(start_vals)
    x_length = 0.5
    for i,val in enumerate(start_vals):
        ax.arrow(val,0.,dir*x_length,0.,head_width=0.1, head_length=0.2,color='k')
    return None


def place_half_fp(x,y,stable_side='right'):
    plt.scatter(x,y,marker=MarkerStyle('o', fillstyle=stable_side), edgecolors='teal', s=200)
    plt.scatter(x,y,marker=MarkerStyle('o', fillstyle='none'), color='black', s=200)
    return None




def xF(r):
    return np.arccosh(r),-np.arccosh(r)

def xdot(x,r):
    return (r - np.cosh(x))



rvals = np.arange(start=1,stop=3,step=0.005)
pos, neg = xF(rvals)

fig, ax = plt.subplots()


plt.axhline(y=0, lw=1, color='k')
plt.axvline(x=0, lw=1, color='k')

plt.plot(rvals,pos,color='navy',label='stable')
plt.plot(rvals[1:],neg[1:],color='navy',ls='--',label='unstable')

plt.xlim(-0.5,3.)
plt.xlabel(r'$r$')
plt.ylabel(r'$x$')

plt.title('Bifurcation diagram: $\dot{x} = r - \cosh{x}$')

plt.grid()
plt.legend()
#plt.savefig('3.1.2_bifurcation.png',dpi=275)
#plt.show()
plt.close()





xarr = np.arange(start=-3.,stop=3.,step=0.01)
##
## r < r_c = 1
fig,ax = plt.subplots()
plt.axhline(y=0, lw=1, color='k')
plt.axvline(x=0, lw=1, color='k')

arrows_along(ax=ax,range=[-3,3],dir=-1.)

plt.plot(xarr,xdot(xarr,r=0.),label=r'$r=0$',color='teal')
plt.ylim(-5.,1.)

plt.xlabel(r'$x$')
plt.ylabel(r'$\dot{x}$')

plt.title(r'$\dot{x}=r-\cosh{x};\quad r<r_c\quad (r_c=1)$')

plt.grid()
plt.legend()

#plt.savefig('3.1.2_rLrc.png',dpi=275)
#plt.show()
plt.close()





##
## r  = r_c = 1
fig,ax = plt.subplots()
plt.axhline(y=0, lw=1, color='k')
plt.axvline(x=0, lw=1, color='k')

arrows_along(ax=ax,range=[-3,3],dir=-1.)

plt.plot(xarr,xdot(xarr,r=1.),label=r'$r=1$',color='teal')
place_half_fp(x=0,y=0,stable_side='right')

plt.ylim(-4.,2.)

plt.xlabel(r'$x$')
plt.ylabel(r'$\dot{x}$')

plt.title(r'$\dot{x}=r-\cosh{x};\quad r=r_c\quad (r_c=1)$')

plt.grid()
plt.legend()

#plt.savefig('3.1.2_rErc.png',dpi=275)
#plt.show()
plt.close()




##
## r  > r_c = 1
fig,ax = plt.subplots()
plt.axhline(y=0, lw=1, color='k')
plt.axvline(x=0, lw=1, color='k')



plt.plot(xarr,xdot(xarr,r=2.),label=r'$r=2$',color='teal')

arrows_along(ax=ax,range=[-3,-np.arccosh(2.)],dir=-1.)
arrows_along(ax=ax,range=[-np.arccosh(2.),np.arccosh(2.)],dir=1.)
arrows_along(ax=ax,range=[np.arccosh(2.),3.],dir=-1.)

plt.scatter(np.arccosh(2),0.,marker=MarkerStyle('o', fillstyle='full'), edgecolors='teal', s=200)
plt.scatter(-np.arccosh(2),0.,marker=MarkerStyle('o', fillstyle='none'), color='black', s=200)

plt.ylim(-3.,2.4)

plt.xlabel(r'$x$')
plt.ylabel(r'$\dot{x}$')

plt.title(r'$\dot{x}=r-\cosh{x};\quad r>r_c\quad (r_c=1)$')

plt.grid()
plt.legend()

#plt.savefig('3.1.2_rGrc.png',dpi=275)
#plt.show()
plt.close()