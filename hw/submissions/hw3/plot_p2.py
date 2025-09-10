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


def place_half_fp(x,y,stable_side='right',color='teal'):
    plt.scatter(x,y,marker=MarkerStyle('o', fillstyle=stable_side), color=color, s=200)
    plt.scatter(x,y,marker=MarkerStyle('o', fillstyle='none'), color='black', s=200)
    return None






xpos = np.arange(start=0.,stop=3.,step=0.01)
xneg = - xpos

fig, ax = plt.subplots()


plt.axhline(y=0, lw=1, color='k')
plt.axvline(x=0, lw=1, color='k')

plt.plot(xneg,xpos,color='navy',label='stable')
plt.plot(xneg,xneg,color='navy',ls='--',label='unstable')
plt.plot(xpos,xpos,color='navy')
plt.plot(xpos,xneg,color='navy',ls='--')

place_half_fp(x=0.,y=0.,stable_side='top',color='navy')
#plt.xlim(-0.5,3.)
plt.xlabel(r'$r$')
plt.ylabel(r'$x$')

plt.title('Bifurcation diagram: $\dot{x} = r^2 - x^2$')

plt.grid()
plt.legend()
#plt.savefig('3.1.5a_bifurcation.png',dpi=275)
#plt.show()
plt.close()





xarr = np.arange(start=-3.,stop=3.,step=0.01)

def xdot(x,r):
    return ((r **2.)-(x**2.))




##
## r  = r_c = 0
fig,ax = plt.subplots()
plt.axhline(y=0, lw=1, color='k')
plt.axvline(x=0, lw=1, color='k')

arrows_along(ax=ax,range=[-3,3],dir=-1.)

plt.plot(xarr,xdot(xarr,r=0.),label=r'$r=0$',color='teal')
place_half_fp(x=0,y=0,stable_side='right')

plt.xlim(-2.,2.)
plt.ylim(-3.,1.)

plt.xlabel(r'$x$')
plt.ylabel(r'$\dot{x}$')

plt.title(r'$\dot{x}=r^2-x^2;\quad r=r_c\quad (r_c=0)$')

plt.grid()
plt.legend()

#plt.savefig('3.1.5a_rErc.png',dpi=275)
#plt.show()
plt.close()







##
## r  > r_c = 0
fig,ax = plt.subplots()
plt.axhline(y=0, lw=1, color='k')
plt.axvline(x=0, lw=1, color='k')

arrows_along(ax=ax,range=[-3,-1],dir=-1.)
arrows_along(ax=ax,range=[-1,1],dir=1.)
arrows_along(ax=ax,range=[1,3],dir=-1.)


plt.plot(xarr,xdot(xarr,r=1.),label=r'$r=1$',color='teal')
plt.scatter(1.,0.,marker=MarkerStyle('o', fillstyle='full'), edgecolors='teal', s=200, label='stable')
plt.scatter(-1.,0.,marker=MarkerStyle('o', fillstyle='none'), color='black', s=200, label='unstable')


plt.xlim(-2.,2.)
plt.ylim(-2.5,1.5)

plt.xlabel(r'$x$')
plt.ylabel(r'$\dot{x}$')

plt.title(r'$\dot{x}=r^2-x^2;\quad r>r_c\quad (r_c=0)$')

plt.grid()
plt.legend()

#plt.savefig('3.1.5a_rGrc.png',dpi=275)
#plt.show()
plt.close()






fig,ax = plt.subplots()
plt.axhline(y=0, lw=1, color='k')
plt.axvline(x=0, lw=1, color='k')

plt.plot(xarr,xarr,color='orange')
plt.plot(xarr,-xarr,color='orange')

plt.xlabel(r'$r$')
plt.ylabel(r'$x^*$')

plt.title(r'$x^*(r)$ for the system $\dot{x}=r^2-x^2$')

plt.grid()
#plt.legend()
plt.savefig('3.1.5a_xstar.png',dpi=275)
#plt.show()
#plt.close()