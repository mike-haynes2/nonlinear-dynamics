import math as m
import numpy as np
from scipy import constants

import matplotlib.pyplot as plt


x = np.arange(start=0.,stop=5.,step=0.3)
y = np.arange(start=0.,stop=5.,step=0.3)

X, Y = np.meshgrid(x,y)

def epidemic(x,y,k,l):
    return (-k * x * y), (k * x * y - l * y)


U, V = epidemic(X,Y,k=1.,l=1.)



fig, ax = plt.subplots(figsize=(8,5))
q = ax.quiver(X,Y,U,V, label='$(\dot{x},\dot{y})$', color='teal')

plt.axhline(y=0, lw=1, color='r', label=r'$kxy=0$')
plt.axvline(x=0, lw=1, color='r')
plt.axvline(x=1., lw=1, color='b', label=r'$x=l/k$')

plt.xlabel(r'$x$')
plt.ylabel(r'$y$')

plt.title('Vector field & Nullclines for Epidemic model: $k=l=1$')
plt.grid()
plt.legend()

#plt.show()
plt.savefig('p1b_vector_field.png', dpi=270)
