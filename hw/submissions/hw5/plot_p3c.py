import numpy as np
import math as m
import matplotlib.pyplot as plt

def LRC(I, phi, L, R, C):
    if L<0. or R<0. or C<0.:
        raise(ValueError('Note that all circuit parameter values must be positive'))
    Idot = phi
    phidot = (-1./L) * ( (R*phi) + I/C)
    return Idot,phidot


l = 2.
xmin = -l
xmax = l
ymin = -l
ymax = l


res = 0.01

Xarr = np.arange(start=xmin,stop=xmax,step=res)
Yarr = np.arange(start=ymin,stop=ymax,step=res)

X, Y = np.meshgrid(Xarr,Yarr)

L = C = 1.


## case i
# R = 3.

# dX, dY = LRC(X,Y, L=L, R=R, C=C)
# mag = np.sqrt(dX**2. + dY**2.)

# fig, ax = plt.subplots(figsize=(10,7))
# #NOTE: NEED matplotlib version 3.6.0 minimum in order to use the broken_streamlines keyword argument for the ax.streamplot() call. 
# #I had to install in user space, so I uninstalled after completion [work desktop]
# #pp = ax.streamplot(X, Y, dX, dY, color='teal', linewidth=0.9, density=2.)
# plt.annotate('R=3, C = L = 1',xy=(0.9, 0.9), xytext=(1, 1),
#                 xycoords='axes fraction', textcoords='axes fraction',
#                 ha='right', va='top', fontsize=14, color='k')

# pp = ax.streamplot(X, Y, dX, dY, color=mag, cmap = 'turbo', linewidth=0.9, broken_streamlines=False, density=2.)
# cbar = fig.colorbar(pp.lines)
# cbar.set_label(r'$\sqrt{\dot{x}^2 + \dot{y}^2}$')

# ax.set_xlim(xmin,xmax)
# ax.set_ylim(ymin,ymax)
# ax.grid()

# plt.title('Phase Portrait: LRC Circuit, $R^2C - 4L > 0$')
# #plt.show()
# plt.savefig('LRC_phase_portrait_1.png', dpi=325.)
# #plt.close()


## case ii
# R = 2.

# dX, dY = LRC(X,Y, L=L, R=R, C=C)
# mag = np.sqrt(dX**2. + dY**2.)

# fig, ax = plt.subplots(figsize=(10,7))
# #NOTE: NEED matplotlib version 3.6.0 minimum in order to use the broken_streamlines keyword argument for the ax.streamplot() call. 
# #I had to install in user space, so I uninstalled after completion [work desktop]
# #pp = ax.streamplot(X, Y, dX, dY, color='teal', linewidth=0.9, density=2.)
# plt.annotate('R = 2; C = L = 1',xy=(0.9, 0.9), xytext=(1, 1),
#                 xycoords='axes fraction', textcoords='axes fraction',
#                 ha='right', va='top', fontsize=14, color='k')

# pp = ax.streamplot(X, Y, dX, dY, color=mag, cmap = 'turbo', linewidth=0.9, broken_streamlines=False, density=2.)
# cbar = fig.colorbar(pp.lines)
# cbar.set_label(r'$\sqrt{\dot{x}^2 + \dot{y}^2}$')

# ax.set_xlim(xmin,xmax)
# ax.set_ylim(ymin,ymax)
# ax.grid()

# plt.title('Phase Portrait: LRC Circuit, $R^2C - 4L = 0$')
# #plt.show()
# plt.savefig('LRC_phase_portrait_2.png', dpi=325.)
# #plt.close()


## case iii
# R = 1.

# dX, dY = LRC(X,Y, L=L, R=R, C=C)
# mag = np.sqrt(dX**2. + dY**2.)

# fig, ax = plt.subplots(figsize=(10,7))
# #NOTE: NEED matplotlib version 3.6.0 minimum in order to use the broken_streamlines keyword argument for the ax.streamplot() call. 
# #I had to install in user space, so I uninstalled after completion [work desktop]
# #pp = ax.streamplot(X, Y, dX, dY, color='teal', linewidth=0.9, density=2.)
# plt.annotate('R = C = L = 1',xy=(0.9, 0.9), xytext=(1, 1),
#                 xycoords='axes fraction', textcoords='axes fraction',
#                 ha='right', va='top', fontsize=14, color='k')

# pp = ax.streamplot(X, Y, dX, dY, color=mag, cmap = 'turbo', linewidth=0.9, broken_streamlines=False, density=2.)
# cbar = fig.colorbar(pp.lines)
# cbar.set_label(r'$\sqrt{\dot{x}^2 + \dot{y}^2}$')

# ax.set_xlim(xmin,xmax)
# ax.set_ylim(ymin,ymax)
# ax.grid()

# plt.title('Phase Portrait: LRC Circuit, $R^2C - 4L = 0$')
# #plt.show()
# plt.savefig('LRC_phase_portrait_2.png', dpi=325.)
# #plt.close()






## case iii B
# R = 1./2.

# dX, dY = LRC(X,Y, L=L, R=R, C=C)
# mag = np.sqrt(dX**2. + dY**2.)

# fig, ax = plt.subplots(figsize=(10,7))
# #NOTE: NEED matplotlib version 3.6.0 minimum in order to use the broken_streamlines keyword argument for the ax.streamplot() call. 
# #I had to install in user space, so I uninstalled after completion [work desktop]
# #pp = ax.streamplot(X, Y, dX, dY, color='teal', linewidth=0.9, density=2.)
# plt.annotate('R = 1/2; C = L = 1',xy=(0.9, 0.9), xytext=(1, 1),
#                 xycoords='axes fraction', textcoords='axes fraction',
#                 ha='right', va='top', fontsize=14, color='k')

# pp = ax.streamplot(X, Y, dX, dY, color=mag, cmap = 'turbo', linewidth=0.9, broken_streamlines=False, density=2.)
# cbar = fig.colorbar(pp.lines)
# cbar.set_label(r'$\sqrt{\dot{x}^2 + \dot{y}^2}$')

# ax.set_xlim(xmin,xmax)
# ax.set_ylim(ymin,ymax)
# ax.grid()

# plt.title('Phase Portrait: LRC Circuit, $R^2C - 4L < 0$, $R≠ 0$')
# #plt.show()
# plt.savefig('LRC_phase_portrait_3.png', dpi=325.)
# #plt.close()




## case ii
R = 2.

dX, dY = LRC(X,Y, L=L, R=R, C=C)
mag = np.sqrt(dX**2. + dY**2.)

fig, ax = plt.subplots(figsize=(10,7))
#NOTE: NEED matplotlib version 3.6.0 minimum in order to use the broken_streamlines keyword argument for the ax.streamplot() call. 
#I had to install in user space, so I uninstalled after completion [work desktop]
#pp = ax.streamplot(X, Y, dX, dY, color='teal', linewidth=0.9, density=2.)
plt.annotate('R = 2; C = L = 1',xy=(0.9, 0.9), xytext=(1, 1),
                xycoords='axes fraction', textcoords='axes fraction',
                ha='right', va='top', fontsize=14, color='k')

pp = ax.streamplot(X, Y, dX, dY, color=mag, cmap = 'turbo', linewidth=0.9, density=2.)
cbar = fig.colorbar(pp.lines)
cbar.set_label(r'$\sqrt{\dot{x}^2 + \dot{y}^2}$')

ax.set_xlim(xmin,xmax)
ax.set_ylim(ymin,ymax)
ax.grid()

plt.title('Phase Portrait: LRC Circuit, $R^2C - 4L = 0$, $R=2$')
plt.show()
#plt.savefig('LRC_phase_portrait_4.png', dpi=325.)
#plt.close()