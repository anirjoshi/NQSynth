import sympy
from sympy import *

def pre_condition_0(y:sympy.Rational):
	#((y >= 3*sqrt(7)/8) | (y > -sqrt(1599)/8)) & ((y >= 3*sqrt(7)/8) | (y < -3*sqrt(7)/8)) & ((y <= sqrt(1599)/8) | (y > -sqrt(1599)/8)) & ((y <= sqrt(1599)/8) | (y < -3*sqrt(7)/8))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(3, 8), Pow(Integer(7), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 8), Pow(Integer(1599), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(3, 8), Pow(Integer(7), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 8), Pow(Integer(7), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 8), Pow(Integer(1599), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 8), Pow(Integer(1599), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 8), Pow(Integer(1599), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 8), Pow(Integer(7), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(y:sympy.Rational):
	#(y >= -2*sqrt(6)) & (y <= 2*sqrt(6))

	pre_cond = And(GreaterThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(6), Rational(1, 2)))), LessThan(Symbol('y'), Mul(Integer(2), Pow(Integer(6), Rational(1, 2)))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_4(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_5(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_6(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_7(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_8(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_9(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_10(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_11(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_12(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_13(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_14(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_15(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_16(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_17(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_18(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_19(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_20(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_21(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_22(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_23(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_24(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_25(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_26(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_27(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_28(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_29(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_30(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_31(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_32(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_33(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_34(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_35(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_36(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_37(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_38(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_39(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_40(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_41(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_42(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_43(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_44(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_45(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_46(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_47(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_48(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_49(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_50(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_51(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_52(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_53(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_54(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_55(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_56(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_57(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_58(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_59(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_60(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_61(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_62(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_63(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_64(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_65(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_66(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_67(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_68(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_69(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_70(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_71(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_72(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_73(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_74(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_75(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_76(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_77(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_78(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_79(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_80(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_81(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_82(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_83(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_84(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_85(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_86(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_87(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_88(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_89(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_90(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_91(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_92(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_93(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_94(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_95(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_96(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_97(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_98(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_99(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_100(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_101(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_102(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_103(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_104(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_105(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_106(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_107(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_108(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_109(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_110(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_111(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_112(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_113(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_114(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_115(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_116(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_117(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_118(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_119(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_120(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_121(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_122(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_123(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_124(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_125(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_126(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_127(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_128(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_129(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_130(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_131(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_132(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_133(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_134(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_135(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_136(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_137(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_138(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_139(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_140(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_141(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_142(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_143(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_144(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_145(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_146(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_147(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_148(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_149(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_150(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_151(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_152(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_153(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_154(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_155(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_156(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_157(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_158(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_159(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_160(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_161(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_162(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_163(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_164(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_165(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_166(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_167(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_168(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_169(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_170(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_171(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_172(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_173(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_174(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_175(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_176(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_177(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_178(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_179(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_180(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_181(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_182(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_183(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_184(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_185(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_186(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_187(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_188(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_189(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_190(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_191(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_192(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_193(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_194(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_195(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_196(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_197(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_198(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_199(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_200(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_201(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_202(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_203(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_204(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_205(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_206(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_207(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_208(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_209(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_210(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_211(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_212(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_213(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_214(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_215(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_216(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_217(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_218(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_219(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_220(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_221(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_222(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_223(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_224(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_225(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_226(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_227(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_228(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_229(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_230(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_231(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_232(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_233(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_234(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_235(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_236(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_237(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_238(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_239(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_240(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_241(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_242(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_243(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_244(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_245(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_246(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_247(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_248(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_249(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_250(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_251(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_252(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_253(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_254(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_255(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_256(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_257(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_258(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_259(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_260(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_261(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_262(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_263(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_264(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_265(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_266(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_267(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_268(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_269(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_270(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_271(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_272(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_273(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_274(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_275(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_276(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_277(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_278(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_279(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_280(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_281(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_282(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_283(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_284(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_285(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_286(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_287(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_288(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_289(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_290(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_291(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_292(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_293(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_294(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_295(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_296(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_297(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_298(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_299(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_300(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_301(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_302(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_303(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_304(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_305(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_306(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_307(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_308(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_309(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_310(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_311(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_312(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_313(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_314(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_315(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_316(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_317(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_318(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_319(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_320(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_321(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_322(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_323(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_324(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_325(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_326(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_327(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_328(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_329(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_330(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_331(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_332(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_333(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_334(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_335(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_336(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_337(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_338(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_339(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_340(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_341(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_342(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_343(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_344(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_345(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_346(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_347(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_348(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_349(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_350(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_351(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_352(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_353(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_354(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_355(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_356(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_357(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_358(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_359(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_360(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_361(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_362(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_363(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_364(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_365(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_366(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_367(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_368(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_369(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_370(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_371(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_372(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_373(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_374(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_375(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_376(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_377(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_378(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_379(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_380(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_381(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_382(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_383(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_384(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_385(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_386(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_387(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_388(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_389(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_390(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_391(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_392(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_393(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_394(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_395(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_396(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_397(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_398(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_399(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_400(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_401(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_402(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_403(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_404(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_405(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_406(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_407(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_408(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_409(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_410(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_411(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_412(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_413(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_414(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_415(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_416(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_417(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_418(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_419(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_420(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_421(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_422(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_423(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_424(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_425(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_426(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_427(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_428(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_429(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_430(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_431(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_432(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_433(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_434(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_435(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_436(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_437(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_438(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_439(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_440(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_441(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_442(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_443(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_444(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_445(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_446(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_447(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_448(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_449(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_450(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_451(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_452(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_453(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_454(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_455(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_456(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_457(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_458(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_459(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_460(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_461(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_462(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_463(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_464(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_465(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_466(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_467(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_468(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_469(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_470(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_471(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_472(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_473(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_474(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_475(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_476(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_477(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_478(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_479(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_480(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_481(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_482(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_483(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_484(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_485(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_486(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_487(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_488(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_489(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_490(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_491(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_492(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_493(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_494(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_495(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_496(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_497(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_498(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_499(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_500(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_501(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_502(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_503(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_504(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_505(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_506(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_507(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_508(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_509(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_510(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_511(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_512(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_513(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_514(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_515(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_516(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_517(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_518(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_519(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_520(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_521(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_522(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_523(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_524(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_525(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_526(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_527(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_528(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_529(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_530(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_531(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_532(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_533(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_534(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_535(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_536(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_537(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_538(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_539(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_540(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_541(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_542(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_543(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_544(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_545(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_546(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_547(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_548(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_549(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_550(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_551(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_552(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_553(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_554(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_555(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_556(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_557(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_558(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_559(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_560(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_561(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_562(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_563(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_564(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_565(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_566(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_567(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_568(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_569(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_570(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_571(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_572(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_573(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_574(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_575(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_576(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_577(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_578(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_579(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_580(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_581(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_582(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_583(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_584(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_585(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_586(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_587(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_588(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_589(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_590(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_591(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_592(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_593(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_594(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_595(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_596(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_597(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_598(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_599(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_600(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_601(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_602(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_603(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_604(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_605(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_606(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_607(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_608(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_609(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_610(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_611(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_612(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_613(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_614(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_615(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_616(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_617(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_618(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_619(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_620(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_621(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_622(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_623(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_624(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_625(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_626(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_627(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_628(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_629(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_630(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_631(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_632(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_633(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_634(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_635(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_636(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_637(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_638(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_639(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_640(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_641(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_642(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_643(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_644(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_645(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_646(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_647(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_648(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_649(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_650(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_651(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_652(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_653(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_654(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_655(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_656(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_657(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_658(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_659(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_660(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_661(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_662(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_663(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_664(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_665(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_666(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_667(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_668(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_669(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_670(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_671(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_672(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_673(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_674(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_675(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_676(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_677(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_678(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_679(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_680(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_681(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_682(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_683(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_684(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_685(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_686(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_687(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_688(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_689(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_690(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_691(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_692(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_693(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_694(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_695(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_696(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_697(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_698(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_699(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_700(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_701(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_702(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_703(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_704(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_705(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_706(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_707(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_708(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_709(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_710(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_711(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_712(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_713(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_714(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_715(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_716(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_717(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_718(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_719(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_720(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_721(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_722(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_723(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_724(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_725(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_726(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_727(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_728(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_729(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_730(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_731(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_732(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_733(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_734(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_735(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_736(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_737(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_738(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_739(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_740(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_741(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_742(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_743(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_744(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_745(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_746(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_747(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_748(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_749(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_750(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_751(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_752(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_753(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_754(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_755(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_756(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_757(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_758(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_759(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_760(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_761(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_762(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_763(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_764(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_765(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_766(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_767(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_768(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_769(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_770(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_771(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_772(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_773(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_774(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_775(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_776(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_777(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_778(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_779(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_780(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_781(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_782(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_783(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_784(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_785(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_786(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_787(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_788(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_789(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_790(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_791(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_792(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_793(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_794(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_795(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_796(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_797(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_798(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_799(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_800(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_801(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_802(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_803(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_804(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_805(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_806(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_807(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_808(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_809(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_810(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_811(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_812(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_813(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_814(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_815(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_816(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_817(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_818(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_819(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_820(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_821(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_822(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_823(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_824(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_825(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_826(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_827(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_828(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_829(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_830(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_831(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_832(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_833(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_834(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_835(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_836(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_837(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_838(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_839(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_840(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_841(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_842(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_843(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_844(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_845(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_846(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_847(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_848(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_849(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_850(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_851(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_852(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_853(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_854(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_855(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_856(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_857(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_858(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_859(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_860(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_861(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_862(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_863(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_864(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_865(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_866(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_867(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_868(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_869(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_870(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_871(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_872(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_873(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_874(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_875(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_876(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_877(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_878(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_879(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_880(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_881(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_882(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_883(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_884(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_885(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_886(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_887(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_888(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_889(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_890(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_891(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_892(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_893(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_894(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_895(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_896(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_897(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_898(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_899(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_900(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_901(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_902(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_903(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_904(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_905(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_906(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_907(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_908(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_909(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_910(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_911(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_912(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_913(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_914(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_915(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_916(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_917(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_918(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_919(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_920(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_921(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_922(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_923(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_924(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_925(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_926(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_927(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_928(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_929(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_930(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_931(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_932(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_933(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_934(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_935(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_936(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_937(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_938(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_939(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_940(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_941(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_942(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_943(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_944(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_945(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_946(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_947(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_948(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_949(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_950(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_951(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_952(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_953(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_954(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_955(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_956(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_957(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_958(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_959(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_960(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_961(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_962(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_963(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_964(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_965(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_966(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_967(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_968(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_969(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_970(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_971(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_972(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_973(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_974(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_975(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_976(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_977(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_978(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_979(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_980(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_981(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_982(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_983(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_984(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_985(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_986(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_987(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_988(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_989(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_990(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_991(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_992(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_993(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_994(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_995(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_996(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_997(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_998(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_999(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1000(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1001(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1002(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1003(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1004(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1005(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1006(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1007(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1008(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1009(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1010(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1011(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1012(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1013(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1014(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1015(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1016(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1017(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1018(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1019(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1020(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1021(y:sympy.Rational):
	#((y >= 1) | (y > -5)) & ((y >= 1) | (y < -1)) & ((y <= 5) | (y > -5)) & ((y <= 5) | (y < -1))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Integer(1)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(GreaterThan(Symbol('y'), Integer(1)), StrictLessThan(Symbol('y'), Integer(-1))), Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Integer(-1))))