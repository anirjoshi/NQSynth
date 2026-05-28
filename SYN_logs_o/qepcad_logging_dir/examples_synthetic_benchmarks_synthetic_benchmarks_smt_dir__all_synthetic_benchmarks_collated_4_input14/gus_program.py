import sys

import sympy

from sympy import *

def pre_condition(x:sympy.Rational):

    #(x >= -4) & (x <= 4)



    pre_cond = And(GreaterThan(Symbol('x'), Integer(-4)), LessThan(Symbol('x'), Integer(4)))



    eval = pre_cond.subs({'x':x})



    return eval==True

print("Enter numerator of x")
x_num = int(input())
print("Enter denominator of x")
x_denm = int(input())
assert x_denm!=0
x_i = sympy.Rational(x_num,x_denm)

if pre_condition(x=x_i)==False:

    print("INFEASIBLE!")

    sys.exit(1)

else:

    _let_1 = ((1) * (x_i * x_i))
    if ((x_i >= (4)) and (((1) * x_i) >= (4)) and not ((_let_1 >= (16)))):
        if (_let_1 >= (14)):
            y_o =  1.0
        else:
            y_o =  (1.0)
    else:
        y_o =  0.0
    _let_1 = ((1) * (x_i * x_i))
    if ((x_i >= (4)) and (((1) * x_i) >= (4)) and not ((_let_1 >= (16)))):
        if (_let_1 >= (14)):
            z_o =  (1.0)
        else:
            z_o =  2.0
    else:
        z_o =  0.0
    print("y=",y_o)
    print("z=",z_o)
