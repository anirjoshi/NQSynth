import sympy
from sympy import *

def pre_condition_0(c:sympy.Rational):
	#(c + y**2 + 161/64 < 0) & (-c**2 + y**2 + 1/64 < 0)

	pre_cond = And(StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(161, 64)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Pow(Symbol('c'), Integer(2))), Pow(Symbol('y'), Integer(2)), Rational(1, 64)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(c:sympy.Rational):
	#(c < -177/64) & (c**2 > 17/64)

	pre_cond = And(StrictLessThan(Symbol('c'), Rational(-177, 64)), StrictGreaterThan(Pow(Symbol('c'), Integer(2)), Rational(17, 64)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(c:sympy.Rational):
	#(c + y**2 + 3625/2304 < 0) & (-c**2 + y**2 + 361/2304 < 0)

	pre_cond = And(StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(3625, 2304)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Pow(Symbol('c'), Integer(2))), Pow(Symbol('y'), Integer(2)), Rational(361, 2304)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(c:sympy.Rational):
	#(c < -3625/2304) & (c**2 > 361/2304)

	pre_cond = And(StrictLessThan(Symbol('c'), Rational(-3625, 2304)), StrictGreaterThan(Pow(Symbol('c'), Integer(2)), Rational(361, 2304)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_4(c:sympy.Rational):
	#(c + y**2 + 629340277777777756388888888888889/400000000000000000000000000000000 < 0) & (-c**2 + y**2 + 62673611111111116388888888888889/400000000000000000000000000000000 < 0)

	pre_cond = And(StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(629340277777777756388888888888889, 400000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Pow(Symbol('c'), Integer(2))), Pow(Symbol('y'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_5(c:sympy.Rational):
	#(c < -629340277777777756388888888888889/400000000000000000000000000000000) & (c**2 > 62673611111111116388888888888889/400000000000000000000000000000000)

	pre_cond = And(StrictLessThan(Symbol('c'), Rational(-629340277777777756388888888888889, 400000000000000000000000000000000)), StrictGreaterThan(Pow(Symbol('c'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_6(c:sympy.Rational):
	#(c + y**2 + 629340277777777756388888888888889/400000000000000000000000000000000 < 0) & (-c**2 + y**2 + 62673611111111116388888888888889/400000000000000000000000000000000 < 0)

	pre_cond = And(StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(629340277777777756388888888888889, 400000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Pow(Symbol('c'), Integer(2))), Pow(Symbol('y'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_7(c:sympy.Rational):
	#(c < -629340277777777756388888888888889/400000000000000000000000000000000) & (c**2 > 62673611111111116388888888888889/400000000000000000000000000000000)

	pre_cond = And(StrictLessThan(Symbol('c'), Rational(-629340277777777756388888888888889, 400000000000000000000000000000000)), StrictGreaterThan(Pow(Symbol('c'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_8(c:sympy.Rational):
	#(c + y**2 + 629340277777777756388888888888889/400000000000000000000000000000000 < 0) & (-c**2 + y**2 + 62673611111111116388888888888889/400000000000000000000000000000000 < 0)

	pre_cond = And(StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(629340277777777756388888888888889, 400000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Pow(Symbol('c'), Integer(2))), Pow(Symbol('y'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_9(c:sympy.Rational):
	#(c < -629340277777777756388888888888889/400000000000000000000000000000000) & (c**2 > 62673611111111116388888888888889/400000000000000000000000000000000)

	pre_cond = And(StrictLessThan(Symbol('c'), Rational(-629340277777777756388888888888889, 400000000000000000000000000000000)), StrictGreaterThan(Pow(Symbol('c'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_10(c:sympy.Rational):
	#(c + y**2 + 629340277777777756388888888888889/400000000000000000000000000000000 < 0) & (-c**2 + y**2 + 62673611111111116388888888888889/400000000000000000000000000000000 < 0)

	pre_cond = And(StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(629340277777777756388888888888889, 400000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Pow(Symbol('c'), Integer(2))), Pow(Symbol('y'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_11(c:sympy.Rational):
	#(c < -629340277777777756388888888888889/400000000000000000000000000000000) & (c**2 > 62673611111111116388888888888889/400000000000000000000000000000000)

	pre_cond = And(StrictLessThan(Symbol('c'), Rational(-629340277777777756388888888888889, 400000000000000000000000000000000)), StrictGreaterThan(Pow(Symbol('c'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_12(c:sympy.Rational):
	#(c + y**2 + 629340277777777756388888888888889/400000000000000000000000000000000 < 0) & (-c**2 + y**2 + 62673611111111116388888888888889/400000000000000000000000000000000 < 0)

	pre_cond = And(StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(629340277777777756388888888888889, 400000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Pow(Symbol('c'), Integer(2))), Pow(Symbol('y'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_13(c:sympy.Rational):
	#(c < -629340277777777756388888888888889/400000000000000000000000000000000) & (c**2 > 62673611111111116388888888888889/400000000000000000000000000000000)

	pre_cond = And(StrictLessThan(Symbol('c'), Rational(-629340277777777756388888888888889, 400000000000000000000000000000000)), StrictGreaterThan(Pow(Symbol('c'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_14(c:sympy.Rational):
	#(c + y**2 + 629340277777777756388888888888889/400000000000000000000000000000000 < 0) & (-c**2 + y**2 + 62673611111111116388888888888889/400000000000000000000000000000000 < 0)

	pre_cond = And(StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(629340277777777756388888888888889, 400000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Pow(Symbol('c'), Integer(2))), Pow(Symbol('y'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_15(c:sympy.Rational):
	#(c < -629340277777777756388888888888889/400000000000000000000000000000000) & (c**2 > 62673611111111116388888888888889/400000000000000000000000000000000)

	pre_cond = And(StrictLessThan(Symbol('c'), Rational(-629340277777777756388888888888889, 400000000000000000000000000000000)), StrictGreaterThan(Pow(Symbol('c'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_16(c:sympy.Rational):
	#(c + y**2 + 629340277777777756388888888888889/400000000000000000000000000000000 < 0) & (-c**2 + y**2 + 62673611111111116388888888888889/400000000000000000000000000000000 < 0)

	pre_cond = And(StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(629340277777777756388888888888889, 400000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Pow(Symbol('c'), Integer(2))), Pow(Symbol('y'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_17(c:sympy.Rational):
	#(c < -629340277777777756388888888888889/400000000000000000000000000000000) & (c**2 > 62673611111111116388888888888889/400000000000000000000000000000000)

	pre_cond = And(StrictLessThan(Symbol('c'), Rational(-629340277777777756388888888888889, 400000000000000000000000000000000)), StrictGreaterThan(Pow(Symbol('c'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_18(c:sympy.Rational):
	#(c + y**2 + 629340277777777756388888888888889/400000000000000000000000000000000 < 0) & (-c**2 + y**2 + 62673611111111116388888888888889/400000000000000000000000000000000 < 0)

	pre_cond = And(StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(629340277777777756388888888888889, 400000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Pow(Symbol('c'), Integer(2))), Pow(Symbol('y'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_19(c:sympy.Rational):
	#(c < -629340277777777756388888888888889/400000000000000000000000000000000) & (c**2 > 62673611111111116388888888888889/400000000000000000000000000000000)

	pre_cond = And(StrictLessThan(Symbol('c'), Rational(-629340277777777756388888888888889, 400000000000000000000000000000000)), StrictGreaterThan(Pow(Symbol('c'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_20(c:sympy.Rational):
	#(c + y**2 + 629340277777777756388888888888889/400000000000000000000000000000000 < 0) & (-c**2 + y**2 + 62673611111111116388888888888889/400000000000000000000000000000000 < 0)

	pre_cond = And(StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(629340277777777756388888888888889, 400000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Pow(Symbol('c'), Integer(2))), Pow(Symbol('y'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_21(c:sympy.Rational):
	#(c < -629340277777777756388888888888889/400000000000000000000000000000000) & (c**2 > 62673611111111116388888888888889/400000000000000000000000000000000)

	pre_cond = And(StrictLessThan(Symbol('c'), Rational(-629340277777777756388888888888889, 400000000000000000000000000000000)), StrictGreaterThan(Pow(Symbol('c'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_22(c:sympy.Rational):
	#(c + y**2 + 629340277777777756388888888888889/400000000000000000000000000000000 < 0) & (-c**2 + y**2 + 62673611111111116388888888888889/400000000000000000000000000000000 < 0)

	pre_cond = And(StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(629340277777777756388888888888889, 400000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Pow(Symbol('c'), Integer(2))), Pow(Symbol('y'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_23(c:sympy.Rational):
	#(c < -629340277777777756388888888888889/400000000000000000000000000000000) & (c**2 > 62673611111111116388888888888889/400000000000000000000000000000000)

	pre_cond = And(StrictLessThan(Symbol('c'), Rational(-629340277777777756388888888888889, 400000000000000000000000000000000)), StrictGreaterThan(Pow(Symbol('c'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_24(c:sympy.Rational):
	#(c + y**2 + 629340277777777756388888888888889/400000000000000000000000000000000 < 0) & (-c**2 + y**2 + 62673611111111116388888888888889/400000000000000000000000000000000 < 0)

	pre_cond = And(StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(629340277777777756388888888888889, 400000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Pow(Symbol('c'), Integer(2))), Pow(Symbol('y'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_25(c:sympy.Rational):
	#(c < -629340277777777756388888888888889/400000000000000000000000000000000) & (c**2 > 62673611111111116388888888888889/400000000000000000000000000000000)

	pre_cond = And(StrictLessThan(Symbol('c'), Rational(-629340277777777756388888888888889, 400000000000000000000000000000000)), StrictGreaterThan(Pow(Symbol('c'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_26(c:sympy.Rational):
	#(c + y**2 + 629340277777777756388888888888889/400000000000000000000000000000000 < 0) & (-c**2 + y**2 + 62673611111111116388888888888889/400000000000000000000000000000000 < 0)

	pre_cond = And(StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(629340277777777756388888888888889, 400000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Pow(Symbol('c'), Integer(2))), Pow(Symbol('y'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_27(c:sympy.Rational):
	#(c < -629340277777777756388888888888889/400000000000000000000000000000000) & (c**2 > 62673611111111116388888888888889/400000000000000000000000000000000)

	pre_cond = And(StrictLessThan(Symbol('c'), Rational(-629340277777777756388888888888889, 400000000000000000000000000000000)), StrictGreaterThan(Pow(Symbol('c'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_28(c:sympy.Rational):
	#(c + y**2 + 629340277777777756388888888888889/400000000000000000000000000000000 < 0) & (-c**2 + y**2 + 62673611111111116388888888888889/400000000000000000000000000000000 < 0)

	pre_cond = And(StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(629340277777777756388888888888889, 400000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Pow(Symbol('c'), Integer(2))), Pow(Symbol('y'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_29(c:sympy.Rational):
	#(c < -629340277777777756388888888888889/400000000000000000000000000000000) & (c**2 > 62673611111111116388888888888889/400000000000000000000000000000000)

	pre_cond = And(StrictLessThan(Symbol('c'), Rational(-629340277777777756388888888888889, 400000000000000000000000000000000)), StrictGreaterThan(Pow(Symbol('c'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_30(c:sympy.Rational):
	#(c + y**2 + 629340277777777756388888888888889/400000000000000000000000000000000 < 0) & (-c**2 + y**2 + 62673611111111116388888888888889/400000000000000000000000000000000 < 0)

	pre_cond = And(StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(629340277777777756388888888888889, 400000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Pow(Symbol('c'), Integer(2))), Pow(Symbol('y'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_31(c:sympy.Rational):
	#(c < -629340277777777756388888888888889/400000000000000000000000000000000) & (c**2 > 62673611111111116388888888888889/400000000000000000000000000000000)

	pre_cond = And(StrictLessThan(Symbol('c'), Rational(-629340277777777756388888888888889, 400000000000000000000000000000000)), StrictGreaterThan(Pow(Symbol('c'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_32(c:sympy.Rational):
	#(c + y**2 + 629340277777777756388888888888889/400000000000000000000000000000000 < 0) & (-c**2 + y**2 + 62673611111111116388888888888889/400000000000000000000000000000000 < 0)

	pre_cond = And(StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(629340277777777756388888888888889, 400000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Pow(Symbol('c'), Integer(2))), Pow(Symbol('y'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_33(c:sympy.Rational):
	#(c < -629340277777777756388888888888889/400000000000000000000000000000000) & (c**2 > 62673611111111116388888888888889/400000000000000000000000000000000)

	pre_cond = And(StrictLessThan(Symbol('c'), Rational(-629340277777777756388888888888889, 400000000000000000000000000000000)), StrictGreaterThan(Pow(Symbol('c'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_34(c:sympy.Rational):
	#(c + y**2 + 629340277777777756388888888888889/400000000000000000000000000000000 < 0) & (-c**2 + y**2 + 62673611111111116388888888888889/400000000000000000000000000000000 < 0)

	pre_cond = And(StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(629340277777777756388888888888889, 400000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Pow(Symbol('c'), Integer(2))), Pow(Symbol('y'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_35(c:sympy.Rational):
	#(c < -629340277777777756388888888888889/400000000000000000000000000000000) & (c**2 > 62673611111111116388888888888889/400000000000000000000000000000000)

	pre_cond = And(StrictLessThan(Symbol('c'), Rational(-629340277777777756388888888888889, 400000000000000000000000000000000)), StrictGreaterThan(Pow(Symbol('c'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_36(c:sympy.Rational):
	#(c + y**2 + 629340277777777756388888888888889/400000000000000000000000000000000 < 0) & (-c**2 + y**2 + 62673611111111116388888888888889/400000000000000000000000000000000 < 0)

	pre_cond = And(StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(629340277777777756388888888888889, 400000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Pow(Symbol('c'), Integer(2))), Pow(Symbol('y'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_37(c:sympy.Rational):
	#(c < -629340277777777756388888888888889/400000000000000000000000000000000) & (c**2 > 62673611111111116388888888888889/400000000000000000000000000000000)

	pre_cond = And(StrictLessThan(Symbol('c'), Rational(-629340277777777756388888888888889, 400000000000000000000000000000000)), StrictGreaterThan(Pow(Symbol('c'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_38(c:sympy.Rational):
	#(c + y**2 + 629340277777777756388888888888889/400000000000000000000000000000000 < 0) & (-c**2 + y**2 + 62673611111111116388888888888889/400000000000000000000000000000000 < 0)

	pre_cond = And(StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(629340277777777756388888888888889, 400000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Pow(Symbol('c'), Integer(2))), Pow(Symbol('y'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_39(c:sympy.Rational):
	#(c < -629340277777777756388888888888889/400000000000000000000000000000000) & (c**2 > 62673611111111116388888888888889/400000000000000000000000000000000)

	pre_cond = And(StrictLessThan(Symbol('c'), Rational(-629340277777777756388888888888889, 400000000000000000000000000000000)), StrictGreaterThan(Pow(Symbol('c'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_40(c:sympy.Rational):
	#(c + y**2 + 629340277777777756388888888888889/400000000000000000000000000000000 < 0) & (-c**2 + y**2 + 62673611111111116388888888888889/400000000000000000000000000000000 < 0)

	pre_cond = And(StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(629340277777777756388888888888889, 400000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Pow(Symbol('c'), Integer(2))), Pow(Symbol('y'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_41(c:sympy.Rational):
	#(c < -629340277777777756388888888888889/400000000000000000000000000000000) & (c**2 > 62673611111111116388888888888889/400000000000000000000000000000000)

	pre_cond = And(StrictLessThan(Symbol('c'), Rational(-629340277777777756388888888888889, 400000000000000000000000000000000)), StrictGreaterThan(Pow(Symbol('c'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_42(c:sympy.Rational):
	#(c + y**2 + 629340277777777756388888888888889/400000000000000000000000000000000 < 0) & (-c**2 + y**2 + 62673611111111116388888888888889/400000000000000000000000000000000 < 0)

	pre_cond = And(StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(629340277777777756388888888888889, 400000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Pow(Symbol('c'), Integer(2))), Pow(Symbol('y'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_43(c:sympy.Rational):
	#(c < -629340277777777756388888888888889/400000000000000000000000000000000) & (c**2 > 62673611111111116388888888888889/400000000000000000000000000000000)

	pre_cond = And(StrictLessThan(Symbol('c'), Rational(-629340277777777756388888888888889, 400000000000000000000000000000000)), StrictGreaterThan(Pow(Symbol('c'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_44(c:sympy.Rational):
	#(c + y**2 + 629340277777777756388888888888889/400000000000000000000000000000000 < 0) & (-c**2 + y**2 + 62673611111111116388888888888889/400000000000000000000000000000000 < 0)

	pre_cond = And(StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(629340277777777756388888888888889, 400000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Pow(Symbol('c'), Integer(2))), Pow(Symbol('y'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_45(c:sympy.Rational):
	#(c < -629340277777777756388888888888889/400000000000000000000000000000000) & (c**2 > 62673611111111116388888888888889/400000000000000000000000000000000)

	pre_cond = And(StrictLessThan(Symbol('c'), Rational(-629340277777777756388888888888889, 400000000000000000000000000000000)), StrictGreaterThan(Pow(Symbol('c'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_46(c:sympy.Rational):
	#(c + y**2 + 629340277777777756388888888888889/400000000000000000000000000000000 < 0) & (-c**2 + y**2 + 62673611111111116388888888888889/400000000000000000000000000000000 < 0)

	pre_cond = And(StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(629340277777777756388888888888889, 400000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Pow(Symbol('c'), Integer(2))), Pow(Symbol('y'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_47(c:sympy.Rational):
	#(c < -629340277777777756388888888888889/400000000000000000000000000000000) & (c**2 > 62673611111111116388888888888889/400000000000000000000000000000000)

	pre_cond = And(StrictLessThan(Symbol('c'), Rational(-629340277777777756388888888888889, 400000000000000000000000000000000)), StrictGreaterThan(Pow(Symbol('c'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_48(c:sympy.Rational):
	#(c + y**2 + 629340277777777756388888888888889/400000000000000000000000000000000 < 0) & (-c**2 + y**2 + 62673611111111116388888888888889/400000000000000000000000000000000 < 0)

	pre_cond = And(StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(629340277777777756388888888888889, 400000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Pow(Symbol('c'), Integer(2))), Pow(Symbol('y'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_49(c:sympy.Rational):
	#(c < -629340277777777756388888888888889/400000000000000000000000000000000) & (c**2 > 62673611111111116388888888888889/400000000000000000000000000000000)

	pre_cond = And(StrictLessThan(Symbol('c'), Rational(-629340277777777756388888888888889, 400000000000000000000000000000000)), StrictGreaterThan(Pow(Symbol('c'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_50(c:sympy.Rational):
	#(c + y**2 + 629340277777777756388888888888889/400000000000000000000000000000000 < 0) & (-c**2 + y**2 + 62673611111111116388888888888889/400000000000000000000000000000000 < 0)

	pre_cond = And(StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(629340277777777756388888888888889, 400000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Pow(Symbol('c'), Integer(2))), Pow(Symbol('y'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_51(c:sympy.Rational):
	#(c < -629340277777777756388888888888889/400000000000000000000000000000000) & (c**2 > 62673611111111116388888888888889/400000000000000000000000000000000)

	pre_cond = And(StrictLessThan(Symbol('c'), Rational(-629340277777777756388888888888889, 400000000000000000000000000000000)), StrictGreaterThan(Pow(Symbol('c'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_52(c:sympy.Rational):
	#(c + y**2 + 629340277777777756388888888888889/400000000000000000000000000000000 < 0) & (-c**2 + y**2 + 62673611111111116388888888888889/400000000000000000000000000000000 < 0)

	pre_cond = And(StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(629340277777777756388888888888889, 400000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Pow(Symbol('c'), Integer(2))), Pow(Symbol('y'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_53(c:sympy.Rational):
	#(c < -629340277777777756388888888888889/400000000000000000000000000000000) & (c**2 > 62673611111111116388888888888889/400000000000000000000000000000000)

	pre_cond = And(StrictLessThan(Symbol('c'), Rational(-629340277777777756388888888888889, 400000000000000000000000000000000)), StrictGreaterThan(Pow(Symbol('c'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_54(c:sympy.Rational):
	#(c + y**2 + 629340277777777756388888888888889/400000000000000000000000000000000 < 0) & (-c**2 + y**2 + 62673611111111116388888888888889/400000000000000000000000000000000 < 0)

	pre_cond = And(StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(629340277777777756388888888888889, 400000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Pow(Symbol('c'), Integer(2))), Pow(Symbol('y'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_55(c:sympy.Rational):
	#(c < -629340277777777756388888888888889/400000000000000000000000000000000) & (c**2 > 62673611111111116388888888888889/400000000000000000000000000000000)

	pre_cond = And(StrictLessThan(Symbol('c'), Rational(-629340277777777756388888888888889, 400000000000000000000000000000000)), StrictGreaterThan(Pow(Symbol('c'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_56(c:sympy.Rational):
	#(c + y**2 + 629340277777777756388888888888889/400000000000000000000000000000000 < 0) & (-c**2 + y**2 + 62673611111111116388888888888889/400000000000000000000000000000000 < 0)

	pre_cond = And(StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(629340277777777756388888888888889, 400000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Pow(Symbol('c'), Integer(2))), Pow(Symbol('y'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_57(c:sympy.Rational):
	#(c < -629340277777777756388888888888889/400000000000000000000000000000000) & (c**2 > 62673611111111116388888888888889/400000000000000000000000000000000)

	pre_cond = And(StrictLessThan(Symbol('c'), Rational(-629340277777777756388888888888889, 400000000000000000000000000000000)), StrictGreaterThan(Pow(Symbol('c'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_58(c:sympy.Rational):
	#(c + y**2 + 629340277777777756388888888888889/400000000000000000000000000000000 < 0) & (-c**2 + y**2 + 62673611111111116388888888888889/400000000000000000000000000000000 < 0)

	pre_cond = And(StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(629340277777777756388888888888889, 400000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Pow(Symbol('c'), Integer(2))), Pow(Symbol('y'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_59(c:sympy.Rational):
	#(c < -629340277777777756388888888888889/400000000000000000000000000000000) & (c**2 > 62673611111111116388888888888889/400000000000000000000000000000000)

	pre_cond = And(StrictLessThan(Symbol('c'), Rational(-629340277777777756388888888888889, 400000000000000000000000000000000)), StrictGreaterThan(Pow(Symbol('c'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_60(c:sympy.Rational):
	#(c + y**2 + 629340277777777756388888888888889/400000000000000000000000000000000 < 0) & (-c**2 + y**2 + 62673611111111116388888888888889/400000000000000000000000000000000 < 0)

	pre_cond = And(StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(629340277777777756388888888888889, 400000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Pow(Symbol('c'), Integer(2))), Pow(Symbol('y'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_61(c:sympy.Rational):
	#(c < -629340277777777756388888888888889/400000000000000000000000000000000) & (c**2 > 62673611111111116388888888888889/400000000000000000000000000000000)

	pre_cond = And(StrictLessThan(Symbol('c'), Rational(-629340277777777756388888888888889, 400000000000000000000000000000000)), StrictGreaterThan(Pow(Symbol('c'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_62(c:sympy.Rational):
	#(c + y**2 + 629340277777777756388888888888889/400000000000000000000000000000000 < 0) & (-c**2 + y**2 + 62673611111111116388888888888889/400000000000000000000000000000000 < 0)

	pre_cond = And(StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(629340277777777756388888888888889, 400000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Pow(Symbol('c'), Integer(2))), Pow(Symbol('y'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_63(c:sympy.Rational):
	#(c < -629340277777777756388888888888889/400000000000000000000000000000000) & (c**2 > 62673611111111116388888888888889/400000000000000000000000000000000)

	pre_cond = And(StrictLessThan(Symbol('c'), Rational(-629340277777777756388888888888889, 400000000000000000000000000000000)), StrictGreaterThan(Pow(Symbol('c'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_64(c:sympy.Rational):
	#(c + y**2 + 629340277777777756388888888888889/400000000000000000000000000000000 < 0) & (-c**2 + y**2 + 62673611111111116388888888888889/400000000000000000000000000000000 < 0)

	pre_cond = And(StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(629340277777777756388888888888889, 400000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Pow(Symbol('c'), Integer(2))), Pow(Symbol('y'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_65(c:sympy.Rational):
	#(c < -629340277777777756388888888888889/400000000000000000000000000000000) & (c**2 > 62673611111111116388888888888889/400000000000000000000000000000000)

	pre_cond = And(StrictLessThan(Symbol('c'), Rational(-629340277777777756388888888888889, 400000000000000000000000000000000)), StrictGreaterThan(Pow(Symbol('c'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_66(c:sympy.Rational):
	#(c + y**2 + 629340277777777756388888888888889/400000000000000000000000000000000 < 0) & (-c**2 + y**2 + 62673611111111116388888888888889/400000000000000000000000000000000 < 0)

	pre_cond = And(StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(629340277777777756388888888888889, 400000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Pow(Symbol('c'), Integer(2))), Pow(Symbol('y'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_67(c:sympy.Rational):
	#(c < -629340277777777756388888888888889/400000000000000000000000000000000) & (c**2 > 62673611111111116388888888888889/400000000000000000000000000000000)

	pre_cond = And(StrictLessThan(Symbol('c'), Rational(-629340277777777756388888888888889, 400000000000000000000000000000000)), StrictGreaterThan(Pow(Symbol('c'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_68(c:sympy.Rational):
	#(c + y**2 + 629340277777777756388888888888889/400000000000000000000000000000000 < 0) & (-c**2 + y**2 + 62673611111111116388888888888889/400000000000000000000000000000000 < 0)

	pre_cond = And(StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(629340277777777756388888888888889, 400000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Pow(Symbol('c'), Integer(2))), Pow(Symbol('y'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_69(c:sympy.Rational):
	#(c < -629340277777777756388888888888889/400000000000000000000000000000000) & (c**2 > 62673611111111116388888888888889/400000000000000000000000000000000)

	pre_cond = And(StrictLessThan(Symbol('c'), Rational(-629340277777777756388888888888889, 400000000000000000000000000000000)), StrictGreaterThan(Pow(Symbol('c'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_70(c:sympy.Rational):
	#(c + y**2 + 629340277777777756388888888888889/400000000000000000000000000000000 < 0) & (-c**2 + y**2 + 62673611111111116388888888888889/400000000000000000000000000000000 < 0)

	pre_cond = And(StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(629340277777777756388888888888889, 400000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Pow(Symbol('c'), Integer(2))), Pow(Symbol('y'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_71(c:sympy.Rational):
	#(c < -629340277777777756388888888888889/400000000000000000000000000000000) & (c**2 > 62673611111111116388888888888889/400000000000000000000000000000000)

	pre_cond = And(StrictLessThan(Symbol('c'), Rational(-629340277777777756388888888888889, 400000000000000000000000000000000)), StrictGreaterThan(Pow(Symbol('c'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_72(c:sympy.Rational):
	#(c + y**2 + 629340277777777756388888888888889/400000000000000000000000000000000 < 0) & (-c**2 + y**2 + 62673611111111116388888888888889/400000000000000000000000000000000 < 0)

	pre_cond = And(StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(629340277777777756388888888888889, 400000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Pow(Symbol('c'), Integer(2))), Pow(Symbol('y'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_73(c:sympy.Rational):
	#(c < -629340277777777756388888888888889/400000000000000000000000000000000) & (c**2 > 62673611111111116388888888888889/400000000000000000000000000000000)

	pre_cond = And(StrictLessThan(Symbol('c'), Rational(-629340277777777756388888888888889, 400000000000000000000000000000000)), StrictGreaterThan(Pow(Symbol('c'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_74(c:sympy.Rational):
	#(c + y**2 + 629340277777777756388888888888889/400000000000000000000000000000000 < 0) & (-c**2 + y**2 + 62673611111111116388888888888889/400000000000000000000000000000000 < 0)

	pre_cond = And(StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(629340277777777756388888888888889, 400000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Pow(Symbol('c'), Integer(2))), Pow(Symbol('y'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_75(c:sympy.Rational):
	#(c < -629340277777777756388888888888889/400000000000000000000000000000000) & (c**2 > 62673611111111116388888888888889/400000000000000000000000000000000)

	pre_cond = And(StrictLessThan(Symbol('c'), Rational(-629340277777777756388888888888889, 400000000000000000000000000000000)), StrictGreaterThan(Pow(Symbol('c'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_76(c:sympy.Rational):
	#(c + y**2 + 629340277777777756388888888888889/400000000000000000000000000000000 < 0) & (-c**2 + y**2 + 62673611111111116388888888888889/400000000000000000000000000000000 < 0)

	pre_cond = And(StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(629340277777777756388888888888889, 400000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Pow(Symbol('c'), Integer(2))), Pow(Symbol('y'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_77(c:sympy.Rational):
	#(c < -629340277777777756388888888888889/400000000000000000000000000000000) & (c**2 > 62673611111111116388888888888889/400000000000000000000000000000000)

	pre_cond = And(StrictLessThan(Symbol('c'), Rational(-629340277777777756388888888888889, 400000000000000000000000000000000)), StrictGreaterThan(Pow(Symbol('c'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_78(c:sympy.Rational):
	#(c + y**2 + 629340277777777756388888888888889/400000000000000000000000000000000 < 0) & (-c**2 + y**2 + 62673611111111116388888888888889/400000000000000000000000000000000 < 0)

	pre_cond = And(StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(629340277777777756388888888888889, 400000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Pow(Symbol('c'), Integer(2))), Pow(Symbol('y'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_79(c:sympy.Rational):
	#(c < -629340277777777756388888888888889/400000000000000000000000000000000) & (c**2 > 62673611111111116388888888888889/400000000000000000000000000000000)

	pre_cond = And(StrictLessThan(Symbol('c'), Rational(-629340277777777756388888888888889, 400000000000000000000000000000000)), StrictGreaterThan(Pow(Symbol('c'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_80(c:sympy.Rational):
	#(c + y**2 + 629340277777777756388888888888889/400000000000000000000000000000000 < 0) & (-c**2 + y**2 + 62673611111111116388888888888889/400000000000000000000000000000000 < 0)

	pre_cond = And(StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(629340277777777756388888888888889, 400000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Pow(Symbol('c'), Integer(2))), Pow(Symbol('y'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_81(c:sympy.Rational):
	#(c < -629340277777777756388888888888889/400000000000000000000000000000000) & (c**2 > 62673611111111116388888888888889/400000000000000000000000000000000)

	pre_cond = And(StrictLessThan(Symbol('c'), Rational(-629340277777777756388888888888889, 400000000000000000000000000000000)), StrictGreaterThan(Pow(Symbol('c'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_82(c:sympy.Rational):
	#(c + y**2 + 629340277777777756388888888888889/400000000000000000000000000000000 < 0) & (-c**2 + y**2 + 62673611111111116388888888888889/400000000000000000000000000000000 < 0)

	pre_cond = And(StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(629340277777777756388888888888889, 400000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Pow(Symbol('c'), Integer(2))), Pow(Symbol('y'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_83(c:sympy.Rational):
	#(c < -629340277777777756388888888888889/400000000000000000000000000000000) & (c**2 > 62673611111111116388888888888889/400000000000000000000000000000000)

	pre_cond = And(StrictLessThan(Symbol('c'), Rational(-629340277777777756388888888888889, 400000000000000000000000000000000)), StrictGreaterThan(Pow(Symbol('c'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_84(c:sympy.Rational):
	#(c + y**2 + 629340277777777756388888888888889/400000000000000000000000000000000 < 0) & (-c**2 + y**2 + 62673611111111116388888888888889/400000000000000000000000000000000 < 0)

	pre_cond = And(StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(629340277777777756388888888888889, 400000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Pow(Symbol('c'), Integer(2))), Pow(Symbol('y'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_85(c:sympy.Rational):
	#(c < -629340277777777756388888888888889/400000000000000000000000000000000) & (c**2 > 62673611111111116388888888888889/400000000000000000000000000000000)

	pre_cond = And(StrictLessThan(Symbol('c'), Rational(-629340277777777756388888888888889, 400000000000000000000000000000000)), StrictGreaterThan(Pow(Symbol('c'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_86(c:sympy.Rational):
	#(c + y**2 + 629340277777777756388888888888889/400000000000000000000000000000000 < 0) & (-c**2 + y**2 + 62673611111111116388888888888889/400000000000000000000000000000000 < 0)

	pre_cond = And(StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(629340277777777756388888888888889, 400000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Pow(Symbol('c'), Integer(2))), Pow(Symbol('y'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_87(c:sympy.Rational):
	#(c < -629340277777777756388888888888889/400000000000000000000000000000000) & (c**2 > 62673611111111116388888888888889/400000000000000000000000000000000)

	pre_cond = And(StrictLessThan(Symbol('c'), Rational(-629340277777777756388888888888889, 400000000000000000000000000000000)), StrictGreaterThan(Pow(Symbol('c'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_88(c:sympy.Rational):
	#(c + y**2 + 629340277777777756388888888888889/400000000000000000000000000000000 < 0) & (-c**2 + y**2 + 62673611111111116388888888888889/400000000000000000000000000000000 < 0)

	pre_cond = And(StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(629340277777777756388888888888889, 400000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Pow(Symbol('c'), Integer(2))), Pow(Symbol('y'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_89(c:sympy.Rational):
	#(c < -629340277777777756388888888888889/400000000000000000000000000000000) & (c**2 > 62673611111111116388888888888889/400000000000000000000000000000000)

	pre_cond = And(StrictLessThan(Symbol('c'), Rational(-629340277777777756388888888888889, 400000000000000000000000000000000)), StrictGreaterThan(Pow(Symbol('c'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_90(c:sympy.Rational):
	#(c + y**2 + 629340277777777756388888888888889/400000000000000000000000000000000 < 0) & (-c**2 + y**2 + 62673611111111116388888888888889/400000000000000000000000000000000 < 0)

	pre_cond = And(StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(629340277777777756388888888888889, 400000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Pow(Symbol('c'), Integer(2))), Pow(Symbol('y'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_91(c:sympy.Rational):
	#(c < -629340277777777756388888888888889/400000000000000000000000000000000) & (c**2 > 62673611111111116388888888888889/400000000000000000000000000000000)

	pre_cond = And(StrictLessThan(Symbol('c'), Rational(-629340277777777756388888888888889, 400000000000000000000000000000000)), StrictGreaterThan(Pow(Symbol('c'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_92(c:sympy.Rational):
	#(c + y**2 + 629340277777777756388888888888889/400000000000000000000000000000000 < 0) & (-c**2 + y**2 + 62673611111111116388888888888889/400000000000000000000000000000000 < 0)

	pre_cond = And(StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(629340277777777756388888888888889, 400000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Pow(Symbol('c'), Integer(2))), Pow(Symbol('y'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_93(c:sympy.Rational):
	#(c < -629340277777777756388888888888889/400000000000000000000000000000000) & (c**2 > 62673611111111116388888888888889/400000000000000000000000000000000)

	pre_cond = And(StrictLessThan(Symbol('c'), Rational(-629340277777777756388888888888889, 400000000000000000000000000000000)), StrictGreaterThan(Pow(Symbol('c'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_94(c:sympy.Rational):
	#(c + y**2 + 629340277777777756388888888888889/400000000000000000000000000000000 < 0) & (-c**2 + y**2 + 62673611111111116388888888888889/400000000000000000000000000000000 < 0)

	pre_cond = And(StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(629340277777777756388888888888889, 400000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Pow(Symbol('c'), Integer(2))), Pow(Symbol('y'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_95(c:sympy.Rational):
	#(c < -629340277777777756388888888888889/400000000000000000000000000000000) & (c**2 > 62673611111111116388888888888889/400000000000000000000000000000000)

	pre_cond = And(StrictLessThan(Symbol('c'), Rational(-629340277777777756388888888888889, 400000000000000000000000000000000)), StrictGreaterThan(Pow(Symbol('c'), Integer(2)), Rational(62673611111111116388888888888889, 400000000000000000000000000000000)))