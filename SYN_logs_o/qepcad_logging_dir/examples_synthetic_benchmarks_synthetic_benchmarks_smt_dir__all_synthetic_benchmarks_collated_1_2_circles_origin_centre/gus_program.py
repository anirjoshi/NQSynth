import sys

import sympy

from sympy import *

def pre_condition(r1:sympy.Rational,r2:sympy.Rational):

    #False



    pre_cond = false



    eval = pre_cond.subs({'r1':r1, 'r2':r2})



    return eval==True

print("Enter numerator of r1")
r1_num = int(input())
print("Enter denominator of r1")
r1_denm = int(input())
assert r1_denm!=0
r1_i = sympy.Rational(r1_num,r1_denm)

print("Enter numerator of r2")
r2_num = int(input())
print("Enter denominator of r2")
r2_denm = int(input())
assert r2_denm!=0
r2_i = sympy.Rational(r2_num,r2_denm)

if pre_condition(r1=r1_i,r2=r2_i)==False:

    print("INFEASIBLE!")

    sys.exit(1)

else:

    x_o =  0.0
    y_o =  0.0
    print("x=",x_o)
    print("y=",y_o)
