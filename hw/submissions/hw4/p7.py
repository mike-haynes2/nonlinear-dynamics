import numpy as np
import math as m
from scipy import constants

import matplotlib.pyplot as plt




def triang(phi):
    if np.abs(phi)>(2.*m.pi):
        phi /= (2.*np.pi)
    if phi < (-np.pi/2.):
        phi += 2.*m.pi
    if phi >= (3.*np.pi/2.):
        phi -= 2.*m.pi
    
    if phi >= -(np.pi/2.) and phi <= (np.pi/2.):
        ret = phi
    elif phi >= (np.pi/2.) and phi <= (3.*np.pi/2.):
        ret = m.pi - phi
    return ret



phis = np.arange(start=-(np.pi/2.),stop=(3.*np.pi/2.),step=(np.pi/200.))

triang_output = [triang(phi) for phi in phis]


fig,ax = plt.subplots(figsize=(9,5))
plt.axhline(y=0, lw=1, color='k')
plt.axvline(x=0, lw=1, color='k')

plt.plot(phis,triang_output, color='teal',lw=1.2)

plt.xlabel('$\phi$')
plt.ylabel('$f(\phi)$')

plt.title('Graph of Firefly response function $f$')
plt.grid()
#plt.show()

plt.savefig('p7_f.png',dpi=260)

