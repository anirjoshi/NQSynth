import sys

import sympy

from sympy import *

def pre_condition(delta:sympy.Rational,skoS:sympy.Rational):

    #(delta >= 0) & (skoS >= 9/20)



    pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(9, 20)))



    eval = pre_cond.subs({'delta':delta, 'skoS':skoS})



    return eval==True

print("Enter numerator of delta")
delta_num = int(input())
print("Enter denominator of delta")
delta_denm = int(input())
assert delta_denm!=0
delta_i = sympy.Rational(delta_num,delta_denm)

print("Enter numerator of skoS")
skoS_num = int(input())
print("Enter denominator of skoS")
skoS_denm = int(input())
assert skoS_denm!=0
skoS_i = sympy.Rational(skoS_num,skoS_denm)

if pre_condition(delta=delta_i,skoS=skoS_i)==False:

    print("INFEASIBLE!")

    sys.exit(1)

else:

    if ((delta_i >= 0) and (skoS_i >= (9 / 20)) and ((((1) * skoS_i) + ((1) * (skoS_i * skoS_i)) + (((1) / 3) * (skoS_i * skoS_i * skoS_i))) >= (1 / 3))):
        skoCOSS_o =  2.0
    else:
        skoCOSS_o =  0.0
    if ((delta_i >= 0) and (skoS_i >= (9 / 20)) and ((((1) * skoS_i) + ((1) * (skoS_i * skoS_i)) + (((1) / 3) * (skoS_i * skoS_i * skoS_i))) >= (1 / 3))):
        skoSINS_o =  (1.0)
    else:
        skoSINS_o =  0.0
    print("skoCOSS=",skoCOSS_o)
    print("skoSINS=",skoSINS_o)
