import sys

import sympy

from sympy import *

def pre_condition(b:sympy.Rational,delta:sympy.Rational):

    #(b**2 + delta - 2 >= 0) & (2*b - delta < 1) & (-b**2 + delta + 2 >= 0)



    pre_cond = And(GreaterThan(Add(Pow(Symbol('b'), Integer(2)), Symbol('delta'), Integer(-2)), Integer(0)), StrictLessThan(Add(Mul(Integer(2), Symbol('b')), Mul(Integer(-1), Symbol('delta'))), Integer(1)), GreaterThan(Add(Mul(Integer(-1), Pow(Symbol('b'), Integer(2))), Symbol('delta'), Integer(2)), Integer(0)))



    eval = pre_cond.subs({'b':b, 'delta':delta})



    return eval==True

print("Enter numerator of b")
b_num = int(input())
print("Enter denominator of b")
b_denm = int(input())
assert b_denm!=0
b_i = sympy.Rational(b_num,b_denm)

print("Enter numerator of delta")
delta_num = int(input())
print("Enter denominator of delta")
delta_denm = int(input())
assert delta_denm!=0
delta_i = sympy.Rational(delta_num,delta_denm)

if pre_condition(b=b_i,delta=delta_i)==False:

    print("INFEASIBLE!")

    sys.exit(1)

else:

    a_o =  ((1 / 2) + ((1 / 2) * delta_i))
    print("a=",a_o)
