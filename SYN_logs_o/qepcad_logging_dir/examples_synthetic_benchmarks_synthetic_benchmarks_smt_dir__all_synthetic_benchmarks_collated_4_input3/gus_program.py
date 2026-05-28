import sys

import sympy

from sympy import *

def pre_condition(c:sympy.Rational):

    #True



    pre_cond = true



    eval = pre_cond.subs({'c':c})



    return eval==True

print("Enter numerator of c")
c_num = int(input())
print("Enter denominator of c")
c_denm = int(input())
assert c_denm!=0
c_i = sympy.Rational(c_num,c_denm)

if pre_condition(c=c_i)==False:

    print("INFEASIBLE!")

    sys.exit(1)

else:

    x_o =  0.0
    y_o =  c_i
    print("x=",x_o)
    print("y=",y_o)
