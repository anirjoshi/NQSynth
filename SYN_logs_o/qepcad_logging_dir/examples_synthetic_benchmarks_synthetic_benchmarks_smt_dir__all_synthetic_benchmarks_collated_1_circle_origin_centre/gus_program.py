import sys

import sympy

from sympy import *

def pre_condition(r:sympy.Rational):

    #Ne(r, 0)



    pre_cond = Unequality(Symbol('r'), Integer(0))



    eval = pre_cond.subs({'r':r})



    return eval==True

print("Enter numerator of r")
r_num = int(input())
print("Enter denominator of r")
r_denm = int(input())
assert r_denm!=0
r_i = sympy.Rational(r_num,r_denm)

if pre_condition(r=r_i)==False:

    print("INFEASIBLE!")

    sys.exit(1)

else:

    if (not ((r_i == 0.0)) and (((1) * (r_i * r_i)) >= 0)):
        x_o =  (1.0)
    else:
        x_o =  0.0
    if (not ((r_i == 0.0)) and (((1) * (r_i * r_i)) >= 0)):
        y_o =  2.0
    else:
        y_o =  0.0
    print("x=",x_o)
    print("y=",y_o)
