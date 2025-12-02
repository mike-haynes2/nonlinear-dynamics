import numpy as np
from scipy import constants
import matplotlib.pyplot as plt
import math as m
from matplotlib.patches import Rectangle



def Lozi(x,y,a=1.7,b=0.5):
    return (1+y-(a*abs(x))),(b*x)




x0 = 0.1
y0 = 0.1

N = 200000

xarr = []
yarr = []

xarr.append(x0)
yarr.append(y0)


for i in range(N):
    xnew, ynew = Lozi(xarr[i],yarr[i])
    xarr.append(xnew)
    yarr.append(ynew)



fig, ax = plt.subplots(3, figsize=(7,9))

square_outline1 = Rectangle(
    (0.9, -0.1),
    0.5,
    0.25,
    facecolor='none',  # No fill color
    edgecolor='red',  # Outline color
    linewidth=2 ,      # Outline thickness
    zorder=100
)

square_outline2 = Rectangle(
    (1.25, -0.05),
    0.1,
    0.08,
    facecolor='none',  # No fill color
    edgecolor='red',  # Outline color
    linewidth=2 ,      # Outline thickness
    zorder=100
)


ax[0].scatter(xarr,yarr, marker='.',s=0.05)
ax[0].grid()
ax[0].set_title('Full domain')
ax[0].set_ylabel('y_n')
ax[0].set_xlim(-1.5,1.5)
ax[0].set_ylim(-0.75,0.75)
ax[0].add_patch(square_outline1)

ax[1].scatter(xarr,yarr, marker='.',s=0.1)
ax[1].grid()
ax[1].set_title('Domain Subset')
ax[1].set_ylabel('y_n')
ax[1].set_xlim(0.9,1.4)
ax[1].set_ylim(-0.1,0.15)
ax[1].add_patch(square_outline2)

ax[2].scatter(xarr,yarr, marker='.',s=0.5)
ax[2].grid()
ax[2].set_title('Domain Sub-subset')
ax[2].set_ylabel('y_n')
ax[2].set_xlabel('x_n')
ax[2].set_xlim(1.25,1.35)
ax[2].set_ylim(-0.05,0.03)



fig.suptitle('Lozi Strange Attractor',fontsize=16)
fig.tight_layout()
#plt.show()
plt.savefig('Lozi_attractor.png',dpi=310)
