import sympy
from sympy import *

def pre_condition_0(y:sympy.Rational):
	#((y >= sqrt(767)/8) | (y > -sqrt(1599)/8)) & ((y >= sqrt(767)/8) | (y < -sqrt(767)/8)) & ((y <= sqrt(1599)/8) | (y > -sqrt(1599)/8)) & ((y <= sqrt(1599)/8) | (y < -sqrt(767)/8))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 8), Pow(Integer(767), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 8), Pow(Integer(1599), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 8), Pow(Integer(767), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 8), Pow(Integer(767), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 8), Pow(Integer(1599), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 8), Pow(Integer(1599), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 8), Pow(Integer(1599), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 8), Pow(Integer(767), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(y:sympy.Rational):
	#(y >= -3) & (y <= 3)

	pre_cond = And(GreaterThan(Symbol('y'), Integer(-3)), LessThan(Symbol('y'), Integer(3)))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(y:sympy.Rational):
	#((y <= sqrt(21)) | (y > -sqrt(21))) & ((y <= sqrt(21)) | (y < -2*sqrt(2))) & ((y >= 2*sqrt(2)) | (y > -sqrt(21))) & ((y >= 2*sqrt(2)) | (y < -2*sqrt(2)))

	pre_cond = And(Or(LessThan(Symbol('y'), Pow(Integer(21), Rational(1, 2))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Pow(Integer(21), Rational(1, 2))))), Or(LessThan(Symbol('y'), Pow(Integer(21), Rational(1, 2))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(2), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(2), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Pow(Integer(21), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(2), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(2), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_4(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_5(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_6(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_7(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_8(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_9(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_10(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_11(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_12(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_13(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_14(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_15(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_16(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_17(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_18(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_19(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_20(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_21(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_22(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_23(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_24(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_25(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_26(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_27(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_28(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_29(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_30(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_31(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_32(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_33(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_34(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_35(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_36(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_37(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_38(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_39(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_40(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_41(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_42(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_43(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_44(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_45(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_46(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_47(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_48(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_49(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_50(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_51(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_52(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_53(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_54(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_55(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_56(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_57(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_58(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_59(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_60(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_61(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_62(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_63(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_64(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_65(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_66(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_67(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_68(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_69(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_70(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_71(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_72(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_73(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_74(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_75(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_76(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_77(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_78(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_79(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_80(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_81(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_82(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_83(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_84(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_85(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_86(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_87(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_88(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_89(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_90(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_91(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_92(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_93(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_94(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_95(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_96(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_97(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_98(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_99(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_100(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_101(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_102(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_103(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_104(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_105(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_106(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_107(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_108(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_109(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_110(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_111(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_112(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_113(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_114(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_115(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_116(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_117(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_118(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_119(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_120(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_121(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_122(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_123(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_124(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_125(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_126(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_127(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_128(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_129(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_130(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_131(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_132(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_133(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_134(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_135(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_136(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_137(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_138(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_139(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_140(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_141(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_142(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_143(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_144(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_145(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_146(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_147(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_148(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_149(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_150(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_151(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_152(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_153(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_154(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_155(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_156(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_157(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_158(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_159(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_160(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_161(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_162(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_163(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_164(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_165(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_166(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_167(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_168(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_169(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_170(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_171(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_172(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_173(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_174(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_175(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_176(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_177(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_178(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_179(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_180(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_181(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_182(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_183(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_184(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_185(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_186(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_187(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_188(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_189(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_190(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_191(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_192(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_193(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_194(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_195(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_196(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_197(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_198(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_199(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_200(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_201(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_202(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_203(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_204(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_205(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_206(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_207(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_208(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_209(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_210(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_211(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_212(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_213(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_214(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_215(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_216(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_217(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_218(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_219(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_220(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_221(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_222(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_223(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_224(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_225(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_226(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_227(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_228(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_229(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_230(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_231(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_232(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_233(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_234(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_235(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_236(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_237(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_238(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_239(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_240(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_241(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_242(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_243(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_244(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_245(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_246(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_247(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_248(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_249(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_250(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_251(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_252(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_253(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_254(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_255(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_256(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_257(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_258(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_259(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_260(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_261(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_262(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_263(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_264(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_265(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_266(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_267(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_268(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_269(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_270(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_271(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_272(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_273(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_274(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_275(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_276(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_277(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_278(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_279(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_280(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_281(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_282(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_283(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_284(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_285(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_286(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_287(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_288(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_289(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_290(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_291(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_292(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_293(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_294(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_295(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_296(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_297(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_298(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_299(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_300(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_301(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_302(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_303(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_304(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_305(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_306(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_307(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_308(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_309(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_310(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_311(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_312(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_313(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_314(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_315(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_316(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_317(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_318(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_319(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_320(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_321(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_322(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_323(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_324(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_325(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_326(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_327(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_328(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_329(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_330(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_331(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_332(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_333(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_334(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_335(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_336(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_337(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_338(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_339(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_340(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_341(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_342(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_343(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_344(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_345(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_346(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_347(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_348(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_349(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_350(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_351(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_352(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_353(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_354(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_355(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_356(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_357(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_358(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_359(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_360(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_361(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_362(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_363(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_364(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_365(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_366(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_367(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_368(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_369(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_370(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_371(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_372(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_373(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_374(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_375(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_376(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_377(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_378(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_379(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_380(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_381(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_382(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_383(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_384(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_385(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_386(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_387(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_388(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_389(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_390(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_391(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_392(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_393(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_394(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_395(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_396(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_397(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_398(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_399(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_400(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_401(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_402(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_403(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_404(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_405(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_406(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_407(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_408(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_409(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_410(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_411(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_412(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_413(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_414(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_415(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_416(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_417(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_418(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_419(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_420(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_421(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_422(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_423(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_424(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_425(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_426(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_427(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_428(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_429(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_430(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_431(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_432(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_433(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_434(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_435(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_436(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_437(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_438(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_439(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_440(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_441(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_442(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_443(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_444(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_445(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_446(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_447(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_448(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_449(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_450(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_451(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_452(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_453(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_454(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_455(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_456(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_457(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_458(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_459(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_460(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_461(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_462(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_463(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_464(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_465(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_466(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_467(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_468(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_469(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_470(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_471(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_472(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_473(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_474(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_475(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_476(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_477(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_478(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_479(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_480(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_481(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_482(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_483(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_484(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_485(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_486(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_487(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_488(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_489(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_490(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_491(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_492(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_493(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_494(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_495(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_496(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_497(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_498(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_499(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_500(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_501(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_502(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_503(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))

	pre_cond = And(Or(LessThan(Symbol('y'), Integer(5)), StrictGreaterThan(Symbol('y'), Integer(-5))), Or(LessThan(Symbol('y'), Integer(5)), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Integer(-5)), GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Integer(2), Pow(Integer(3), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Integer(2), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_504(y:sympy.Rational):
	#((y <= 5) | (y > -5)) & ((y <= 5) | (y < -2*sqrt(3))) & ((y > -5) | (y >= 2*sqrt(3))) & ((y >= 2*sqrt(3)) | (y < -2*sqrt(3)))