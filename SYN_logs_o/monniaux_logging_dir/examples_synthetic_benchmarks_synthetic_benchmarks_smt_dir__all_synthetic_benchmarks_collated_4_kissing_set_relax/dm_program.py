import sympy
from sympy import *

def pre_condition_0(d:sympy.Rational,x_5_0:sympy.Rational,x_5_1:sympy.Rational):
	#(d > 0) & (d - x_0_1**2 + 63/64 > 0) & (d - x_1_0**2 - x_1_1**2 + 1 > 0) & (d - x_2_0**2 - x_2_1**2 + 1 > 0) & (d - x_3_0**2 - x_3_1**2 + 1 > 0) & (d - x_4_0**2 - x_4_1**2 + 1 > 0) & (d - x_5_0**2 - x_5_1**2 + 1 > 0) & (d + x_0_1**2 - 2*x_0_1*x_1_1 + x_1_0**2 - x_1_0/4 + x_1_1**2 - 63/64 > 0) & (d + x_0_1**2 - 2*x_0_1*x_2_1 + x_2_0**2 - x_2_0/4 + x_2_1**2 - 63/64 > 0) & (d + x_0_1**2 - 2*x_0_1*x_3_1 + x_3_0**2 - x_3_0/4 + x_3_1**2 - 63/64 > 0) & (d + x_0_1**2 - 2*x_0_1*x_4_1 + x_4_0**2 - x_4_0/4 + x_4_1**2 - 63/64 > 0) & (d + x_0_1**2 - 2*x_0_1*x_5_1 + x_5_0**2 - x_5_0/4 + x_5_1**2 - 63/64 > 0) & (d + x_1_0**2 - 2*x_1_0*x_2_0 + x_1_1**2 - 2*x_1_1*x_2_1 + x_2_0**2 + x_2_1**2 - 1 > 0) & (d + x_1_0**2 - 2*x_1_0*x_3_0 + x_1_1**2 - 2*x_1_1*x_3_1 + x_3_0**2 + x_3_1**2 - 1 > 0) & (d + x_1_0**2 - 2*x_1_0*x_4_0 + x_1_1**2 - 2*x_1_1*x_4_1 + x_4_0**2 + x_4_1**2 - 1 > 0) & (d + x_1_0**2 - 2*x_1_0*x_5_0 + x_1_1**2 - 2*x_1_1*x_5_1 + x_5_0**2 + x_5_1**2 - 1 > 0) & (d + x_2_0**2 - 2*x_2_0*x_3_0 + x_2_1**2 - 2*x_2_1*x_3_1 + x_3_0**2 + x_3_1**2 - 1 > 0) & (d + x_2_0**2 - 2*x_2_0*x_4_0 + x_2_1**2 - 2*x_2_1*x_4_1 + x_4_0**2 + x_4_1**2 - 1 > 0) & (d + x_2_0**2 - 2*x_2_0*x_5_0 + x_2_1**2 - 2*x_2_1*x_5_1 + x_5_0**2 + x_5_1**2 - 1 > 0) & (d + x_3_0**2 - 2*x_3_0*x_4_0 + x_3_1**2 - 2*x_3_1*x_4_1 + x_4_0**2 + x_4_1**2 - 1 > 0) & (d + x_3_0**2 - 2*x_3_0*x_5_0 + x_3_1**2 - 2*x_3_1*x_5_1 + x_5_0**2 + x_5_1**2 - 1 > 0) & (d + x_4_0**2 - 2*x_4_0*x_5_0 + x_4_1**2 - 2*x_4_1*x_5_1 + x_5_0**2 + x_5_1**2 - 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('d'), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Mul(Integer(-1), Pow(Symbol('x_0_1'), Integer(2))), Rational(63, 64)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Mul(Integer(-1), Pow(Symbol('x_1_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_1_1'), Integer(2))), Integer(1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Mul(Integer(-1), Pow(Symbol('x_2_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_2_1'), Integer(2))), Integer(1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Mul(Integer(-1), Pow(Symbol('x_3_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_3_1'), Integer(2))), Integer(1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Mul(Integer(-1), Pow(Symbol('x_4_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_4_1'), Integer(2))), Integer(1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Mul(Integer(-1), Pow(Symbol('x_5_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_5_1'), Integer(2))), Integer(1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_0_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_0_1'), Symbol('x_1_1')), Pow(Symbol('x_1_0'), Integer(2)), Mul(Integer(-1), Rational(1, 4), Symbol('x_1_0')), Pow(Symbol('x_1_1'), Integer(2)), Rational(-63, 64)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_0_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_0_1'), Symbol('x_2_1')), Pow(Symbol('x_2_0'), Integer(2)), Mul(Integer(-1), Rational(1, 4), Symbol('x_2_0')), Pow(Symbol('x_2_1'), Integer(2)), Rational(-63, 64)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_0_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_0_1'), Symbol('x_3_1')), Pow(Symbol('x_3_0'), Integer(2)), Mul(Integer(-1), Rational(1, 4), Symbol('x_3_0')), Pow(Symbol('x_3_1'), Integer(2)), Rational(-63, 64)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_0_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_0_1'), Symbol('x_4_1')), Pow(Symbol('x_4_0'), Integer(2)), Mul(Integer(-1), Rational(1, 4), Symbol('x_4_0')), Pow(Symbol('x_4_1'), Integer(2)), Rational(-63, 64)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_0_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_0_1'), Symbol('x_5_1')), Pow(Symbol('x_5_0'), Integer(2)), Mul(Integer(-1), Rational(1, 4), Symbol('x_5_0')), Pow(Symbol('x_5_1'), Integer(2)), Rational(-63, 64)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_1_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_1_0'), Symbol('x_2_0')), Pow(Symbol('x_1_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_1_1'), Symbol('x_2_1')), Pow(Symbol('x_2_0'), Integer(2)), Pow(Symbol('x_2_1'), Integer(2)), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_1_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_1_0'), Symbol('x_3_0')), Pow(Symbol('x_1_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_1_1'), Symbol('x_3_1')), Pow(Symbol('x_3_0'), Integer(2)), Pow(Symbol('x_3_1'), Integer(2)), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_1_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_1_0'), Symbol('x_4_0')), Pow(Symbol('x_1_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_1_1'), Symbol('x_4_1')), Pow(Symbol('x_4_0'), Integer(2)), Pow(Symbol('x_4_1'), Integer(2)), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_1_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_1_0'), Symbol('x_5_0')), Pow(Symbol('x_1_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_1_1'), Symbol('x_5_1')), Pow(Symbol('x_5_0'), Integer(2)), Pow(Symbol('x_5_1'), Integer(2)), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_2_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_2_0'), Symbol('x_3_0')), Pow(Symbol('x_2_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_2_1'), Symbol('x_3_1')), Pow(Symbol('x_3_0'), Integer(2)), Pow(Symbol('x_3_1'), Integer(2)), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_2_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_2_0'), Symbol('x_4_0')), Pow(Symbol('x_2_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_2_1'), Symbol('x_4_1')), Pow(Symbol('x_4_0'), Integer(2)), Pow(Symbol('x_4_1'), Integer(2)), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_2_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_2_0'), Symbol('x_5_0')), Pow(Symbol('x_2_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_2_1'), Symbol('x_5_1')), Pow(Symbol('x_5_0'), Integer(2)), Pow(Symbol('x_5_1'), Integer(2)), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_3_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_3_0'), Symbol('x_4_0')), Pow(Symbol('x_3_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_3_1'), Symbol('x_4_1')), Pow(Symbol('x_4_0'), Integer(2)), Pow(Symbol('x_4_1'), Integer(2)), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_3_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_3_0'), Symbol('x_5_0')), Pow(Symbol('x_3_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_3_1'), Symbol('x_5_1')), Pow(Symbol('x_5_0'), Integer(2)), Pow(Symbol('x_5_1'), Integer(2)), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_4_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_4_0'), Symbol('x_5_0')), Pow(Symbol('x_4_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_4_1'), Symbol('x_5_1')), Pow(Symbol('x_5_0'), Integer(2)), Pow(Symbol('x_5_1'), Integer(2)), Integer(-1)), Integer(0)))

	eval = pre_cond.subs( { 'd':d, 'x_5_0':x_5_0, 'x_5_1':x_5_1 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(d:sympy.Rational,x_5_0:sympy.Rational,x_5_1:sympy.Rational):
	#(d > 0) & (d - x_1_0**2 - x_1_1**2 + 1 > 0) & (d - x_2_0**2 - x_2_1**2 + 1 > 0) & (d - x_3_0**2 - x_3_1**2 + 1 > 0) & (d - x_4_0**2 - x_4_1**2 + 1 > 0) & (d - x_5_0**2 - x_5_1**2 + 1 > 0) & (d + x_1_0**2 - x_1_0/4 + x_1_1**2 - x_1_1 - 47/64 > 0) & (d + x_2_0**2 - x_2_0/4 + x_2_1**2 - x_2_1 - 47/64 > 0) & (d + x_3_0**2 - x_3_0/4 + x_3_1**2 - x_3_1 - 47/64 > 0) & (d + x_4_0**2 - x_4_0/4 + x_4_1**2 - x_4_1 - 47/64 > 0) & (d + x_5_0**2 - x_5_0/4 + x_5_1**2 - x_5_1 - 47/64 > 0) & (d + x_1_0**2 - 2*x_1_0*x_2_0 + x_1_1**2 - 2*x_1_1*x_2_1 + x_2_0**2 + x_2_1**2 - 1 > 0) & (d + x_1_0**2 - 2*x_1_0*x_3_0 + x_1_1**2 - 2*x_1_1*x_3_1 + x_3_0**2 + x_3_1**2 - 1 > 0) & (d + x_1_0**2 - 2*x_1_0*x_4_0 + x_1_1**2 - 2*x_1_1*x_4_1 + x_4_0**2 + x_4_1**2 - 1 > 0) & (d + x_1_0**2 - 2*x_1_0*x_5_0 + x_1_1**2 - 2*x_1_1*x_5_1 + x_5_0**2 + x_5_1**2 - 1 > 0) & (d + x_2_0**2 - 2*x_2_0*x_3_0 + x_2_1**2 - 2*x_2_1*x_3_1 + x_3_0**2 + x_3_1**2 - 1 > 0) & (d + x_2_0**2 - 2*x_2_0*x_4_0 + x_2_1**2 - 2*x_2_1*x_4_1 + x_4_0**2 + x_4_1**2 - 1 > 0) & (d + x_2_0**2 - 2*x_2_0*x_5_0 + x_2_1**2 - 2*x_2_1*x_5_1 + x_5_0**2 + x_5_1**2 - 1 > 0) & (d + x_3_0**2 - 2*x_3_0*x_4_0 + x_3_1**2 - 2*x_3_1*x_4_1 + x_4_0**2 + x_4_1**2 - 1 > 0) & (d + x_3_0**2 - 2*x_3_0*x_5_0 + x_3_1**2 - 2*x_3_1*x_5_1 + x_5_0**2 + x_5_1**2 - 1 > 0) & (d + x_4_0**2 - 2*x_4_0*x_5_0 + x_4_1**2 - 2*x_4_1*x_5_1 + x_5_0**2 + x_5_1**2 - 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('d'), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Mul(Integer(-1), Pow(Symbol('x_1_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_1_1'), Integer(2))), Integer(1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Mul(Integer(-1), Pow(Symbol('x_2_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_2_1'), Integer(2))), Integer(1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Mul(Integer(-1), Pow(Symbol('x_3_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_3_1'), Integer(2))), Integer(1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Mul(Integer(-1), Pow(Symbol('x_4_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_4_1'), Integer(2))), Integer(1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Mul(Integer(-1), Pow(Symbol('x_5_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_5_1'), Integer(2))), Integer(1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_1_0'), Integer(2)), Mul(Integer(-1), Rational(1, 4), Symbol('x_1_0')), Pow(Symbol('x_1_1'), Integer(2)), Mul(Integer(-1), Symbol('x_1_1')), Rational(-47, 64)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_2_0'), Integer(2)), Mul(Integer(-1), Rational(1, 4), Symbol('x_2_0')), Pow(Symbol('x_2_1'), Integer(2)), Mul(Integer(-1), Symbol('x_2_1')), Rational(-47, 64)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_3_0'), Integer(2)), Mul(Integer(-1), Rational(1, 4), Symbol('x_3_0')), Pow(Symbol('x_3_1'), Integer(2)), Mul(Integer(-1), Symbol('x_3_1')), Rational(-47, 64)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_4_0'), Integer(2)), Mul(Integer(-1), Rational(1, 4), Symbol('x_4_0')), Pow(Symbol('x_4_1'), Integer(2)), Mul(Integer(-1), Symbol('x_4_1')), Rational(-47, 64)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_5_0'), Integer(2)), Mul(Integer(-1), Rational(1, 4), Symbol('x_5_0')), Pow(Symbol('x_5_1'), Integer(2)), Mul(Integer(-1), Symbol('x_5_1')), Rational(-47, 64)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_1_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_1_0'), Symbol('x_2_0')), Pow(Symbol('x_1_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_1_1'), Symbol('x_2_1')), Pow(Symbol('x_2_0'), Integer(2)), Pow(Symbol('x_2_1'), Integer(2)), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_1_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_1_0'), Symbol('x_3_0')), Pow(Symbol('x_1_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_1_1'), Symbol('x_3_1')), Pow(Symbol('x_3_0'), Integer(2)), Pow(Symbol('x_3_1'), Integer(2)), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_1_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_1_0'), Symbol('x_4_0')), Pow(Symbol('x_1_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_1_1'), Symbol('x_4_1')), Pow(Symbol('x_4_0'), Integer(2)), Pow(Symbol('x_4_1'), Integer(2)), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_1_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_1_0'), Symbol('x_5_0')), Pow(Symbol('x_1_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_1_1'), Symbol('x_5_1')), Pow(Symbol('x_5_0'), Integer(2)), Pow(Symbol('x_5_1'), Integer(2)), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_2_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_2_0'), Symbol('x_3_0')), Pow(Symbol('x_2_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_2_1'), Symbol('x_3_1')), Pow(Symbol('x_3_0'), Integer(2)), Pow(Symbol('x_3_1'), Integer(2)), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_2_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_2_0'), Symbol('x_4_0')), Pow(Symbol('x_2_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_2_1'), Symbol('x_4_1')), Pow(Symbol('x_4_0'), Integer(2)), Pow(Symbol('x_4_1'), Integer(2)), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_2_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_2_0'), Symbol('x_5_0')), Pow(Symbol('x_2_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_2_1'), Symbol('x_5_1')), Pow(Symbol('x_5_0'), Integer(2)), Pow(Symbol('x_5_1'), Integer(2)), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_3_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_3_0'), Symbol('x_4_0')), Pow(Symbol('x_3_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_3_1'), Symbol('x_4_1')), Pow(Symbol('x_4_0'), Integer(2)), Pow(Symbol('x_4_1'), Integer(2)), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_3_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_3_0'), Symbol('x_5_0')), Pow(Symbol('x_3_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_3_1'), Symbol('x_5_1')), Pow(Symbol('x_5_0'), Integer(2)), Pow(Symbol('x_5_1'), Integer(2)), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_4_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_4_0'), Symbol('x_5_0')), Pow(Symbol('x_4_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_4_1'), Symbol('x_5_1')), Pow(Symbol('x_5_0'), Integer(2)), Pow(Symbol('x_5_1'), Integer(2)), Integer(-1)), Integer(0)))

	eval = pre_cond.subs( { 'd':d, 'x_5_0':x_5_0, 'x_5_1':x_5_1 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(d:sympy.Rational,x_5_0:sympy.Rational,x_5_1:sympy.Rational):
	#(d > 0) & (d - x_1_1**2 + 3/4 > 0) & (d + x_1_1**2 - x_1_1 - 23/64 > 0) & (d - x_2_0**2 - x_2_1**2 + 1 > 0) & (d - x_3_0**2 - x_3_1**2 + 1 > 0) & (d - x_4_0**2 - x_4_1**2 + 1 > 0) & (d - x_5_0**2 - x_5_1**2 + 1 > 0) & (d + x_2_0**2 - x_2_0/4 + x_2_1**2 - x_2_1 - 47/64 > 0) & (d + x_3_0**2 - x_3_0/4 + x_3_1**2 - x_3_1 - 47/64 > 0) & (d + x_4_0**2 - x_4_0/4 + x_4_1**2 - x_4_1 - 47/64 > 0) & (d + x_5_0**2 - x_5_0/4 + x_5_1**2 - x_5_1 - 47/64 > 0) & (d + x_1_1**2 - 2*x_1_1*x_2_1 + x_2_0**2 + x_2_0 + x_2_1**2 - 3/4 > 0) & (d + x_1_1**2 - 2*x_1_1*x_3_1 + x_3_0**2 + x_3_0 + x_3_1**2 - 3/4 > 0) & (d + x_1_1**2 - 2*x_1_1*x_4_1 + x_4_0**2 + x_4_0 + x_4_1**2 - 3/4 > 0) & (d + x_1_1**2 - 2*x_1_1*x_5_1 + x_5_0**2 + x_5_0 + x_5_1**2 - 3/4 > 0) & (d + x_2_0**2 - 2*x_2_0*x_3_0 + x_2_1**2 - 2*x_2_1*x_3_1 + x_3_0**2 + x_3_1**2 - 1 > 0) & (d + x_2_0**2 - 2*x_2_0*x_4_0 + x_2_1**2 - 2*x_2_1*x_4_1 + x_4_0**2 + x_4_1**2 - 1 > 0) & (d + x_2_0**2 - 2*x_2_0*x_5_0 + x_2_1**2 - 2*x_2_1*x_5_1 + x_5_0**2 + x_5_1**2 - 1 > 0) & (d + x_3_0**2 - 2*x_3_0*x_4_0 + x_3_1**2 - 2*x_3_1*x_4_1 + x_4_0**2 + x_4_1**2 - 1 > 0) & (d + x_3_0**2 - 2*x_3_0*x_5_0 + x_3_1**2 - 2*x_3_1*x_5_1 + x_5_0**2 + x_5_1**2 - 1 > 0) & (d + x_4_0**2 - 2*x_4_0*x_5_0 + x_4_1**2 - 2*x_4_1*x_5_1 + x_5_0**2 + x_5_1**2 - 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('d'), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Mul(Integer(-1), Pow(Symbol('x_1_1'), Integer(2))), Rational(3, 4)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_1_1'), Integer(2)), Mul(Integer(-1), Symbol('x_1_1')), Rational(-23, 64)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Mul(Integer(-1), Pow(Symbol('x_2_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_2_1'), Integer(2))), Integer(1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Mul(Integer(-1), Pow(Symbol('x_3_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_3_1'), Integer(2))), Integer(1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Mul(Integer(-1), Pow(Symbol('x_4_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_4_1'), Integer(2))), Integer(1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Mul(Integer(-1), Pow(Symbol('x_5_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_5_1'), Integer(2))), Integer(1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_2_0'), Integer(2)), Mul(Integer(-1), Rational(1, 4), Symbol('x_2_0')), Pow(Symbol('x_2_1'), Integer(2)), Mul(Integer(-1), Symbol('x_2_1')), Rational(-47, 64)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_3_0'), Integer(2)), Mul(Integer(-1), Rational(1, 4), Symbol('x_3_0')), Pow(Symbol('x_3_1'), Integer(2)), Mul(Integer(-1), Symbol('x_3_1')), Rational(-47, 64)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_4_0'), Integer(2)), Mul(Integer(-1), Rational(1, 4), Symbol('x_4_0')), Pow(Symbol('x_4_1'), Integer(2)), Mul(Integer(-1), Symbol('x_4_1')), Rational(-47, 64)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_5_0'), Integer(2)), Mul(Integer(-1), Rational(1, 4), Symbol('x_5_0')), Pow(Symbol('x_5_1'), Integer(2)), Mul(Integer(-1), Symbol('x_5_1')), Rational(-47, 64)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_1_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_1_1'), Symbol('x_2_1')), Pow(Symbol('x_2_0'), Integer(2)), Symbol('x_2_0'), Pow(Symbol('x_2_1'), Integer(2)), Rational(-3, 4)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_1_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_1_1'), Symbol('x_3_1')), Pow(Symbol('x_3_0'), Integer(2)), Symbol('x_3_0'), Pow(Symbol('x_3_1'), Integer(2)), Rational(-3, 4)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_1_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_1_1'), Symbol('x_4_1')), Pow(Symbol('x_4_0'), Integer(2)), Symbol('x_4_0'), Pow(Symbol('x_4_1'), Integer(2)), Rational(-3, 4)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_1_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_1_1'), Symbol('x_5_1')), Pow(Symbol('x_5_0'), Integer(2)), Symbol('x_5_0'), Pow(Symbol('x_5_1'), Integer(2)), Rational(-3, 4)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_2_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_2_0'), Symbol('x_3_0')), Pow(Symbol('x_2_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_2_1'), Symbol('x_3_1')), Pow(Symbol('x_3_0'), Integer(2)), Pow(Symbol('x_3_1'), Integer(2)), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_2_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_2_0'), Symbol('x_4_0')), Pow(Symbol('x_2_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_2_1'), Symbol('x_4_1')), Pow(Symbol('x_4_0'), Integer(2)), Pow(Symbol('x_4_1'), Integer(2)), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_2_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_2_0'), Symbol('x_5_0')), Pow(Symbol('x_2_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_2_1'), Symbol('x_5_1')), Pow(Symbol('x_5_0'), Integer(2)), Pow(Symbol('x_5_1'), Integer(2)), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_3_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_3_0'), Symbol('x_4_0')), Pow(Symbol('x_3_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_3_1'), Symbol('x_4_1')), Pow(Symbol('x_4_0'), Integer(2)), Pow(Symbol('x_4_1'), Integer(2)), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_3_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_3_0'), Symbol('x_5_0')), Pow(Symbol('x_3_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_3_1'), Symbol('x_5_1')), Pow(Symbol('x_5_0'), Integer(2)), Pow(Symbol('x_5_1'), Integer(2)), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_4_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_4_0'), Symbol('x_5_0')), Pow(Symbol('x_4_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_4_1'), Symbol('x_5_1')), Pow(Symbol('x_5_0'), Integer(2)), Pow(Symbol('x_5_1'), Integer(2)), Integer(-1)), Integer(0)))

	eval = pre_cond.subs( { 'd':d, 'x_5_0':x_5_0, 'x_5_1':x_5_1 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(d:sympy.Rational,x_5_0:sympy.Rational,x_5_1:sympy.Rational):
	#(d > 0) & (d + x_2_0**2 + x_2_0 + x_2_1**2 + x_2_1 - 1/2 > 0) & (d + x_3_0**2 + x_3_0 + x_3_1**2 + x_3_1 - 1/2 > 0) & (d + x_4_0**2 + x_4_0 + x_4_1**2 + x_4_1 - 1/2 > 0) & (d + x_5_0**2 + x_5_0 + x_5_1**2 + x_5_1 - 1/2 > 0) & (d - x_2_0**2 - x_2_1**2 + 1 > 0) & (d - x_3_0**2 - x_3_1**2 + 1 > 0) & (d - x_4_0**2 - x_4_1**2 + 1 > 0) & (d - x_5_0**2 - x_5_1**2 + 1 > 0) & (d + x_2_0**2 - x_2_0/4 + x_2_1**2 - x_2_1 - 47/64 > 0) & (d + x_3_0**2 - x_3_0/4 + x_3_1**2 - x_3_1 - 47/64 > 0) & (d + x_4_0**2 - x_4_0/4 + x_4_1**2 - x_4_1 - 47/64 > 0) & (d + x_5_0**2 - x_5_0/4 + x_5_1**2 - x_5_1 - 47/64 > 0) & (d + x_2_0**2 - 2*x_2_0*x_3_0 + x_2_1**2 - 2*x_2_1*x_3_1 + x_3_0**2 + x_3_1**2 - 1 > 0) & (d + x_2_0**2 - 2*x_2_0*x_4_0 + x_2_1**2 - 2*x_2_1*x_4_1 + x_4_0**2 + x_4_1**2 - 1 > 0) & (d + x_2_0**2 - 2*x_2_0*x_5_0 + x_2_1**2 - 2*x_2_1*x_5_1 + x_5_0**2 + x_5_1**2 - 1 > 0) & (d + x_3_0**2 - 2*x_3_0*x_4_0 + x_3_1**2 - 2*x_3_1*x_4_1 + x_4_0**2 + x_4_1**2 - 1 > 0) & (d + x_3_0**2 - 2*x_3_0*x_5_0 + x_3_1**2 - 2*x_3_1*x_5_1 + x_5_0**2 + x_5_1**2 - 1 > 0) & (d + x_4_0**2 - 2*x_4_0*x_5_0 + x_4_1**2 - 2*x_4_1*x_5_1 + x_5_0**2 + x_5_1**2 - 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('d'), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_2_0'), Integer(2)), Symbol('x_2_0'), Pow(Symbol('x_2_1'), Integer(2)), Symbol('x_2_1'), Rational(-1, 2)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_3_0'), Integer(2)), Symbol('x_3_0'), Pow(Symbol('x_3_1'), Integer(2)), Symbol('x_3_1'), Rational(-1, 2)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_4_0'), Integer(2)), Symbol('x_4_0'), Pow(Symbol('x_4_1'), Integer(2)), Symbol('x_4_1'), Rational(-1, 2)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_5_0'), Integer(2)), Symbol('x_5_0'), Pow(Symbol('x_5_1'), Integer(2)), Symbol('x_5_1'), Rational(-1, 2)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Mul(Integer(-1), Pow(Symbol('x_2_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_2_1'), Integer(2))), Integer(1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Mul(Integer(-1), Pow(Symbol('x_3_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_3_1'), Integer(2))), Integer(1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Mul(Integer(-1), Pow(Symbol('x_4_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_4_1'), Integer(2))), Integer(1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Mul(Integer(-1), Pow(Symbol('x_5_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_5_1'), Integer(2))), Integer(1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_2_0'), Integer(2)), Mul(Integer(-1), Rational(1, 4), Symbol('x_2_0')), Pow(Symbol('x_2_1'), Integer(2)), Mul(Integer(-1), Symbol('x_2_1')), Rational(-47, 64)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_3_0'), Integer(2)), Mul(Integer(-1), Rational(1, 4), Symbol('x_3_0')), Pow(Symbol('x_3_1'), Integer(2)), Mul(Integer(-1), Symbol('x_3_1')), Rational(-47, 64)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_4_0'), Integer(2)), Mul(Integer(-1), Rational(1, 4), Symbol('x_4_0')), Pow(Symbol('x_4_1'), Integer(2)), Mul(Integer(-1), Symbol('x_4_1')), Rational(-47, 64)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_5_0'), Integer(2)), Mul(Integer(-1), Rational(1, 4), Symbol('x_5_0')), Pow(Symbol('x_5_1'), Integer(2)), Mul(Integer(-1), Symbol('x_5_1')), Rational(-47, 64)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_2_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_2_0'), Symbol('x_3_0')), Pow(Symbol('x_2_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_2_1'), Symbol('x_3_1')), Pow(Symbol('x_3_0'), Integer(2)), Pow(Symbol('x_3_1'), Integer(2)), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_2_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_2_0'), Symbol('x_4_0')), Pow(Symbol('x_2_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_2_1'), Symbol('x_4_1')), Pow(Symbol('x_4_0'), Integer(2)), Pow(Symbol('x_4_1'), Integer(2)), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_2_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_2_0'), Symbol('x_5_0')), Pow(Symbol('x_2_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_2_1'), Symbol('x_5_1')), Pow(Symbol('x_5_0'), Integer(2)), Pow(Symbol('x_5_1'), Integer(2)), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_3_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_3_0'), Symbol('x_4_0')), Pow(Symbol('x_3_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_3_1'), Symbol('x_4_1')), Pow(Symbol('x_4_0'), Integer(2)), Pow(Symbol('x_4_1'), Integer(2)), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_3_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_3_0'), Symbol('x_5_0')), Pow(Symbol('x_3_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_3_1'), Symbol('x_5_1')), Pow(Symbol('x_5_0'), Integer(2)), Pow(Symbol('x_5_1'), Integer(2)), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_4_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_4_0'), Symbol('x_5_0')), Pow(Symbol('x_4_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_4_1'), Symbol('x_5_1')), Pow(Symbol('x_5_0'), Integer(2)), Pow(Symbol('x_5_1'), Integer(2)), Integer(-1)), Integer(0)))

	eval = pre_cond.subs( { 'd':d, 'x_5_0':x_5_0, 'x_5_1':x_5_1 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_4(d:sympy.Rational,x_5_0:sympy.Rational,x_5_1:sympy.Rational):
	#(d > 0) & (d - x_2_1**2 > 0) & (d + x_2_1**2 + x_2_1 + 3/2 > 0) & (d + x_2_1**2 - x_2_1 + 1/64 > 0) & (d + x_3_0**2 + x_3_0 + x_3_1**2 + x_3_1 - 1/2 > 0) & (d + x_4_0**2 + x_4_0 + x_4_1**2 + x_4_1 - 1/2 > 0) & (d + x_5_0**2 + x_5_0 + x_5_1**2 + x_5_1 - 1/2 > 0) & (d - x_3_0**2 - x_3_1**2 + 1 > 0) & (d - x_4_0**2 - x_4_1**2 + 1 > 0) & (d - x_5_0**2 - x_5_1**2 + 1 > 0) & (d + x_3_0**2 - x_3_0/4 + x_3_1**2 - x_3_1 - 47/64 > 0) & (d + x_4_0**2 - x_4_0/4 + x_4_1**2 - x_4_1 - 47/64 > 0) & (d + x_5_0**2 - x_5_0/4 + x_5_1**2 - x_5_1 - 47/64 > 0) & (d + x_2_1**2 - 2*x_2_1*x_3_1 + x_3_0**2 - 2*x_3_0 + x_3_1**2 > 0) & (d + x_2_1**2 - 2*x_2_1*x_4_1 + x_4_0**2 - 2*x_4_0 + x_4_1**2 > 0) & (d + x_2_1**2 - 2*x_2_1*x_5_1 + x_5_0**2 - 2*x_5_0 + x_5_1**2 > 0) & (d + x_3_0**2 - 2*x_3_0*x_4_0 + x_3_1**2 - 2*x_3_1*x_4_1 + x_4_0**2 + x_4_1**2 - 1 > 0) & (d + x_3_0**2 - 2*x_3_0*x_5_0 + x_3_1**2 - 2*x_3_1*x_5_1 + x_5_0**2 + x_5_1**2 - 1 > 0) & (d + x_4_0**2 - 2*x_4_0*x_5_0 + x_4_1**2 - 2*x_4_1*x_5_1 + x_5_0**2 + x_5_1**2 - 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('d'), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Mul(Integer(-1), Pow(Symbol('x_2_1'), Integer(2)))), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_2_1'), Integer(2)), Symbol('x_2_1'), Rational(3, 2)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_2_1'), Integer(2)), Mul(Integer(-1), Symbol('x_2_1')), Rational(1, 64)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_3_0'), Integer(2)), Symbol('x_3_0'), Pow(Symbol('x_3_1'), Integer(2)), Symbol('x_3_1'), Rational(-1, 2)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_4_0'), Integer(2)), Symbol('x_4_0'), Pow(Symbol('x_4_1'), Integer(2)), Symbol('x_4_1'), Rational(-1, 2)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_5_0'), Integer(2)), Symbol('x_5_0'), Pow(Symbol('x_5_1'), Integer(2)), Symbol('x_5_1'), Rational(-1, 2)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Mul(Integer(-1), Pow(Symbol('x_3_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_3_1'), Integer(2))), Integer(1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Mul(Integer(-1), Pow(Symbol('x_4_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_4_1'), Integer(2))), Integer(1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Mul(Integer(-1), Pow(Symbol('x_5_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_5_1'), Integer(2))), Integer(1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_3_0'), Integer(2)), Mul(Integer(-1), Rational(1, 4), Symbol('x_3_0')), Pow(Symbol('x_3_1'), Integer(2)), Mul(Integer(-1), Symbol('x_3_1')), Rational(-47, 64)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_4_0'), Integer(2)), Mul(Integer(-1), Rational(1, 4), Symbol('x_4_0')), Pow(Symbol('x_4_1'), Integer(2)), Mul(Integer(-1), Symbol('x_4_1')), Rational(-47, 64)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_5_0'), Integer(2)), Mul(Integer(-1), Rational(1, 4), Symbol('x_5_0')), Pow(Symbol('x_5_1'), Integer(2)), Mul(Integer(-1), Symbol('x_5_1')), Rational(-47, 64)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_2_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_2_1'), Symbol('x_3_1')), Pow(Symbol('x_3_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_3_0')), Pow(Symbol('x_3_1'), Integer(2))), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_2_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_2_1'), Symbol('x_4_1')), Pow(Symbol('x_4_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_4_0')), Pow(Symbol('x_4_1'), Integer(2))), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_2_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_2_1'), Symbol('x_5_1')), Pow(Symbol('x_5_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_5_0')), Pow(Symbol('x_5_1'), Integer(2))), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_3_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_3_0'), Symbol('x_4_0')), Pow(Symbol('x_3_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_3_1'), Symbol('x_4_1')), Pow(Symbol('x_4_0'), Integer(2)), Pow(Symbol('x_4_1'), Integer(2)), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_3_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_3_0'), Symbol('x_5_0')), Pow(Symbol('x_3_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_3_1'), Symbol('x_5_1')), Pow(Symbol('x_5_0'), Integer(2)), Pow(Symbol('x_5_1'), Integer(2)), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_4_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_4_0'), Symbol('x_5_0')), Pow(Symbol('x_4_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_4_1'), Symbol('x_5_1')), Pow(Symbol('x_5_0'), Integer(2)), Pow(Symbol('x_5_1'), Integer(2)), Integer(-1)), Integer(0)))

	eval = pre_cond.subs( { 'd':d, 'x_5_0':x_5_0, 'x_5_1':x_5_1 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_5(d:sympy.Rational,x_5_0:sympy.Rational,x_5_1:sympy.Rational):
	#(d > 1) & (d + x_3_0**2 + x_3_0 + x_3_1**2 + x_3_1 - 1/2 > 0) & (d + x_4_0**2 + x_4_0 + x_4_1**2 + x_4_1 - 1/2 > 0) & (d + x_5_0**2 + x_5_0 + x_5_1**2 + x_5_1 - 1/2 > 0) & (d - x_3_0**2 - x_3_1**2 + 1 > 0) & (d - x_4_0**2 - x_4_1**2 + 1 > 0) & (d - x_5_0**2 - x_5_1**2 + 1 > 0) & (d + x_3_0**2 - 2*x_3_0 + x_3_1**2 + 2*x_3_1 + 1 > 0) & (d + x_3_0**2 - x_3_0/4 + x_3_1**2 - x_3_1 - 47/64 > 0) & (d + x_4_0**2 - 2*x_4_0 + x_4_1**2 + 2*x_4_1 + 1 > 0) & (d + x_4_0**2 - x_4_0/4 + x_4_1**2 - x_4_1 - 47/64 > 0) & (d + x_5_0**2 - 2*x_5_0 + x_5_1**2 + 2*x_5_1 + 1 > 0) & (d + x_5_0**2 - x_5_0/4 + x_5_1**2 - x_5_1 - 47/64 > 0) & (d + x_3_0**2 - 2*x_3_0*x_4_0 + x_3_1**2 - 2*x_3_1*x_4_1 + x_4_0**2 + x_4_1**2 - 1 > 0) & (d + x_3_0**2 - 2*x_3_0*x_5_0 + x_3_1**2 - 2*x_3_1*x_5_1 + x_5_0**2 + x_5_1**2 - 1 > 0) & (d + x_4_0**2 - 2*x_4_0*x_5_0 + x_4_1**2 - 2*x_4_1*x_5_1 + x_5_0**2 + x_5_1**2 - 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('d'), Integer(1)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_3_0'), Integer(2)), Symbol('x_3_0'), Pow(Symbol('x_3_1'), Integer(2)), Symbol('x_3_1'), Rational(-1, 2)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_4_0'), Integer(2)), Symbol('x_4_0'), Pow(Symbol('x_4_1'), Integer(2)), Symbol('x_4_1'), Rational(-1, 2)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_5_0'), Integer(2)), Symbol('x_5_0'), Pow(Symbol('x_5_1'), Integer(2)), Symbol('x_5_1'), Rational(-1, 2)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Mul(Integer(-1), Pow(Symbol('x_3_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_3_1'), Integer(2))), Integer(1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Mul(Integer(-1), Pow(Symbol('x_4_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_4_1'), Integer(2))), Integer(1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Mul(Integer(-1), Pow(Symbol('x_5_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_5_1'), Integer(2))), Integer(1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_3_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_3_0')), Pow(Symbol('x_3_1'), Integer(2)), Mul(Integer(2), Symbol('x_3_1')), Integer(1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_3_0'), Integer(2)), Mul(Integer(-1), Rational(1, 4), Symbol('x_3_0')), Pow(Symbol('x_3_1'), Integer(2)), Mul(Integer(-1), Symbol('x_3_1')), Rational(-47, 64)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_4_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_4_0')), Pow(Symbol('x_4_1'), Integer(2)), Mul(Integer(2), Symbol('x_4_1')), Integer(1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_4_0'), Integer(2)), Mul(Integer(-1), Rational(1, 4), Symbol('x_4_0')), Pow(Symbol('x_4_1'), Integer(2)), Mul(Integer(-1), Symbol('x_4_1')), Rational(-47, 64)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_5_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_5_0')), Pow(Symbol('x_5_1'), Integer(2)), Mul(Integer(2), Symbol('x_5_1')), Integer(1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_5_0'), Integer(2)), Mul(Integer(-1), Rational(1, 4), Symbol('x_5_0')), Pow(Symbol('x_5_1'), Integer(2)), Mul(Integer(-1), Symbol('x_5_1')), Rational(-47, 64)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_3_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_3_0'), Symbol('x_4_0')), Pow(Symbol('x_3_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_3_1'), Symbol('x_4_1')), Pow(Symbol('x_4_0'), Integer(2)), Pow(Symbol('x_4_1'), Integer(2)), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_3_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_3_0'), Symbol('x_5_0')), Pow(Symbol('x_3_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_3_1'), Symbol('x_5_1')), Pow(Symbol('x_5_0'), Integer(2)), Pow(Symbol('x_5_1'), Integer(2)), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_4_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_4_0'), Symbol('x_5_0')), Pow(Symbol('x_4_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_4_1'), Symbol('x_5_1')), Pow(Symbol('x_5_0'), Integer(2)), Pow(Symbol('x_5_1'), Integer(2)), Integer(-1)), Integer(0)))

	eval = pre_cond.subs( { 'd':d, 'x_5_0':x_5_0, 'x_5_1':x_5_1 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_6(d:sympy.Rational,x_5_0:sympy.Rational,x_5_1:sympy.Rational):
	#(d > 1) & (d + x_3_1**2 + x_3_1 + 1/4 > 0) & (d - x_3_1**2 + 3/4 > 0) & (d + x_3_1**2 - x_3_1 - 39/64 > 0) & (d + x_3_1**2 + 2*x_3_1 + 1/4 > 0) & (d + x_4_0**2 + x_4_0 + x_4_1**2 + x_4_1 - 1/2 > 0) & (d + x_5_0**2 + x_5_0 + x_5_1**2 + x_5_1 - 1/2 > 0) & (d - x_4_0**2 - x_4_1**2 + 1 > 0) & (d - x_5_0**2 - x_5_1**2 + 1 > 0) & (d + x_4_0**2 - 2*x_4_0 + x_4_1**2 + 2*x_4_1 + 1 > 0) & (d + x_4_0**2 - x_4_0/4 + x_4_1**2 - x_4_1 - 47/64 > 0) & (d + x_5_0**2 - 2*x_5_0 + x_5_1**2 + 2*x_5_1 + 1 > 0) & (d + x_5_0**2 - x_5_0/4 + x_5_1**2 - x_5_1 - 47/64 > 0) & (d + x_3_1**2 - 2*x_3_1*x_4_1 + x_4_0**2 - x_4_0 + x_4_1**2 - 3/4 > 0) & (d + x_3_1**2 - 2*x_3_1*x_5_1 + x_5_0**2 - x_5_0 + x_5_1**2 - 3/4 > 0) & (d + x_4_0**2 - 2*x_4_0*x_5_0 + x_4_1**2 - 2*x_4_1*x_5_1 + x_5_0**2 + x_5_1**2 - 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('d'), Integer(1)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_3_1'), Integer(2)), Symbol('x_3_1'), Rational(1, 4)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Mul(Integer(-1), Pow(Symbol('x_3_1'), Integer(2))), Rational(3, 4)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_3_1'), Integer(2)), Mul(Integer(-1), Symbol('x_3_1')), Rational(-39, 64)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_3_1'), Integer(2)), Mul(Integer(2), Symbol('x_3_1')), Rational(1, 4)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_4_0'), Integer(2)), Symbol('x_4_0'), Pow(Symbol('x_4_1'), Integer(2)), Symbol('x_4_1'), Rational(-1, 2)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_5_0'), Integer(2)), Symbol('x_5_0'), Pow(Symbol('x_5_1'), Integer(2)), Symbol('x_5_1'), Rational(-1, 2)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Mul(Integer(-1), Pow(Symbol('x_4_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_4_1'), Integer(2))), Integer(1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Mul(Integer(-1), Pow(Symbol('x_5_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_5_1'), Integer(2))), Integer(1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_4_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_4_0')), Pow(Symbol('x_4_1'), Integer(2)), Mul(Integer(2), Symbol('x_4_1')), Integer(1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_4_0'), Integer(2)), Mul(Integer(-1), Rational(1, 4), Symbol('x_4_0')), Pow(Symbol('x_4_1'), Integer(2)), Mul(Integer(-1), Symbol('x_4_1')), Rational(-47, 64)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_5_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_5_0')), Pow(Symbol('x_5_1'), Integer(2)), Mul(Integer(2), Symbol('x_5_1')), Integer(1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_5_0'), Integer(2)), Mul(Integer(-1), Rational(1, 4), Symbol('x_5_0')), Pow(Symbol('x_5_1'), Integer(2)), Mul(Integer(-1), Symbol('x_5_1')), Rational(-47, 64)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_3_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_3_1'), Symbol('x_4_1')), Pow(Symbol('x_4_0'), Integer(2)), Mul(Integer(-1), Symbol('x_4_0')), Pow(Symbol('x_4_1'), Integer(2)), Rational(-3, 4)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_3_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_3_1'), Symbol('x_5_1')), Pow(Symbol('x_5_0'), Integer(2)), Mul(Integer(-1), Symbol('x_5_0')), Pow(Symbol('x_5_1'), Integer(2)), Rational(-3, 4)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_4_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_4_0'), Symbol('x_5_0')), Pow(Symbol('x_4_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_4_1'), Symbol('x_5_1')), Pow(Symbol('x_5_0'), Integer(2)), Pow(Symbol('x_5_1'), Integer(2)), Integer(-1)), Integer(0)))

	eval = pre_cond.subs( { 'd':d, 'x_5_0':x_5_0, 'x_5_1':x_5_1 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_7(d:sympy.Rational,x_5_0:sympy.Rational,x_5_1:sympy.Rational):
	#(d > 1) & (d + x_4_0**2 + x_4_0 + x_4_1**2 + x_4_1 - 1/2 > 0) & (d + x_5_0**2 + x_5_0 + x_5_1**2 + x_5_1 - 1/2 > 0) & (d - x_4_0**2 - x_4_1**2 + 1 > 0) & (d - x_5_0**2 - x_5_1**2 + 1 > 0) & (d + x_4_0**2 - x_4_0 + x_4_1**2 + x_4_1 - 1/2 > 0) & (d + x_5_0**2 - x_5_0 + x_5_1**2 + x_5_1 - 1/2 > 0) & (d + x_4_0**2 - 2*x_4_0 + x_4_1**2 + 2*x_4_1 + 1 > 0) & (d + x_4_0**2 - x_4_0/4 + x_4_1**2 - x_4_1 - 47/64 > 0) & (d + x_5_0**2 - 2*x_5_0 + x_5_1**2 + 2*x_5_1 + 1 > 0) & (d + x_5_0**2 - x_5_0/4 + x_5_1**2 - x_5_1 - 47/64 > 0) & (d + x_4_0**2 - 2*x_4_0*x_5_0 + x_4_1**2 - 2*x_4_1*x_5_1 + x_5_0**2 + x_5_1**2 - 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('d'), Integer(1)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_4_0'), Integer(2)), Symbol('x_4_0'), Pow(Symbol('x_4_1'), Integer(2)), Symbol('x_4_1'), Rational(-1, 2)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_5_0'), Integer(2)), Symbol('x_5_0'), Pow(Symbol('x_5_1'), Integer(2)), Symbol('x_5_1'), Rational(-1, 2)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Mul(Integer(-1), Pow(Symbol('x_4_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_4_1'), Integer(2))), Integer(1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Mul(Integer(-1), Pow(Symbol('x_5_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_5_1'), Integer(2))), Integer(1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_4_0'), Integer(2)), Mul(Integer(-1), Symbol('x_4_0')), Pow(Symbol('x_4_1'), Integer(2)), Symbol('x_4_1'), Rational(-1, 2)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_5_0'), Integer(2)), Mul(Integer(-1), Symbol('x_5_0')), Pow(Symbol('x_5_1'), Integer(2)), Symbol('x_5_1'), Rational(-1, 2)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_4_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_4_0')), Pow(Symbol('x_4_1'), Integer(2)), Mul(Integer(2), Symbol('x_4_1')), Integer(1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_4_0'), Integer(2)), Mul(Integer(-1), Rational(1, 4), Symbol('x_4_0')), Pow(Symbol('x_4_1'), Integer(2)), Mul(Integer(-1), Symbol('x_4_1')), Rational(-47, 64)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_5_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_5_0')), Pow(Symbol('x_5_1'), Integer(2)), Mul(Integer(2), Symbol('x_5_1')), Integer(1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_5_0'), Integer(2)), Mul(Integer(-1), Rational(1, 4), Symbol('x_5_0')), Pow(Symbol('x_5_1'), Integer(2)), Mul(Integer(-1), Symbol('x_5_1')), Rational(-47, 64)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_4_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_4_0'), Symbol('x_5_0')), Pow(Symbol('x_4_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_4_1'), Symbol('x_5_1')), Pow(Symbol('x_5_0'), Integer(2)), Pow(Symbol('x_5_1'), Integer(2)), Integer(-1)), Integer(0)))

	eval = pre_cond.subs( { 'd':d, 'x_5_0':x_5_0, 'x_5_1':x_5_1 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_8(d:sympy.Rational,x_5_0:sympy.Rational,x_5_1:sympy.Rational):
	#(d > 1) & (d + x_4_1**2 + x_4_1 - 3/4 > 0) & (d - x_4_1**2 + 3/4 > 0) & (d + x_4_1**2 - x_4_1 - 23/64 > 0) & (d + x_4_1**2 + 2*x_4_1 + 9/4 > 0) & (d + x_5_0**2 + x_5_0 + x_5_1**2 + x_5_1 - 1/2 > 0) & (d - x_5_0**2 - x_5_1**2 + 1 > 0) & (d + x_5_0**2 - x_5_0 + x_5_1**2 + x_5_1 - 1/2 > 0) & (d + x_5_0**2 - 2*x_5_0 + x_5_1**2 + 2*x_5_1 + 1 > 0) & (d + x_5_0**2 - x_5_0/4 + x_5_1**2 - x_5_1 - 47/64 > 0) & (d + x_4_1**2 - 2*x_4_1*x_5_1 + x_5_0**2 + x_5_0 + x_5_1**2 - 3/4 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('d'), Integer(1)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_4_1'), Integer(2)), Symbol('x_4_1'), Rational(-3, 4)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Mul(Integer(-1), Pow(Symbol('x_4_1'), Integer(2))), Rational(3, 4)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_4_1'), Integer(2)), Mul(Integer(-1), Symbol('x_4_1')), Rational(-23, 64)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_4_1'), Integer(2)), Mul(Integer(2), Symbol('x_4_1')), Rational(9, 4)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_5_0'), Integer(2)), Symbol('x_5_0'), Pow(Symbol('x_5_1'), Integer(2)), Symbol('x_5_1'), Rational(-1, 2)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Mul(Integer(-1), Pow(Symbol('x_5_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_5_1'), Integer(2))), Integer(1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_5_0'), Integer(2)), Mul(Integer(-1), Symbol('x_5_0')), Pow(Symbol('x_5_1'), Integer(2)), Symbol('x_5_1'), Rational(-1, 2)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_5_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_5_0')), Pow(Symbol('x_5_1'), Integer(2)), Mul(Integer(2), Symbol('x_5_1')), Integer(1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_5_0'), Integer(2)), Mul(Integer(-1), Rational(1, 4), Symbol('x_5_0')), Pow(Symbol('x_5_1'), Integer(2)), Mul(Integer(-1), Symbol('x_5_1')), Rational(-47, 64)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_4_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_4_1'), Symbol('x_5_1')), Pow(Symbol('x_5_0'), Integer(2)), Symbol('x_5_0'), Pow(Symbol('x_5_1'), Integer(2)), Rational(-3, 4)), Integer(0)))

	eval = pre_cond.subs( { 'd':d, 'x_5_0':x_5_0, 'x_5_1':x_5_1 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_9(d:sympy.Rational,x_5_0:sympy.Rational,x_5_1:sympy.Rational):
	#(d > 1) & (d + x_5_0**2 + x_5_0 + x_5_1**2 + x_5_1 - 1/2 > 0) & (d - x_5_0**2 - x_5_1**2 + 1 > 0) & (d + x_5_0**2 - x_5_0 + x_5_1**2 + x_5_1 - 1/2 > 0) & (d + x_5_0**2 + x_5_0 + x_5_1**2 + 2*x_5_1 + 1/4 > 0) & (d + x_5_0**2 - 2*x_5_0 + x_5_1**2 + 2*x_5_1 + 1 > 0) & (d + x_5_0**2 - x_5_0/4 + x_5_1**2 - x_5_1 - 47/64 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('d'), Integer(1)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_5_0'), Integer(2)), Symbol('x_5_0'), Pow(Symbol('x_5_1'), Integer(2)), Symbol('x_5_1'), Rational(-1, 2)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Mul(Integer(-1), Pow(Symbol('x_5_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_5_1'), Integer(2))), Integer(1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_5_0'), Integer(2)), Mul(Integer(-1), Symbol('x_5_0')), Pow(Symbol('x_5_1'), Integer(2)), Symbol('x_5_1'), Rational(-1, 2)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_5_0'), Integer(2)), Symbol('x_5_0'), Pow(Symbol('x_5_1'), Integer(2)), Mul(Integer(2), Symbol('x_5_1')), Rational(1, 4)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_5_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_5_0')), Pow(Symbol('x_5_1'), Integer(2)), Mul(Integer(2), Symbol('x_5_1')), Integer(1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_5_0'), Integer(2)), Mul(Integer(-1), Rational(1, 4), Symbol('x_5_0')), Pow(Symbol('x_5_1'), Integer(2)), Mul(Integer(-1), Symbol('x_5_1')), Rational(-47, 64)), Integer(0)))

	eval = pre_cond.subs( { 'd':d, 'x_5_0':x_5_0, 'x_5_1':x_5_1 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_10(d:sympy.Rational,x_5_0:sympy.Rational,x_5_1:sympy.Rational):
	#(d > 0) & (d - x_0_1**2 + 1 > 0) & (d - x_1_0**2 - x_1_1**2 + 1 > 0) & (d - x_2_0**2 - x_2_1**2 + 1 > 0) & (d - x_3_0**2 - x_3_1**2 + 1 > 0) & (d - x_4_0**2 - x_4_1**2 + 1 > 0) & (d - x_5_0**2 - x_5_1**2 + 1 > 0) & (d + x_0_1**2 - 2*x_0_1*x_1_1 + x_1_0**2 + x_1_1**2 - 1 > 0) & (d + x_0_1**2 - 2*x_0_1*x_2_1 + x_2_0**2 + x_2_1**2 - 1 > 0) & (d + x_0_1**2 - 2*x_0_1*x_3_1 + x_3_0**2 + x_3_1**2 - 1 > 0) & (d + x_0_1**2 - 2*x_0_1*x_4_1 + x_4_0**2 + x_4_1**2 - 1 > 0) & (d + x_0_1**2 - 2*x_0_1*x_5_1 + x_5_0**2 + x_5_1**2 - 1 > 0) & (d + x_1_0**2 - 2*x_1_0*x_2_0 + x_1_1**2 - 2*x_1_1*x_2_1 + x_2_0**2 + x_2_1**2 - 1 > 0) & (d + x_1_0**2 - 2*x_1_0*x_3_0 + x_1_1**2 - 2*x_1_1*x_3_1 + x_3_0**2 + x_3_1**2 - 1 > 0) & (d + x_1_0**2 - 2*x_1_0*x_4_0 + x_1_1**2 - 2*x_1_1*x_4_1 + x_4_0**2 + x_4_1**2 - 1 > 0) & (d + x_1_0**2 - 2*x_1_0*x_5_0 + x_1_1**2 - 2*x_1_1*x_5_1 + x_5_0**2 + x_5_1**2 - 1 > 0) & (d + x_2_0**2 - 2*x_2_0*x_3_0 + x_2_1**2 - 2*x_2_1*x_3_1 + x_3_0**2 + x_3_1**2 - 1 > 0) & (d + x_2_0**2 - 2*x_2_0*x_4_0 + x_2_1**2 - 2*x_2_1*x_4_1 + x_4_0**2 + x_4_1**2 - 1 > 0) & (d + x_2_0**2 - 2*x_2_0*x_5_0 + x_2_1**2 - 2*x_2_1*x_5_1 + x_5_0**2 + x_5_1**2 - 1 > 0) & (d + x_3_0**2 - 2*x_3_0*x_4_0 + x_3_1**2 - 2*x_3_1*x_4_1 + x_4_0**2 + x_4_1**2 - 1 > 0) & (d + x_3_0**2 - 2*x_3_0*x_5_0 + x_3_1**2 - 2*x_3_1*x_5_1 + x_5_0**2 + x_5_1**2 - 1 > 0) & (d + x_4_0**2 - 2*x_4_0*x_5_0 + x_4_1**2 - 2*x_4_1*x_5_1 + x_5_0**2 + x_5_1**2 - 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('d'), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Mul(Integer(-1), Pow(Symbol('x_0_1'), Integer(2))), Integer(1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Mul(Integer(-1), Pow(Symbol('x_1_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_1_1'), Integer(2))), Integer(1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Mul(Integer(-1), Pow(Symbol('x_2_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_2_1'), Integer(2))), Integer(1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Mul(Integer(-1), Pow(Symbol('x_3_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_3_1'), Integer(2))), Integer(1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Mul(Integer(-1), Pow(Symbol('x_4_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_4_1'), Integer(2))), Integer(1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Mul(Integer(-1), Pow(Symbol('x_5_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_5_1'), Integer(2))), Integer(1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_0_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_0_1'), Symbol('x_1_1')), Pow(Symbol('x_1_0'), Integer(2)), Pow(Symbol('x_1_1'), Integer(2)), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_0_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_0_1'), Symbol('x_2_1')), Pow(Symbol('x_2_0'), Integer(2)), Pow(Symbol('x_2_1'), Integer(2)), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_0_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_0_1'), Symbol('x_3_1')), Pow(Symbol('x_3_0'), Integer(2)), Pow(Symbol('x_3_1'), Integer(2)), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_0_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_0_1'), Symbol('x_4_1')), Pow(Symbol('x_4_0'), Integer(2)), Pow(Symbol('x_4_1'), Integer(2)), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_0_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_0_1'), Symbol('x_5_1')), Pow(Symbol('x_5_0'), Integer(2)), Pow(Symbol('x_5_1'), Integer(2)), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_1_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_1_0'), Symbol('x_2_0')), Pow(Symbol('x_1_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_1_1'), Symbol('x_2_1')), Pow(Symbol('x_2_0'), Integer(2)), Pow(Symbol('x_2_1'), Integer(2)), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_1_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_1_0'), Symbol('x_3_0')), Pow(Symbol('x_1_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_1_1'), Symbol('x_3_1')), Pow(Symbol('x_3_0'), Integer(2)), Pow(Symbol('x_3_1'), Integer(2)), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_1_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_1_0'), Symbol('x_4_0')), Pow(Symbol('x_1_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_1_1'), Symbol('x_4_1')), Pow(Symbol('x_4_0'), Integer(2)), Pow(Symbol('x_4_1'), Integer(2)), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_1_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_1_0'), Symbol('x_5_0')), Pow(Symbol('x_1_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_1_1'), Symbol('x_5_1')), Pow(Symbol('x_5_0'), Integer(2)), Pow(Symbol('x_5_1'), Integer(2)), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_2_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_2_0'), Symbol('x_3_0')), Pow(Symbol('x_2_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_2_1'), Symbol('x_3_1')), Pow(Symbol('x_3_0'), Integer(2)), Pow(Symbol('x_3_1'), Integer(2)), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_2_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_2_0'), Symbol('x_4_0')), Pow(Symbol('x_2_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_2_1'), Symbol('x_4_1')), Pow(Symbol('x_4_0'), Integer(2)), Pow(Symbol('x_4_1'), Integer(2)), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_2_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_2_0'), Symbol('x_5_0')), Pow(Symbol('x_2_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_2_1'), Symbol('x_5_1')), Pow(Symbol('x_5_0'), Integer(2)), Pow(Symbol('x_5_1'), Integer(2)), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_3_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_3_0'), Symbol('x_4_0')), Pow(Symbol('x_3_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_3_1'), Symbol('x_4_1')), Pow(Symbol('x_4_0'), Integer(2)), Pow(Symbol('x_4_1'), Integer(2)), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_3_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_3_0'), Symbol('x_5_0')), Pow(Symbol('x_3_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_3_1'), Symbol('x_5_1')), Pow(Symbol('x_5_0'), Integer(2)), Pow(Symbol('x_5_1'), Integer(2)), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_4_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_4_0'), Symbol('x_5_0')), Pow(Symbol('x_4_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_4_1'), Symbol('x_5_1')), Pow(Symbol('x_5_0'), Integer(2)), Pow(Symbol('x_5_1'), Integer(2)), Integer(-1)), Integer(0)))

	eval = pre_cond.subs( { 'd':d, 'x_5_0':x_5_0, 'x_5_1':x_5_1 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_11(d:sympy.Rational,x_5_0:sympy.Rational,x_5_1:sympy.Rational):
	#(d > 9/16) & (d + x_1_0**2 + x_1_1**2 - 5*x_1_1/2 + 9/16 > 0) & (d + x_2_0**2 + x_2_1**2 - 5*x_2_1/2 + 9/16 > 0) & (d + x_3_0**2 + x_3_1**2 - 5*x_3_1/2 + 9/16 > 0) & (d + x_4_0**2 + x_4_1**2 - 5*x_4_1/2 + 9/16 > 0) & (d + x_5_0**2 + x_5_1**2 - 5*x_5_1/2 + 9/16 > 0) & (d - x_1_0**2 - x_1_1**2 + 1 > 0) & (d - x_2_0**2 - x_2_1**2 + 1 > 0) & (d - x_3_0**2 - x_3_1**2 + 1 > 0) & (d - x_4_0**2 - x_4_1**2 + 1 > 0) & (d - x_5_0**2 - x_5_1**2 + 1 > 0) & (d + x_1_0**2 - 2*x_1_0*x_2_0 + x_1_1**2 - 2*x_1_1*x_2_1 + x_2_0**2 + x_2_1**2 - 1 > 0) & (d + x_1_0**2 - 2*x_1_0*x_3_0 + x_1_1**2 - 2*x_1_1*x_3_1 + x_3_0**2 + x_3_1**2 - 1 > 0) & (d + x_1_0**2 - 2*x_1_0*x_4_0 + x_1_1**2 - 2*x_1_1*x_4_1 + x_4_0**2 + x_4_1**2 - 1 > 0) & (d + x_1_0**2 - 2*x_1_0*x_5_0 + x_1_1**2 - 2*x_1_1*x_5_1 + x_5_0**2 + x_5_1**2 - 1 > 0) & (d + x_2_0**2 - 2*x_2_0*x_3_0 + x_2_1**2 - 2*x_2_1*x_3_1 + x_3_0**2 + x_3_1**2 - 1 > 0) & (d + x_2_0**2 - 2*x_2_0*x_4_0 + x_2_1**2 - 2*x_2_1*x_4_1 + x_4_0**2 + x_4_1**2 - 1 > 0) & (d + x_2_0**2 - 2*x_2_0*x_5_0 + x_2_1**2 - 2*x_2_1*x_5_1 + x_5_0**2 + x_5_1**2 - 1 > 0) & (d + x_3_0**2 - 2*x_3_0*x_4_0 + x_3_1**2 - 2*x_3_1*x_4_1 + x_4_0**2 + x_4_1**2 - 1 > 0) & (d + x_3_0**2 - 2*x_3_0*x_5_0 + x_3_1**2 - 2*x_3_1*x_5_1 + x_5_0**2 + x_5_1**2 - 1 > 0) & (d + x_4_0**2 - 2*x_4_0*x_5_0 + x_4_1**2 - 2*x_4_1*x_5_1 + x_5_0**2 + x_5_1**2 - 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('d'), Rational(9, 16)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_1_0'), Integer(2)), Pow(Symbol('x_1_1'), Integer(2)), Mul(Integer(-1), Rational(5, 2), Symbol('x_1_1')), Rational(9, 16)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_2_0'), Integer(2)), Pow(Symbol('x_2_1'), Integer(2)), Mul(Integer(-1), Rational(5, 2), Symbol('x_2_1')), Rational(9, 16)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_3_0'), Integer(2)), Pow(Symbol('x_3_1'), Integer(2)), Mul(Integer(-1), Rational(5, 2), Symbol('x_3_1')), Rational(9, 16)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_4_0'), Integer(2)), Pow(Symbol('x_4_1'), Integer(2)), Mul(Integer(-1), Rational(5, 2), Symbol('x_4_1')), Rational(9, 16)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_5_0'), Integer(2)), Pow(Symbol('x_5_1'), Integer(2)), Mul(Integer(-1), Rational(5, 2), Symbol('x_5_1')), Rational(9, 16)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Mul(Integer(-1), Pow(Symbol('x_1_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_1_1'), Integer(2))), Integer(1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Mul(Integer(-1), Pow(Symbol('x_2_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_2_1'), Integer(2))), Integer(1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Mul(Integer(-1), Pow(Symbol('x_3_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_3_1'), Integer(2))), Integer(1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Mul(Integer(-1), Pow(Symbol('x_4_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_4_1'), Integer(2))), Integer(1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Mul(Integer(-1), Pow(Symbol('x_5_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_5_1'), Integer(2))), Integer(1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_1_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_1_0'), Symbol('x_2_0')), Pow(Symbol('x_1_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_1_1'), Symbol('x_2_1')), Pow(Symbol('x_2_0'), Integer(2)), Pow(Symbol('x_2_1'), Integer(2)), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_1_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_1_0'), Symbol('x_3_0')), Pow(Symbol('x_1_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_1_1'), Symbol('x_3_1')), Pow(Symbol('x_3_0'), Integer(2)), Pow(Symbol('x_3_1'), Integer(2)), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_1_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_1_0'), Symbol('x_4_0')), Pow(Symbol('x_1_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_1_1'), Symbol('x_4_1')), Pow(Symbol('x_4_0'), Integer(2)), Pow(Symbol('x_4_1'), Integer(2)), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_1_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_1_0'), Symbol('x_5_0')), Pow(Symbol('x_1_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_1_1'), Symbol('x_5_1')), Pow(Symbol('x_5_0'), Integer(2)), Pow(Symbol('x_5_1'), Integer(2)), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_2_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_2_0'), Symbol('x_3_0')), Pow(Symbol('x_2_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_2_1'), Symbol('x_3_1')), Pow(Symbol('x_3_0'), Integer(2)), Pow(Symbol('x_3_1'), Integer(2)), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_2_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_2_0'), Symbol('x_4_0')), Pow(Symbol('x_2_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_2_1'), Symbol('x_4_1')), Pow(Symbol('x_4_0'), Integer(2)), Pow(Symbol('x_4_1'), Integer(2)), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_2_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_2_0'), Symbol('x_5_0')), Pow(Symbol('x_2_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_2_1'), Symbol('x_5_1')), Pow(Symbol('x_5_0'), Integer(2)), Pow(Symbol('x_5_1'), Integer(2)), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_3_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_3_0'), Symbol('x_4_0')), Pow(Symbol('x_3_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_3_1'), Symbol('x_4_1')), Pow(Symbol('x_4_0'), Integer(2)), Pow(Symbol('x_4_1'), Integer(2)), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_3_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_3_0'), Symbol('x_5_0')), Pow(Symbol('x_3_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_3_1'), Symbol('x_5_1')), Pow(Symbol('x_5_0'), Integer(2)), Pow(Symbol('x_5_1'), Integer(2)), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_4_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_4_0'), Symbol('x_5_0')), Pow(Symbol('x_4_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_4_1'), Symbol('x_5_1')), Pow(Symbol('x_5_0'), Integer(2)), Pow(Symbol('x_5_1'), Integer(2)), Integer(-1)), Integer(0)))

	eval = pre_cond.subs( { 'd':d, 'x_5_0':x_5_0, 'x_5_1':x_5_1 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_12(d:sympy.Rational,x_5_0:sympy.Rational,x_5_1:sympy.Rational):
	#(d > 9/16) & (d - x_1_1**2 > 0) & (d + x_1_1**2 - 5*x_1_1/2 + 25/16 > 0) & (d + x_2_0**2 + x_2_1**2 - 5*x_2_1/2 + 9/16 > 0) & (d + x_3_0**2 + x_3_1**2 - 5*x_3_1/2 + 9/16 > 0) & (d + x_4_0**2 + x_4_1**2 - 5*x_4_1/2 + 9/16 > 0) & (d + x_5_0**2 + x_5_1**2 - 5*x_5_1/2 + 9/16 > 0) & (d - x_2_0**2 - x_2_1**2 + 1 > 0) & (d - x_3_0**2 - x_3_1**2 + 1 > 0) & (d - x_4_0**2 - x_4_1**2 + 1 > 0) & (d - x_5_0**2 - x_5_1**2 + 1 > 0) & (d + x_1_1**2 - 2*x_1_1*x_2_1 + x_2_0**2 + 2*x_2_0 + x_2_1**2 > 0) & (d + x_1_1**2 - 2*x_1_1*x_3_1 + x_3_0**2 + 2*x_3_0 + x_3_1**2 > 0) & (d + x_1_1**2 - 2*x_1_1*x_4_1 + x_4_0**2 + 2*x_4_0 + x_4_1**2 > 0) & (d + x_1_1**2 - 2*x_1_1*x_5_1 + x_5_0**2 + 2*x_5_0 + x_5_1**2 > 0) & (d + x_2_0**2 - 2*x_2_0*x_3_0 + x_2_1**2 - 2*x_2_1*x_3_1 + x_3_0**2 + x_3_1**2 - 1 > 0) & (d + x_2_0**2 - 2*x_2_0*x_4_0 + x_2_1**2 - 2*x_2_1*x_4_1 + x_4_0**2 + x_4_1**2 - 1 > 0) & (d + x_2_0**2 - 2*x_2_0*x_5_0 + x_2_1**2 - 2*x_2_1*x_5_1 + x_5_0**2 + x_5_1**2 - 1 > 0) & (d + x_3_0**2 - 2*x_3_0*x_4_0 + x_3_1**2 - 2*x_3_1*x_4_1 + x_4_0**2 + x_4_1**2 - 1 > 0) & (d + x_3_0**2 - 2*x_3_0*x_5_0 + x_3_1**2 - 2*x_3_1*x_5_1 + x_5_0**2 + x_5_1**2 - 1 > 0) & (d + x_4_0**2 - 2*x_4_0*x_5_0 + x_4_1**2 - 2*x_4_1*x_5_1 + x_5_0**2 + x_5_1**2 - 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('d'), Rational(9, 16)), StrictGreaterThan(Add(Symbol('d'), Mul(Integer(-1), Pow(Symbol('x_1_1'), Integer(2)))), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_1_1'), Integer(2)), Mul(Integer(-1), Rational(5, 2), Symbol('x_1_1')), Rational(25, 16)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_2_0'), Integer(2)), Pow(Symbol('x_2_1'), Integer(2)), Mul(Integer(-1), Rational(5, 2), Symbol('x_2_1')), Rational(9, 16)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_3_0'), Integer(2)), Pow(Symbol('x_3_1'), Integer(2)), Mul(Integer(-1), Rational(5, 2), Symbol('x_3_1')), Rational(9, 16)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_4_0'), Integer(2)), Pow(Symbol('x_4_1'), Integer(2)), Mul(Integer(-1), Rational(5, 2), Symbol('x_4_1')), Rational(9, 16)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_5_0'), Integer(2)), Pow(Symbol('x_5_1'), Integer(2)), Mul(Integer(-1), Rational(5, 2), Symbol('x_5_1')), Rational(9, 16)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Mul(Integer(-1), Pow(Symbol('x_2_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_2_1'), Integer(2))), Integer(1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Mul(Integer(-1), Pow(Symbol('x_3_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_3_1'), Integer(2))), Integer(1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Mul(Integer(-1), Pow(Symbol('x_4_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_4_1'), Integer(2))), Integer(1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Mul(Integer(-1), Pow(Symbol('x_5_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_5_1'), Integer(2))), Integer(1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_1_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_1_1'), Symbol('x_2_1')), Pow(Symbol('x_2_0'), Integer(2)), Mul(Integer(2), Symbol('x_2_0')), Pow(Symbol('x_2_1'), Integer(2))), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_1_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_1_1'), Symbol('x_3_1')), Pow(Symbol('x_3_0'), Integer(2)), Mul(Integer(2), Symbol('x_3_0')), Pow(Symbol('x_3_1'), Integer(2))), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_1_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_1_1'), Symbol('x_4_1')), Pow(Symbol('x_4_0'), Integer(2)), Mul(Integer(2), Symbol('x_4_0')), Pow(Symbol('x_4_1'), Integer(2))), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_1_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_1_1'), Symbol('x_5_1')), Pow(Symbol('x_5_0'), Integer(2)), Mul(Integer(2), Symbol('x_5_0')), Pow(Symbol('x_5_1'), Integer(2))), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_2_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_2_0'), Symbol('x_3_0')), Pow(Symbol('x_2_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_2_1'), Symbol('x_3_1')), Pow(Symbol('x_3_0'), Integer(2)), Pow(Symbol('x_3_1'), Integer(2)), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_2_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_2_0'), Symbol('x_4_0')), Pow(Symbol('x_2_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_2_1'), Symbol('x_4_1')), Pow(Symbol('x_4_0'), Integer(2)), Pow(Symbol('x_4_1'), Integer(2)), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_2_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_2_0'), Symbol('x_5_0')), Pow(Symbol('x_2_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_2_1'), Symbol('x_5_1')), Pow(Symbol('x_5_0'), Integer(2)), Pow(Symbol('x_5_1'), Integer(2)), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_3_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_3_0'), Symbol('x_4_0')), Pow(Symbol('x_3_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_3_1'), Symbol('x_4_1')), Pow(Symbol('x_4_0'), Integer(2)), Pow(Symbol('x_4_1'), Integer(2)), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_3_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_3_0'), Symbol('x_5_0')), Pow(Symbol('x_3_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_3_1'), Symbol('x_5_1')), Pow(Symbol('x_5_0'), Integer(2)), Pow(Symbol('x_5_1'), Integer(2)), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_4_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_4_0'), Symbol('x_5_0')), Pow(Symbol('x_4_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_4_1'), Symbol('x_5_1')), Pow(Symbol('x_5_0'), Integer(2)), Pow(Symbol('x_5_1'), Integer(2)), Integer(-1)), Integer(0)))

	eval = pre_cond.subs( { 'd':d, 'x_5_0':x_5_0, 'x_5_1':x_5_1 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_13(d:sympy.Rational,x_5_0:sympy.Rational,x_5_1:sympy.Rational):
	#(d > 9/16) & (d + x_2_0**2 + x_2_1**2 - 5*x_2_1/2 + 9/16 > 0) & (d + x_3_0**2 + x_3_1**2 - 5*x_3_1/2 + 9/16 > 0) & (d + x_4_0**2 + x_4_1**2 - 5*x_4_1/2 + 9/16 > 0) & (d + x_5_0**2 + x_5_1**2 - 5*x_5_1/2 + 9/16 > 0) & (d - x_2_0**2 - x_2_1**2 + 1 > 0) & (d - x_3_0**2 - x_3_1**2 + 1 > 0) & (d - x_4_0**2 - x_4_1**2 + 1 > 0) & (d - x_5_0**2 - x_5_1**2 + 1 > 0) & (d + x_2_0**2 + 2*x_2_0 + x_2_1**2 - x_2_1 + 1/4 > 0) & (d + x_3_0**2 + 2*x_3_0 + x_3_1**2 - x_3_1 + 1/4 > 0) & (d + x_4_0**2 + 2*x_4_0 + x_4_1**2 - x_4_1 + 1/4 > 0) & (d + x_5_0**2 + 2*x_5_0 + x_5_1**2 - x_5_1 + 1/4 > 0) & (d + x_2_0**2 - 2*x_2_0*x_3_0 + x_2_1**2 - 2*x_2_1*x_3_1 + x_3_0**2 + x_3_1**2 - 1 > 0) & (d + x_2_0**2 - 2*x_2_0*x_4_0 + x_2_1**2 - 2*x_2_1*x_4_1 + x_4_0**2 + x_4_1**2 - 1 > 0) & (d + x_2_0**2 - 2*x_2_0*x_5_0 + x_2_1**2 - 2*x_2_1*x_5_1 + x_5_0**2 + x_5_1**2 - 1 > 0) & (d + x_3_0**2 - 2*x_3_0*x_4_0 + x_3_1**2 - 2*x_3_1*x_4_1 + x_4_0**2 + x_4_1**2 - 1 > 0) & (d + x_3_0**2 - 2*x_3_0*x_5_0 + x_3_1**2 - 2*x_3_1*x_5_1 + x_5_0**2 + x_5_1**2 - 1 > 0) & (d + x_4_0**2 - 2*x_4_0*x_5_0 + x_4_1**2 - 2*x_4_1*x_5_1 + x_5_0**2 + x_5_1**2 - 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('d'), Rational(9, 16)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_2_0'), Integer(2)), Pow(Symbol('x_2_1'), Integer(2)), Mul(Integer(-1), Rational(5, 2), Symbol('x_2_1')), Rational(9, 16)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_3_0'), Integer(2)), Pow(Symbol('x_3_1'), Integer(2)), Mul(Integer(-1), Rational(5, 2), Symbol('x_3_1')), Rational(9, 16)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_4_0'), Integer(2)), Pow(Symbol('x_4_1'), Integer(2)), Mul(Integer(-1), Rational(5, 2), Symbol('x_4_1')), Rational(9, 16)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_5_0'), Integer(2)), Pow(Symbol('x_5_1'), Integer(2)), Mul(Integer(-1), Rational(5, 2), Symbol('x_5_1')), Rational(9, 16)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Mul(Integer(-1), Pow(Symbol('x_2_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_2_1'), Integer(2))), Integer(1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Mul(Integer(-1), Pow(Symbol('x_3_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_3_1'), Integer(2))), Integer(1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Mul(Integer(-1), Pow(Symbol('x_4_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_4_1'), Integer(2))), Integer(1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Mul(Integer(-1), Pow(Symbol('x_5_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_5_1'), Integer(2))), Integer(1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_2_0'), Integer(2)), Mul(Integer(2), Symbol('x_2_0')), Pow(Symbol('x_2_1'), Integer(2)), Mul(Integer(-1), Symbol('x_2_1')), Rational(1, 4)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_3_0'), Integer(2)), Mul(Integer(2), Symbol('x_3_0')), Pow(Symbol('x_3_1'), Integer(2)), Mul(Integer(-1), Symbol('x_3_1')), Rational(1, 4)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_4_0'), Integer(2)), Mul(Integer(2), Symbol('x_4_0')), Pow(Symbol('x_4_1'), Integer(2)), Mul(Integer(-1), Symbol('x_4_1')), Rational(1, 4)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_5_0'), Integer(2)), Mul(Integer(2), Symbol('x_5_0')), Pow(Symbol('x_5_1'), Integer(2)), Mul(Integer(-1), Symbol('x_5_1')), Rational(1, 4)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_2_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_2_0'), Symbol('x_3_0')), Pow(Symbol('x_2_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_2_1'), Symbol('x_3_1')), Pow(Symbol('x_3_0'), Integer(2)), Pow(Symbol('x_3_1'), Integer(2)), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_2_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_2_0'), Symbol('x_4_0')), Pow(Symbol('x_2_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_2_1'), Symbol('x_4_1')), Pow(Symbol('x_4_0'), Integer(2)), Pow(Symbol('x_4_1'), Integer(2)), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_2_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_2_0'), Symbol('x_5_0')), Pow(Symbol('x_2_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_2_1'), Symbol('x_5_1')), Pow(Symbol('x_5_0'), Integer(2)), Pow(Symbol('x_5_1'), Integer(2)), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_3_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_3_0'), Symbol('x_4_0')), Pow(Symbol('x_3_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_3_1'), Symbol('x_4_1')), Pow(Symbol('x_4_0'), Integer(2)), Pow(Symbol('x_4_1'), Integer(2)), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_3_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_3_0'), Symbol('x_5_0')), Pow(Symbol('x_3_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_3_1'), Symbol('x_5_1')), Pow(Symbol('x_5_0'), Integer(2)), Pow(Symbol('x_5_1'), Integer(2)), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Symbol('d'), Pow(Symbol('x_4_0'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_4_0'), Symbol('x_5_0')), Pow(Symbol('x_4_1'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x_4_1'), Symbol('x_5_1')), Pow(Symbol('x_5_0'), Integer(2)), Pow(Symbol('x_5_1'), Integer(2)), Integer(-1)), Integer(0)))

	eval = pre_cond.subs( { 'd':d, 'x_5_0':x_5_0, 'x_5_1':x_5_1 })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(d:sympy.Rational, x_5_0:sympy.Rational, x_5_1:sympy.Rational, x_0_0:sympy.Rational, x_0_1:sympy.Rational, x_1_0:sympy.Rational, x_1_1:sympy.Rational, x_2_0:sympy.Rational, x_2_1:sympy.Rational, x_3_0:sympy.Rational, x_3_1:sympy.Rational, x_4_0:sympy.Rational, x_4_1:sympy.Rational):
	# (0 > -d) & (0 > -d + x_0_0**2 + x_0_1**2 - 1) & (0 > -d + x_1_0**2 + x_1_1**2 - 1) & (0 > -d + x_2_0**2 + x_2_1**2 - 1) & (0 > -d + x_3_0**2 + x_3_1**2 - 1) & (0 > -d + x_4_0**2 + x_4_1**2 - 1) & (0 > -d + x_5_0**2 + x_5_1**2 - 1) & (0 > -d - x_0_0**2 + 2*x_0_0*x_1_0 - x_0_1**2 + 2*x_0_1*x_1_1 - x_1_0**2 - x_1_1**2 + 1) & (0 > -d - x_0_0**2 + 2*x_0_0*x_2_0 - x_0_1**2 + 2*x_0_1*x_2_1 - x_2_0**2 - x_2_1**2 + 1) & (0 > -d - x_0_0**2 + 2*x_0_0*x_3_0 - x_0_1**2 + 2*x_0_1*x_3_1 - x_3_0**2 - x_3_1**2 + 1) & (0 > -d - x_0_0**2 + 2*x_0_0*x_4_0 - x_0_1**2 + 2*x_0_1*x_4_1 - x_4_0**2 - x_4_1**2 + 1) & (0 > -d - x_0_0**2 + 2*x_0_0*x_5_0 - x_0_1**2 + 2*x_0_1*x_5_1 - x_5_0**2 - x_5_1**2 + 1) & (0 > -d - x_1_0**2 + 2*x_1_0*x_2_0 - x_1_1**2 + 2*x_1_1*x_2_1 - x_2_0**2 - x_2_1**2 + 1) & (0 > -d - x_1_0**2 + 2*x_1_0*x_3_0 - x_1_1**2 + 2*x_1_1*x_3_1 - x_3_0**2 - x_3_1**2 + 1) & (0 > -d - x_1_0**2 + 2*x_1_0*x_4_0 - x_1_1**2 + 2*x_1_1*x_4_1 - x_4_0**2 - x_4_1**2 + 1) & (0 > -d - x_1_0**2 + 2*x_1_0*x_5_0 - x_1_1**2 + 2*x_1_1*x_5_1 - x_5_0**2 - x_5_1**2 + 1) & (0 > -d - x_2_0**2 + 2*x_2_0*x_3_0 - x_2_1**2 + 2*x_2_1*x_3_1 - x_3_0**2 - x_3_1**2 + 1) & (0 > -d - x_2_0**2 + 2*x_2_0*x_4_0 - x_2_1**2 + 2*x_2_1*x_4_1 - x_4_0**2 - x_4_1**2 + 1) & (0 > -d - x_2_0**2 + 2*x_2_0*x_5_0 - x_2_1**2 + 2*x_2_1*x_5_1 - x_5_0**2 - x_5_1**2 + 1) & (0 > -d - x_3_0**2 + 2*x_3_0*x_4_0 - x_3_1**2 + 2*x_3_1*x_4_1 - x_4_0**2 - x_4_1**2 + 1) & (0 > -d - x_3_0**2 + 2*x_3_0*x_5_0 - x_3_1**2 + 2*x_3_1*x_5_1 - x_5_0**2 - x_5_1**2 + 1) & (0 > -d - x_4_0**2 + 2*x_4_0*x_5_0 - x_4_1**2 + 2*x_4_1*x_5_1 - x_5_0**2 - x_5_1**2 + 1)

	post_cond =  And(StrictGreaterThan(Integer(0), Mul(Integer(-1), Symbol('d'))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('d')), Pow(Symbol('x_0_0'), Integer(2)), Pow(Symbol('x_0_1'), Integer(2)), Integer(-1))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('d')), Pow(Symbol('x_1_0'), Integer(2)), Pow(Symbol('x_1_1'), Integer(2)), Integer(-1))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('d')), Pow(Symbol('x_2_0'), Integer(2)), Pow(Symbol('x_2_1'), Integer(2)), Integer(-1))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('d')), Pow(Symbol('x_3_0'), Integer(2)), Pow(Symbol('x_3_1'), Integer(2)), Integer(-1))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('d')), Pow(Symbol('x_4_0'), Integer(2)), Pow(Symbol('x_4_1'), Integer(2)), Integer(-1))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('d')), Pow(Symbol('x_5_0'), Integer(2)), Pow(Symbol('x_5_1'), Integer(2)), Integer(-1))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('d')), Mul(Integer(-1), Pow(Symbol('x_0_0'), Integer(2))), Mul(Integer(2), Symbol('x_0_0'), Symbol('x_1_0')), Mul(Integer(-1), Pow(Symbol('x_0_1'), Integer(2))), Mul(Integer(2), Symbol('x_0_1'), Symbol('x_1_1')), Mul(Integer(-1), Pow(Symbol('x_1_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_1_1'), Integer(2))), Integer(1))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('d')), Mul(Integer(-1), Pow(Symbol('x_0_0'), Integer(2))), Mul(Integer(2), Symbol('x_0_0'), Symbol('x_2_0')), Mul(Integer(-1), Pow(Symbol('x_0_1'), Integer(2))), Mul(Integer(2), Symbol('x_0_1'), Symbol('x_2_1')), Mul(Integer(-1), Pow(Symbol('x_2_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_2_1'), Integer(2))), Integer(1))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('d')), Mul(Integer(-1), Pow(Symbol('x_0_0'), Integer(2))), Mul(Integer(2), Symbol('x_0_0'), Symbol('x_3_0')), Mul(Integer(-1), Pow(Symbol('x_0_1'), Integer(2))), Mul(Integer(2), Symbol('x_0_1'), Symbol('x_3_1')), Mul(Integer(-1), Pow(Symbol('x_3_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_3_1'), Integer(2))), Integer(1))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('d')), Mul(Integer(-1), Pow(Symbol('x_0_0'), Integer(2))), Mul(Integer(2), Symbol('x_0_0'), Symbol('x_4_0')), Mul(Integer(-1), Pow(Symbol('x_0_1'), Integer(2))), Mul(Integer(2), Symbol('x_0_1'), Symbol('x_4_1')), Mul(Integer(-1), Pow(Symbol('x_4_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_4_1'), Integer(2))), Integer(1))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('d')), Mul(Integer(-1), Pow(Symbol('x_0_0'), Integer(2))), Mul(Integer(2), Symbol('x_0_0'), Symbol('x_5_0')), Mul(Integer(-1), Pow(Symbol('x_0_1'), Integer(2))), Mul(Integer(2), Symbol('x_0_1'), Symbol('x_5_1')), Mul(Integer(-1), Pow(Symbol('x_5_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_5_1'), Integer(2))), Integer(1))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('d')), Mul(Integer(-1), Pow(Symbol('x_1_0'), Integer(2))), Mul(Integer(2), Symbol('x_1_0'), Symbol('x_2_0')), Mul(Integer(-1), Pow(Symbol('x_1_1'), Integer(2))), Mul(Integer(2), Symbol('x_1_1'), Symbol('x_2_1')), Mul(Integer(-1), Pow(Symbol('x_2_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_2_1'), Integer(2))), Integer(1))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('d')), Mul(Integer(-1), Pow(Symbol('x_1_0'), Integer(2))), Mul(Integer(2), Symbol('x_1_0'), Symbol('x_3_0')), Mul(Integer(-1), Pow(Symbol('x_1_1'), Integer(2))), Mul(Integer(2), Symbol('x_1_1'), Symbol('x_3_1')), Mul(Integer(-1), Pow(Symbol('x_3_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_3_1'), Integer(2))), Integer(1))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('d')), Mul(Integer(-1), Pow(Symbol('x_1_0'), Integer(2))), Mul(Integer(2), Symbol('x_1_0'), Symbol('x_4_0')), Mul(Integer(-1), Pow(Symbol('x_1_1'), Integer(2))), Mul(Integer(2), Symbol('x_1_1'), Symbol('x_4_1')), Mul(Integer(-1), Pow(Symbol('x_4_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_4_1'), Integer(2))), Integer(1))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('d')), Mul(Integer(-1), Pow(Symbol('x_1_0'), Integer(2))), Mul(Integer(2), Symbol('x_1_0'), Symbol('x_5_0')), Mul(Integer(-1), Pow(Symbol('x_1_1'), Integer(2))), Mul(Integer(2), Symbol('x_1_1'), Symbol('x_5_1')), Mul(Integer(-1), Pow(Symbol('x_5_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_5_1'), Integer(2))), Integer(1))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('d')), Mul(Integer(-1), Pow(Symbol('x_2_0'), Integer(2))), Mul(Integer(2), Symbol('x_2_0'), Symbol('x_3_0')), Mul(Integer(-1), Pow(Symbol('x_2_1'), Integer(2))), Mul(Integer(2), Symbol('x_2_1'), Symbol('x_3_1')), Mul(Integer(-1), Pow(Symbol('x_3_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_3_1'), Integer(2))), Integer(1))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('d')), Mul(Integer(-1), Pow(Symbol('x_2_0'), Integer(2))), Mul(Integer(2), Symbol('x_2_0'), Symbol('x_4_0')), Mul(Integer(-1), Pow(Symbol('x_2_1'), Integer(2))), Mul(Integer(2), Symbol('x_2_1'), Symbol('x_4_1')), Mul(Integer(-1), Pow(Symbol('x_4_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_4_1'), Integer(2))), Integer(1))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('d')), Mul(Integer(-1), Pow(Symbol('x_2_0'), Integer(2))), Mul(Integer(2), Symbol('x_2_0'), Symbol('x_5_0')), Mul(Integer(-1), Pow(Symbol('x_2_1'), Integer(2))), Mul(Integer(2), Symbol('x_2_1'), Symbol('x_5_1')), Mul(Integer(-1), Pow(Symbol('x_5_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_5_1'), Integer(2))), Integer(1))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('d')), Mul(Integer(-1), Pow(Symbol('x_3_0'), Integer(2))), Mul(Integer(2), Symbol('x_3_0'), Symbol('x_4_0')), Mul(Integer(-1), Pow(Symbol('x_3_1'), Integer(2))), Mul(Integer(2), Symbol('x_3_1'), Symbol('x_4_1')), Mul(Integer(-1), Pow(Symbol('x_4_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_4_1'), Integer(2))), Integer(1))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('d')), Mul(Integer(-1), Pow(Symbol('x_3_0'), Integer(2))), Mul(Integer(2), Symbol('x_3_0'), Symbol('x_5_0')), Mul(Integer(-1), Pow(Symbol('x_3_1'), Integer(2))), Mul(Integer(2), Symbol('x_3_1'), Symbol('x_5_1')), Mul(Integer(-1), Pow(Symbol('x_5_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_5_1'), Integer(2))), Integer(1))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('d')), Mul(Integer(-1), Pow(Symbol('x_4_0'), Integer(2))), Mul(Integer(2), Symbol('x_4_0'), Symbol('x_5_0')), Mul(Integer(-1), Pow(Symbol('x_4_1'), Integer(2))), Mul(Integer(2), Symbol('x_4_1'), Symbol('x_5_1')), Mul(Integer(-1), Pow(Symbol('x_5_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_5_1'), Integer(2))), Integer(1))))

	eval = post_cond.subs( { 'd':d, 'x_5_0':x_5_0, 'x_5_1':x_5_1, 'x_0_0':x_0_0, 'x_0_1':x_0_1, 'x_1_0':x_1_0, 'x_1_1':x_1_1, 'x_2_0':x_2_0, 'x_2_1':x_2_1, 'x_3_0':x_3_0, 'x_3_1':x_3_1, 'x_4_0':x_4_0, 'x_4_1':x_4_1 })

	return eval == sympy.logic.boolalg.BooleanTrue





if __name__=="__main__":
	
	ip_0=int(input("enter integer numerator of d:\n"))
	ip_1=int(input("enter integer denominator of d:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	d=sympy.Rational(ip_0,ip_1)
	
	
	ip_0=int(input("enter integer numerator of x_5_0:\n"))
	ip_1=int(input("enter integer denominator of x_5_0:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	x_5_0=sympy.Rational(ip_0,ip_1)
	
	
	ip_0=int(input("enter integer numerator of x_5_1:\n"))
	ip_1=int(input("enter integer denominator of x_5_1:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	x_5_1=sympy.Rational(ip_0,ip_1)
	
	
	
	
	if pre_condition_0(d=d,x_5_0=x_5_0,x_5_1=x_5_1)==True:
		print("pre_condition_0 SAT")
		print('d = 2')
		print('x_0_0 = 1/8')
		print('x_0_1 = 1/2')
		print('x_1_0 = -1/2')
		print('x_1_1 = -1/2')
		print('x_2_0 = 1')
		print('x_2_1 = -1')
		print('x_3_0 = 1/2')
		print('x_3_1 = -1/2')
		print('x_4_0 = -1/2')
		print('x_4_1 = -1')
		print('x_5_0 = 1/8')
		print('x_5_1 = -1/4')
		exit(0)
	
	
	if pre_condition_1(d=d,x_5_0=x_5_0,x_5_1=x_5_1)==True:
		print("pre_condition_1 SAT")
		print('d = 2')
		print('x_0_0 = 1/8')
		print('x_0_1 = 1/2')
		print('x_1_0 = -1/2')
		print('x_1_1 = -1/2')
		print('x_2_0 = 1')
		print('x_2_1 = -1')
		print('x_3_0 = 1/2')
		print('x_3_1 = -1/2')
		print('x_4_0 = -1/2')
		print('x_4_1 = -1')
		print('x_5_0 = 1/8')
		print('x_5_1 = -1/4')
		exit(0)
	
	
	if pre_condition_2(d=d,x_5_0=x_5_0,x_5_1=x_5_1)==True:
		print("pre_condition_2 SAT")
		print('d = 2')
		print('x_0_0 = 1/8')
		print('x_0_1 = 1/2')
		print('x_1_0 = -1/2')
		print('x_1_1 = -1/2')
		print('x_2_0 = 1')
		print('x_2_1 = -1')
		print('x_3_0 = 1/2')
		print('x_3_1 = -1/2')
		print('x_4_0 = -1/2')
		print('x_4_1 = -1')
		print('x_5_0 = 1/8')
		print('x_5_1 = -1/4')
		exit(0)
	
	
	if pre_condition_3(d=d,x_5_0=x_5_0,x_5_1=x_5_1)==True:
		print("pre_condition_3 SAT")
		print('d = 2')
		print('x_0_0 = 1/8')
		print('x_0_1 = 1/2')
		print('x_1_0 = -1/2')
		print('x_1_1 = -1/2')
		print('x_2_0 = 1')
		print('x_2_1 = -1')
		print('x_3_0 = 1/2')
		print('x_3_1 = -1/2')
		print('x_4_0 = -1/2')
		print('x_4_1 = -1')
		print('x_5_0 = 1/8')
		print('x_5_1 = -1/4')
		exit(0)
	
	
	if pre_condition_4(d=d,x_5_0=x_5_0,x_5_1=x_5_1)==True:
		print("pre_condition_4 SAT")
		print('d = 2')
		print('x_0_0 = 1/8')
		print('x_0_1 = 1/2')
		print('x_1_0 = -1/2')
		print('x_1_1 = -1/2')
		print('x_2_0 = 1')
		print('x_2_1 = -1')
		print('x_3_0 = 1/2')
		print('x_3_1 = -1/2')
		print('x_4_0 = -1/2')
		print('x_4_1 = -1')
		print('x_5_0 = 1/8')
		print('x_5_1 = -1/4')
		exit(0)
	
	
	if pre_condition_5(d=d,x_5_0=x_5_0,x_5_1=x_5_1)==True:
		print("pre_condition_5 SAT")
		print('d = 2')
		print('x_0_0 = 1/8')
		print('x_0_1 = 1/2')
		print('x_1_0 = -1/2')
		print('x_1_1 = -1/2')
		print('x_2_0 = 1')
		print('x_2_1 = -1')
		print('x_3_0 = 1/2')
		print('x_3_1 = -1/2')
		print('x_4_0 = -1/2')
		print('x_4_1 = -1')
		print('x_5_0 = 1/8')
		print('x_5_1 = -1/4')
		exit(0)
	
	
	if pre_condition_6(d=d,x_5_0=x_5_0,x_5_1=x_5_1)==True:
		print("pre_condition_6 SAT")
		print('d = 2')
		print('x_0_0 = 1/8')
		print('x_0_1 = 1/2')
		print('x_1_0 = -1/2')
		print('x_1_1 = -1/2')
		print('x_2_0 = 1')
		print('x_2_1 = -1')
		print('x_3_0 = 1/2')
		print('x_3_1 = -1/2')
		print('x_4_0 = -1/2')
		print('x_4_1 = -1')
		print('x_5_0 = 1/8')
		print('x_5_1 = -1/4')
		exit(0)
	
	
	if pre_condition_7(d=d,x_5_0=x_5_0,x_5_1=x_5_1)==True:
		print("pre_condition_7 SAT")
		print('d = 2')
		print('x_0_0 = 1/8')
		print('x_0_1 = 1/2')
		print('x_1_0 = -1/2')
		print('x_1_1 = -1/2')
		print('x_2_0 = 1')
		print('x_2_1 = -1')
		print('x_3_0 = 1/2')
		print('x_3_1 = -1/2')
		print('x_4_0 = -1/2')
		print('x_4_1 = -1')
		print('x_5_0 = 1/8')
		print('x_5_1 = -1/4')
		exit(0)
	
	
	if pre_condition_8(d=d,x_5_0=x_5_0,x_5_1=x_5_1)==True:
		print("pre_condition_8 SAT")
		print('d = 2')
		print('x_0_0 = 1/8')
		print('x_0_1 = 1/2')
		print('x_1_0 = -1/2')
		print('x_1_1 = -1/2')
		print('x_2_0 = 1')
		print('x_2_1 = -1')
		print('x_3_0 = 1/2')
		print('x_3_1 = -1/2')
		print('x_4_0 = -1/2')
		print('x_4_1 = -1')
		print('x_5_0 = 1/8')
		print('x_5_1 = -1/4')
		exit(0)
	
	
	if pre_condition_9(d=d,x_5_0=x_5_0,x_5_1=x_5_1)==True:
		print("pre_condition_9 SAT")
		print('d = 2')
		print('x_0_0 = 1/8')
		print('x_0_1 = 1/2')
		print('x_1_0 = -1/2')
		print('x_1_1 = -1/2')
		print('x_2_0 = 1')
		print('x_2_1 = -1')
		print('x_3_0 = 1/2')
		print('x_3_1 = -1/2')
		print('x_4_0 = -1/2')
		print('x_4_1 = -1')
		print('x_5_0 = 1/8')
		print('x_5_1 = -1/4')
		exit(0)
	
	
	if pre_condition_10(d=d,x_5_0=x_5_0,x_5_1=x_5_1)==True:
		print("pre_condition_10 SAT")
		print('d = 73/128')
		print('x_0_0 = 0')
		print('x_0_1 = 5/4')
		print('x_1_0 = -1')
		print('x_1_1 = 1/2')
		print('x_2_0 = 3/4')
		print('x_2_1 = -1')
		print('x_3_0 = -1')
		print('x_3_1 = -1/2')
		print('x_4_0 = 0')
		print('x_4_1 = -1')
		print('x_5_0 = 0')
		print('x_5_1 = 0')
		exit(0)
	
	
	if pre_condition_11(d=d,x_5_0=x_5_0,x_5_1=x_5_1)==True:
		print("pre_condition_11 SAT")
		print('d = 73/128')
		print('x_0_0 = 0')
		print('x_0_1 = 5/4')
		print('x_1_0 = -1')
		print('x_1_1 = 1/2')
		print('x_2_0 = 3/4')
		print('x_2_1 = -1')
		print('x_3_0 = -1')
		print('x_3_1 = -1/2')
		print('x_4_0 = 0')
		print('x_4_1 = -1')
		print('x_5_0 = 0')
		print('x_5_1 = 0')
		exit(0)
	
	
	if pre_condition_12(d=d,x_5_0=x_5_0,x_5_1=x_5_1)==True:
		print("pre_condition_12 SAT")
		print('d = 73/128')
		print('x_0_0 = 0')
		print('x_0_1 = 5/4')
		print('x_1_0 = -1')
		print('x_1_1 = 1/2')
		print('x_2_0 = 3/4')
		print('x_2_1 = -1')
		print('x_3_0 = -1')
		print('x_3_1 = -1/2')
		print('x_4_0 = 0')
		print('x_4_1 = -1')
		print('x_5_0 = 0')
		print('x_5_1 = 0')
		exit(0)
	
	
	if pre_condition_13(d=d,x_5_0=x_5_0,x_5_1=x_5_1)==True:
		print("pre_condition_13 SAT")
		print('d = 73/128')
		print('x_0_0 = 0')
		print('x_0_1 = 5/4')
		print('x_1_0 = -1')
		print('x_1_1 = 1/2')
		print('x_2_0 = 3/4')
		print('x_2_1 = -1')
		print('x_3_0 = -1')
		print('x_3_1 = -1/2')
		print('x_4_0 = 0')
		print('x_4_1 = -1')
		print('x_5_0 = 0')
		print('x_5_1 = 0')
		exit(0)


	print("UNKNOWN")
	exit(0)
