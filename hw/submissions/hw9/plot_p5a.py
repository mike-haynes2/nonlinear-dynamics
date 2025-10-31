import numpy as np
import math as m
from scipy import constants 
import matplotlib.pyplot as plt



Xs = np.arange(start=-4.,stop=4.,step=0.02)

bs = [1.,2.,4.]
colors=['salmon','magenta','navy']


for i,b in enumerate(bs):
    N1 = ((b+1)*Xs-1)/((Xs**2))
    plt.plot(Xs,N1, color=colors[i],ls='dashed',lw=2,label=f'b = {b}')
    N2 = b/Xs
    plt.plot(Xs,N2, color=colors[i],lw=2.)



plt.xlim(-4.,4.)
plt.ylim(-6.,6.)
plt.xlabel('$x$')
plt.ylabel('$y$')

plt.grid()
plt.legend()
plt.title('Nullclines (8.3.1): $(x,y)-plane$')
plt.savefig('p5b_nclines.png', dpi=260.)