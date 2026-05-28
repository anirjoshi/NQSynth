import sys

import sympy

from sympy import *

def pre_condition(y:sympy.Rational):

    #(y >= -5) & (y <= 5)



    pre_cond = And(GreaterThan(Symbol('y'), Integer(-5)), LessThan(Symbol('y'), Integer(5)))



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

    _let_1 = (y_i * y_i)
    _let_2 = ((1) * _let_1)
    if ((y_i >= (5)) and (((1) * y_i) >= (5)) and (not ((_let_2 >= (25))) or not ((_let_1 >= 4)))):
        if ((_let_2 >= (24)) and (_let_1 >= 3)):
            x_o =  (1.0)
        else:
            x_o =  (2.0)
    else:
        x_o =  0.0
    print("x=",x_o)
