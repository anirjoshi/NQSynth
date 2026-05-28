import sympy
from sympy import *

def pre_condition_0(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 7/4) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(7, 4)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1/4) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1, 4)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 7/64) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(7, 64)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_4(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 17/256) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(17, 256)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_5(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 23/1024) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(23, 1024)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_6(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 89/4096) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(89, 4096)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_7(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 7/16384) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(7, 16384)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_8(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_9(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_10(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_11(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_12(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_13(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_14(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_15(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_16(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_17(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_18(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_19(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_20(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_21(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_22(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_23(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_24(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_25(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_26(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_27(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_28(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_29(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_30(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_31(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_32(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_33(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_34(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_35(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_36(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_37(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_38(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_39(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_40(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_41(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_42(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_43(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_44(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_45(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_46(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_47(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_48(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_49(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_50(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_51(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_52(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_53(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_54(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_55(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_56(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_57(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_58(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_59(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_60(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_61(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_62(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_63(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_64(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_65(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_66(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_67(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_68(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_69(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_70(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_71(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_72(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_73(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_74(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_75(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_76(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_77(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_78(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_79(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_80(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_81(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_82(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_83(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_84(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_85(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_86(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_87(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_88(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_89(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_90(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_91(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_92(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_93(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_94(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_95(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_96(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_97(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_98(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_99(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_100(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_101(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_102(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_103(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_104(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_105(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_106(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_107(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_108(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_109(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_110(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_111(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_112(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_113(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_114(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_115(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_116(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_117(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_118(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_119(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_120(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_121(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_122(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_123(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_124(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_125(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_126(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_127(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_128(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_129(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_130(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_131(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_132(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_133(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_134(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_135(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_136(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_137(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_138(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_139(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_140(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_141(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_142(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_143(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_144(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_145(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_146(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_147(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_148(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_149(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_150(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_151(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_152(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_153(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_154(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_155(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_156(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_157(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_158(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_159(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_160(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_161(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_162(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_163(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_164(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_165(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_166(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_167(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_168(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_169(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_170(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_171(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_172(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_173(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_174(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_175(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_176(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_177(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_178(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_179(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_180(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_181(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_182(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_183(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_184(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_185(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_186(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_187(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_188(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_189(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_190(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_191(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_192(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_193(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_194(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_195(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_196(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_197(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_198(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_199(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_200(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_201(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_202(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_203(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_204(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_205(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_206(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_207(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_208(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_209(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_210(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_211(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_212(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_213(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_214(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_215(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_216(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_217(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_218(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_219(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_220(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_221(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_222(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_223(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_224(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_225(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_226(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_227(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_228(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_229(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_230(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_231(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_232(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_233(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_234(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_235(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_236(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_237(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_238(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_239(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_240(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_241(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_242(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_243(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_244(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_245(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_246(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_247(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_248(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_249(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_250(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_251(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_252(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_253(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_254(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_255(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_256(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_257(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_258(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_259(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_260(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_261(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_262(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_263(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_264(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_265(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_266(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_267(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_268(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_269(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_270(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_271(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_272(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_273(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_274(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_275(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_276(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_277(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_278(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_279(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_280(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_281(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_282(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_283(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_284(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_285(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_286(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_287(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_288(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_289(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_290(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_291(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_292(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_293(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_294(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_295(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_296(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_297(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_298(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_299(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_300(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_301(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_302(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_303(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_304(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_305(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_306(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_307(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_308(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_309(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_310(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_311(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_312(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_313(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_314(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_315(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_316(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_317(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_318(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_319(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_320(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_321(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_322(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_323(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_324(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_325(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_326(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_327(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_328(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_329(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_330(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_331(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_332(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_333(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_334(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_335(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_336(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_337(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_338(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_339(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_340(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_341(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_342(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_343(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_344(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_345(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_346(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_347(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_348(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_349(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_350(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_351(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_352(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_353(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_354(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_355(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_356(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_357(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_358(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_359(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_360(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_361(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_362(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_363(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_364(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_365(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_366(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_367(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_368(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_369(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_370(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_371(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_372(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_373(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_374(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_375(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_376(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_377(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_378(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_379(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_380(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_381(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_382(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_383(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_384(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_385(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_386(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_387(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_388(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_389(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_390(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_391(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_392(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_393(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_394(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_395(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_396(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_397(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_398(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_399(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_400(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_401(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_402(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_403(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_404(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_405(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_406(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_407(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_408(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_409(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_410(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_411(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_412(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_413(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_414(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_415(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_416(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_417(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_418(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_419(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_420(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_421(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_422(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_423(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_424(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_425(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_426(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_427(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_428(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_429(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_430(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_431(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_432(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_433(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_434(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_435(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_436(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_437(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_438(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_439(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_440(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_441(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_442(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_443(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_444(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_445(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_446(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_447(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_448(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_449(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_450(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_451(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_452(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_453(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_454(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_455(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_456(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_457(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_458(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_459(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_460(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_461(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_462(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_463(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_464(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_465(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_466(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_467(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_468(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_469(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_470(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_471(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_472(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_473(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_474(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_475(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_476(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_477(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_478(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_479(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_480(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_481(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_482(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_483(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_484(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_485(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_486(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_487(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_488(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_489(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_490(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_491(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_492(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_493(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_494(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_495(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_496(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_497(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_498(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_499(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_500(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_501(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_502(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_503(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_504(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_505(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_506(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_507(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_508(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_509(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_510(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_511(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_512(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_513(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_514(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_515(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_516(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_517(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_518(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_519(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_520(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_521(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_522(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_523(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_524(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_525(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_526(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_527(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_528(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_529(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_530(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_531(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_532(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_533(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_534(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_535(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_536(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_537(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_538(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_539(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_540(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_541(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_542(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_543(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_544(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_545(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_546(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_547(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_548(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_549(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_550(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_551(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_552(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_553(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_554(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_555(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_556(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_557(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_558(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_559(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_560(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_561(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_562(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_563(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_564(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_565(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_566(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_567(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_568(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_569(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_570(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_571(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_572(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_573(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_574(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_575(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_576(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_577(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_578(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_579(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_580(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_581(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_582(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_583(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_584(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_585(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_586(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_587(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_588(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_589(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_590(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_591(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_592(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_593(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_594(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_595(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_596(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4417/16777216) & (delta >= b**3 - 3) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4417, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(b:sympy.Rational, delta:sympy.Rational, a:sympy.Rational):
	# (0 <= delta) & (a**2 - 2 <= delta) & (b**3 - 3 <= delta) & (2 - a**2 <= delta) & (3 - b**3 <= delta)

	post_cond =  And(LessThan(Integer(0), Symbol('delta')), LessThan(Add(Pow(Symbol('a'), Integer(2)), Integer(-2)), Symbol('delta')), LessThan(Add(Pow(Symbol('b'), Integer(3)), Integer(-3)), Symbol('delta')), LessThan(Add(Integer(2), Mul(Integer(-1), Pow(Symbol('a'), Integer(2)))), Symbol('delta')), LessThan(Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3)))), Symbol('delta')))

	eval = post_cond.subs( { 'b':b, 'delta':delta, 'a':a })

	return eval == sympy.logic.boolalg.BooleanTrue





if __name__=="__main__":
	
	ip_0=int(input("enter integer numerator of b:\n"))
	ip_1=int(input("enter integer denominator of b:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	b=sympy.Rational(ip_0,ip_1)
	
	
	ip_0=int(input("enter integer numerator of delta:\n"))
	ip_1=int(input("enter integer denominator of delta:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	delta=sympy.Rational(ip_0,ip_1)
	
	
	
	
	if pre_condition_0(b=b,delta=delta)==True:
		print("pre_condition_0 SAT")
		print('delta = 4')
		print('a = 1/2')
		print('b = 1/8')
		exit(0)
	
	
	if pre_condition_1(b=b,delta=delta)==True:
		print("pre_condition_1 SAT")
		print('delta = 1')
		print('a = -1')
		print('b = 3/2')
		exit(0)
	
	
	if pre_condition_2(b=b,delta=delta)==True:
		print("pre_condition_2 SAT")
		print('delta = 1/2')
		print('a = -3/2')
		print('b = 3/2')
		exit(0)
	
	
	if pre_condition_3(b=b,delta=delta)==True:
		print("pre_condition_3 SAT")
		print('delta = 1/8')
		print('a = -11/8')
		print('b = 23/16')
		exit(0)
	
	
	if pre_condition_4(b=b,delta=delta)==True:
		print("pre_condition_4 SAT")
		print('delta = 3/32')
		print('a = -23/16')
		print('b = 23/16')
		exit(0)
	
	
	if pre_condition_5(b=b,delta=delta)==True:
		print("pre_condition_5 SAT")
		print('delta = 1/16')
		print('a = -45/32')
		print('b = 23/16')
		exit(0)
	
	
	if pre_condition_6(b=b,delta=delta)==True:
		print("pre_condition_6 SAT")
		print('delta = 45/2048')
		print('a = -91/64')
		print('b = 185/128')
		exit(0)
	
	
	if pre_condition_7(b=b,delta=delta)==True:
		print("pre_condition_7 SAT")
		print('delta = 5/256')
		print('a = -181/128')
		print('b = 185/128')
		exit(0)
	
	
	if pre_condition_8(b=b,delta=delta)==True:
		print("pre_condition_8 SAT")
		print('delta = 3/8192')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_9(b=b,delta=delta)==True:
		print("pre_condition_9 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_10(b=b,delta=delta)==True:
		print("pre_condition_10 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_11(b=b,delta=delta)==True:
		print("pre_condition_11 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_12(b=b,delta=delta)==True:
		print("pre_condition_12 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_13(b=b,delta=delta)==True:
		print("pre_condition_13 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_14(b=b,delta=delta)==True:
		print("pre_condition_14 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_15(b=b,delta=delta)==True:
		print("pre_condition_15 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_16(b=b,delta=delta)==True:
		print("pre_condition_16 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_17(b=b,delta=delta)==True:
		print("pre_condition_17 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_18(b=b,delta=delta)==True:
		print("pre_condition_18 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_19(b=b,delta=delta)==True:
		print("pre_condition_19 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_20(b=b,delta=delta)==True:
		print("pre_condition_20 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_21(b=b,delta=delta)==True:
		print("pre_condition_21 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_22(b=b,delta=delta)==True:
		print("pre_condition_22 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_23(b=b,delta=delta)==True:
		print("pre_condition_23 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_24(b=b,delta=delta)==True:
		print("pre_condition_24 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_25(b=b,delta=delta)==True:
		print("pre_condition_25 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_26(b=b,delta=delta)==True:
		print("pre_condition_26 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_27(b=b,delta=delta)==True:
		print("pre_condition_27 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_28(b=b,delta=delta)==True:
		print("pre_condition_28 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_29(b=b,delta=delta)==True:
		print("pre_condition_29 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_30(b=b,delta=delta)==True:
		print("pre_condition_30 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_31(b=b,delta=delta)==True:
		print("pre_condition_31 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_32(b=b,delta=delta)==True:
		print("pre_condition_32 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_33(b=b,delta=delta)==True:
		print("pre_condition_33 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_34(b=b,delta=delta)==True:
		print("pre_condition_34 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_35(b=b,delta=delta)==True:
		print("pre_condition_35 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_36(b=b,delta=delta)==True:
		print("pre_condition_36 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_37(b=b,delta=delta)==True:
		print("pre_condition_37 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_38(b=b,delta=delta)==True:
		print("pre_condition_38 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_39(b=b,delta=delta)==True:
		print("pre_condition_39 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_40(b=b,delta=delta)==True:
		print("pre_condition_40 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_41(b=b,delta=delta)==True:
		print("pre_condition_41 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_42(b=b,delta=delta)==True:
		print("pre_condition_42 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_43(b=b,delta=delta)==True:
		print("pre_condition_43 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_44(b=b,delta=delta)==True:
		print("pre_condition_44 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_45(b=b,delta=delta)==True:
		print("pre_condition_45 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_46(b=b,delta=delta)==True:
		print("pre_condition_46 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_47(b=b,delta=delta)==True:
		print("pre_condition_47 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_48(b=b,delta=delta)==True:
		print("pre_condition_48 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_49(b=b,delta=delta)==True:
		print("pre_condition_49 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_50(b=b,delta=delta)==True:
		print("pre_condition_50 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_51(b=b,delta=delta)==True:
		print("pre_condition_51 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_52(b=b,delta=delta)==True:
		print("pre_condition_52 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_53(b=b,delta=delta)==True:
		print("pre_condition_53 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_54(b=b,delta=delta)==True:
		print("pre_condition_54 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_55(b=b,delta=delta)==True:
		print("pre_condition_55 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_56(b=b,delta=delta)==True:
		print("pre_condition_56 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_57(b=b,delta=delta)==True:
		print("pre_condition_57 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_58(b=b,delta=delta)==True:
		print("pre_condition_58 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_59(b=b,delta=delta)==True:
		print("pre_condition_59 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_60(b=b,delta=delta)==True:
		print("pre_condition_60 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_61(b=b,delta=delta)==True:
		print("pre_condition_61 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_62(b=b,delta=delta)==True:
		print("pre_condition_62 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_63(b=b,delta=delta)==True:
		print("pre_condition_63 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_64(b=b,delta=delta)==True:
		print("pre_condition_64 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_65(b=b,delta=delta)==True:
		print("pre_condition_65 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_66(b=b,delta=delta)==True:
		print("pre_condition_66 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_67(b=b,delta=delta)==True:
		print("pre_condition_67 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_68(b=b,delta=delta)==True:
		print("pre_condition_68 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_69(b=b,delta=delta)==True:
		print("pre_condition_69 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_70(b=b,delta=delta)==True:
		print("pre_condition_70 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_71(b=b,delta=delta)==True:
		print("pre_condition_71 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_72(b=b,delta=delta)==True:
		print("pre_condition_72 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_73(b=b,delta=delta)==True:
		print("pre_condition_73 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_74(b=b,delta=delta)==True:
		print("pre_condition_74 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_75(b=b,delta=delta)==True:
		print("pre_condition_75 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_76(b=b,delta=delta)==True:
		print("pre_condition_76 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_77(b=b,delta=delta)==True:
		print("pre_condition_77 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_78(b=b,delta=delta)==True:
		print("pre_condition_78 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_79(b=b,delta=delta)==True:
		print("pre_condition_79 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_80(b=b,delta=delta)==True:
		print("pre_condition_80 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_81(b=b,delta=delta)==True:
		print("pre_condition_81 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_82(b=b,delta=delta)==True:
		print("pre_condition_82 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_83(b=b,delta=delta)==True:
		print("pre_condition_83 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_84(b=b,delta=delta)==True:
		print("pre_condition_84 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_85(b=b,delta=delta)==True:
		print("pre_condition_85 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_86(b=b,delta=delta)==True:
		print("pre_condition_86 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_87(b=b,delta=delta)==True:
		print("pre_condition_87 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_88(b=b,delta=delta)==True:
		print("pre_condition_88 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_89(b=b,delta=delta)==True:
		print("pre_condition_89 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_90(b=b,delta=delta)==True:
		print("pre_condition_90 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_91(b=b,delta=delta)==True:
		print("pre_condition_91 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_92(b=b,delta=delta)==True:
		print("pre_condition_92 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_93(b=b,delta=delta)==True:
		print("pre_condition_93 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_94(b=b,delta=delta)==True:
		print("pre_condition_94 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_95(b=b,delta=delta)==True:
		print("pre_condition_95 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_96(b=b,delta=delta)==True:
		print("pre_condition_96 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_97(b=b,delta=delta)==True:
		print("pre_condition_97 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_98(b=b,delta=delta)==True:
		print("pre_condition_98 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_99(b=b,delta=delta)==True:
		print("pre_condition_99 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_100(b=b,delta=delta)==True:
		print("pre_condition_100 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_101(b=b,delta=delta)==True:
		print("pre_condition_101 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_102(b=b,delta=delta)==True:
		print("pre_condition_102 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_103(b=b,delta=delta)==True:
		print("pre_condition_103 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_104(b=b,delta=delta)==True:
		print("pre_condition_104 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_105(b=b,delta=delta)==True:
		print("pre_condition_105 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_106(b=b,delta=delta)==True:
		print("pre_condition_106 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_107(b=b,delta=delta)==True:
		print("pre_condition_107 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_108(b=b,delta=delta)==True:
		print("pre_condition_108 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_109(b=b,delta=delta)==True:
		print("pre_condition_109 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_110(b=b,delta=delta)==True:
		print("pre_condition_110 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_111(b=b,delta=delta)==True:
		print("pre_condition_111 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_112(b=b,delta=delta)==True:
		print("pre_condition_112 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_113(b=b,delta=delta)==True:
		print("pre_condition_113 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_114(b=b,delta=delta)==True:
		print("pre_condition_114 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_115(b=b,delta=delta)==True:
		print("pre_condition_115 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_116(b=b,delta=delta)==True:
		print("pre_condition_116 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_117(b=b,delta=delta)==True:
		print("pre_condition_117 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_118(b=b,delta=delta)==True:
		print("pre_condition_118 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_119(b=b,delta=delta)==True:
		print("pre_condition_119 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_120(b=b,delta=delta)==True:
		print("pre_condition_120 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_121(b=b,delta=delta)==True:
		print("pre_condition_121 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_122(b=b,delta=delta)==True:
		print("pre_condition_122 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_123(b=b,delta=delta)==True:
		print("pre_condition_123 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_124(b=b,delta=delta)==True:
		print("pre_condition_124 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_125(b=b,delta=delta)==True:
		print("pre_condition_125 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_126(b=b,delta=delta)==True:
		print("pre_condition_126 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_127(b=b,delta=delta)==True:
		print("pre_condition_127 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_128(b=b,delta=delta)==True:
		print("pre_condition_128 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_129(b=b,delta=delta)==True:
		print("pre_condition_129 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_130(b=b,delta=delta)==True:
		print("pre_condition_130 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_131(b=b,delta=delta)==True:
		print("pre_condition_131 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_132(b=b,delta=delta)==True:
		print("pre_condition_132 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_133(b=b,delta=delta)==True:
		print("pre_condition_133 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_134(b=b,delta=delta)==True:
		print("pre_condition_134 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_135(b=b,delta=delta)==True:
		print("pre_condition_135 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_136(b=b,delta=delta)==True:
		print("pre_condition_136 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_137(b=b,delta=delta)==True:
		print("pre_condition_137 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_138(b=b,delta=delta)==True:
		print("pre_condition_138 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_139(b=b,delta=delta)==True:
		print("pre_condition_139 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_140(b=b,delta=delta)==True:
		print("pre_condition_140 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_141(b=b,delta=delta)==True:
		print("pre_condition_141 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_142(b=b,delta=delta)==True:
		print("pre_condition_142 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_143(b=b,delta=delta)==True:
		print("pre_condition_143 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_144(b=b,delta=delta)==True:
		print("pre_condition_144 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_145(b=b,delta=delta)==True:
		print("pre_condition_145 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_146(b=b,delta=delta)==True:
		print("pre_condition_146 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_147(b=b,delta=delta)==True:
		print("pre_condition_147 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_148(b=b,delta=delta)==True:
		print("pre_condition_148 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_149(b=b,delta=delta)==True:
		print("pre_condition_149 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_150(b=b,delta=delta)==True:
		print("pre_condition_150 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_151(b=b,delta=delta)==True:
		print("pre_condition_151 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_152(b=b,delta=delta)==True:
		print("pre_condition_152 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_153(b=b,delta=delta)==True:
		print("pre_condition_153 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_154(b=b,delta=delta)==True:
		print("pre_condition_154 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_155(b=b,delta=delta)==True:
		print("pre_condition_155 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_156(b=b,delta=delta)==True:
		print("pre_condition_156 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_157(b=b,delta=delta)==True:
		print("pre_condition_157 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_158(b=b,delta=delta)==True:
		print("pre_condition_158 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_159(b=b,delta=delta)==True:
		print("pre_condition_159 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_160(b=b,delta=delta)==True:
		print("pre_condition_160 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_161(b=b,delta=delta)==True:
		print("pre_condition_161 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_162(b=b,delta=delta)==True:
		print("pre_condition_162 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_163(b=b,delta=delta)==True:
		print("pre_condition_163 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_164(b=b,delta=delta)==True:
		print("pre_condition_164 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_165(b=b,delta=delta)==True:
		print("pre_condition_165 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_166(b=b,delta=delta)==True:
		print("pre_condition_166 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_167(b=b,delta=delta)==True:
		print("pre_condition_167 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_168(b=b,delta=delta)==True:
		print("pre_condition_168 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_169(b=b,delta=delta)==True:
		print("pre_condition_169 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_170(b=b,delta=delta)==True:
		print("pre_condition_170 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_171(b=b,delta=delta)==True:
		print("pre_condition_171 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_172(b=b,delta=delta)==True:
		print("pre_condition_172 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_173(b=b,delta=delta)==True:
		print("pre_condition_173 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_174(b=b,delta=delta)==True:
		print("pre_condition_174 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_175(b=b,delta=delta)==True:
		print("pre_condition_175 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_176(b=b,delta=delta)==True:
		print("pre_condition_176 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_177(b=b,delta=delta)==True:
		print("pre_condition_177 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_178(b=b,delta=delta)==True:
		print("pre_condition_178 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_179(b=b,delta=delta)==True:
		print("pre_condition_179 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_180(b=b,delta=delta)==True:
		print("pre_condition_180 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_181(b=b,delta=delta)==True:
		print("pre_condition_181 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_182(b=b,delta=delta)==True:
		print("pre_condition_182 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_183(b=b,delta=delta)==True:
		print("pre_condition_183 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_184(b=b,delta=delta)==True:
		print("pre_condition_184 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_185(b=b,delta=delta)==True:
		print("pre_condition_185 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_186(b=b,delta=delta)==True:
		print("pre_condition_186 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_187(b=b,delta=delta)==True:
		print("pre_condition_187 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_188(b=b,delta=delta)==True:
		print("pre_condition_188 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_189(b=b,delta=delta)==True:
		print("pre_condition_189 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_190(b=b,delta=delta)==True:
		print("pre_condition_190 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_191(b=b,delta=delta)==True:
		print("pre_condition_191 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_192(b=b,delta=delta)==True:
		print("pre_condition_192 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_193(b=b,delta=delta)==True:
		print("pre_condition_193 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_194(b=b,delta=delta)==True:
		print("pre_condition_194 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_195(b=b,delta=delta)==True:
		print("pre_condition_195 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_196(b=b,delta=delta)==True:
		print("pre_condition_196 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_197(b=b,delta=delta)==True:
		print("pre_condition_197 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_198(b=b,delta=delta)==True:
		print("pre_condition_198 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_199(b=b,delta=delta)==True:
		print("pre_condition_199 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_200(b=b,delta=delta)==True:
		print("pre_condition_200 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_201(b=b,delta=delta)==True:
		print("pre_condition_201 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_202(b=b,delta=delta)==True:
		print("pre_condition_202 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_203(b=b,delta=delta)==True:
		print("pre_condition_203 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_204(b=b,delta=delta)==True:
		print("pre_condition_204 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_205(b=b,delta=delta)==True:
		print("pre_condition_205 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_206(b=b,delta=delta)==True:
		print("pre_condition_206 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_207(b=b,delta=delta)==True:
		print("pre_condition_207 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_208(b=b,delta=delta)==True:
		print("pre_condition_208 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_209(b=b,delta=delta)==True:
		print("pre_condition_209 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_210(b=b,delta=delta)==True:
		print("pre_condition_210 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_211(b=b,delta=delta)==True:
		print("pre_condition_211 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_212(b=b,delta=delta)==True:
		print("pre_condition_212 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_213(b=b,delta=delta)==True:
		print("pre_condition_213 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_214(b=b,delta=delta)==True:
		print("pre_condition_214 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_215(b=b,delta=delta)==True:
		print("pre_condition_215 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_216(b=b,delta=delta)==True:
		print("pre_condition_216 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_217(b=b,delta=delta)==True:
		print("pre_condition_217 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_218(b=b,delta=delta)==True:
		print("pre_condition_218 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_219(b=b,delta=delta)==True:
		print("pre_condition_219 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_220(b=b,delta=delta)==True:
		print("pre_condition_220 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_221(b=b,delta=delta)==True:
		print("pre_condition_221 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_222(b=b,delta=delta)==True:
		print("pre_condition_222 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_223(b=b,delta=delta)==True:
		print("pre_condition_223 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_224(b=b,delta=delta)==True:
		print("pre_condition_224 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_225(b=b,delta=delta)==True:
		print("pre_condition_225 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_226(b=b,delta=delta)==True:
		print("pre_condition_226 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_227(b=b,delta=delta)==True:
		print("pre_condition_227 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_228(b=b,delta=delta)==True:
		print("pre_condition_228 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_229(b=b,delta=delta)==True:
		print("pre_condition_229 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_230(b=b,delta=delta)==True:
		print("pre_condition_230 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_231(b=b,delta=delta)==True:
		print("pre_condition_231 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_232(b=b,delta=delta)==True:
		print("pre_condition_232 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_233(b=b,delta=delta)==True:
		print("pre_condition_233 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_234(b=b,delta=delta)==True:
		print("pre_condition_234 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_235(b=b,delta=delta)==True:
		print("pre_condition_235 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_236(b=b,delta=delta)==True:
		print("pre_condition_236 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_237(b=b,delta=delta)==True:
		print("pre_condition_237 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_238(b=b,delta=delta)==True:
		print("pre_condition_238 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_239(b=b,delta=delta)==True:
		print("pre_condition_239 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_240(b=b,delta=delta)==True:
		print("pre_condition_240 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_241(b=b,delta=delta)==True:
		print("pre_condition_241 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_242(b=b,delta=delta)==True:
		print("pre_condition_242 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_243(b=b,delta=delta)==True:
		print("pre_condition_243 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_244(b=b,delta=delta)==True:
		print("pre_condition_244 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_245(b=b,delta=delta)==True:
		print("pre_condition_245 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_246(b=b,delta=delta)==True:
		print("pre_condition_246 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_247(b=b,delta=delta)==True:
		print("pre_condition_247 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_248(b=b,delta=delta)==True:
		print("pre_condition_248 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_249(b=b,delta=delta)==True:
		print("pre_condition_249 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_250(b=b,delta=delta)==True:
		print("pre_condition_250 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_251(b=b,delta=delta)==True:
		print("pre_condition_251 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_252(b=b,delta=delta)==True:
		print("pre_condition_252 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_253(b=b,delta=delta)==True:
		print("pre_condition_253 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_254(b=b,delta=delta)==True:
		print("pre_condition_254 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_255(b=b,delta=delta)==True:
		print("pre_condition_255 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_256(b=b,delta=delta)==True:
		print("pre_condition_256 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_257(b=b,delta=delta)==True:
		print("pre_condition_257 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_258(b=b,delta=delta)==True:
		print("pre_condition_258 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_259(b=b,delta=delta)==True:
		print("pre_condition_259 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_260(b=b,delta=delta)==True:
		print("pre_condition_260 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_261(b=b,delta=delta)==True:
		print("pre_condition_261 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_262(b=b,delta=delta)==True:
		print("pre_condition_262 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_263(b=b,delta=delta)==True:
		print("pre_condition_263 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_264(b=b,delta=delta)==True:
		print("pre_condition_264 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_265(b=b,delta=delta)==True:
		print("pre_condition_265 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_266(b=b,delta=delta)==True:
		print("pre_condition_266 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_267(b=b,delta=delta)==True:
		print("pre_condition_267 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_268(b=b,delta=delta)==True:
		print("pre_condition_268 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_269(b=b,delta=delta)==True:
		print("pre_condition_269 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_270(b=b,delta=delta)==True:
		print("pre_condition_270 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_271(b=b,delta=delta)==True:
		print("pre_condition_271 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_272(b=b,delta=delta)==True:
		print("pre_condition_272 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_273(b=b,delta=delta)==True:
		print("pre_condition_273 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_274(b=b,delta=delta)==True:
		print("pre_condition_274 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_275(b=b,delta=delta)==True:
		print("pre_condition_275 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_276(b=b,delta=delta)==True:
		print("pre_condition_276 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_277(b=b,delta=delta)==True:
		print("pre_condition_277 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_278(b=b,delta=delta)==True:
		print("pre_condition_278 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_279(b=b,delta=delta)==True:
		print("pre_condition_279 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_280(b=b,delta=delta)==True:
		print("pre_condition_280 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_281(b=b,delta=delta)==True:
		print("pre_condition_281 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_282(b=b,delta=delta)==True:
		print("pre_condition_282 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_283(b=b,delta=delta)==True:
		print("pre_condition_283 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_284(b=b,delta=delta)==True:
		print("pre_condition_284 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_285(b=b,delta=delta)==True:
		print("pre_condition_285 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_286(b=b,delta=delta)==True:
		print("pre_condition_286 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_287(b=b,delta=delta)==True:
		print("pre_condition_287 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_288(b=b,delta=delta)==True:
		print("pre_condition_288 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_289(b=b,delta=delta)==True:
		print("pre_condition_289 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_290(b=b,delta=delta)==True:
		print("pre_condition_290 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_291(b=b,delta=delta)==True:
		print("pre_condition_291 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_292(b=b,delta=delta)==True:
		print("pre_condition_292 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_293(b=b,delta=delta)==True:
		print("pre_condition_293 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_294(b=b,delta=delta)==True:
		print("pre_condition_294 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_295(b=b,delta=delta)==True:
		print("pre_condition_295 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_296(b=b,delta=delta)==True:
		print("pre_condition_296 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_297(b=b,delta=delta)==True:
		print("pre_condition_297 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_298(b=b,delta=delta)==True:
		print("pre_condition_298 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_299(b=b,delta=delta)==True:
		print("pre_condition_299 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_300(b=b,delta=delta)==True:
		print("pre_condition_300 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_301(b=b,delta=delta)==True:
		print("pre_condition_301 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_302(b=b,delta=delta)==True:
		print("pre_condition_302 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_303(b=b,delta=delta)==True:
		print("pre_condition_303 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_304(b=b,delta=delta)==True:
		print("pre_condition_304 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_305(b=b,delta=delta)==True:
		print("pre_condition_305 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_306(b=b,delta=delta)==True:
		print("pre_condition_306 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_307(b=b,delta=delta)==True:
		print("pre_condition_307 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_308(b=b,delta=delta)==True:
		print("pre_condition_308 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_309(b=b,delta=delta)==True:
		print("pre_condition_309 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_310(b=b,delta=delta)==True:
		print("pre_condition_310 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_311(b=b,delta=delta)==True:
		print("pre_condition_311 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_312(b=b,delta=delta)==True:
		print("pre_condition_312 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_313(b=b,delta=delta)==True:
		print("pre_condition_313 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_314(b=b,delta=delta)==True:
		print("pre_condition_314 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_315(b=b,delta=delta)==True:
		print("pre_condition_315 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_316(b=b,delta=delta)==True:
		print("pre_condition_316 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_317(b=b,delta=delta)==True:
		print("pre_condition_317 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_318(b=b,delta=delta)==True:
		print("pre_condition_318 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_319(b=b,delta=delta)==True:
		print("pre_condition_319 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_320(b=b,delta=delta)==True:
		print("pre_condition_320 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_321(b=b,delta=delta)==True:
		print("pre_condition_321 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_322(b=b,delta=delta)==True:
		print("pre_condition_322 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_323(b=b,delta=delta)==True:
		print("pre_condition_323 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_324(b=b,delta=delta)==True:
		print("pre_condition_324 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_325(b=b,delta=delta)==True:
		print("pre_condition_325 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_326(b=b,delta=delta)==True:
		print("pre_condition_326 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_327(b=b,delta=delta)==True:
		print("pre_condition_327 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_328(b=b,delta=delta)==True:
		print("pre_condition_328 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_329(b=b,delta=delta)==True:
		print("pre_condition_329 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_330(b=b,delta=delta)==True:
		print("pre_condition_330 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_331(b=b,delta=delta)==True:
		print("pre_condition_331 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_332(b=b,delta=delta)==True:
		print("pre_condition_332 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_333(b=b,delta=delta)==True:
		print("pre_condition_333 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_334(b=b,delta=delta)==True:
		print("pre_condition_334 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_335(b=b,delta=delta)==True:
		print("pre_condition_335 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_336(b=b,delta=delta)==True:
		print("pre_condition_336 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_337(b=b,delta=delta)==True:
		print("pre_condition_337 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_338(b=b,delta=delta)==True:
		print("pre_condition_338 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_339(b=b,delta=delta)==True:
		print("pre_condition_339 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_340(b=b,delta=delta)==True:
		print("pre_condition_340 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_341(b=b,delta=delta)==True:
		print("pre_condition_341 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_342(b=b,delta=delta)==True:
		print("pre_condition_342 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_343(b=b,delta=delta)==True:
		print("pre_condition_343 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_344(b=b,delta=delta)==True:
		print("pre_condition_344 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_345(b=b,delta=delta)==True:
		print("pre_condition_345 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_346(b=b,delta=delta)==True:
		print("pre_condition_346 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_347(b=b,delta=delta)==True:
		print("pre_condition_347 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_348(b=b,delta=delta)==True:
		print("pre_condition_348 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_349(b=b,delta=delta)==True:
		print("pre_condition_349 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_350(b=b,delta=delta)==True:
		print("pre_condition_350 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_351(b=b,delta=delta)==True:
		print("pre_condition_351 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_352(b=b,delta=delta)==True:
		print("pre_condition_352 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_353(b=b,delta=delta)==True:
		print("pre_condition_353 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_354(b=b,delta=delta)==True:
		print("pre_condition_354 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_355(b=b,delta=delta)==True:
		print("pre_condition_355 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_356(b=b,delta=delta)==True:
		print("pre_condition_356 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_357(b=b,delta=delta)==True:
		print("pre_condition_357 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_358(b=b,delta=delta)==True:
		print("pre_condition_358 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_359(b=b,delta=delta)==True:
		print("pre_condition_359 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_360(b=b,delta=delta)==True:
		print("pre_condition_360 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_361(b=b,delta=delta)==True:
		print("pre_condition_361 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_362(b=b,delta=delta)==True:
		print("pre_condition_362 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_363(b=b,delta=delta)==True:
		print("pre_condition_363 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_364(b=b,delta=delta)==True:
		print("pre_condition_364 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_365(b=b,delta=delta)==True:
		print("pre_condition_365 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_366(b=b,delta=delta)==True:
		print("pre_condition_366 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_367(b=b,delta=delta)==True:
		print("pre_condition_367 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_368(b=b,delta=delta)==True:
		print("pre_condition_368 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_369(b=b,delta=delta)==True:
		print("pre_condition_369 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_370(b=b,delta=delta)==True:
		print("pre_condition_370 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_371(b=b,delta=delta)==True:
		print("pre_condition_371 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_372(b=b,delta=delta)==True:
		print("pre_condition_372 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_373(b=b,delta=delta)==True:
		print("pre_condition_373 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_374(b=b,delta=delta)==True:
		print("pre_condition_374 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_375(b=b,delta=delta)==True:
		print("pre_condition_375 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_376(b=b,delta=delta)==True:
		print("pre_condition_376 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_377(b=b,delta=delta)==True:
		print("pre_condition_377 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_378(b=b,delta=delta)==True:
		print("pre_condition_378 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_379(b=b,delta=delta)==True:
		print("pre_condition_379 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_380(b=b,delta=delta)==True:
		print("pre_condition_380 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_381(b=b,delta=delta)==True:
		print("pre_condition_381 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_382(b=b,delta=delta)==True:
		print("pre_condition_382 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_383(b=b,delta=delta)==True:
		print("pre_condition_383 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_384(b=b,delta=delta)==True:
		print("pre_condition_384 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_385(b=b,delta=delta)==True:
		print("pre_condition_385 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_386(b=b,delta=delta)==True:
		print("pre_condition_386 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_387(b=b,delta=delta)==True:
		print("pre_condition_387 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_388(b=b,delta=delta)==True:
		print("pre_condition_388 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_389(b=b,delta=delta)==True:
		print("pre_condition_389 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_390(b=b,delta=delta)==True:
		print("pre_condition_390 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_391(b=b,delta=delta)==True:
		print("pre_condition_391 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_392(b=b,delta=delta)==True:
		print("pre_condition_392 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_393(b=b,delta=delta)==True:
		print("pre_condition_393 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_394(b=b,delta=delta)==True:
		print("pre_condition_394 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_395(b=b,delta=delta)==True:
		print("pre_condition_395 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_396(b=b,delta=delta)==True:
		print("pre_condition_396 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_397(b=b,delta=delta)==True:
		print("pre_condition_397 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_398(b=b,delta=delta)==True:
		print("pre_condition_398 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_399(b=b,delta=delta)==True:
		print("pre_condition_399 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_400(b=b,delta=delta)==True:
		print("pre_condition_400 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_401(b=b,delta=delta)==True:
		print("pre_condition_401 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_402(b=b,delta=delta)==True:
		print("pre_condition_402 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_403(b=b,delta=delta)==True:
		print("pre_condition_403 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_404(b=b,delta=delta)==True:
		print("pre_condition_404 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_405(b=b,delta=delta)==True:
		print("pre_condition_405 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_406(b=b,delta=delta)==True:
		print("pre_condition_406 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_407(b=b,delta=delta)==True:
		print("pre_condition_407 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_408(b=b,delta=delta)==True:
		print("pre_condition_408 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_409(b=b,delta=delta)==True:
		print("pre_condition_409 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_410(b=b,delta=delta)==True:
		print("pre_condition_410 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_411(b=b,delta=delta)==True:
		print("pre_condition_411 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_412(b=b,delta=delta)==True:
		print("pre_condition_412 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_413(b=b,delta=delta)==True:
		print("pre_condition_413 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_414(b=b,delta=delta)==True:
		print("pre_condition_414 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_415(b=b,delta=delta)==True:
		print("pre_condition_415 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_416(b=b,delta=delta)==True:
		print("pre_condition_416 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_417(b=b,delta=delta)==True:
		print("pre_condition_417 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_418(b=b,delta=delta)==True:
		print("pre_condition_418 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_419(b=b,delta=delta)==True:
		print("pre_condition_419 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_420(b=b,delta=delta)==True:
		print("pre_condition_420 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_421(b=b,delta=delta)==True:
		print("pre_condition_421 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_422(b=b,delta=delta)==True:
		print("pre_condition_422 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_423(b=b,delta=delta)==True:
		print("pre_condition_423 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_424(b=b,delta=delta)==True:
		print("pre_condition_424 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_425(b=b,delta=delta)==True:
		print("pre_condition_425 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_426(b=b,delta=delta)==True:
		print("pre_condition_426 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_427(b=b,delta=delta)==True:
		print("pre_condition_427 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_428(b=b,delta=delta)==True:
		print("pre_condition_428 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_429(b=b,delta=delta)==True:
		print("pre_condition_429 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_430(b=b,delta=delta)==True:
		print("pre_condition_430 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_431(b=b,delta=delta)==True:
		print("pre_condition_431 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_432(b=b,delta=delta)==True:
		print("pre_condition_432 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_433(b=b,delta=delta)==True:
		print("pre_condition_433 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_434(b=b,delta=delta)==True:
		print("pre_condition_434 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_435(b=b,delta=delta)==True:
		print("pre_condition_435 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_436(b=b,delta=delta)==True:
		print("pre_condition_436 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_437(b=b,delta=delta)==True:
		print("pre_condition_437 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_438(b=b,delta=delta)==True:
		print("pre_condition_438 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_439(b=b,delta=delta)==True:
		print("pre_condition_439 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_440(b=b,delta=delta)==True:
		print("pre_condition_440 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_441(b=b,delta=delta)==True:
		print("pre_condition_441 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_442(b=b,delta=delta)==True:
		print("pre_condition_442 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_443(b=b,delta=delta)==True:
		print("pre_condition_443 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_444(b=b,delta=delta)==True:
		print("pre_condition_444 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_445(b=b,delta=delta)==True:
		print("pre_condition_445 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_446(b=b,delta=delta)==True:
		print("pre_condition_446 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_447(b=b,delta=delta)==True:
		print("pre_condition_447 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_448(b=b,delta=delta)==True:
		print("pre_condition_448 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_449(b=b,delta=delta)==True:
		print("pre_condition_449 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_450(b=b,delta=delta)==True:
		print("pre_condition_450 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_451(b=b,delta=delta)==True:
		print("pre_condition_451 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_452(b=b,delta=delta)==True:
		print("pre_condition_452 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_453(b=b,delta=delta)==True:
		print("pre_condition_453 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_454(b=b,delta=delta)==True:
		print("pre_condition_454 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_455(b=b,delta=delta)==True:
		print("pre_condition_455 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_456(b=b,delta=delta)==True:
		print("pre_condition_456 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_457(b=b,delta=delta)==True:
		print("pre_condition_457 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_458(b=b,delta=delta)==True:
		print("pre_condition_458 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_459(b=b,delta=delta)==True:
		print("pre_condition_459 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_460(b=b,delta=delta)==True:
		print("pre_condition_460 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_461(b=b,delta=delta)==True:
		print("pre_condition_461 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_462(b=b,delta=delta)==True:
		print("pre_condition_462 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_463(b=b,delta=delta)==True:
		print("pre_condition_463 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_464(b=b,delta=delta)==True:
		print("pre_condition_464 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_465(b=b,delta=delta)==True:
		print("pre_condition_465 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_466(b=b,delta=delta)==True:
		print("pre_condition_466 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_467(b=b,delta=delta)==True:
		print("pre_condition_467 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_468(b=b,delta=delta)==True:
		print("pre_condition_468 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_469(b=b,delta=delta)==True:
		print("pre_condition_469 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_470(b=b,delta=delta)==True:
		print("pre_condition_470 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_471(b=b,delta=delta)==True:
		print("pre_condition_471 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_472(b=b,delta=delta)==True:
		print("pre_condition_472 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_473(b=b,delta=delta)==True:
		print("pre_condition_473 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_474(b=b,delta=delta)==True:
		print("pre_condition_474 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_475(b=b,delta=delta)==True:
		print("pre_condition_475 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_476(b=b,delta=delta)==True:
		print("pre_condition_476 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_477(b=b,delta=delta)==True:
		print("pre_condition_477 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_478(b=b,delta=delta)==True:
		print("pre_condition_478 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_479(b=b,delta=delta)==True:
		print("pre_condition_479 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_480(b=b,delta=delta)==True:
		print("pre_condition_480 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_481(b=b,delta=delta)==True:
		print("pre_condition_481 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_482(b=b,delta=delta)==True:
		print("pre_condition_482 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_483(b=b,delta=delta)==True:
		print("pre_condition_483 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_484(b=b,delta=delta)==True:
		print("pre_condition_484 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_485(b=b,delta=delta)==True:
		print("pre_condition_485 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_486(b=b,delta=delta)==True:
		print("pre_condition_486 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_487(b=b,delta=delta)==True:
		print("pre_condition_487 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_488(b=b,delta=delta)==True:
		print("pre_condition_488 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_489(b=b,delta=delta)==True:
		print("pre_condition_489 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_490(b=b,delta=delta)==True:
		print("pre_condition_490 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_491(b=b,delta=delta)==True:
		print("pre_condition_491 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_492(b=b,delta=delta)==True:
		print("pre_condition_492 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_493(b=b,delta=delta)==True:
		print("pre_condition_493 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_494(b=b,delta=delta)==True:
		print("pre_condition_494 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_495(b=b,delta=delta)==True:
		print("pre_condition_495 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_496(b=b,delta=delta)==True:
		print("pre_condition_496 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_497(b=b,delta=delta)==True:
		print("pre_condition_497 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_498(b=b,delta=delta)==True:
		print("pre_condition_498 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_499(b=b,delta=delta)==True:
		print("pre_condition_499 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_500(b=b,delta=delta)==True:
		print("pre_condition_500 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_501(b=b,delta=delta)==True:
		print("pre_condition_501 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_502(b=b,delta=delta)==True:
		print("pre_condition_502 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_503(b=b,delta=delta)==True:
		print("pre_condition_503 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_504(b=b,delta=delta)==True:
		print("pre_condition_504 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_505(b=b,delta=delta)==True:
		print("pre_condition_505 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_506(b=b,delta=delta)==True:
		print("pre_condition_506 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_507(b=b,delta=delta)==True:
		print("pre_condition_507 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_508(b=b,delta=delta)==True:
		print("pre_condition_508 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_509(b=b,delta=delta)==True:
		print("pre_condition_509 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_510(b=b,delta=delta)==True:
		print("pre_condition_510 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_511(b=b,delta=delta)==True:
		print("pre_condition_511 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_512(b=b,delta=delta)==True:
		print("pre_condition_512 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_513(b=b,delta=delta)==True:
		print("pre_condition_513 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_514(b=b,delta=delta)==True:
		print("pre_condition_514 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_515(b=b,delta=delta)==True:
		print("pre_condition_515 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_516(b=b,delta=delta)==True:
		print("pre_condition_516 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_517(b=b,delta=delta)==True:
		print("pre_condition_517 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_518(b=b,delta=delta)==True:
		print("pre_condition_518 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_519(b=b,delta=delta)==True:
		print("pre_condition_519 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_520(b=b,delta=delta)==True:
		print("pre_condition_520 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_521(b=b,delta=delta)==True:
		print("pre_condition_521 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_522(b=b,delta=delta)==True:
		print("pre_condition_522 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_523(b=b,delta=delta)==True:
		print("pre_condition_523 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_524(b=b,delta=delta)==True:
		print("pre_condition_524 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_525(b=b,delta=delta)==True:
		print("pre_condition_525 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_526(b=b,delta=delta)==True:
		print("pre_condition_526 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_527(b=b,delta=delta)==True:
		print("pre_condition_527 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_528(b=b,delta=delta)==True:
		print("pre_condition_528 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_529(b=b,delta=delta)==True:
		print("pre_condition_529 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_530(b=b,delta=delta)==True:
		print("pre_condition_530 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_531(b=b,delta=delta)==True:
		print("pre_condition_531 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_532(b=b,delta=delta)==True:
		print("pre_condition_532 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_533(b=b,delta=delta)==True:
		print("pre_condition_533 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_534(b=b,delta=delta)==True:
		print("pre_condition_534 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_535(b=b,delta=delta)==True:
		print("pre_condition_535 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_536(b=b,delta=delta)==True:
		print("pre_condition_536 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_537(b=b,delta=delta)==True:
		print("pre_condition_537 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_538(b=b,delta=delta)==True:
		print("pre_condition_538 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_539(b=b,delta=delta)==True:
		print("pre_condition_539 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_540(b=b,delta=delta)==True:
		print("pre_condition_540 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_541(b=b,delta=delta)==True:
		print("pre_condition_541 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_542(b=b,delta=delta)==True:
		print("pre_condition_542 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_543(b=b,delta=delta)==True:
		print("pre_condition_543 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_544(b=b,delta=delta)==True:
		print("pre_condition_544 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_545(b=b,delta=delta)==True:
		print("pre_condition_545 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_546(b=b,delta=delta)==True:
		print("pre_condition_546 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_547(b=b,delta=delta)==True:
		print("pre_condition_547 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_548(b=b,delta=delta)==True:
		print("pre_condition_548 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_549(b=b,delta=delta)==True:
		print("pre_condition_549 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_550(b=b,delta=delta)==True:
		print("pre_condition_550 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_551(b=b,delta=delta)==True:
		print("pre_condition_551 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_552(b=b,delta=delta)==True:
		print("pre_condition_552 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_553(b=b,delta=delta)==True:
		print("pre_condition_553 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_554(b=b,delta=delta)==True:
		print("pre_condition_554 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_555(b=b,delta=delta)==True:
		print("pre_condition_555 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_556(b=b,delta=delta)==True:
		print("pre_condition_556 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_557(b=b,delta=delta)==True:
		print("pre_condition_557 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_558(b=b,delta=delta)==True:
		print("pre_condition_558 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_559(b=b,delta=delta)==True:
		print("pre_condition_559 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_560(b=b,delta=delta)==True:
		print("pre_condition_560 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_561(b=b,delta=delta)==True:
		print("pre_condition_561 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_562(b=b,delta=delta)==True:
		print("pre_condition_562 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_563(b=b,delta=delta)==True:
		print("pre_condition_563 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_564(b=b,delta=delta)==True:
		print("pre_condition_564 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_565(b=b,delta=delta)==True:
		print("pre_condition_565 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_566(b=b,delta=delta)==True:
		print("pre_condition_566 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_567(b=b,delta=delta)==True:
		print("pre_condition_567 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_568(b=b,delta=delta)==True:
		print("pre_condition_568 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_569(b=b,delta=delta)==True:
		print("pre_condition_569 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_570(b=b,delta=delta)==True:
		print("pre_condition_570 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_571(b=b,delta=delta)==True:
		print("pre_condition_571 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_572(b=b,delta=delta)==True:
		print("pre_condition_572 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_573(b=b,delta=delta)==True:
		print("pre_condition_573 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_574(b=b,delta=delta)==True:
		print("pre_condition_574 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_575(b=b,delta=delta)==True:
		print("pre_condition_575 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_576(b=b,delta=delta)==True:
		print("pre_condition_576 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_577(b=b,delta=delta)==True:
		print("pre_condition_577 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_578(b=b,delta=delta)==True:
		print("pre_condition_578 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_579(b=b,delta=delta)==True:
		print("pre_condition_579 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_580(b=b,delta=delta)==True:
		print("pre_condition_580 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_581(b=b,delta=delta)==True:
		print("pre_condition_581 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_582(b=b,delta=delta)==True:
		print("pre_condition_582 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_583(b=b,delta=delta)==True:
		print("pre_condition_583 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_584(b=b,delta=delta)==True:
		print("pre_condition_584 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_585(b=b,delta=delta)==True:
		print("pre_condition_585 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_586(b=b,delta=delta)==True:
		print("pre_condition_586 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_587(b=b,delta=delta)==True:
		print("pre_condition_587 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_588(b=b,delta=delta)==True:
		print("pre_condition_588 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_589(b=b,delta=delta)==True:
		print("pre_condition_589 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_590(b=b,delta=delta)==True:
		print("pre_condition_590 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_591(b=b,delta=delta)==True:
		print("pre_condition_591 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_592(b=b,delta=delta)==True:
		print("pre_condition_592 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_593(b=b,delta=delta)==True:
		print("pre_condition_593 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_594(b=b,delta=delta)==True:
		print("pre_condition_594 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_595(b=b,delta=delta)==True:
		print("pre_condition_595 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)
	
	
	if pre_condition_596(b=b,delta=delta)==True:
		print("pre_condition_596 SAT")
		print('delta = 38852342879092737/147573952589676412928')
		print('a = -5793/4096')
		print('b = 11815/8192')
		exit(0)


	print("UNKNOWN")
	exit(0)
