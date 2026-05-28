import sys

import sympy

from sympy import *

def pre_condition(y:sympy.Rational):

    #True



    pre_cond = true



    eval = pre_cond.subs({'y':y})



    return eval==True

print("Enter numerator of y")
y_num = int(input())
print("Enter denominator of y")
y_denm = int(input())
assert y_denm!=0
y_i = sympy.Rational(y_num,y_denm)

if pre_condition(y=y_i)==False:

    print("INFEASIBLE!")

    sys.exit(1)

else:

    x_o =  y_i
    print("x=",x_o)
