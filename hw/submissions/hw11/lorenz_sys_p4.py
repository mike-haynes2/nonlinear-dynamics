import math as m
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np







def Lorenz(x0,y0,z0, tmax=100,res=0.01,r=(28.),s=(10.),b=(8./3.)):
    # DEFINE LORENZ SYSTEM
    def sys(x,y,z,r,s,b):
        return (s*(y-x)), (r*x-y-(x*z)), (x*y - b*z)
    # CREATE TIME ARRAY AND LOOP OVER TIME
    tarr = np.arange(start=0.,stop=tmax,step=res)
    Xarr= [x0];Yarr=[y0];Zarr=[z0];
    for i,t in enumerate(tarr[1:]):
        # UPDATE POSITION USING LORENZ SYSTEM GRADIENT
        dx,dy,dz=sys(Xarr[i],Yarr[i],Zarr[i],r=r,s=s,b=b)
        # E-FORWARD STEP
        x = Xarr[i]+(dx*res)
        y = Yarr[i]+(dy*res)
        z = Zarr[i]+(dz*res)
        # WRITE TO ARRAY 
        Xarr.append(x);Yarr.append(y);Zarr.append(z);
    X=np.array(Xarr); Y=np.array(Yarr); Z=np.array(Zarr);
    # WRTIE OUT ALL 4 COORDINATES
    return tarr,X,Y,Z


eps = 1.e-10
length = 100.
mint=12
maxt=38


ts, x1, y1, z1 = Lorenz(1.,1.,1., tmax=length, res=0.0001)
t2, x2, y2, z2 = Lorenz(1.+eps,1.,1., tmax=length, res=0.0001)


min_idx = int((mint/length)*len(ts))
max_idx = int((maxt/length)*len(ts))


r_diff = np.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2 )


coef = np.polyfit(ts[min_idx:max_idx],np.log(r_diff[min_idx:max_idx]),1)
poly1d_fn = np.poly1d(coef)



fig = plt.figure(figsize=(8,11))

gs=gridspec.GridSpec(3,1, height_ratios=[1,1,2])

ax0 = fig.add_subplot(gs[0,0])
ax1 = fig.add_subplot(gs[1,0])
ax2 = fig.add_subplot(gs[2,0])

ax0.plot(ts, x1, color='navy',lw=1.3)
ax0.set_ylabel('$x_1(t)$')
ax0.set_xlabel('$t$')
ax0.grid()
ax0.text(-0.07,-0.14,'(a)',fontsize=16,transform=ax0.transAxes)
ax0.set_title(r'Trajectory ($x(t),\,y(t)$)')

ax1.plot(ts, x2, color='navy',lw=1.3)
ax1.set_ylabel('$x_2(t)$')
ax1.set_xlabel('$t$')
ax1.grid()
ax1.text(-0.07,-0.13,'(b)',fontsize=16,transform=ax1.transAxes)



ax2.plot(ts,np.log(r_diff), color='cyan', lw=2)
ax2.plot(ts[min_idx:max_idx],  coef[0]*ts[min_idx:max_idx] + coef[1], '--k', label=f'fit: $λ =$ {round(coef[0],3)}', lw=2)
ax2.set_xlabel('$t$')
ax2.set_ylabel('$\log{|\boldsymbol{\delta}(t)|$')
ax2.grid()
ax2.text(-0.06,-0.08,'(c)',fontsize=16,transform=ax2.transAxes)
ax2.set_title(r'Log trajectory separation')
ax2.axvspan(mint,maxt,color='navy',alpha=0.3)
ax2.legend()

fig.suptitle(r'Lorenz Attractor: $r=28$, $\sigma=10$, $b=8/3$', fontsize=16)

plt.tight_layout() # Adjust layout to prevent overlapping titles/labels
plt.show()
#plt.savefig('Lorenz_p4_Lyapunov.png', dpi=290)
#plt.close()

