import sys

import sympy

from sympy import *

def pre_condition(c:sympy.Rational):

    #(c < -5/2) & (c > -5/2 - sqrt(13)/2)



    pre_cond = And(StrictLessThan(Symbol('c'), Rational(-5, 2)), StrictGreaterThan(Symbol('c'), Add(Rational(-5, 2), Mul(Integer(-1), Rational(1, 2), Pow(Integer(13), Rational(1, 2))))))



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

    _let_1 = (c_i * c_i)
    _let_2 = ((1) * _let_1)
    if (not ((c_i >= ((5) / 2))) and not (((c_i + ((1 / 5) * _let_1)) >= ((3) / 5))) and ((_let_2 >= 0) or (c_i >= (3)))):
        if (not ((_let_2 >= (2))) and not ((c_i >= (1)))):
            x_o =  1.0
        else:
            x_o =  (39 / 16)
    else:
        x_o =  0.0
    _let_1 = (c_i * c_i)
    _let_2 = ((1) * _let_1)
    if (not ((c_i >= ((5) / 2))) and not (((c_i + ((1 / 5) * _let_1)) >= ((3) / 5))) and ((_let_2 >= 0) or (c_i >= (3))) and not ((_let_2 >= (2))) and not ((c_i >= (1)))):
        y_o =  (1.0)
    else:
        y_o =  0.0
    print("x=",x_o)
    print("y=",y_o)
