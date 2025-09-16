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






marr = np.arange(start=0.,stop=1.,step=0.01)

T_arr = np.array([1.,2.,4.])
Jn_arr = np.array([0.5,1.,2.,4.])


def h(m,T,Jn):
    return ((T*np.arctanh(m)) - Jn*m)

color = iter(plt.cm.rainbow(np.linspace(0, 1, len(T_arr)*len(Jn_arr))))

fig, ax = plt.subplots()

plt.axhline(y=0, lw=1, color='k')
plt.axvline(x=0, lw=1, color='k')

for i,T in enumerate(T_arr):
    for j,Jn in enumerate(Jn_arr):
        clr = next(color)
        if T > Jn:
            plt.plot(marr,h(marr,T=T,Jn=Jn),lw=1,color=clr,ls='--',label=f'$T=${T}; $J\,n=${Jn}')
        else:
            plt.plot(marr,h(marr,T=T,Jn=Jn),lw=1,color=clr,label=f'$T=${T}; $J\,n=${Jn}')

plt.title(r'Equilibrium magnetization ($h=T\tanh^{-1}{m}-Jnm$) for various $T, J⋅n$')
plt.grid()
plt.legend()
plt.savefig('3.6.7_params.png',dpi=275)
#plt.show()
plt.close()


Marr = np.arange(start=-1.,stop=1.,step=0.01)

fig, ax = plt.subplots()

plt.axhline(y=0, lw=1, color='k')
plt.axvline(x=0, lw=1, color='k')

plt.plot(Marr,h(Marr,T=4.,Jn=2.),lw=2,color='teal')
plt.scatter(0.,0.,marker=MarkerStyle('o', fillstyle='none'), color='black', s=200,label='unstable')


plt.title(r'$h=T\tanh^{-1}{m}-Jnm$ for $T>J⋅n$')
plt.grid()
plt.legend()
plt.savefig('3.6.7_Tg.png',dpi=275)
#plt.show()
plt.close()




fig, ax = plt.subplots()

plt.axhline(y=0, lw=1, color='k')
plt.axvline(x=0, lw=1, color='k')

plt.plot(Marr,h(Marr,T=1.,Jn=2.),lw=2,color='teal')
plt.scatter(-0.957,0.,marker=MarkerStyle('o', fillstyle='none'), color='teal', s=200, label='unstable')
plt.scatter(0.957,0.,marker=MarkerStyle('o', fillstyle='none'), color='teal', s=200)
plt.scatter(0.,0.,marker=MarkerStyle('o', fillstyle='full'), color='teal', s=200, label='stable',zorder=10)


plt.title(r'$h=T\tanh^{-1}{m}-Jnm$ for $T<J⋅n$')
plt.grid()
plt.legend()
plt.savefig('3.6.7_Tl.png',dpi=275)
#plt.show()
plt.close()

