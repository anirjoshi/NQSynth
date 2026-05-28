import sys

import sympy

from sympy import *

def pre_condition(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):

    #(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1)



    pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)))



    eval = pre_cond.subs({'delta':delta, 'skoX':skoX, 'skoS2':skoS2})



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

print("Enter numerator of skoS2")
skoS2_num = int(input())
print("Enter denominator of skoS2")
skoS2_denm = int(input())
assert skoS2_denm!=0
skoS2_i = sympy.Rational(skoS2_num,skoS2_denm)

if pre_condition(delta=delta_i,skoX=skoX_i,skoS2=skoS2_i)==False:

    print("INFEASIBLE!")

    sys.exit(1)

else:

    if ((delta_i >= 0) and not ((((1) * skoS2_i) >= 0)) and not ((((1) * skoX_i) >= 0)) and not ((skoX_i >= 1))):
        skoSP_o =  (4 / 69)
    else:
        skoSP_o =  1.0
    if ((delta_i >= 0) and not ((((1) * skoS2_i) >= 0)) and not ((((1) * skoX_i) >= 0)) and not ((skoX_i >= 1))):
        skoSM_o =  (1072 / 4209)
    else:
        skoSM_o =  1.0
    print("skoSP=",skoSP_o)
    print("skoSM=",skoSM_o)
