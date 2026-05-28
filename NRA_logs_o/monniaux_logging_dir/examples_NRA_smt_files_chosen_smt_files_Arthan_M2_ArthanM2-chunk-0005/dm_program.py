import sympy
from sympy import *

def pre_condition_0(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 63/64) & (delta >= 63/64 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-63, 64))), GreaterThan(Symbol('delta'), Add(Rational(63, 64), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 63/64) & (delta >= 63/64 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-63, 64))), GreaterThan(Symbol('delta'), Add(Rational(63, 64), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2) & (delta >= -skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Pow(Symbol('skoSINS'), Integer(2))), GreaterThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2) & (delta >= -skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Pow(Symbol('skoSINS'), Integer(2))), GreaterThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_4(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 255/256) & (delta >= 255/256 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-255, 256))), GreaterThan(Symbol('delta'), Add(Rational(255, 256), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_5(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 255/256) & (delta >= 255/256 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-255, 256))), GreaterThan(Symbol('delta'), Add(Rational(255, 256), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_6(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_7(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_8(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_9(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_10(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_11(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_12(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_13(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_14(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_15(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_16(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_17(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_18(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_19(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_20(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_21(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_22(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_23(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_24(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_25(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_26(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_27(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_28(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_29(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_30(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_31(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_32(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_33(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_34(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_35(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_36(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_37(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_38(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_39(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_40(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_41(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_42(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_43(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_44(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_45(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_46(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_47(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_48(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_49(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_50(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_51(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_52(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_53(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_54(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_55(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_56(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_57(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_58(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_59(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_60(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_61(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_62(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_63(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_64(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_65(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_66(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_67(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_68(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_69(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_70(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_71(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_72(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_73(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_74(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_75(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_76(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_77(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_78(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_79(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_80(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_81(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_82(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_83(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_84(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_85(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_86(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_87(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_88(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_89(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_90(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_91(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_92(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_93(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_94(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_95(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_96(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_97(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_98(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_99(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_100(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_101(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_102(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_103(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_104(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_105(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_106(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_107(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_108(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_109(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_110(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_111(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_112(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_113(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_114(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_115(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_116(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_117(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_118(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_119(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_120(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_121(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_122(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_123(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_124(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_125(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_126(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_127(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_128(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_129(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_130(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_131(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_132(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_133(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_134(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_135(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_136(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_137(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_138(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_139(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_140(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_141(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_142(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_143(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_144(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_145(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_146(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_147(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_148(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_149(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_150(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_151(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_152(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_153(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_154(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_155(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_156(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_157(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_158(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_159(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_160(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_161(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_162(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_163(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_164(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_165(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_166(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_167(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_168(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_169(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_170(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_171(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_172(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_173(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_174(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_175(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_176(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_177(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_178(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_179(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_180(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_181(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_182(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_183(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_184(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_185(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_186(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_187(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_188(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_189(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_190(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_191(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_192(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_193(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_194(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_195(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_196(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_197(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_198(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_199(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_200(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_201(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_202(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_203(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_204(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_205(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_206(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_207(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_208(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_209(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_210(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_211(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_212(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_213(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_214(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_215(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_216(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_217(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_218(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_219(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_220(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_221(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_222(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_223(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_224(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_225(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_226(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_227(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_228(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_229(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_230(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_231(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_232(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_233(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_234(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_235(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_236(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_237(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_238(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_239(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_240(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_241(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_242(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_243(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_244(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_245(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_246(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_247(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_248(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_249(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_250(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_251(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_252(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_253(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_254(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_255(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_256(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_257(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_258(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_259(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_260(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_261(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_262(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_263(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_264(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_265(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_266(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_267(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_268(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_269(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_270(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_271(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_272(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_273(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_274(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_275(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_276(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_277(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_278(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_279(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_280(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_281(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_282(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_283(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_284(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_285(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_286(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_287(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_288(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_289(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_290(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_291(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_292(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_293(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_294(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_295(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_296(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_297(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_298(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_299(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_300(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))