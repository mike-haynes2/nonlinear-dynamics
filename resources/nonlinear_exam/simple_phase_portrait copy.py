import matplotlib.pyplot as plt
import numpy as np
Xs = np.arange(start=-3.,stop=3.,step=0.01)
X,Y = np.meshgrid(Xs,Xs)
XD = X*(3.-Y-2.*np.exp(X**2.))
YD = (Y-1.)*(X-1./2.)
plt.streamplot(X,Y, XD, YD,color=np.sqrt((XD)**2 + (YD)**2), cmap='plasma',linewidth=0.9,density=2)
plt.show()
