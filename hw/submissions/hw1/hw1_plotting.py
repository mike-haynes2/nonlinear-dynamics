import numpy as np
import math as m
from scipy import constants
import matplotlib.pyplot as plt



def find_zeroes(f, precision=0.01,  pos_only=False):
    test_vals = np.arange(start=-10,stop=10,step=precision)
    if pos_only: test_vals = np.arange(start=0.,stop=10,step=precision)
    test_outs = f(test_vals)
    zeroes =  np.where(np.diff(np.sign(test_outs)))[0]
    false_zeroes = np.where(np.diff(zeroes)==1)
    for idx in false_zeroes:
        zeroes = np.delete(zeroes,idx)
    print('zeroes of ',f,test_vals[zeroes])
    return test_vals[zeroes]


def f(N, a=1., b=1.):
    func = -a * N * np.log(b * N)
    return func


def plot_vectors(sgn_left,sgn_right,zero,eps, pos_only):
    space = eps * 15. + 0.3 * (not pos_only)
    differ = 0.2 + 0.3*(not pos_only)
    if sgn_left < 0:
        plt.arrow(x=zero-space, y=0, dx=-differ, dy=0., head_width=0.1,head_length=0.1,width=0.02,color='black')
    elif sgn_left>0:
        plt.arrow(x=zero-differ-space, y=0, dx=differ, dy=0., head_width=0.1,head_length=0.1,width=0.02,color='black')
    if sgn_right < 0:
        plt.arrow(x=zero+space+differ, y=0, dx=-differ, dy=0., head_width=0.1,head_length=0.1,width=0.02,color='black')
    elif sgn_right>0:
        plt.arrow(x=zero+space, y=0, dx=differ, dy=0., head_width=0.1,head_length=0.1,width=0.02,color='black')


find_zeroes(f=f, pos_only=True)

def plot_vector_field_1D(f, eps=0.01, pos_only = True, save=False):
    test_vals = np.arange(start=-10,stop=10,step=eps)
    if pos_only: test_vals = np.arange(start=0.,stop=10,step=eps)
    fig, ax = plt.subplots(figsize=(10,8))
    plt.plot(test_vals, f(test_vals), lw=2., color='teal', label='$\dot{N}$')
    plt.title('Vector Field for $f(N)=\dot{N}$')
    plt.grid()
    zeroes = find_zeroes(f)
    for ind,zero in enumerate(zeroes):
        sgn_left  = np.sign(f(zero-eps))
        sgn_right = np.sign(f(zero+eps))
        if ind == 0:
            if pos_only==True:
                sgn_left == 0.
        plot_vectors(sgn_left, sgn_right, zero=zero, eps=eps, pos_only=pos_only)
        if sgn_left > 0. and sgn_right < 0.:
            plt.scatter(zero,0.,marker=',',lw=5,color='black')    
        if sgn_left < 0. and sgn_right > 0.:
            plt.scatter(zero,0.,marker='o',lw=5,color='black', alpha=0.5)
    plt.xlim(zeroes[0]-0.5,zeroes[-1]+1.)
    plt.ylim(np.nanmin(f(np.arange(start=zeroes[0]-0.5,stop=zeroes[-1]+0.5, step=0.1)))-0.25, np.nanmax(f(np.arange(start=zeroes[0]-0.5,stop=zeroes[-1]+0.5, step=0.1)))+0.25)

    plt.legend()
    if save:
        plt.savefig('1D_vector_field_f.png',dpi=275.)
    else:
        plt.show()

    return None


#plot_vector_field_1D(f=f, save=True)



def N(t, N0, a=1., b=1.):
    top = np.exp(-a * t)
    num = (b * N0) ** top
    return (num / b)

def plot_curves_N(func,set, save=True):
    plt.close()
    fig, ax = plt.subplots(figsize=(10,8))
    ts = np.arange(start=0.,stop=5,step=0.1)
    for idx, N0 in enumerate(set):
        plt.plot(ts, func(ts,N0), label=('N0 = '+str(N0)), lw=2.)
    plt.grid()
    plt.legend()
    plt.title('$N(t):\quad a=1;b=1$')
    if save==True:
        plt.savefig('plot_Ns.png', dpi=275)
    else:
        plt.show()

#plot_curves_N(N,[0,0.25,0.5,1,2,3,4])



# example case to compare to Figure 2.1.1 in Strogatz
# def g(x):
#     return np.sin(x)
# plot_vector_field_1D(f=g, pos_only=False)

def x_pa(t,x0):
    den = 2.*t + (1./x0**2.)
    return (1./np.sqrt(den))

def x_pb(t,x0):
    return x0 * np.exp(-t)



def plot_p5(x0):
    plt.close()
    fig, ax = plt.subplots(figsize=(10,8))
    ts = np.arange(start=0.,stop=10.,step=0.02)
    plt.title('Dynamical systems: [$\dot{x} = -x^3$ (navy)] versus [$\dot{x} = -x$ (orange)]')
    plt.plot(ts, x_pa(ts,x0=x0), color='navy', lw=2, label='x(t) [part (a)]')
    plt.plot(ts, x_pb(ts,x0=x0), color='orange', lw=2, label='x(t) [part (b)]')
    plt.grid()
    plt.legend()
    #plt.show()
    plt.savefig('plot_xt.png', dpi=270.)

plot_p5(10.)