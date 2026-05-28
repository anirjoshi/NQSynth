import sys

import sympy

from sympy import *

def pre_condition(delta:sympy.Rational,skoX:sympy.Rational,pi:sympy.Rational):

    #(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1)



    pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)))



    eval = pre_cond.subs({'delta':delta, 'skoX':skoX, 'pi':pi})



    return eval==True

print("Enter numerator of delta")
delta_num = int(input())
print("Enter denominator of delta")
delta_denm = int(input())
assert delta_denm!=0
delta_i = sympy.Rational(delta_num,delta_denm)

print("Enter numerator of skoX")
skoX_num = int(input())
print("Enter denominator of skoX")
skoX_denm = int(input())
assert skoX_denm!=0
skoX_i = sympy.Rational(skoX_num,skoX_denm)

print("Enter numerator of pi")
pi_num = int(input())
print("Enter denominator of pi")
pi_denm = int(input())
assert pi_denm!=0
pi_i = sympy.Rational(pi_num,pi_denm)

if pre_condition(delta=delta_i,skoX=skoX_i,pi=pi_i)==False:

    print("INFEASIBLE!")

    sys.exit(1)

else:

    if ((delta_i >= 0) and not ((((1) * skoX_i) >= 0)) and not ((skoX_i >= 1)) and not ((((1) * pi_i) >= ((15707963) / 5000000))) and not ((pi_i >= (31415927 / 10000000))) and (skoX_i >= 0)):
        skoSP_o =  ((30000001) / 10000000)
    else:
        skoSP_o =  0.0
    if ((delta_i >= 0) and not ((((1) * skoX_i) >= 0)) and not ((skoX_i >= 1)) and not ((((1) * pi_i) >= ((15707963) / 5000000))) and not ((pi_i >= (31415927 / 10000000))) and (skoX_i >= 0)):
        skoSM_o =  (1.0)
    else:
        skoSM_o =  0.0
    print("skoSP=",skoSP_o)
    print("skoSM=",skoSM_o)
