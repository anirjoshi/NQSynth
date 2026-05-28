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

    _let_1 = (skoS2_i * pi_i)
    _let_2 = (pi_i + (2 * _let_1))
    _let_3 = ((1) * pi_i)
    _let_4 = (_let_3 + ((2) * _let_1))
    _let_5 = (skoX_i >= 0)
    _let_6 = not (_let_5)
    _let_7 = (skoX_i * pi_i)
    _let_8 = (skoS2_i * pi_i * pi_i)
    _let_9 = (pi_i * pi_i)
    _let_10 = ((1) * skoS2_i)
    if ((delta_i >= 0) and not ((((1) * skoX_i) >= 0)) and not ((skoX_i >= 1)) and not ((_let_3 >= ((15707963) / 5000000))) and not ((pi_i >= (31415927 / 10000000)))):
        if (not (((skoX_i + (10 * _let_7) + (20 * (skoX_i * skoS2_i * pi_i))) >= (4))) and not (((skoX_i + ((1 / 4) * (skoX_i * skoX_i))) >= 0))):
            skoSP_o =  skoX_i
        else:
            if (not (((_let_10 + ((10) * _let_1) + ((20) * (skoS2_i * skoS2_i * pi_i))) >= (4))) and not (((skoX_i + (((1) / 4) * (skoX_i * skoS2_i))) >= 0))):
                skoSP_o =  _let_10
            else:
                if (_let_6 and not ((_let_4 >= ((2) / 5)))):
                    skoSP_o =  ((1) / 2)
                else:
                    if (_let_6 and not ((_let_2 >= ((13) / 70)))):
                        skoSP_o =  3.0
                    else:
                        if (_let_6 and not ((_let_4 >= ((131) / 490)))):
                            skoSP_o =  (11 / 15)
                        else:
                            if (_let_4 >= (3 / 110)):
                                if (not (((_let_3 + (10 * _let_9) + (20 * _let_8)) >= (4))) and not (((skoX_i + (((1) / 4) * _let_7)) >= 0))):
                                    skoSP_o =  0.0
                                else:
                                    if ((_let_5 or ((_let_2 >= ((1) / 10)) and (_let_4 >= ((3) / 10)))) and (((pi_i + ((5 / 2) * _let_1) + ((5 / 2) * _let_9) + (5 * _let_8)) >= ((9) / 8)) or ((skoX_i + (((2) / 9) * _let_7)) >= 0))):
                                        if (_let_6 and not ((_let_4 >= ((1) / 15)))):
                                            skoSP_o =  (3.0)
                                        else:
                                            if (_let_6 and not ((_let_4 >= ((7) / 10)))):
                                                skoSP_o =  ((1) / 2)
                                            else:
                                                if (_let_2 >= (62500000000 / 373035649025431900673005710007)):
                                                    skoSP_o =  3.0
                                                else:
                                                    skoSP_o =  (123370054731675250000 / 373035648963746872682168085007)
                                    else:
                                        skoSP_o =  (1 / 2)
                            else:
                                skoSP_o =  ((25) / 2)
    else:
        skoSP_o =  0.0
    _let_1 = ((1) * pi_i)
    _let_2 = (skoS2_i * pi_i)
    _let_3 = (pi_i + (2 * _let_2))
    _let_4 = (_let_1 + ((2) * _let_2))
    _let_5 = (skoX_i >= 0)
    _let_6 = not (_let_5)
    _let_7 = (skoX_i * pi_i)
    _let_8 = (skoS2_i * pi_i * pi_i)
    _let_9 = (pi_i * pi_i)
    if ((delta_i >= 0) and not ((((1) * skoX_i) >= 0)) and not ((skoX_i >= 1)) and not ((_let_1 >= ((15707963) / 5000000))) and not ((pi_i >= (31415927 / 10000000))) and (((((1) * skoS2_i) + ((10) * _let_2) + ((20) * (skoS2_i * skoS2_i * pi_i))) >= (4)) or ((skoX_i + (((1) / 4) * (skoX_i * skoS2_i))) >= 0)) and (((skoX_i + (10 * _let_7) + (20 * (skoX_i * skoS2_i * pi_i))) >= (4)) or ((skoX_i + ((1 / 4) * (skoX_i * skoX_i))) >= 0))):
        if (_let_6 and not ((_let_4 >= ((2) / 5)))):
            skoSM_o =  (1 / 2)
        else:
            if (_let_6 and not ((_let_3 >= ((13) / 70)))):
                skoSM_o =  ((1) / 2)
            else:
                if ((_let_4 >= (3 / 110)) and (_let_5 or (_let_4 >= ((131) / 490)))):
                    if ((((pi_i + ((5 / 2) * _let_2) + ((5 / 2) * _let_9) + (5 * _let_8)) >= ((9) / 8)) or ((skoX_i + (((2) / 9) * _let_7)) >= 0)) and (((_let_1 + (10 * _let_9) + (20 * _let_8)) >= (4)) or ((skoX_i + (((1) / 4) * _let_7)) >= 0))):
                        if (_let_6 and not ((_let_3 >= ((1) / 10)))):
                            skoSM_o =  (2.0)
                        else:
                            if (_let_6 and (not ((_let_4 >= ((1) / 15))) or not ((_let_4 >= ((3) / 10))))):
                                skoSM_o =  3.0
                            else:
                                if (_let_6 and not ((_let_4 >= ((7) / 10)))):
                                    skoSM_o =  0.0
                                else:
                                    if (_let_3 >= (62500000000 / 373035649025431900673005710007)):
                                        skoSM_o =  ((5) / 3)
                                    else:
                                        skoSM_o =  ((1492142595978357547960347590028) / 373035648963746872682168085007)
                    else:
                        skoSM_o =  _let_1
                else:
                    skoSM_o =  4.0
    else:
        skoSM_o =  0.0
    print("skoSP=",skoSP_o)
    print("skoSM=",skoSM_o)
