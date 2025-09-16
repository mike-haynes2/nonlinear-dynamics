import numpy as np
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






## params to set:
# width of time interval, symmetric about the $x(t)$ (vertical) axis
width = 2.*m.pi # s
# resolution of plot routine
st = 0.01


tarr = np.arange(start=-width+m.pi, stop=width+st, step=st)


def g(th):
    return (np.sin(th) + np.cos(2.*th))

def f(th,mu):
    return (mu + g(th=th))



zero1= 0.25268
zero2 = m.pi - zero1


# mu = -9/8

fig,ax = plt.subplots(figsize=(9,5))
plt.axhline(y=0, lw=1, color='k')
plt.axvline(x=0, lw=1, color='k')

plt.plot(tarr, f(tarr,mu=(-9./8.)), color='teal', label=r'$\mu=-\frac{9}{8}$')

place_half_fp(x=zero1,y=0,stable_side='right',color='teal')
place_half_fp(x=zero2,y=0,stable_side='right',color='teal')

plt.title(r'Dynamical system $\dot{\theta}= f(\theta,\mu=-\frac{9}{8})$')
plt.grid()
plt.legend()
#plt.show()
#plt.savefig('4.3.6_muL.png', dpi=250)
plt.close()




#-9/8 < mu < 0

fig,ax = plt.subplots(figsize=(9,5))
plt.axhline(y=0, lw=1, color='k')
plt.axvline(x=0, lw=1, color='k')

plt.plot(tarr, f(tarr,mu=(-1./2.)), color='teal', label=r'$\mu=-\frac{1}{2}$')

plt.scatter(x=-m.pi/10.,y=0,marker=MarkerStyle('o', fillstyle='none'), color='teal', s=200,zorder=10)
plt.scatter(x=7.*m.pi/10.,y=0,marker=MarkerStyle('o', fillstyle='none'), color='teal', s=200,zorder=10)

plt.scatter(x=3.*m.pi/10.,y=0.,marker=MarkerStyle('o', fillstyle='full'), color='teal', s=200,zorder=10)
plt.scatter(x=11.*m.pi/10.,y=0.,marker=MarkerStyle('o', fillstyle='full'), color='teal', s=200,zorder=10)


plt.title(r'Dynamical system $\dot{\theta}= f(\theta,\mu): \quad -\frac{9}{8}<\mu<0$')
plt.grid()
plt.legend()
#plt.show()
#plt.savefig('4.3.6_muLm.png', dpi=250)
plt.close()




# mu = 0

fig,ax = plt.subplots(figsize=(9,5))
plt.axhline(y=0, lw=1, color='k')
plt.axvline(x=0, lw=1, color='k')

plt.plot(tarr, f(tarr,mu=(0.)), color='teal', label=r'$\mu=0$')

place_half_fp(x=m.pi/2.,y=0,stable_side='left',color='teal')

plt.scatter(x=7.*m.pi/6.,y=0.,marker=MarkerStyle('o', fillstyle='full'), color='teal', s=200,zorder=10)
plt.scatter(x=-m.pi/6.,y=0.,marker=MarkerStyle('o', fillstyle='none'), color='teal', s=200,zorder=10)


plt.title(r'Dynamical system $\dot{\theta}= f(\theta,\mu=0)$')
plt.grid()
plt.legend()
#plt.show()
#plt.savefig('4.3.6_muE0.png', dpi=250)
plt.close()


# mu = 1

fig,ax = plt.subplots(figsize=(9,5))
plt.axhline(y=0, lw=1, color='k')
plt.axvline(x=0, lw=1, color='k')

plt.plot(tarr, f(tarr,mu=(1.)), color='teal', label=r'$\mu=1$')

plt.scatter(x=4.0375,y=0.,marker=MarkerStyle('o', fillstyle='full'), color='teal', s=200,zorder=10)
plt.scatter(x=-0.891,y=0.,marker=MarkerStyle('o', fillstyle='none'), color='teal', s=200,zorder=10)


plt.title(r'Dynamical system $\dot{\theta}= f(\theta,\mu=1)$')
plt.grid()
plt.legend()
#plt.show()
#plt.savefig('4.3.6_mu1.png', dpi=250)
plt.close()





# mu = 2

fig,ax = plt.subplots(figsize=(9,5))
plt.axhline(y=0, lw=1, color='k')
plt.axvline(x=0, lw=1, color='k')

plt.plot(tarr, f(tarr,mu=(2.)), color='teal', label=r'$\mu=2$')

place_half_fp(x=3.*m.pi/2.,y=0,stable_side='left',color='teal')

plt.title(r'Dynamical system $\dot{\theta}= f(\theta,\mu=2)$')
plt.grid()
plt.legend()
#plt.show()
#plt.savefig('4.3.6_mu2.png', dpi=250)
plt.close()