import numpy as np
import math as m
import matplotlib.pyplot as plt

e = m.e

## part (2.8.3.b)

def eul(f, x, dt):
    return (x + f(x)*dt)

def f(x):
    return (-x)


dt_arr = np.logspace(base=10.,start=0, stop = -4, num=5)
analytical_soln = np.exp(-1.)

def estimate_one(f, eul, dt, x0):
    x = x0
    t = 0.
    n = 0
    x_arr = []; t_arr = []
    while t <1:
        x_arr.append(x)
        t_arr.append(t)
        x = eul(f=f, x=x, dt=dt)
        t +=dt
        n +=1
    return (np.array(x_arr), np.array(t_arr), n)

X_vault=[]; T_vault = []; errors = []

for i, dt in enumerate(dt_arr):
    print('working on iteration: ',i,' with dt=',dt,' ...\n...')
    Xs, Ts, n = estimate_one(f=f,eul=eul,dt=dt,x0=1.)
    X_vault.append(Xs)
    T_vault.append(Ts)
    val = Xs[-1]
    err = np.abs(val-analytical_soln)
    errors.append(err)
    print('estimate is 1/e = ',Xs[-1],'on step',n)
    print('error E=',round(err,6),'\n\n')

print('analytical soln is:', analytical_soln)


## part (2.8.3.c)
plt.plot(dt_arr,errors,color='navy',lw=2)
plt.scatter(dt_arr,errors,color='orange', marker='+',lw=2,zorder=10)
plt.xlim(dt_arr[0]+dt_arr[0]/10.,dt_arr[-1]-dt_arr[-1]/10.)
plt.xlabel(r'timestep $\Delta t$')
plt.ylabel('error $E$')
plt.title(r'Error $E(\Delta t) \,= \,|\hat x(t=1) - x(t=1)|$')
plt.grid()
plt.savefig('figure2.8.3.c.i.png',dpi=290)
plt.clf()

plt.loglog(dt_arr,errors,color='teal',lw=2,zorder=10)
plt.scatter(dt_arr,errors,color='purple', marker='o',lw=3,zorder=10)
plt.xlabel(r'timestep $\log{\Delta t}$')
plt.ylabel('error $\log{E}$')
plt.xscale('log')
plt.yscale('log')
plt.title(r'Error $E(\Delta t) \,= \,|\hat x(t=1) - x(t=1)|$')
plt.xlim(dt_arr[0]+dt_arr[0]/10.,dt_arr[-1]-dt_arr[-1]/10.)
plt.grid()


plt.savefig('figure2.8.3.c.ii.png',dpi=290)