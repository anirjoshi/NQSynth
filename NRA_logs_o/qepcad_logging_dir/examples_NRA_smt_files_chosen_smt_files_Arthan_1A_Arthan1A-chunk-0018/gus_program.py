import sys

import sympy

from sympy import *

def pre_condition(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):

    #(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS)



    pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))))



    eval = pre_cond.subs({'delta':delta, 'skoS':skoS, 'pi':pi})



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

print("Enter numerator of pi")
pi_num = int(input())
print("Enter denominator of pi")
pi_denm = int(input())
assert pi_denm!=0
pi_i = sympy.Rational(pi_num,pi_denm)

if pre_condition(delta=delta_i,skoS=skoS_i,pi=pi_i)==False:

    print("INFEASIBLE!")

    sys.exit(1)

else:

    _let_1 = (skoS_i * skoS_i * skoS_i)
    _let_2 = (skoS_i * skoS_i)
    _let_3 = ((1) * skoS_i)
    if ((delta_i >= 0) and not ((((1) * pi_i) >= ((15707963) / 5000000))) and not ((pi_i >= (31415927 / 10000000))) and not (((skoS_i + (((1) / 2) * pi_i)) >= 0)) and ((((1) * _let_2) + (((1) / 3) * _let_1)) >= ((1) / 3))):
        if ((_let_3 + (((7) / 20) * _let_2)) >= (7 / 10)):
            if (((skoS_i + (((6) / 5) * _let_2) + (((2) / 3) * _let_1)) >= (1 / 15)) and ((skoS_i + (((2) / 3) * _let_2) + (((4) / 9) * _let_1)) >= ((5) / 9))):
                if ((skoS_i + ((4 / 11) * _let_2) + (((2) / 11) * _let_1)) >= (1 / 5)):
                    if ((_let_3 + ((9) * _let_2) + ((5) * _let_1)) >= (1)):
                        skoCOSS_o =  (40000001 / 40000000)
                    else:
                        skoCOSS_o =  skoS_i
                else:
                    skoCOSS_o =  (2.0)
            else:
                skoCOSS_o =  ((1) / 2)
        else:
            skoCOSS_o =  2.0
    else:
        skoCOSS_o =  0.0
    _let_1 = (skoS_i * skoS_i * skoS_i)
    _let_2 = (skoS_i * skoS_i)
    if ((delta_i >= 0) and not ((((1) * pi_i) >= ((15707963) / 5000000))) and not ((pi_i >= (31415927 / 10000000))) and not (((skoS_i + (((1) / 2) * pi_i)) >= 0)) and ((((1) * _let_2) + (((1) / 3) * _let_1)) >= ((1) / 3))):
        if ((((1) * skoS_i) + (((7) / 20) * _let_2)) >= (7 / 10)):
            if ((skoS_i + (((2) / 3) * _let_2) + (((4) / 9) * _let_1)) >= ((5) / 9)):
                if ((skoS_i + (((6) / 5) * _let_2) + (((2) / 3) * _let_1)) >= (1 / 15)):
                    if ((skoS_i + ((4 / 11) * _let_2) + (((2) / 11) * _let_1)) >= (1 / 5)):
                        skoSINS_o =  0.0
                    else:
                        skoSINS_o =  (1 / 2)
                else:
                    skoSINS_o =  3.0
            else:
                skoSINS_o =  0.0
        else:
            skoSINS_o =  (2.0)
    else:
        skoSINS_o =  0.0
    print("skoCOSS=",skoCOSS_o)
    print("skoSINS=",skoSINS_o)
