import sys

import sympy

from sympy import *

def pre_condition(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):

    #(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1)



    pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)))



    eval = pre_cond.subs({'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi})



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

print("Enter numerator of pi")
pi_num = int(input())
print("Enter denominator of pi")
pi_denm = int(input())
assert pi_denm!=0
pi_i = sympy.Rational(pi_num,pi_denm)

if pre_condition(delta=delta_i,skoX=skoX_i,skoS2=skoS2_i,pi=pi_i)==False:

    print("INFEASIBLE!")

    sys.exit(1)

else:

    _let_1 = ((1) * pi_i)
    _let_2 = (skoS2_i * pi_i)
    _let_3 = (pi_i + (2 * _let_2))
    _let_4 = (_let_1 + ((2) * _let_2))
    _let_5 = (skoS2_i * pi_i * pi_i)
    _let_6 = (pi_i * pi_i)
    if ((delta_i >= 0) and not ((((1) * skoX_i) >= 0)) and not ((skoX_i >= 1)) and not ((_let_1 >= ((15707963) / 5000000))) and not ((pi_i >= (31415927 / 10000000))) and ((skoS2_i + ((10) * _let_2) + ((20) * (skoS2_i * skoS2_i * pi_i))) >= (4))):
        if ((_let_3 >= ((2) / 5)) and (_let_4 >= ((3) / 5)) and (_let_4 >= ((11) / 10))):
            if (((_let_1 + ((10) * _let_6) + ((20) * _let_5)) >= (4)) and ((_let_1 + (((80) / 41) * _let_2) + (((10) / 41) * _let_6) + (((20) / 41) * _let_5)) >= ((8) / 41))):
                if (_let_4 >= (1 / 1600000010)):
                    if (_let_4 >= ((1) / 10)):
                        if ((_let_4 >= ((9) / 10)) and (_let_4 >= ((7) / 30)) and (_let_3 >= ((1) / 30)) and (_let_4 >= ((13) / 10)) and ((_let_1 + (10 * _let_6) + (20 * _let_5)) >= (4)) and (_let_3 >= ((11) / 10))):
                            if ((_let_3 >= ((1) / 40)) and (_let_4 >= ((1) / 5)) and (_let_4 >= ((1) / 2))):
                                if (_let_3 >= ((7) / 10)):
                                    skoSP_o =  (6.0)
                                else:
                                    skoSP_o =  (4 / 3)
                            else:
                                skoSP_o =  ((1) / 3)
                        else:
                            skoSP_o =  0.0
                    else:
                        skoSP_o =  (2.0)
                else:
                    skoSP_o =  ((160000001) / 40000000)
            else:
                skoSP_o =  _let_1
        else:
            skoSP_o =  (1 / 2)
    else:
        skoSP_o =  0.0
    _let_1 = ((1) * pi_i)
    _let_2 = (skoS2_i * pi_i)
    _let_3 = (pi_i + (2 * _let_2))
    _let_4 = (_let_1 + ((2) * _let_2))
    _let_5 = (skoS2_i * pi_i * pi_i)
    _let_6 = (pi_i * pi_i)
    if ((delta_i >= 0) and not ((((1) * skoX_i) >= 0)) and not ((skoX_i >= 1)) and not ((_let_1 >= ((15707963) / 5000000))) and not ((pi_i >= (31415927 / 10000000)))):
        if ((skoS2_i + ((10) * _let_2) + ((20) * (skoS2_i * skoS2_i * pi_i))) >= (4)):
            if (_let_4 >= ((11) / 10)):
                if (_let_3 >= ((2) / 5)):
                    if (_let_4 >= ((3) / 5)):
                        if ((_let_1 + ((10) * _let_6) + ((20) * _let_5)) >= (4)):
                            if ((_let_1 + (((80) / 41) * _let_2) + (((10) / 41) * _let_6) + (((20) / 41) * _let_5)) >= ((8) / 41)):
                                if (_let_4 >= (1 / 1600000010)):
                                    if ((_let_4 >= ((1) / 10)) and (_let_4 >= ((9) / 10))):
                                        if ((_let_1 + (10 * _let_6) + (20 * _let_5)) >= (4)):
                                            if (_let_4 >= ((7) / 30)):
                                                if (_let_3 >= ((1) / 30)):
                                                    if (_let_4 >= ((13) / 10)):
                                                        if (_let_3 >= ((11) / 10)):
                                                            if (_let_4 >= ((1) / 2)):
                                                                if (_let_4 >= ((1) / 5)):
                                                                    if (_let_3 >= ((1) / 40)):
                                                                        if (_let_3 >= ((7) / 10)):
                                                                            skoSM_o =  (1 / 8)
                                                                        else:
                                                                            skoSM_o =  (1 / 2)
                                                                    else:
                                                                        skoSM_o =  (3.0)
                                                                else:
                                                                    skoSM_o =  3.0
                                                            else:
                                                                skoSM_o =  (1 / 2)
                                                        else:
                                                            skoSM_o =  ((1) / 3)
                                                    else:
                                                        skoSM_o =  (1 / 3)
                                                else:
                                                    skoSM_o =  (3.0)
                                            else:
                                                skoSM_o =  3.0
                                        else:
                                            skoSM_o =  _let_1
                                    else:
                                        skoSM_o =  (1 / 2)
                                else:
                                    skoSM_o =  0.0
                            else:
                                skoSM_o =  4.0
                        else:
                            skoSM_o =  0.0
                    else:
                        skoSM_o =  (3 / 2)
                else:
                    skoSM_o =  ((1) / 2)
            else:
                skoSM_o =  1.0
        else:
            skoSM_o =  skoS2_i
    else:
        skoSM_o =  0.0
    print("skoSP=",skoSP_o)
    print("skoSM=",skoSM_o)
