import math as m
import numpy as np
from scipy import constants
import matplotlib.pyplot as plt



def f(x,r):
    return (r*np.cos(x))

rs = np.arange(start=0.,stop=8.,step=0.05)


Nmax = 1000


fig, ax = plt.subplots()

for rdx,rval in enumerate(rs):
    x0 = np.random.rand()
    
    xn = []
    xn.append(x0)
    for i in range(Nmax):
        xnew = f(xn[i],rval)
        xn.append(xnew)

    xnK = xn[250:]
    arR = np.ones_like(xnK)*rval
    plt.scatter(arR,xnK,marker=',', s=1, linewidths=0,color='navy')


plt.grid()
plt.title('Orbit Diagram: $f(x_n) = r\cos{x_n}$')

#plt.show()
plt.savefig('p2_orbit.png',dpi=300)