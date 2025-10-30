import numpy as np
import math as m
from scipy import constants 
import matplotlib.pyplot as plt



xs = np.arange(start=0.,stop=3.,step=0.02)
eps = np.copy(xs)
eps1 = 1./(4.*(xs+1))
eps2 = 1./(4.*(xs-1))

eps_ = xs / (4.*(1.- (xs**2)*np.cos(2.*np.arccos(1./xs))))

plt.plot(xs,eps1,color='r',label=r'even $n$')
plt.plot(xs,eps2,color='b',label=r'odd $n$')
plt.plot(xs,eps_,color='teal',label=r'$\phi^*=\arccos{(1/\gamma)}$')
plt.xlim(0.,2.)
plt.ylim(0.,2.)
plt.xlabel('$\gamma$')
plt.ylabel('$\epsilon$')
#plt.plot(xs,eps2)
# plt.plot(xs, (np.cos(2.*np.arccos(1./xs))), color='teal' )
# plt.plot(xs, -(np.cos(2.*np.arccos(1./xs))), color='teal', label='stable')
# plt.plot(xs[len(xs)//3:], np.zeros_like(xs[len(xs)//3:]), color='teal', ls='dashed', label='unstable')
plt.grid()
plt.legend()
plt.title('Stability Diagram: $(\gamma,\epsilon)$')
plt.savefig('p1b_stability.png', dpi=260.)