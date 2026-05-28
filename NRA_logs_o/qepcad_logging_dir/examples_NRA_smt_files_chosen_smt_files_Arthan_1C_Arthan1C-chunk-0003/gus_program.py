import sys

import sympy

from sympy import *

def pre_condition(delta:sympy.Rational,skoS:sympy.Rational):

    #delta >= 0



    pre_cond = GreaterThan(Symbol('delta'), Integer(0))



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

    _let_1 = (skoS_i * skoS_i * skoS_i)
    _let_2 = (skoS_i * skoS_i)
    _let_3 = ((1) * skoS_i)
    _let_4 = (((1) / 3) * _let_1)
    if ((delta_i >= 0) and ((((1) * _let_2) + _let_4) >= ((1) / 3))):
        if ((_let_3 + (((7) / 20) * _let_2)) >= (7 / 10)):
            if ((skoS_i + (((1) / 3) * _let_2) + _let_4) >= 0):
                if (((_let_3 + (((32) / 31) * _let_2) + (((6) / 31) * _let_1)) >= (7 / 31)) and ((_let_3 + (((18) / 11) * _let_2) + (((4) / 11) * _let_1)) >= ((1) / 11))):
                    if ((_let_3 + ((9) * _let_2) + ((5) * _let_1)) >= (1)):
                        skoCOSS_o =  (4 / 3)
                    else:
                        skoCOSS_o =  skoS_i
                else:
                    skoCOSS_o =  (1 / 2)
            else:
                skoCOSS_o =  (1.0)
        else:
            skoCOSS_o =  2.0
    else:
        skoCOSS_o =  0.0
    _let_1 = (skoS_i * skoS_i * skoS_i)
    _let_2 = (skoS_i * skoS_i)
    _let_3 = ((1) * skoS_i)
    _let_4 = (((1) / 3) * _let_1)
    if ((delta_i >= 0) and ((((1) * _let_2) + _let_4) >= ((1) / 3))):
        if ((_let_3 + (((7) / 20) * _let_2)) >= (7 / 10)):
            if ((skoS_i + (((1) / 3) * _let_2) + _let_4) >= 0):
                if (not (((_let_3 + (((32) / 31) * _let_2) + (((6) / 31) * _let_1)) >= (7 / 31))) and ((_let_3 + (((18) / 11) * _let_2) + (((4) / 11) * _let_1)) >= ((1) / 11))):
                    skoSINS_o =  ((1) / 2)
                else:
                    skoSINS_o =  0.0
            else:
                skoSINS_o =  2.0
        else:
            skoSINS_o =  (2.0)
    else:
        skoSINS_o =  0.0
    print("skoCOSS=",skoCOSS_o)
    print("skoSINS=",skoSINS_o)
