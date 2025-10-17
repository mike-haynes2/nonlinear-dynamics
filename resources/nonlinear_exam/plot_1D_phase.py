import numpy as np
from scipy import constants
import math as m
import matplotlib.pyplot as plt

from matplotlib.markers import MarkerStyle


def arrows_along(ax, range, dir):
    dir = 1. * np.sign(dir)
    start_vals = np.arange(start=range[0],stop=range[-1],step=1)
    if dir < 0:
        start_vals += (np.ones_like(start_vals))
    x_length = 0.5
    for i,val in enumerate(start_vals):
        ax.arrow(val,0.,dir*x_length,0.,head_width=0.1, head_length=0.2,color='k')
    return None


def place_half_fp(x,y,stable_side='right',color='teal'):
    plt.scatter(x,y,marker=MarkerStyle('o', fillstyle=stable_side), color=color, s=200)
    plt.scatter(x,y,marker=MarkerStyle('o', fillstyle='none'), color='black', s=200)
    return None






xarr = np.arange(start=-3.,stop=3.,step=0.001)

xpo = xarr[xarr > 0.]
xne = xarr[xarr<=0.]

xstar = np.sqrt(xpo)/2.


fig, ax = plt.subplots()


plt.axhline(y=0, lw=1, color='k')
plt.axvline(x=0, lw=1, color='k')

plt.plot(xpo,xstar,color='navy')
plt.plot(xpo,-xstar,color='navy')
plt.plot(xpo,np.zeros_like(xpo),color='navy',linestyle='dashed',lw=2,label=r'unstable')
plt.plot(xne,np.zeros_like(xne),color='navy',lw=2,label=r'stable')
# plt.plot(xneg,xpos,color='navy',label='stable')
# plt.plot(xneg,xneg,color='navy',ls='--',label='unstable')
# plt.plot(xpos,xpos,color='navy')
# plt.plot(xpos,xneg,color='navy',ls='--')

#place_half_fp(x=0.,y=0.,stable_side='bottom',color='navy')
#plt.xlim(-0.5,3.)
plt.xlabel(r'$r$')
plt.ylabel(r'$x$')

plt.title('Bifurcation diagram: $\dot{x} = rx\,-\,4x^3$')

plt.grid()
plt.legend()
#plt.savefig('3.4.3_bifurcation.png',dpi=275)
#plt.show()
plt.close()





def xdot(x,r):
    return ((x*r)-(4.*(x**3)))




##
# r  <=  0
fig,ax = plt.subplots()
plt.axhline(y=0, lw=1, color='k')
plt.axvline(x=0, lw=1, color='k')

# note: due to plot range this requires you to change the arrow head width in function
arrows_along(ax=ax,range=[-3,0],dir=1.)
arrows_along(ax=ax,range=[ 0,3],dir=-1.)

plt.plot(xarr,xdot(xarr,r=0.),label=r'$r=0$',color='teal')
#place_half_fp(x=0,y=0,stable_side='left')
plt.scatter(x=0,y=0,marker=MarkerStyle('o', fillstyle='full'), color='teal', s=200,zorder=10)

# plt.xlim(-2.,1.5)
# plt.ylim(-5.,4.)

plt.xlabel(r'$x$')
plt.ylabel(r'$\dot{x}$')

plt.title(r'$\dot{x} = rx\,-\,4x^3\quad r≤ r_c\quad (r_c=0)$')

plt.grid()
plt.legend()

#plt.savefig('3.4.3_rErc.png',dpi=275)
#plt.show()
plt.close()





##
# r  <=  0
fig,ax = plt.subplots()
plt.axhline(y=0, lw=1, color='k')
plt.axvline(x=0, lw=1, color='k')

arrows_along(ax=ax,range=[-3,-1.],dir=1.)
arrows_along(ax=ax,range=[ -1.,0],dir=-1.)
arrows_along(ax=ax,range=[ 0,1.],dir=1.)
arrows_along(ax=ax,range=[ 1.,3.],dir=-1.)


plt.plot(xarr,xdot(xarr,r=4.),label=r'$r=4$',color='teal')
#place_half_fp(x=0,y=0,stable_side='left')
plt.scatter(x=0,y=0,marker=MarkerStyle('o', fillstyle='none'), color='black', s=200,zorder=10)
plt.scatter(x=-1,y=0,marker=MarkerStyle('o', fillstyle='full'), color='teal', s=200,zorder=10)
plt.scatter(x=1,y=0,marker=MarkerStyle('o', fillstyle='full'), color='teal', s=200,zorder=10)
plt.xlim(-2.,2.)
plt.ylim(-4.,4.)

plt.xlabel(r'$x$')
plt.ylabel(r'$\dot{x}$')

plt.title(r'$\dot{x} = rx\,-\,4x^3\quad r ≥ r_c\quad (r_c=0)$')

plt.grid()
plt.legend()

#plt.savefig('3.4.3_rGrc.png',dpi=275)
plt.show()
#plt.close()
