import math as m
import numpy as np
from scipy import constants
import matplotlib.pyplot as plt



def f(x,r):
    return (r*np.exp(x))

Xarr = np.arange(start=-2.,stop=5.,step=0.01)



#plt.plot(Xarr,f(Xarr,r=1./10.),color='navy',lw=2,label='r = 0.1')
plt.plot(Xarr,f(Xarr,r=1./2.),color='teal',lw=2,label='r = 1/2')
# plt.plot(Xarr,f(Xarr,r=1),color='cyan',lw=2,label='r = 1')
plt.plot(Xarr,Xarr,lw=1.5,color='k',label='x_[n+1] = x_n')

plt.xlabel('$x_n$')
plt.ylabel('$x_{n+1}$')


plt.grid()
plt.legend()
plt.savefig('p4a_cobH.png', dpi=295.)