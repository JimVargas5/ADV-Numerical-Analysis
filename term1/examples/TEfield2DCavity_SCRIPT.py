# Jim Vargas
# This is a script version of the notbook of a similar name

import ngsolve as ng
from netgen.geom2d import unit_square
from ngsolve import curl, dx

import numpy as np

BLOCK=0

def f(P):
    x=P[0]
    y=P[1]

    ans=np.array([0,0])
    ans[0] = np.exp(
        -100*(  (x-1/2)**2 + (y-3/4)**2 )
    )
    return ans
omega=30
x_0=1/2
y_0=3/4


BLOCK+=1
input("Block done="+str(BLOCK)+"\ncontinue?\n>>> ")







print("Done")

