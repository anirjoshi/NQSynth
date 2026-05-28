import sys

import sympy

from sympy import *

def pre_condition(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):

    #(delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (skoS**3 + 4*skoS**2 - skoS <= 2)



    pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), LessThan(Add(Pow(Symbol('skoS'), Integer(3)), Mul(Integer(4), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Symbol('skoS'))), Integer(2)))



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
    _let_3 = ((skoS_i + (((1) / 2) * pi_i)) >= 0)
    _let_4 = ((1) * _let_2)
    if ((delta_i >= 0) and (skoS_i >= 0) and not ((((1) * pi_i) >= ((15707963) / 5000000))) and not ((pi_i >= (31415927 / 10000000))) and ((skoS_i + ((4) * _let_2) + ((1) * _let_1)) >= (2)) and (_let_3 or (not (((skoS_i + _let_4 + (((5) / 3) * _let_1) + (((1) / 3) * (skoS_i * skoS_i * skoS_i * skoS_i))) >= ((2) / 3))) and not (((_let_4 + (((1) / 3) * _let_1)) >= ((1) / 3)))))):
        if (not (_let_3) and (skoS_i >= 3) and ((((1) * skoS_i) + (((2) / 3) * _let_2) + (((1) / 9) * _let_1)) >= (4 / 45))):
            skoCOSS_o =  3.0
        else:
            skoCOSS_o =  (2.0)
    else:
        skoCOSS_o =  0.0
    _let_1 = (skoS_i * skoS_i * skoS_i)
    _let_2 = (skoS_i * skoS_i)
    _let_3 = ((skoS_i + (((1) / 2) * pi_i)) >= 0)
    _let_4 = not (_let_3)
    _let_5 = ((1) * _let_2)
    _let_6 = ((_let_5 + (((1) / 3) * _let_1)) >= ((1) / 3))
    if ((delta_i >= 0) and (skoS_i >= 0) and not ((((1) * pi_i) >= ((15707963) / 5000000))) and not ((pi_i >= (31415927 / 10000000))) and ((skoS_i + ((4) * _let_2) + ((1) * _let_1)) >= (2)) and (_let_3 or not (_let_6))):
        if (_let_4 and ((skoS_i + _let_5 + (((5) / 3) * _let_1) + (((1) / 3) * (skoS_i * skoS_i * skoS_i * skoS_i))) >= ((2) / 3))):
            skoSINS_o =  skoS_i
        else:
            if (_let_6 and _let_4):
                skoSINS_o =  0.0
            else:
                if (_let_4 and (skoS_i >= 3) and ((((1) * skoS_i) + (((2) / 3) * _let_2) + (((1) / 9) * _let_1)) >= (4 / 45))):
                    skoSINS_o =  3.0
                else:
                    skoSINS_o =  (1 / 2)
    else:
        skoSINS_o =  0.0
    print("skoCOSS=",skoCOSS_o)
    print("skoSINS=",skoSINS_o)
