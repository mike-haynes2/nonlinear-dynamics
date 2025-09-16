import numpy as np
import math as m
import matplotlib.pyplot as plt



## params to set:
# width of time interval, symmetric about the $x(t)$ (vertical) axis
width = 20. # s
# resolution of plot routine
st = 0.02


tarr = np.arange(start=-width, stop=width+st, step=st)


xarr = np.sin(8.*tarr) + np.sin(9.*tarr)


fig, ax = plt.subplots(figsize=(12,5))

plt.axhline(y=0, lw=1, color='k')
plt.axvline(x=0, lw=1, color='k')

plt.plot(tarr,xarr, color='magenta', lw=1.2)

plt.plot(tarr, 1. + np.cos((1.)*tarr),color='cyan', lw=2, ls='dashed')
plt.plot(tarr, -(1. + np.cos((1.)*tarr)),color='cyan', lw=2,ls='dashed')

plt.plot(tarr, np.abs(2.*np.cos(tarr/2.)), color='springgreen',lw=3)
plt.plot(tarr, -np.abs(2.*np.cos(tarr/2.)), color='springgreen',lw=3)

plt.xlabel('$t$')
plt.ylabel('$x(t)$')
plt.title(r'Amplitude Modulation of $x(t)=\sin{8t} \,+\, \sin{9t}$')

plt.grid()
#plt.show()
plt.savefig('4.2.2_exact.png', dpi=290)
plt.close()
