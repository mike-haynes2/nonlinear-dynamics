import numpy as np 
import math as m 
from scipy import constants
import matplotlib.pyplot as plt 
from matplotlib.pyplot import rcParams


def f_3(x):
    return np.sin(x)

def V_3(x):
    return np.cos(x)



points = np.arange(start=-3.*np.pi,stop=3.*np.pi,step=0.01)

plt.plot(points,V_3(points),label=r'potential $V(x)$', color='gold', lw=1.8)
plt.plot(points,f_3(points),label=r'system $\dot{x}=\sin{x}$',color='navy',lw=1.8,linestyle='dashed')
plt.grid()
plt.xlim(-2.*np.pi-0.1,2.*np.pi+0.1)
plt.ylim(-1.-0.1,1.+0.1)
plt.legend()
plt.xlabel('$x$')
plt.ylabel('$\dot{x}$ and $V(x)$')
#plt.grid()
plt.rcParams["axes.axisbelow"] = False

plt.title('System $f$ and Potential $V$')
plt.show()