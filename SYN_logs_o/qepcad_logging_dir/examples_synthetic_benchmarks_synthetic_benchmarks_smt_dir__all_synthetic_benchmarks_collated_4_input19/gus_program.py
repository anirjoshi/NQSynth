import sys

import sympy

from sympy import *

def pre_condition(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):

    #(a > 0) & (b > 0) & (c > 0)



    pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(0)), StrictGreaterThan(Symbol('b'), Integer(0)), StrictGreaterThan(Symbol('c'), Integer(0)))



    eval = pre_cond.subs({'a':a, 'b':b, 'c':c})



    return eval==True

print("Enter numerator of a")
a_num = int(input())
print("Enter denominator of a")
a_denm = int(input())
assert a_denm!=0
a_i = sympy.Rational(a_num,a_denm)

print("Enter numerator of b")
b_num = int(input())
print("Enter denominator of b")
b_denm = int(input())
assert b_denm!=0
b_i = sympy.Rational(b_num,b_denm)

print("Enter numerator of c")
c_num = int(input())
print("Enter denominator of c")
c_denm = int(input())
assert c_denm!=0
c_i = sympy.Rational(c_num,c_denm)

if pre_condition(a=a_i,b=b_i,c=c_i)==False:

    print("INFEASIBLE!")

    sys.exit(1)

else:

    x_o =  0.0
    y_o =  0.0
    z_o =  0.0
    print("x=",x_o)
    print("y=",y_o)
    print("z=",z_o)
