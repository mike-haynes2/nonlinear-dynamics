import numpy as np
from scipy import constants
import math as m
import matplotlib.pyplot as plt

from hw1_plotting import plot_vector_field_1D





def plot_bif_field(f,crits,savdir=None):
    nplt = len(crits)+1
    if nplt == 2:
        for rval in [crits[0]-1,crits[0]+1]:
            def g(x):
                return f(x,rval)
            plot_vector_field_1D(g,pos_only=False)
    else:
        for i in range(nplt):
            r = crits[i]
            if i == 0:
                r -= 1.
            elif i == range(nplt)[-1]:
                r += 1
            else:
                r = (crits[i]+crits[i+1])/2.
            def g(x):
                return f(x,r)
            sav_var = True
            if savdir == None:
                sav_var = False
            plot_vector_field_1D(g, pos_only=False,save=sav_var)

        


def f(x,r):
    return (r-np.cosh(x))

plot_bif_field(f,crits=[0],savdir=None)


