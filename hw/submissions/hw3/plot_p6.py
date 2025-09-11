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
unit = np.arange(start=0.001,stop=1.,step=0.001)

xpo = xarr[xarr > 0.]
xne = xarr[xarr<=0.]

xstar = np.sqrt((1./unit)-1)


fig, ax = plt.subplots()


plt.axhline(y=0, lw=1, color='k')
plt.axvline(x=0, lw=1, color='k')

plt.plot(unit,xstar,color='navy',linestyle='dashed')
plt.plot(unit,-xstar,color='navy',linestyle='dashed')
plt.plot(xarr[xarr>1],np.zeros_like(xarr[xarr>1]),color='navy',linestyle='dashed',lw=2,label=r'unstable')
plt.plot(xarr[xarr<=1],np.zeros_like(xarr[xarr<=1]),color='navy',lw=2,label=r'stable')
# plt.plot(xneg,xpos,color='navy',label='stable')
# plt.plot(xneg,xneg,color='navy',ls='--',label='unstable')
# plt.plot(xpos,xpos,color='navy')
# plt.plot(xpos,xneg,color='navy',ls='--')

#place_half_fp(x=0.,y=0.,stable_side='bottom',color='navy')
#plt.xlim(-0.5,3.)
plt.xlabel(r'$r$')
plt.ylabel(r'$x$')

plt.title(r'Bifurcation diagram: $\dot{x} = rx\,-\,\frac{x}{1+x^2}$')

plt.grid()
plt.legend()
plt.savefig('3.4.8_bifurcation.png',dpi=275)
#plt.show()
#plt.close()





def xdot(x,r):
    return ((x*r)-(x/(1. + x**2)))




# ##
# # r  <  0
fig,ax = plt.subplots()
plt.axhline(y=0, lw=1, color='k')
plt.axvline(x=0, lw=1, color='k')

# note: due to plot range this requires you to change the arrow head width in function
arrows_along(ax=ax,range=[-3,0],dir=1.)
arrows_along(ax=ax,range=[ 0,3],dir=-1.)

plt.plot(xarr,xdot(xarr,r=-1.),label=r'$r=-1$',color='teal')
#place_half_fp(x=0,y=0,stable_side='left')
plt.scatter(x=0,y=0,marker=MarkerStyle('o', fillstyle='full'), color='teal', s=200,zorder=10)

# plt.xlim(-2.,1.5)
# plt.ylim(-5.,4.)

plt.xlabel(r'$x$')
plt.ylabel(r'$\dot{x}$')

plt.title(r'$\dot{x} = rx\,-\,\frac{x}{1+x^2}\quad r < 0\quad (r_c=1)$')

plt.grid()
plt.legend()

#plt.savefig('3.4.8_rL0.png',dpi=275)
#plt.show()
plt.close()


# # r  =  0
fig,ax = plt.subplots()
plt.axhline(y=0, lw=1, color='k')
plt.axvline(x=0, lw=1, color='k')

# note: due to plot range this requires you to change the arrow head width in function
arrows_along(ax=ax,range=[-3,0],dir=1.)
arrows_along(ax=ax,range=[ 0,3],dir=-1.)

plt.plot(xarr,xdot(xarr,r=0.),label=r'$r=0$',color='teal')
#place_half_fp(x=0,y=0,stable_side='left')
plt.scatter(x=0,y=0,marker=MarkerStyle('o', fillstyle='full'), color='teal', s=200,zorder=10)

plt.xlim(-3.,3.)
plt.ylim(-1.,1.)

plt.xlabel(r'$x$')
plt.ylabel(r'$\dot{x}$')

plt.title(r'$\dot{x} = rx\,-\,\frac{x}{1+x^2}\quad r < 0\quad (r_c=1)$')

plt.grid()
plt.legend()

#plt.savefig('3.4.8_rE0.png',dpi=275)
#plt.show()
plt.close()



# # 0 < r < 1
fig,ax = plt.subplots()
plt.axhline(y=0, lw=1, color='k')
plt.axvline(x=0, lw=1, color='k')

# note: due to plot range this requires you to change the arrow head width in function
arrows_along(ax=ax,range=[-3,-1],dir=-1.)
arrows_along(ax=ax,range=[ -1,0],dir=1.)
arrows_along(ax=ax,range=[ 0,1],dir=-1.)
arrows_along(ax=ax,range=[ 1,3],dir=1.)

plt.plot(xarr,xdot(xarr,r=1./2.),label=r'$r=\frac{1}{2}$',color='teal')
#place_half_fp(x=0,y=0,stable_side='left')
plt.scatter(x=0,y=0,marker=MarkerStyle('o', fillstyle='full'), color='teal', s=200,zorder=10)
plt.scatter(x=-1,y=0,marker=MarkerStyle('o', fillstyle='none'), color='k', s=200,zorder=10)
plt.scatter(x=1,y=0,marker=MarkerStyle('o', fillstyle='none'), color='k', s=200,zorder=10)

plt.xlim(-3.,3.)
plt.ylim(-1.,1.)

plt.xlabel(r'$x$')
plt.ylabel(r'$\dot{x}$')

plt.title(r'$\dot{x} = rx\,-\,\frac{x}{1+x^2}\quad 0 < r < r_c\quad (r_c=1)$')

plt.grid()
plt.legend()

#plt.savefig('3.4.8_rLrc.png',dpi=275)
#plt.show()
plt.close()



# # r = 1
fig,ax = plt.subplots()
plt.axhline(y=0, lw=1, color='k')
plt.axvline(x=0, lw=1, color='k')

# note: due to plot range this requires you to change the arrow head width in function
arrows_along(ax=ax,range=[-3,0],dir=-1.)
arrows_along(ax=ax,range=[ 0,3],dir=1.)

plt.plot(xarr,xdot(xarr,r=1.),label=r'$r=1$',color='teal')
#place_half_fp(x=0,y=0,stable_side='left')
plt.scatter(x=0,y=0,marker=MarkerStyle('o', fillstyle='none'), color='k', s=200,zorder=10)
#plt.scatter(x=-1,y=0,marker=MarkerStyle('o', fillstyle='none'), color='k', s=200,zorder=10)
#plt.scatter(x=1,y=0,marker=MarkerStyle('o', fillstyle='none'), color='k', s=200,zorder=10)

plt.xlim(-3.,3.)
plt.ylim(-1.,1.)

plt.xlabel(r'$x$')
plt.ylabel(r'$\dot{x}$')

plt.title(r'$\dot{x} = rx\,-\,\frac{x}{1+x^2}\quad r = r_c\quad (r_c=1)$')

plt.grid()
plt.legend()

#plt.savefig('3.4.8_rErc.png',dpi=275)
#plt.show()
plt.close()


