import sys

import sympy

from sympy import *

def pre_condition(delta:sympy.Rational,skoS:sympy.Rational):

    #(delta >= 0) & (skoS >= 217/100)



    pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)))



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

    _let_1 = ((1) * skoS_i)
    _let_2 = (skoS_i * skoS_i * skoS_i)
    _let_3 = (skoS_i * skoS_i)
    if ((delta_i >= 0) and (skoS_i >= (217 / 100)) and not (((((1) * _let_3) + (((1) / 3) * _let_2)) >= ((1) / 3)))):
        if ((_let_1 + (((7) / 20) * _let_3)) >= (7 / 10)):
            skoCOSS_o =  2.0
        else:
            if (not (((_let_1 + (((32) / 31) * _let_3) + (((6) / 31) * _let_2)) >= (7 / 31))) and not (((_let_1 + (((18) / 11) * _let_3) + (((4) / 11) * _let_2)) >= ((1) / 11)))):
                if ((skoS_i + ((80 / 73) * _let_3) + (((40) / 247) * _let_2)) >= (15209 / 18031)):
                    skoCOSS_o =  (3.0)
                else:
                    if ((skoS_i + ((1 / 2) * _let_3) + (((1) / 6) * _let_2)) >= (1 / 6)):
                        skoCOSS_o =  (2.0)
                    else:
                        if ((skoS_i + ((9 / 4) * _let_3) + (((1) / 4) * _let_2)) >= (11 / 4)):
                            skoCOSS_o =  (4.0)
                        else:
                            if ((_let_1 + (((10) / 13) * _let_3) + (((4) / 39) * _let_2)) >= (11 / 39)):
                                skoCOSS_o =  (3 / 2)
                            else:
                                if ((skoS_i + _let_3 + _let_2) >= (1)):
                                    skoCOSS_o =  _let_1
                                else:
                                    skoCOSS_o =  (1.0)
            else:
                skoCOSS_o =  (1 / 2)
    else:
        skoCOSS_o =  0.0
    _let_1 = (skoS_i * skoS_i * skoS_i)
    _let_2 = (skoS_i * skoS_i)
    _let_3 = ((1) * skoS_i)
    _let_4 = (((1) / 4) * _let_1)
    if ((delta_i >= 0) and (skoS_i >= (217 / 100)) and not (((((1) * _let_2) + (((1) / 3) * _let_1)) >= ((1) / 3)))):
        if ((_let_3 + (((7) / 20) * _let_2)) >= (7 / 10)):
            skoSINS_o =  (2.0)
        else:
            if ((_let_3 + (((18) / 11) * _let_2) + (((4) / 11) * _let_1)) >= ((1) / 11)):
                skoSINS_o =  0.0
            else:
                if ((_let_3 + (((32) / 31) * _let_2) + (((6) / 31) * _let_1)) >= (7 / 31)):
                    skoSINS_o =  ((1) / 2)
                else:
                    if ((skoS_i + ((80 / 73) * _let_2) + (((40) / 247) * _let_1)) >= (15209 / 18031)):
                        skoSINS_o =  ((7) / 40)
                    else:
                        if (not (((skoS_i + _let_4) >= ((1) / 4))) and not (((skoS_i + ((1 / 2) * _let_2) + (((1) / 6) * _let_1)) >= (1 / 6))) and not (((skoS_i + ((9 / 4) * _let_2) + _let_4) >= (11 / 4))) and not (((_let_3 + (((10) / 13) * _let_2) + (((4) / 39) * _let_1)) >= (11 / 39))) and not (((skoS_i + _let_2 + _let_1) >= (1)))):
                            skoSINS_o =  (1 / 2)
                        else:
                            skoSINS_o =  0.0
    else:
        skoSINS_o =  0.0
    print("skoCOSS=",skoCOSS_o)
    print("skoSINS=",skoSINS_o)
