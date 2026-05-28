import sys

import sympy

from sympy import *

def pre_condition(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):

    #(delta >= skoM) & (skoM >= 2) & (delta - skoSINS**2 + 1 >= 0)



    pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoM')), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(1)), Integer(0)))



    eval = pre_cond.subs({'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM})



    return eval==True

print("Enter numerator of delta")
delta_num = int(input())
print("Enter denominator of delta")
delta_denm = int(input())
assert delta_denm!=0
delta_i = sympy.Rational(delta_num,delta_denm)

print("Enter numerator of skoSINS")
skoSINS_num = int(input())
print("Enter denominator of skoSINS")
skoSINS_denm = int(input())
assert skoSINS_denm!=0
skoSINS_i = sympy.Rational(skoSINS_num,skoSINS_denm)

print("Enter numerator of skoM")
skoM_num = int(input())
print("Enter denominator of skoM")
skoM_denm = int(input())
assert skoM_denm!=0
skoM_i = sympy.Rational(skoM_num,skoM_denm)

if pre_condition(delta=delta_i,skoSINS=skoSINS_i,skoM=skoM_i)==False:

    print("INFEASIBLE!")

    sys.exit(1)

else:

    _let_1 = (skoSINS_i * skoSINS_i)
    if ((delta_i >= 2) and (skoM_i >= 2) and ((delta_i + ((1) * skoM_i)) >= 0) and ((delta_i + ((1) * _let_1)) >= (1)) and (not ((delta_i >= 0)) or not (((delta_i + skoM_i) >= 0)) or not (((delta_i + _let_1) >= 1)))):
        skoCOSS_o =  (2.0)
    else:
        skoCOSS_o =  0.0
    _let_1 = (skoSINS_i * skoSINS_i)
    if ((delta_i >= 2) and (skoM_i >= 2) and ((delta_i + ((1) * skoM_i)) >= 0) and ((delta_i + ((1) * _let_1)) >= (1)) and (not ((delta_i >= 0)) or not (((delta_i + skoM_i) >= 0)) or not (((delta_i + _let_1) >= 1)))):
        skoS_o =  (1 / 2)
    else:
        skoS_o =  2.0
    print("skoCOSS=",skoCOSS_o)
    print("skoS=",skoS_o)
