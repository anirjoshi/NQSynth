import sys

import sympy

from sympy import *

def pre_condition(a:sympy.Rational):

    #True



    pre_cond = true



    eval = pre_cond.subs({'a':a})



    return eval==True

print("Enter numerator of a")
a_num = int(input())
print("Enter denominator of a")
a_denm = int(input())
assert a_denm!=0
a_i = sympy.Rational(a_num,a_denm)

if pre_condition(a=a_i)==False:

    print("INFEASIBLE!")

    sys.exit(1)

else:

    _let_1 = (a_i >= (4))
    _let_2 = (a_i >= 0)
    _let_3 = ((1) * a_i)
    _let_4 = not ((a_i >= (35 / 4)))
    _let_5 = (a_i * a_i * a_i)
    if ((((a_i + _let_5) >= 0) or ((_let_3 + ((1 / 5) * _let_5)) >= 0)) and ((_let_3 >= 0) or (_let_2 and ((a_i + ((2 / 5) * (a_i * a_i)) + (((1) / 25) * (a_i * a_i * a_i * a_i))) >= 1)))):
        if (not ((a_i >= (3 / 5))) and not ((_let_3 >= 3))):
            x_o =  (1.0)
        else:
            if (_let_4 and not ((_let_3 >= ((1) / 16)))):
                x_o =  (1 / 2)
            else:
                if (_let_4 and not ((_let_3 >= ((1) / 8)))):
                    x_o =  ((1) / 2)
                else:
                    if (not (_let_1) and not ((_let_3 >= ((65) / 72)))):
                        x_o =  3.0
                    else:
                        if (((a_i >= (3)) or (a_i >= ((39) / 8))) and ((a_i >= ((3) / 8)) or (a_i >= (25))) and (_let_2 or (a_i >= ((25) / 8))) and (_let_1 or (a_i >= ((15) / 4)))):
                            x_o =  a_i
                        else:
                            x_o =  (2.0)
    else:
        x_o =  0.0
    _let_1 = not ((a_i >= 0))
    _let_2 = not ((a_i >= (4)))
    _let_3 = ((1) * a_i)
    _let_4 = not ((_let_3 >= 0))
    _let_5 = (a_i * a_i * a_i)
    if (_let_1 and _let_4):
        y_o =  0.0
    else:
        if (not (((a_i + _let_5) >= 0)) and not (((_let_3 + ((1 / 5) * _let_5)) >= 0))):
            y_o =  a_i
        else:
            if (_let_4 and (_let_1 or not (((a_i + ((2 / 5) * (a_i * a_i)) + (((1) / 25) * (a_i * a_i * a_i * a_i))) >= 1)))):
                y_o =  0.0
            else:
                if (not ((a_i >= (3 / 5))) and not ((_let_3 >= 3))):
                    y_o =  (2.0)
                else:
                    if (not ((a_i >= (35 / 4))) and (not ((_let_3 >= ((1) / 16))) or not ((_let_3 >= ((1) / 8))))):
                        y_o =  0.0
                    else:
                        if (_let_2 and not ((_let_3 >= ((65) / 72)))):
                            y_o =  (1 / 2)
                        else:
                            if (_let_2 and not ((a_i >= ((15) / 4)))):
                                y_o =  0.0
                            else:
                                if (not ((a_i >= (3))) and not ((a_i >= ((39) / 8)))):
                                    y_o =  ((1) / 2)
                                else:
                                    if (not ((a_i >= ((3) / 8))) and not ((a_i >= (25)))):
                                        y_o =  3.0
                                    else:
                                        if (_let_1 and not ((a_i >= ((25) / 8)))):
                                            y_o =  (1 / 2)
                                        else:
                                            y_o =  0.0
    _let_1 = (a_i >= 0)
    _let_2 = (a_i >= (4))
    _let_3 = ((1) * a_i)
    _let_4 = (a_i * a_i)
    _let_5 = (_let_3 >= 0)
    _let_6 = (a_i * a_i * a_i)
    if ((_let_1 or _let_5) and (((a_i + _let_6) >= 0) or ((_let_3 + ((1 / 5) * _let_6)) >= 0))):
        if (not (_let_5) and not (((a_i + ((2 / 5) * _let_4) + (((1) / 25) * (a_i * a_i * a_i * a_i))) >= 1))):
            z_o =  ((1) + ((1 / 5) * _let_4))
        else:
            if (not ((a_i >= (3 / 5))) and not ((_let_3 >= 3))):
                z_o =  2.0
            else:
                if (not ((a_i >= (35 / 4))) and (not ((_let_3 >= ((1) / 16))) or not ((_let_3 >= ((1) / 8))))):
                    z_o =  3.0
                else:
                    if (not (_let_2) and not ((_let_3 >= ((65) / 72)))):
                        z_o =  2.0
                    else:
                        if (((a_i >= (3)) or (a_i >= ((39) / 8))) and ((a_i >= ((3) / 8)) or (a_i >= (25))) and (_let_2 or (a_i >= ((15) / 4)))):
                            if (not (_let_1) and not ((a_i >= ((25) / 8)))):
                                z_o =  (2.0)
                            else:
                                z_o =  0.0
                        else:
                            z_o =  (1 / 2)
    else:
        z_o =  0.0
    print("x=",x_o)
    print("y=",y_o)
    print("z=",z_o)
