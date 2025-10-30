import numpy as np
import math as m
from scipy import constants 
import matplotlib.pyplot as plt



Xs = np.arange(start=-2.,stop=2.,step=0.02)

bs = [0.,0.5,1.,1.5]


N2 = Xs/(1.+Xs)
plt.plot(Xs,N2,lw=2.,label=r'$y=\frac{x}{a(1-x)}$, $a=1$', color='magenta')


for b in bs:
    N1 = (b-Xs)*(1+Xs)
    plt.plot(Xs,N1, color='teal',ls='dashed',lw=2,label=f'b = {b}')


plt.xlim(-1.,2.)
plt.ylim(-1.,2.)
plt.xlabel('$x$')
plt.ylabel('$y$')

plt.grid()
plt.legend()
plt.title('Nullclines (8.2.9): $(x,y)-plane$')
plt.savefig('p4a_nclines.png', dpi=260.)