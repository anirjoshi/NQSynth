import sys

import sympy

from sympy import *

def pre_condition(r:sympy.Rational):

    #r >= 0



    pre_cond = GreaterThan(Symbol('r'), Integer(0))



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

    y_o =  0.0
    x_o =  0.0
    print("y=",y_o)
    print("x=",x_o)
