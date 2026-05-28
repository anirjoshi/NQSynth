import sys

import sympy

from sympy import *

def pre_condition(delta:sympy.Rational):

    #delta >= 3



    pre_cond = GreaterThan(Symbol('delta'), Integer(3))



    eval = pre_cond.subs({'delta':delta})



    return eval==True

print("Enter numerator of delta")
delta_num = int(input())
print("Enter denominator of delta")
delta_denm = int(input())
assert delta_denm!=0
delta_i = sympy.Rational(delta_num,delta_denm)

if pre_condition(delta=delta_i)==False:

    print("INFEASIBLE!")

    sys.exit(1)

else:

    a_o =  0.0
    print("a=",a_o)
