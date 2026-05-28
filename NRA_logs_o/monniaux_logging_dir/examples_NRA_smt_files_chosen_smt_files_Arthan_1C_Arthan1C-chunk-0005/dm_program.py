import sympy
from sympy import *

def pre_condition_0(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 63/64) & (delta >= 63/64 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-63, 64))), GreaterThan(Symbol('delta'), Add(Rational(63, 64), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 47/64) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(47, 64)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2) & (delta >= -skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Pow(Symbol('skoSINS'), Integer(2))), GreaterThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 1/64) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1, 64)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_4(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 255/256) & (delta >= 255/256 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-255, 256))), GreaterThan(Symbol('delta'), Add(Rational(255, 256), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_5(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 1/256) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1, 256)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_6(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_7(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_8(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_9(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_10(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_11(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_12(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_13(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_14(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_15(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_16(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_17(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_18(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_19(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_20(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_21(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_22(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_23(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_24(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_25(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_26(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_27(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_28(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_29(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_30(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_31(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_32(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_33(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_34(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_35(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_36(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_37(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_38(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_39(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_40(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_41(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_42(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_43(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_44(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_45(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_46(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_47(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_48(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_49(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_50(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_51(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_52(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_53(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_54(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_55(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_56(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_57(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_58(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_59(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_60(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_61(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_62(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_63(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_64(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_65(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_66(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_67(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_68(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_69(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_70(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_71(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_72(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_73(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_74(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_75(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_76(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_77(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_78(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_79(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_80(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_81(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_82(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_83(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_84(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_85(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_86(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_87(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_88(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_89(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_90(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_91(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_92(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_93(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_94(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_95(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_96(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_97(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_98(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_99(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_100(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_101(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_102(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_103(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_104(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_105(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_106(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_107(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_108(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_109(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_110(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_111(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_112(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_113(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_114(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_115(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_116(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_117(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_118(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_119(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_120(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_121(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_122(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_123(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_124(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_125(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_126(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_127(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_128(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_129(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_130(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_131(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_132(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_133(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_134(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_135(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_136(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_137(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_138(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_139(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_140(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_141(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_142(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_143(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_144(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_145(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_146(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_147(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_148(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_149(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_150(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_151(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_152(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_153(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_154(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_155(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_156(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_157(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_158(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_159(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_160(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_161(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_162(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_163(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_164(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_165(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_166(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_167(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_168(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_169(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_170(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_171(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_172(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_173(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_174(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_175(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_176(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_177(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_178(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_179(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_180(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_181(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_182(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_183(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_184(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_185(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_186(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_187(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_188(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_189(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_190(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_191(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_192(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_193(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_194(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_195(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_196(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_197(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_198(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_199(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_200(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_201(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_202(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_203(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_204(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_205(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_206(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_207(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_208(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_209(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_210(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_211(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_212(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_213(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_214(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_215(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_216(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_217(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_218(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_219(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_220(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_221(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_222(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_223(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_224(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_225(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_226(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_227(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_228(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_229(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_230(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_231(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_232(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_233(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_234(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_235(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_236(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_237(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_238(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_239(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_240(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_241(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_242(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_243(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_244(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_245(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_246(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_247(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_248(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_249(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_250(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_251(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_252(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_253(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_254(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_255(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_256(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_257(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_258(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_259(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_260(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_261(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_262(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_263(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_264(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_265(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_266(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_267(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_268(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_269(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_270(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_271(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_272(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_273(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_274(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_275(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_276(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_277(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_278(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_279(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_280(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_281(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_282(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_283(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_284(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_285(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_286(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_287(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_288(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_289(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_290(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_291(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_292(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_293(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_294(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_295(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_296(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_297(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_298(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_299(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_300(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_301(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_302(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_303(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_304(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_305(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_306(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_307(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_308(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_309(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_310(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_311(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_312(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_313(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_314(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_315(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_316(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_317(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_318(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_319(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_320(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_321(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_322(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_323(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_324(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_325(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_326(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_327(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_328(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_329(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_330(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_331(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_332(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_333(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_334(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_335(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_336(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_337(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_338(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_339(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_340(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_341(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_342(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_343(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_344(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_345(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_346(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_347(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_348(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_349(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_350(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_351(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_352(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_353(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_354(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_355(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_356(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_357(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_358(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_359(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_360(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_361(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_362(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_363(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_364(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_365(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_366(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_367(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_368(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_369(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_370(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_371(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_372(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_373(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_374(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_375(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_376(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_377(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_378(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_379(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_380(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_381(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_382(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_383(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_384(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_385(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_386(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_387(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_388(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_389(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_390(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_391(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_392(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_393(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_394(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_395(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_396(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_397(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_398(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_399(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_400(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_401(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_402(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_403(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_404(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_405(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_406(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_407(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_408(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_409(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_410(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_411(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_412(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_413(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_414(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_415(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_416(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_417(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_418(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_419(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_420(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_421(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_422(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_423(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_424(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_425(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_426(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_427(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_428(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_429(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_430(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_431(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_432(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_433(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_434(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_435(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_436(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_437(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_438(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_439(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_440(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_441(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_442(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_443(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_444(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_445(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_446(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_447(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_448(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_449(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_450(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_451(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_452(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_453(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_454(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_455(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_456(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_457(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_458(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_459(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_460(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_461(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_462(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_463(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_464(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_465(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_466(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_467(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_468(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_469(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_470(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_471(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_472(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_473(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_474(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_475(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_476(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_477(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_478(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_479(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_480(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_481(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_482(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_483(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_484(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_485(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_486(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_487(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_488(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_489(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_490(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_491(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_492(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_493(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_494(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_495(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_496(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_497(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_498(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_499(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_500(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_501(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_502(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_503(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_504(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_505(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_506(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_507(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_508(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_509(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_510(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_511(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_512(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_513(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_514(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_515(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_516(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_517(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_518(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_519(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_520(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_521(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_522(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_523(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_524(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_525(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_526(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_527(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_528(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_529(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_530(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_531(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_532(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_533(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_534(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_535(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_536(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_537(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_538(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_539(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_540(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_541(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_542(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_543(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_544(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_545(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_546(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_547(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_548(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_549(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_550(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_551(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_552(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_553(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_554(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_555(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_556(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_557(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_558(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_559(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_560(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_561(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_562(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_563(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_564(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_565(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_566(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_567(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_568(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_569(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_570(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_571(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_572(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_573(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_574(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_575(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_576(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_577(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_578(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_579(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_580(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_581(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_582(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_583(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_584(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_585(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_586(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_587(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_588(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_589(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_590(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_591(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_592(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_593(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_594(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_595(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_596(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_597(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_598(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_599(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_600(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_601(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_602(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_603(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_604(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_605(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_606(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_607(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_608(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_609(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_610(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_611(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_612(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_613(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_614(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_615(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_616(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_617(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_618(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_619(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_620(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_621(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_622(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_623(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_624(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_625(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_626(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_627(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_628(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_629(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_630(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_631(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_632(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_633(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_634(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_635(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_636(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_637(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_638(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_639(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_640(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_641(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_642(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_643(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_644(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_645(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_646(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_647(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_648(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_649(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_650(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_651(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_652(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_653(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_654(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_655(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_656(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_657(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_658(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_659(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_660(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_661(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_662(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_663(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_664(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_665(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_666(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_667(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_668(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_669(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_670(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_671(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_672(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_673(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_674(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_675(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_676(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_677(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_678(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_679(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_680(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_681(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_682(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_683(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_684(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_685(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_686(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_687(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_688(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_689(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_690(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_691(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_692(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_693(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_694(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_695(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_696(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_697(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_698(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_699(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_700(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_701(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_702(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_703(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_704(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_705(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_706(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_707(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_708(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_709(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_710(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_711(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_712(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_713(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_714(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_715(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_716(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_717(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_718(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_719(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_720(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_721(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_722(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_723(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_724(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_725(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_726(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_727(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_728(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_729(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_730(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_731(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_732(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_733(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_734(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_735(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_736(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_737(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_738(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_739(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_740(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_741(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_742(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_743(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_744(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_745(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_746(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_747(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_748(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_749(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_750(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_751(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_752(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_753(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_754(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_755(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_756(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_757(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_758(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_759(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_760(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_761(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_762(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_763(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_764(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_765(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_766(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_767(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_768(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_769(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_770(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_771(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_772(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_773(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_774(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_775(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_776(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_777(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_778(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_779(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_780(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_781(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_782(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_783(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_784(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_785(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_786(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_787(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_788(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_789(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_790(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_791(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_792(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_793(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_794(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_795(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_796(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_797(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_798(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_799(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_800(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_801(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_802(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_803(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_804(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_805(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_806(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_807(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_808(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_809(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_810(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_811(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_812(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_813(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_814(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_815(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_816(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_817(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_818(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_819(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_820(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_821(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_822(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_823(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_824(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_825(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_826(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_827(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_828(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_829(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_830(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_831(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_832(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_833(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_834(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_835(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_836(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_837(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_838(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_839(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_840(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_841(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_842(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_843(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_844(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_845(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_846(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_847(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_848(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_849(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_850(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_851(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_852(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_853(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_854(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_855(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_856(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_857(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_858(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_859(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_860(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_861(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_862(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_863(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_864(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_865(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_866(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_867(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_868(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_869(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_870(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_871(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_872(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_873(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_874(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_875(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_876(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_877(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_878(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_879(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_880(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_881(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_882(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_883(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_884(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_885(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_886(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_887(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_888(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_889(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_890(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_891(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_892(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_893(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_894(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_895(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 255/4194304) & (skoS >= 217/100)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_896(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4129279/4194304) & (delta >= 4129279/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4129279, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4129279, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(delta:sympy.Rational, skoS:sympy.Rational, skoCOSS:sympy.Rational, skoSINS:sympy.Rational):
	# (0 <= delta) & (217/100 <= skoS) & (skoCOSS**2 + skoSINS**2 - 1 <= delta) & (-skoCOSS**2 - skoSINS**2 + 1 <= delta)

	post_cond =  And(LessThan(Integer(0), Symbol('delta')), LessThan(Rational(217, 100), Symbol('skoS')), LessThan(Add(Pow(Symbol('skoCOSS'), Integer(2)), Pow(Symbol('skoSINS'), Integer(2)), Integer(-1)), Symbol('delta')), LessThan(Add(Mul(Integer(-1), Pow(Symbol('skoCOSS'), Integer(2))), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(1)), Symbol('delta')))

	eval = post_cond.subs( { 'delta':delta, 'skoS':skoS, 'skoCOSS':skoCOSS, 'skoSINS':skoSINS })

	return eval == sympy.logic.boolalg.BooleanTrue





if __name__=="__main__":
	
	ip_0=int(input("enter integer numerator of delta:\n"))
	ip_1=int(input("enter integer denominator of delta:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	delta=sympy.Rational(ip_0,ip_1)
	
	
	ip_0=int(input("enter integer numerator of skoS:\n"))
	ip_1=int(input("enter integer denominator of skoS:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	skoS=sympy.Rational(ip_0,ip_1)
	
	
	
	
	if pre_condition_0(delta=delta,skoS=skoS)==True:
		print("pre_condition_0 SAT")
		print('delta = 2')
		print('skoS = 217/100')
		print('skoCOSS = 1/8')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_1(delta=delta,skoS=skoS)==True:
		print("pre_condition_1 SAT")
		print('delta = 2')
		print('skoS = 217/100')
		print('skoCOSS = 1/8')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_2(delta=delta,skoS=skoS)==True:
		print("pre_condition_2 SAT")
		print('delta = 1/2')
		print('skoS = 217/100')
		print('skoCOSS = -1')
		print('skoSINS = 1/8')
		exit(0)
	
	
	if pre_condition_3(delta=delta,skoS=skoS)==True:
		print("pre_condition_3 SAT")
		print('delta = 1/2')
		print('skoS = 217/100')
		print('skoCOSS = -1')
		print('skoSINS = 1/8')
		exit(0)
	
	
	if pre_condition_4(delta=delta,skoS=skoS)==True:
		print("pre_condition_4 SAT")
		print('delta = 1/128')
		print('skoS = 217/100')
		print('skoCOSS = -1/16')
		print('skoSINS = 1')
		exit(0)
	
	
	if pre_condition_5(delta=delta,skoS=skoS)==True:
		print("pre_condition_5 SAT")
		print('delta = 1/128')
		print('skoS = 217/100')
		print('skoCOSS = -1/16')
		print('skoSINS = 1')
		exit(0)
	
	
	if pre_condition_6(delta=delta,skoS=skoS)==True:
		print("pre_condition_6 SAT")
		print('delta = 511/8388608')
		print('skoS = 217/100')
		print('skoCOSS = -255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_7(delta=delta,skoS=skoS)==True:
		print("pre_condition_7 SAT")
		print('delta = 511/8388608')
		print('skoS = 217/100')
		print('skoCOSS = -255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_8(delta=delta,skoS=skoS)==True:
		print("pre_condition_8 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = -255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_9(delta=delta,skoS=skoS)==True:
		print("pre_condition_9 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = -255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_10(delta=delta,skoS=skoS)==True:
		print("pre_condition_10 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = -255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_11(delta=delta,skoS=skoS)==True:
		print("pre_condition_11 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = -255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_12(delta=delta,skoS=skoS)==True:
		print("pre_condition_12 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = -255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_13(delta=delta,skoS=skoS)==True:
		print("pre_condition_13 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = -255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_14(delta=delta,skoS=skoS)==True:
		print("pre_condition_14 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_15(delta=delta,skoS=skoS)==True:
		print("pre_condition_15 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_16(delta=delta,skoS=skoS)==True:
		print("pre_condition_16 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = -255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_17(delta=delta,skoS=skoS)==True:
		print("pre_condition_17 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = -255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_18(delta=delta,skoS=skoS)==True:
		print("pre_condition_18 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = -255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_19(delta=delta,skoS=skoS)==True:
		print("pre_condition_19 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = -255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_20(delta=delta,skoS=skoS)==True:
		print("pre_condition_20 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_21(delta=delta,skoS=skoS)==True:
		print("pre_condition_21 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_22(delta=delta,skoS=skoS)==True:
		print("pre_condition_22 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_23(delta=delta,skoS=skoS)==True:
		print("pre_condition_23 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_24(delta=delta,skoS=skoS)==True:
		print("pre_condition_24 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_25(delta=delta,skoS=skoS)==True:
		print("pre_condition_25 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_26(delta=delta,skoS=skoS)==True:
		print("pre_condition_26 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_27(delta=delta,skoS=skoS)==True:
		print("pre_condition_27 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_28(delta=delta,skoS=skoS)==True:
		print("pre_condition_28 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_29(delta=delta,skoS=skoS)==True:
		print("pre_condition_29 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_30(delta=delta,skoS=skoS)==True:
		print("pre_condition_30 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_31(delta=delta,skoS=skoS)==True:
		print("pre_condition_31 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_32(delta=delta,skoS=skoS)==True:
		print("pre_condition_32 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_33(delta=delta,skoS=skoS)==True:
		print("pre_condition_33 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_34(delta=delta,skoS=skoS)==True:
		print("pre_condition_34 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_35(delta=delta,skoS=skoS)==True:
		print("pre_condition_35 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_36(delta=delta,skoS=skoS)==True:
		print("pre_condition_36 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_37(delta=delta,skoS=skoS)==True:
		print("pre_condition_37 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_38(delta=delta,skoS=skoS)==True:
		print("pre_condition_38 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_39(delta=delta,skoS=skoS)==True:
		print("pre_condition_39 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_40(delta=delta,skoS=skoS)==True:
		print("pre_condition_40 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_41(delta=delta,skoS=skoS)==True:
		print("pre_condition_41 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_42(delta=delta,skoS=skoS)==True:
		print("pre_condition_42 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_43(delta=delta,skoS=skoS)==True:
		print("pre_condition_43 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_44(delta=delta,skoS=skoS)==True:
		print("pre_condition_44 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_45(delta=delta,skoS=skoS)==True:
		print("pre_condition_45 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_46(delta=delta,skoS=skoS)==True:
		print("pre_condition_46 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_47(delta=delta,skoS=skoS)==True:
		print("pre_condition_47 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_48(delta=delta,skoS=skoS)==True:
		print("pre_condition_48 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_49(delta=delta,skoS=skoS)==True:
		print("pre_condition_49 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_50(delta=delta,skoS=skoS)==True:
		print("pre_condition_50 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_51(delta=delta,skoS=skoS)==True:
		print("pre_condition_51 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_52(delta=delta,skoS=skoS)==True:
		print("pre_condition_52 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_53(delta=delta,skoS=skoS)==True:
		print("pre_condition_53 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_54(delta=delta,skoS=skoS)==True:
		print("pre_condition_54 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_55(delta=delta,skoS=skoS)==True:
		print("pre_condition_55 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_56(delta=delta,skoS=skoS)==True:
		print("pre_condition_56 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_57(delta=delta,skoS=skoS)==True:
		print("pre_condition_57 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_58(delta=delta,skoS=skoS)==True:
		print("pre_condition_58 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_59(delta=delta,skoS=skoS)==True:
		print("pre_condition_59 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_60(delta=delta,skoS=skoS)==True:
		print("pre_condition_60 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_61(delta=delta,skoS=skoS)==True:
		print("pre_condition_61 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_62(delta=delta,skoS=skoS)==True:
		print("pre_condition_62 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_63(delta=delta,skoS=skoS)==True:
		print("pre_condition_63 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_64(delta=delta,skoS=skoS)==True:
		print("pre_condition_64 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_65(delta=delta,skoS=skoS)==True:
		print("pre_condition_65 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_66(delta=delta,skoS=skoS)==True:
		print("pre_condition_66 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_67(delta=delta,skoS=skoS)==True:
		print("pre_condition_67 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_68(delta=delta,skoS=skoS)==True:
		print("pre_condition_68 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_69(delta=delta,skoS=skoS)==True:
		print("pre_condition_69 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_70(delta=delta,skoS=skoS)==True:
		print("pre_condition_70 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_71(delta=delta,skoS=skoS)==True:
		print("pre_condition_71 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_72(delta=delta,skoS=skoS)==True:
		print("pre_condition_72 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_73(delta=delta,skoS=skoS)==True:
		print("pre_condition_73 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_74(delta=delta,skoS=skoS)==True:
		print("pre_condition_74 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_75(delta=delta,skoS=skoS)==True:
		print("pre_condition_75 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_76(delta=delta,skoS=skoS)==True:
		print("pre_condition_76 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_77(delta=delta,skoS=skoS)==True:
		print("pre_condition_77 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_78(delta=delta,skoS=skoS)==True:
		print("pre_condition_78 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_79(delta=delta,skoS=skoS)==True:
		print("pre_condition_79 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_80(delta=delta,skoS=skoS)==True:
		print("pre_condition_80 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_81(delta=delta,skoS=skoS)==True:
		print("pre_condition_81 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_82(delta=delta,skoS=skoS)==True:
		print("pre_condition_82 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_83(delta=delta,skoS=skoS)==True:
		print("pre_condition_83 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_84(delta=delta,skoS=skoS)==True:
		print("pre_condition_84 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_85(delta=delta,skoS=skoS)==True:
		print("pre_condition_85 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_86(delta=delta,skoS=skoS)==True:
		print("pre_condition_86 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_87(delta=delta,skoS=skoS)==True:
		print("pre_condition_87 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_88(delta=delta,skoS=skoS)==True:
		print("pre_condition_88 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_89(delta=delta,skoS=skoS)==True:
		print("pre_condition_89 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_90(delta=delta,skoS=skoS)==True:
		print("pre_condition_90 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_91(delta=delta,skoS=skoS)==True:
		print("pre_condition_91 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_92(delta=delta,skoS=skoS)==True:
		print("pre_condition_92 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_93(delta=delta,skoS=skoS)==True:
		print("pre_condition_93 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_94(delta=delta,skoS=skoS)==True:
		print("pre_condition_94 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_95(delta=delta,skoS=skoS)==True:
		print("pre_condition_95 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_96(delta=delta,skoS=skoS)==True:
		print("pre_condition_96 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_97(delta=delta,skoS=skoS)==True:
		print("pre_condition_97 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_98(delta=delta,skoS=skoS)==True:
		print("pre_condition_98 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_99(delta=delta,skoS=skoS)==True:
		print("pre_condition_99 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_100(delta=delta,skoS=skoS)==True:
		print("pre_condition_100 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_101(delta=delta,skoS=skoS)==True:
		print("pre_condition_101 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_102(delta=delta,skoS=skoS)==True:
		print("pre_condition_102 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_103(delta=delta,skoS=skoS)==True:
		print("pre_condition_103 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_104(delta=delta,skoS=skoS)==True:
		print("pre_condition_104 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_105(delta=delta,skoS=skoS)==True:
		print("pre_condition_105 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_106(delta=delta,skoS=skoS)==True:
		print("pre_condition_106 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_107(delta=delta,skoS=skoS)==True:
		print("pre_condition_107 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_108(delta=delta,skoS=skoS)==True:
		print("pre_condition_108 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_109(delta=delta,skoS=skoS)==True:
		print("pre_condition_109 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_110(delta=delta,skoS=skoS)==True:
		print("pre_condition_110 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_111(delta=delta,skoS=skoS)==True:
		print("pre_condition_111 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_112(delta=delta,skoS=skoS)==True:
		print("pre_condition_112 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_113(delta=delta,skoS=skoS)==True:
		print("pre_condition_113 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_114(delta=delta,skoS=skoS)==True:
		print("pre_condition_114 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_115(delta=delta,skoS=skoS)==True:
		print("pre_condition_115 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_116(delta=delta,skoS=skoS)==True:
		print("pre_condition_116 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_117(delta=delta,skoS=skoS)==True:
		print("pre_condition_117 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_118(delta=delta,skoS=skoS)==True:
		print("pre_condition_118 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_119(delta=delta,skoS=skoS)==True:
		print("pre_condition_119 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_120(delta=delta,skoS=skoS)==True:
		print("pre_condition_120 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_121(delta=delta,skoS=skoS)==True:
		print("pre_condition_121 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_122(delta=delta,skoS=skoS)==True:
		print("pre_condition_122 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_123(delta=delta,skoS=skoS)==True:
		print("pre_condition_123 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_124(delta=delta,skoS=skoS)==True:
		print("pre_condition_124 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_125(delta=delta,skoS=skoS)==True:
		print("pre_condition_125 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_126(delta=delta,skoS=skoS)==True:
		print("pre_condition_126 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_127(delta=delta,skoS=skoS)==True:
		print("pre_condition_127 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_128(delta=delta,skoS=skoS)==True:
		print("pre_condition_128 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_129(delta=delta,skoS=skoS)==True:
		print("pre_condition_129 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_130(delta=delta,skoS=skoS)==True:
		print("pre_condition_130 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_131(delta=delta,skoS=skoS)==True:
		print("pre_condition_131 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_132(delta=delta,skoS=skoS)==True:
		print("pre_condition_132 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_133(delta=delta,skoS=skoS)==True:
		print("pre_condition_133 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_134(delta=delta,skoS=skoS)==True:
		print("pre_condition_134 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_135(delta=delta,skoS=skoS)==True:
		print("pre_condition_135 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_136(delta=delta,skoS=skoS)==True:
		print("pre_condition_136 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_137(delta=delta,skoS=skoS)==True:
		print("pre_condition_137 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_138(delta=delta,skoS=skoS)==True:
		print("pre_condition_138 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_139(delta=delta,skoS=skoS)==True:
		print("pre_condition_139 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_140(delta=delta,skoS=skoS)==True:
		print("pre_condition_140 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_141(delta=delta,skoS=skoS)==True:
		print("pre_condition_141 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_142(delta=delta,skoS=skoS)==True:
		print("pre_condition_142 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_143(delta=delta,skoS=skoS)==True:
		print("pre_condition_143 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_144(delta=delta,skoS=skoS)==True:
		print("pre_condition_144 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_145(delta=delta,skoS=skoS)==True:
		print("pre_condition_145 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_146(delta=delta,skoS=skoS)==True:
		print("pre_condition_146 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_147(delta=delta,skoS=skoS)==True:
		print("pre_condition_147 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_148(delta=delta,skoS=skoS)==True:
		print("pre_condition_148 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_149(delta=delta,skoS=skoS)==True:
		print("pre_condition_149 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_150(delta=delta,skoS=skoS)==True:
		print("pre_condition_150 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_151(delta=delta,skoS=skoS)==True:
		print("pre_condition_151 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_152(delta=delta,skoS=skoS)==True:
		print("pre_condition_152 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_153(delta=delta,skoS=skoS)==True:
		print("pre_condition_153 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_154(delta=delta,skoS=skoS)==True:
		print("pre_condition_154 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_155(delta=delta,skoS=skoS)==True:
		print("pre_condition_155 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_156(delta=delta,skoS=skoS)==True:
		print("pre_condition_156 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_157(delta=delta,skoS=skoS)==True:
		print("pre_condition_157 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_158(delta=delta,skoS=skoS)==True:
		print("pre_condition_158 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_159(delta=delta,skoS=skoS)==True:
		print("pre_condition_159 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_160(delta=delta,skoS=skoS)==True:
		print("pre_condition_160 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_161(delta=delta,skoS=skoS)==True:
		print("pre_condition_161 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_162(delta=delta,skoS=skoS)==True:
		print("pre_condition_162 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_163(delta=delta,skoS=skoS)==True:
		print("pre_condition_163 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_164(delta=delta,skoS=skoS)==True:
		print("pre_condition_164 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_165(delta=delta,skoS=skoS)==True:
		print("pre_condition_165 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_166(delta=delta,skoS=skoS)==True:
		print("pre_condition_166 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_167(delta=delta,skoS=skoS)==True:
		print("pre_condition_167 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_168(delta=delta,skoS=skoS)==True:
		print("pre_condition_168 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_169(delta=delta,skoS=skoS)==True:
		print("pre_condition_169 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_170(delta=delta,skoS=skoS)==True:
		print("pre_condition_170 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_171(delta=delta,skoS=skoS)==True:
		print("pre_condition_171 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_172(delta=delta,skoS=skoS)==True:
		print("pre_condition_172 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_173(delta=delta,skoS=skoS)==True:
		print("pre_condition_173 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_174(delta=delta,skoS=skoS)==True:
		print("pre_condition_174 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_175(delta=delta,skoS=skoS)==True:
		print("pre_condition_175 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_176(delta=delta,skoS=skoS)==True:
		print("pre_condition_176 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_177(delta=delta,skoS=skoS)==True:
		print("pre_condition_177 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_178(delta=delta,skoS=skoS)==True:
		print("pre_condition_178 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_179(delta=delta,skoS=skoS)==True:
		print("pre_condition_179 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_180(delta=delta,skoS=skoS)==True:
		print("pre_condition_180 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_181(delta=delta,skoS=skoS)==True:
		print("pre_condition_181 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_182(delta=delta,skoS=skoS)==True:
		print("pre_condition_182 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_183(delta=delta,skoS=skoS)==True:
		print("pre_condition_183 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_184(delta=delta,skoS=skoS)==True:
		print("pre_condition_184 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_185(delta=delta,skoS=skoS)==True:
		print("pre_condition_185 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_186(delta=delta,skoS=skoS)==True:
		print("pre_condition_186 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_187(delta=delta,skoS=skoS)==True:
		print("pre_condition_187 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_188(delta=delta,skoS=skoS)==True:
		print("pre_condition_188 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_189(delta=delta,skoS=skoS)==True:
		print("pre_condition_189 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_190(delta=delta,skoS=skoS)==True:
		print("pre_condition_190 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_191(delta=delta,skoS=skoS)==True:
		print("pre_condition_191 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_192(delta=delta,skoS=skoS)==True:
		print("pre_condition_192 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_193(delta=delta,skoS=skoS)==True:
		print("pre_condition_193 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_194(delta=delta,skoS=skoS)==True:
		print("pre_condition_194 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_195(delta=delta,skoS=skoS)==True:
		print("pre_condition_195 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_196(delta=delta,skoS=skoS)==True:
		print("pre_condition_196 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_197(delta=delta,skoS=skoS)==True:
		print("pre_condition_197 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_198(delta=delta,skoS=skoS)==True:
		print("pre_condition_198 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_199(delta=delta,skoS=skoS)==True:
		print("pre_condition_199 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_200(delta=delta,skoS=skoS)==True:
		print("pre_condition_200 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_201(delta=delta,skoS=skoS)==True:
		print("pre_condition_201 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_202(delta=delta,skoS=skoS)==True:
		print("pre_condition_202 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_203(delta=delta,skoS=skoS)==True:
		print("pre_condition_203 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_204(delta=delta,skoS=skoS)==True:
		print("pre_condition_204 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_205(delta=delta,skoS=skoS)==True:
		print("pre_condition_205 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_206(delta=delta,skoS=skoS)==True:
		print("pre_condition_206 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_207(delta=delta,skoS=skoS)==True:
		print("pre_condition_207 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_208(delta=delta,skoS=skoS)==True:
		print("pre_condition_208 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_209(delta=delta,skoS=skoS)==True:
		print("pre_condition_209 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_210(delta=delta,skoS=skoS)==True:
		print("pre_condition_210 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_211(delta=delta,skoS=skoS)==True:
		print("pre_condition_211 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_212(delta=delta,skoS=skoS)==True:
		print("pre_condition_212 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_213(delta=delta,skoS=skoS)==True:
		print("pre_condition_213 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_214(delta=delta,skoS=skoS)==True:
		print("pre_condition_214 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_215(delta=delta,skoS=skoS)==True:
		print("pre_condition_215 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_216(delta=delta,skoS=skoS)==True:
		print("pre_condition_216 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_217(delta=delta,skoS=skoS)==True:
		print("pre_condition_217 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_218(delta=delta,skoS=skoS)==True:
		print("pre_condition_218 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_219(delta=delta,skoS=skoS)==True:
		print("pre_condition_219 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_220(delta=delta,skoS=skoS)==True:
		print("pre_condition_220 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_221(delta=delta,skoS=skoS)==True:
		print("pre_condition_221 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_222(delta=delta,skoS=skoS)==True:
		print("pre_condition_222 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_223(delta=delta,skoS=skoS)==True:
		print("pre_condition_223 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_224(delta=delta,skoS=skoS)==True:
		print("pre_condition_224 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_225(delta=delta,skoS=skoS)==True:
		print("pre_condition_225 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_226(delta=delta,skoS=skoS)==True:
		print("pre_condition_226 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_227(delta=delta,skoS=skoS)==True:
		print("pre_condition_227 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_228(delta=delta,skoS=skoS)==True:
		print("pre_condition_228 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_229(delta=delta,skoS=skoS)==True:
		print("pre_condition_229 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_230(delta=delta,skoS=skoS)==True:
		print("pre_condition_230 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_231(delta=delta,skoS=skoS)==True:
		print("pre_condition_231 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_232(delta=delta,skoS=skoS)==True:
		print("pre_condition_232 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_233(delta=delta,skoS=skoS)==True:
		print("pre_condition_233 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_234(delta=delta,skoS=skoS)==True:
		print("pre_condition_234 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_235(delta=delta,skoS=skoS)==True:
		print("pre_condition_235 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_236(delta=delta,skoS=skoS)==True:
		print("pre_condition_236 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_237(delta=delta,skoS=skoS)==True:
		print("pre_condition_237 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_238(delta=delta,skoS=skoS)==True:
		print("pre_condition_238 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_239(delta=delta,skoS=skoS)==True:
		print("pre_condition_239 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_240(delta=delta,skoS=skoS)==True:
		print("pre_condition_240 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_241(delta=delta,skoS=skoS)==True:
		print("pre_condition_241 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_242(delta=delta,skoS=skoS)==True:
		print("pre_condition_242 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_243(delta=delta,skoS=skoS)==True:
		print("pre_condition_243 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_244(delta=delta,skoS=skoS)==True:
		print("pre_condition_244 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_245(delta=delta,skoS=skoS)==True:
		print("pre_condition_245 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_246(delta=delta,skoS=skoS)==True:
		print("pre_condition_246 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_247(delta=delta,skoS=skoS)==True:
		print("pre_condition_247 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_248(delta=delta,skoS=skoS)==True:
		print("pre_condition_248 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_249(delta=delta,skoS=skoS)==True:
		print("pre_condition_249 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_250(delta=delta,skoS=skoS)==True:
		print("pre_condition_250 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_251(delta=delta,skoS=skoS)==True:
		print("pre_condition_251 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_252(delta=delta,skoS=skoS)==True:
		print("pre_condition_252 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_253(delta=delta,skoS=skoS)==True:
		print("pre_condition_253 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_254(delta=delta,skoS=skoS)==True:
		print("pre_condition_254 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_255(delta=delta,skoS=skoS)==True:
		print("pre_condition_255 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_256(delta=delta,skoS=skoS)==True:
		print("pre_condition_256 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_257(delta=delta,skoS=skoS)==True:
		print("pre_condition_257 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_258(delta=delta,skoS=skoS)==True:
		print("pre_condition_258 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_259(delta=delta,skoS=skoS)==True:
		print("pre_condition_259 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_260(delta=delta,skoS=skoS)==True:
		print("pre_condition_260 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_261(delta=delta,skoS=skoS)==True:
		print("pre_condition_261 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_262(delta=delta,skoS=skoS)==True:
		print("pre_condition_262 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_263(delta=delta,skoS=skoS)==True:
		print("pre_condition_263 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_264(delta=delta,skoS=skoS)==True:
		print("pre_condition_264 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_265(delta=delta,skoS=skoS)==True:
		print("pre_condition_265 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_266(delta=delta,skoS=skoS)==True:
		print("pre_condition_266 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_267(delta=delta,skoS=skoS)==True:
		print("pre_condition_267 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_268(delta=delta,skoS=skoS)==True:
		print("pre_condition_268 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_269(delta=delta,skoS=skoS)==True:
		print("pre_condition_269 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_270(delta=delta,skoS=skoS)==True:
		print("pre_condition_270 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_271(delta=delta,skoS=skoS)==True:
		print("pre_condition_271 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_272(delta=delta,skoS=skoS)==True:
		print("pre_condition_272 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_273(delta=delta,skoS=skoS)==True:
		print("pre_condition_273 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_274(delta=delta,skoS=skoS)==True:
		print("pre_condition_274 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_275(delta=delta,skoS=skoS)==True:
		print("pre_condition_275 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_276(delta=delta,skoS=skoS)==True:
		print("pre_condition_276 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_277(delta=delta,skoS=skoS)==True:
		print("pre_condition_277 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_278(delta=delta,skoS=skoS)==True:
		print("pre_condition_278 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_279(delta=delta,skoS=skoS)==True:
		print("pre_condition_279 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_280(delta=delta,skoS=skoS)==True:
		print("pre_condition_280 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_281(delta=delta,skoS=skoS)==True:
		print("pre_condition_281 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_282(delta=delta,skoS=skoS)==True:
		print("pre_condition_282 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_283(delta=delta,skoS=skoS)==True:
		print("pre_condition_283 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_284(delta=delta,skoS=skoS)==True:
		print("pre_condition_284 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_285(delta=delta,skoS=skoS)==True:
		print("pre_condition_285 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_286(delta=delta,skoS=skoS)==True:
		print("pre_condition_286 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_287(delta=delta,skoS=skoS)==True:
		print("pre_condition_287 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_288(delta=delta,skoS=skoS)==True:
		print("pre_condition_288 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_289(delta=delta,skoS=skoS)==True:
		print("pre_condition_289 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_290(delta=delta,skoS=skoS)==True:
		print("pre_condition_290 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_291(delta=delta,skoS=skoS)==True:
		print("pre_condition_291 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_292(delta=delta,skoS=skoS)==True:
		print("pre_condition_292 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_293(delta=delta,skoS=skoS)==True:
		print("pre_condition_293 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_294(delta=delta,skoS=skoS)==True:
		print("pre_condition_294 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_295(delta=delta,skoS=skoS)==True:
		print("pre_condition_295 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_296(delta=delta,skoS=skoS)==True:
		print("pre_condition_296 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_297(delta=delta,skoS=skoS)==True:
		print("pre_condition_297 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_298(delta=delta,skoS=skoS)==True:
		print("pre_condition_298 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_299(delta=delta,skoS=skoS)==True:
		print("pre_condition_299 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_300(delta=delta,skoS=skoS)==True:
		print("pre_condition_300 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_301(delta=delta,skoS=skoS)==True:
		print("pre_condition_301 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_302(delta=delta,skoS=skoS)==True:
		print("pre_condition_302 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_303(delta=delta,skoS=skoS)==True:
		print("pre_condition_303 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_304(delta=delta,skoS=skoS)==True:
		print("pre_condition_304 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_305(delta=delta,skoS=skoS)==True:
		print("pre_condition_305 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_306(delta=delta,skoS=skoS)==True:
		print("pre_condition_306 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_307(delta=delta,skoS=skoS)==True:
		print("pre_condition_307 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_308(delta=delta,skoS=skoS)==True:
		print("pre_condition_308 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_309(delta=delta,skoS=skoS)==True:
		print("pre_condition_309 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_310(delta=delta,skoS=skoS)==True:
		print("pre_condition_310 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_311(delta=delta,skoS=skoS)==True:
		print("pre_condition_311 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_312(delta=delta,skoS=skoS)==True:
		print("pre_condition_312 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_313(delta=delta,skoS=skoS)==True:
		print("pre_condition_313 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_314(delta=delta,skoS=skoS)==True:
		print("pre_condition_314 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_315(delta=delta,skoS=skoS)==True:
		print("pre_condition_315 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_316(delta=delta,skoS=skoS)==True:
		print("pre_condition_316 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_317(delta=delta,skoS=skoS)==True:
		print("pre_condition_317 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_318(delta=delta,skoS=skoS)==True:
		print("pre_condition_318 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_319(delta=delta,skoS=skoS)==True:
		print("pre_condition_319 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_320(delta=delta,skoS=skoS)==True:
		print("pre_condition_320 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_321(delta=delta,skoS=skoS)==True:
		print("pre_condition_321 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_322(delta=delta,skoS=skoS)==True:
		print("pre_condition_322 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_323(delta=delta,skoS=skoS)==True:
		print("pre_condition_323 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_324(delta=delta,skoS=skoS)==True:
		print("pre_condition_324 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_325(delta=delta,skoS=skoS)==True:
		print("pre_condition_325 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_326(delta=delta,skoS=skoS)==True:
		print("pre_condition_326 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_327(delta=delta,skoS=skoS)==True:
		print("pre_condition_327 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_328(delta=delta,skoS=skoS)==True:
		print("pre_condition_328 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_329(delta=delta,skoS=skoS)==True:
		print("pre_condition_329 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_330(delta=delta,skoS=skoS)==True:
		print("pre_condition_330 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_331(delta=delta,skoS=skoS)==True:
		print("pre_condition_331 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_332(delta=delta,skoS=skoS)==True:
		print("pre_condition_332 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_333(delta=delta,skoS=skoS)==True:
		print("pre_condition_333 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_334(delta=delta,skoS=skoS)==True:
		print("pre_condition_334 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_335(delta=delta,skoS=skoS)==True:
		print("pre_condition_335 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_336(delta=delta,skoS=skoS)==True:
		print("pre_condition_336 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_337(delta=delta,skoS=skoS)==True:
		print("pre_condition_337 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_338(delta=delta,skoS=skoS)==True:
		print("pre_condition_338 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_339(delta=delta,skoS=skoS)==True:
		print("pre_condition_339 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_340(delta=delta,skoS=skoS)==True:
		print("pre_condition_340 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_341(delta=delta,skoS=skoS)==True:
		print("pre_condition_341 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_342(delta=delta,skoS=skoS)==True:
		print("pre_condition_342 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_343(delta=delta,skoS=skoS)==True:
		print("pre_condition_343 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_344(delta=delta,skoS=skoS)==True:
		print("pre_condition_344 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_345(delta=delta,skoS=skoS)==True:
		print("pre_condition_345 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_346(delta=delta,skoS=skoS)==True:
		print("pre_condition_346 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_347(delta=delta,skoS=skoS)==True:
		print("pre_condition_347 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_348(delta=delta,skoS=skoS)==True:
		print("pre_condition_348 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_349(delta=delta,skoS=skoS)==True:
		print("pre_condition_349 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_350(delta=delta,skoS=skoS)==True:
		print("pre_condition_350 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_351(delta=delta,skoS=skoS)==True:
		print("pre_condition_351 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_352(delta=delta,skoS=skoS)==True:
		print("pre_condition_352 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_353(delta=delta,skoS=skoS)==True:
		print("pre_condition_353 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_354(delta=delta,skoS=skoS)==True:
		print("pre_condition_354 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_355(delta=delta,skoS=skoS)==True:
		print("pre_condition_355 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_356(delta=delta,skoS=skoS)==True:
		print("pre_condition_356 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_357(delta=delta,skoS=skoS)==True:
		print("pre_condition_357 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_358(delta=delta,skoS=skoS)==True:
		print("pre_condition_358 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_359(delta=delta,skoS=skoS)==True:
		print("pre_condition_359 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_360(delta=delta,skoS=skoS)==True:
		print("pre_condition_360 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_361(delta=delta,skoS=skoS)==True:
		print("pre_condition_361 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_362(delta=delta,skoS=skoS)==True:
		print("pre_condition_362 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_363(delta=delta,skoS=skoS)==True:
		print("pre_condition_363 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_364(delta=delta,skoS=skoS)==True:
		print("pre_condition_364 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_365(delta=delta,skoS=skoS)==True:
		print("pre_condition_365 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_366(delta=delta,skoS=skoS)==True:
		print("pre_condition_366 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_367(delta=delta,skoS=skoS)==True:
		print("pre_condition_367 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_368(delta=delta,skoS=skoS)==True:
		print("pre_condition_368 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_369(delta=delta,skoS=skoS)==True:
		print("pre_condition_369 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_370(delta=delta,skoS=skoS)==True:
		print("pre_condition_370 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_371(delta=delta,skoS=skoS)==True:
		print("pre_condition_371 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_372(delta=delta,skoS=skoS)==True:
		print("pre_condition_372 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_373(delta=delta,skoS=skoS)==True:
		print("pre_condition_373 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_374(delta=delta,skoS=skoS)==True:
		print("pre_condition_374 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_375(delta=delta,skoS=skoS)==True:
		print("pre_condition_375 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_376(delta=delta,skoS=skoS)==True:
		print("pre_condition_376 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_377(delta=delta,skoS=skoS)==True:
		print("pre_condition_377 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_378(delta=delta,skoS=skoS)==True:
		print("pre_condition_378 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_379(delta=delta,skoS=skoS)==True:
		print("pre_condition_379 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_380(delta=delta,skoS=skoS)==True:
		print("pre_condition_380 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_381(delta=delta,skoS=skoS)==True:
		print("pre_condition_381 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_382(delta=delta,skoS=skoS)==True:
		print("pre_condition_382 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_383(delta=delta,skoS=skoS)==True:
		print("pre_condition_383 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_384(delta=delta,skoS=skoS)==True:
		print("pre_condition_384 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_385(delta=delta,skoS=skoS)==True:
		print("pre_condition_385 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_386(delta=delta,skoS=skoS)==True:
		print("pre_condition_386 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_387(delta=delta,skoS=skoS)==True:
		print("pre_condition_387 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_388(delta=delta,skoS=skoS)==True:
		print("pre_condition_388 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_389(delta=delta,skoS=skoS)==True:
		print("pre_condition_389 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_390(delta=delta,skoS=skoS)==True:
		print("pre_condition_390 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_391(delta=delta,skoS=skoS)==True:
		print("pre_condition_391 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_392(delta=delta,skoS=skoS)==True:
		print("pre_condition_392 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_393(delta=delta,skoS=skoS)==True:
		print("pre_condition_393 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_394(delta=delta,skoS=skoS)==True:
		print("pre_condition_394 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_395(delta=delta,skoS=skoS)==True:
		print("pre_condition_395 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_396(delta=delta,skoS=skoS)==True:
		print("pre_condition_396 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_397(delta=delta,skoS=skoS)==True:
		print("pre_condition_397 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_398(delta=delta,skoS=skoS)==True:
		print("pre_condition_398 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_399(delta=delta,skoS=skoS)==True:
		print("pre_condition_399 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_400(delta=delta,skoS=skoS)==True:
		print("pre_condition_400 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_401(delta=delta,skoS=skoS)==True:
		print("pre_condition_401 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_402(delta=delta,skoS=skoS)==True:
		print("pre_condition_402 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_403(delta=delta,skoS=skoS)==True:
		print("pre_condition_403 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_404(delta=delta,skoS=skoS)==True:
		print("pre_condition_404 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_405(delta=delta,skoS=skoS)==True:
		print("pre_condition_405 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_406(delta=delta,skoS=skoS)==True:
		print("pre_condition_406 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_407(delta=delta,skoS=skoS)==True:
		print("pre_condition_407 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_408(delta=delta,skoS=skoS)==True:
		print("pre_condition_408 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_409(delta=delta,skoS=skoS)==True:
		print("pre_condition_409 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_410(delta=delta,skoS=skoS)==True:
		print("pre_condition_410 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_411(delta=delta,skoS=skoS)==True:
		print("pre_condition_411 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_412(delta=delta,skoS=skoS)==True:
		print("pre_condition_412 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_413(delta=delta,skoS=skoS)==True:
		print("pre_condition_413 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_414(delta=delta,skoS=skoS)==True:
		print("pre_condition_414 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_415(delta=delta,skoS=skoS)==True:
		print("pre_condition_415 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_416(delta=delta,skoS=skoS)==True:
		print("pre_condition_416 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_417(delta=delta,skoS=skoS)==True:
		print("pre_condition_417 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_418(delta=delta,skoS=skoS)==True:
		print("pre_condition_418 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_419(delta=delta,skoS=skoS)==True:
		print("pre_condition_419 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_420(delta=delta,skoS=skoS)==True:
		print("pre_condition_420 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_421(delta=delta,skoS=skoS)==True:
		print("pre_condition_421 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_422(delta=delta,skoS=skoS)==True:
		print("pre_condition_422 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_423(delta=delta,skoS=skoS)==True:
		print("pre_condition_423 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_424(delta=delta,skoS=skoS)==True:
		print("pre_condition_424 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_425(delta=delta,skoS=skoS)==True:
		print("pre_condition_425 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_426(delta=delta,skoS=skoS)==True:
		print("pre_condition_426 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_427(delta=delta,skoS=skoS)==True:
		print("pre_condition_427 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_428(delta=delta,skoS=skoS)==True:
		print("pre_condition_428 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_429(delta=delta,skoS=skoS)==True:
		print("pre_condition_429 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_430(delta=delta,skoS=skoS)==True:
		print("pre_condition_430 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_431(delta=delta,skoS=skoS)==True:
		print("pre_condition_431 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_432(delta=delta,skoS=skoS)==True:
		print("pre_condition_432 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_433(delta=delta,skoS=skoS)==True:
		print("pre_condition_433 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_434(delta=delta,skoS=skoS)==True:
		print("pre_condition_434 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_435(delta=delta,skoS=skoS)==True:
		print("pre_condition_435 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_436(delta=delta,skoS=skoS)==True:
		print("pre_condition_436 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_437(delta=delta,skoS=skoS)==True:
		print("pre_condition_437 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_438(delta=delta,skoS=skoS)==True:
		print("pre_condition_438 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_439(delta=delta,skoS=skoS)==True:
		print("pre_condition_439 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_440(delta=delta,skoS=skoS)==True:
		print("pre_condition_440 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_441(delta=delta,skoS=skoS)==True:
		print("pre_condition_441 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_442(delta=delta,skoS=skoS)==True:
		print("pre_condition_442 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_443(delta=delta,skoS=skoS)==True:
		print("pre_condition_443 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_444(delta=delta,skoS=skoS)==True:
		print("pre_condition_444 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_445(delta=delta,skoS=skoS)==True:
		print("pre_condition_445 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_446(delta=delta,skoS=skoS)==True:
		print("pre_condition_446 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_447(delta=delta,skoS=skoS)==True:
		print("pre_condition_447 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_448(delta=delta,skoS=skoS)==True:
		print("pre_condition_448 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_449(delta=delta,skoS=skoS)==True:
		print("pre_condition_449 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_450(delta=delta,skoS=skoS)==True:
		print("pre_condition_450 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_451(delta=delta,skoS=skoS)==True:
		print("pre_condition_451 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_452(delta=delta,skoS=skoS)==True:
		print("pre_condition_452 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_453(delta=delta,skoS=skoS)==True:
		print("pre_condition_453 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_454(delta=delta,skoS=skoS)==True:
		print("pre_condition_454 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_455(delta=delta,skoS=skoS)==True:
		print("pre_condition_455 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_456(delta=delta,skoS=skoS)==True:
		print("pre_condition_456 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_457(delta=delta,skoS=skoS)==True:
		print("pre_condition_457 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_458(delta=delta,skoS=skoS)==True:
		print("pre_condition_458 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_459(delta=delta,skoS=skoS)==True:
		print("pre_condition_459 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_460(delta=delta,skoS=skoS)==True:
		print("pre_condition_460 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_461(delta=delta,skoS=skoS)==True:
		print("pre_condition_461 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_462(delta=delta,skoS=skoS)==True:
		print("pre_condition_462 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_463(delta=delta,skoS=skoS)==True:
		print("pre_condition_463 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_464(delta=delta,skoS=skoS)==True:
		print("pre_condition_464 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_465(delta=delta,skoS=skoS)==True:
		print("pre_condition_465 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_466(delta=delta,skoS=skoS)==True:
		print("pre_condition_466 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_467(delta=delta,skoS=skoS)==True:
		print("pre_condition_467 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_468(delta=delta,skoS=skoS)==True:
		print("pre_condition_468 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_469(delta=delta,skoS=skoS)==True:
		print("pre_condition_469 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_470(delta=delta,skoS=skoS)==True:
		print("pre_condition_470 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_471(delta=delta,skoS=skoS)==True:
		print("pre_condition_471 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_472(delta=delta,skoS=skoS)==True:
		print("pre_condition_472 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_473(delta=delta,skoS=skoS)==True:
		print("pre_condition_473 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_474(delta=delta,skoS=skoS)==True:
		print("pre_condition_474 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_475(delta=delta,skoS=skoS)==True:
		print("pre_condition_475 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_476(delta=delta,skoS=skoS)==True:
		print("pre_condition_476 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_477(delta=delta,skoS=skoS)==True:
		print("pre_condition_477 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_478(delta=delta,skoS=skoS)==True:
		print("pre_condition_478 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_479(delta=delta,skoS=skoS)==True:
		print("pre_condition_479 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_480(delta=delta,skoS=skoS)==True:
		print("pre_condition_480 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_481(delta=delta,skoS=skoS)==True:
		print("pre_condition_481 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_482(delta=delta,skoS=skoS)==True:
		print("pre_condition_482 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_483(delta=delta,skoS=skoS)==True:
		print("pre_condition_483 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_484(delta=delta,skoS=skoS)==True:
		print("pre_condition_484 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_485(delta=delta,skoS=skoS)==True:
		print("pre_condition_485 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_486(delta=delta,skoS=skoS)==True:
		print("pre_condition_486 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_487(delta=delta,skoS=skoS)==True:
		print("pre_condition_487 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_488(delta=delta,skoS=skoS)==True:
		print("pre_condition_488 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_489(delta=delta,skoS=skoS)==True:
		print("pre_condition_489 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_490(delta=delta,skoS=skoS)==True:
		print("pre_condition_490 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_491(delta=delta,skoS=skoS)==True:
		print("pre_condition_491 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_492(delta=delta,skoS=skoS)==True:
		print("pre_condition_492 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_493(delta=delta,skoS=skoS)==True:
		print("pre_condition_493 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_494(delta=delta,skoS=skoS)==True:
		print("pre_condition_494 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_495(delta=delta,skoS=skoS)==True:
		print("pre_condition_495 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_496(delta=delta,skoS=skoS)==True:
		print("pre_condition_496 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_497(delta=delta,skoS=skoS)==True:
		print("pre_condition_497 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_498(delta=delta,skoS=skoS)==True:
		print("pre_condition_498 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_499(delta=delta,skoS=skoS)==True:
		print("pre_condition_499 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_500(delta=delta,skoS=skoS)==True:
		print("pre_condition_500 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_501(delta=delta,skoS=skoS)==True:
		print("pre_condition_501 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_502(delta=delta,skoS=skoS)==True:
		print("pre_condition_502 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_503(delta=delta,skoS=skoS)==True:
		print("pre_condition_503 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_504(delta=delta,skoS=skoS)==True:
		print("pre_condition_504 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_505(delta=delta,skoS=skoS)==True:
		print("pre_condition_505 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_506(delta=delta,skoS=skoS)==True:
		print("pre_condition_506 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_507(delta=delta,skoS=skoS)==True:
		print("pre_condition_507 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_508(delta=delta,skoS=skoS)==True:
		print("pre_condition_508 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_509(delta=delta,skoS=skoS)==True:
		print("pre_condition_509 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_510(delta=delta,skoS=skoS)==True:
		print("pre_condition_510 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_511(delta=delta,skoS=skoS)==True:
		print("pre_condition_511 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_512(delta=delta,skoS=skoS)==True:
		print("pre_condition_512 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_513(delta=delta,skoS=skoS)==True:
		print("pre_condition_513 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_514(delta=delta,skoS=skoS)==True:
		print("pre_condition_514 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_515(delta=delta,skoS=skoS)==True:
		print("pre_condition_515 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_516(delta=delta,skoS=skoS)==True:
		print("pre_condition_516 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_517(delta=delta,skoS=skoS)==True:
		print("pre_condition_517 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_518(delta=delta,skoS=skoS)==True:
		print("pre_condition_518 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_519(delta=delta,skoS=skoS)==True:
		print("pre_condition_519 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_520(delta=delta,skoS=skoS)==True:
		print("pre_condition_520 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_521(delta=delta,skoS=skoS)==True:
		print("pre_condition_521 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_522(delta=delta,skoS=skoS)==True:
		print("pre_condition_522 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_523(delta=delta,skoS=skoS)==True:
		print("pre_condition_523 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_524(delta=delta,skoS=skoS)==True:
		print("pre_condition_524 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_525(delta=delta,skoS=skoS)==True:
		print("pre_condition_525 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_526(delta=delta,skoS=skoS)==True:
		print("pre_condition_526 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_527(delta=delta,skoS=skoS)==True:
		print("pre_condition_527 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_528(delta=delta,skoS=skoS)==True:
		print("pre_condition_528 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_529(delta=delta,skoS=skoS)==True:
		print("pre_condition_529 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_530(delta=delta,skoS=skoS)==True:
		print("pre_condition_530 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_531(delta=delta,skoS=skoS)==True:
		print("pre_condition_531 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_532(delta=delta,skoS=skoS)==True:
		print("pre_condition_532 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_533(delta=delta,skoS=skoS)==True:
		print("pre_condition_533 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_534(delta=delta,skoS=skoS)==True:
		print("pre_condition_534 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_535(delta=delta,skoS=skoS)==True:
		print("pre_condition_535 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_536(delta=delta,skoS=skoS)==True:
		print("pre_condition_536 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_537(delta=delta,skoS=skoS)==True:
		print("pre_condition_537 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_538(delta=delta,skoS=skoS)==True:
		print("pre_condition_538 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_539(delta=delta,skoS=skoS)==True:
		print("pre_condition_539 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_540(delta=delta,skoS=skoS)==True:
		print("pre_condition_540 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_541(delta=delta,skoS=skoS)==True:
		print("pre_condition_541 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_542(delta=delta,skoS=skoS)==True:
		print("pre_condition_542 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_543(delta=delta,skoS=skoS)==True:
		print("pre_condition_543 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_544(delta=delta,skoS=skoS)==True:
		print("pre_condition_544 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_545(delta=delta,skoS=skoS)==True:
		print("pre_condition_545 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_546(delta=delta,skoS=skoS)==True:
		print("pre_condition_546 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_547(delta=delta,skoS=skoS)==True:
		print("pre_condition_547 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_548(delta=delta,skoS=skoS)==True:
		print("pre_condition_548 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_549(delta=delta,skoS=skoS)==True:
		print("pre_condition_549 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_550(delta=delta,skoS=skoS)==True:
		print("pre_condition_550 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_551(delta=delta,skoS=skoS)==True:
		print("pre_condition_551 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_552(delta=delta,skoS=skoS)==True:
		print("pre_condition_552 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_553(delta=delta,skoS=skoS)==True:
		print("pre_condition_553 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_554(delta=delta,skoS=skoS)==True:
		print("pre_condition_554 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_555(delta=delta,skoS=skoS)==True:
		print("pre_condition_555 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_556(delta=delta,skoS=skoS)==True:
		print("pre_condition_556 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_557(delta=delta,skoS=skoS)==True:
		print("pre_condition_557 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_558(delta=delta,skoS=skoS)==True:
		print("pre_condition_558 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_559(delta=delta,skoS=skoS)==True:
		print("pre_condition_559 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_560(delta=delta,skoS=skoS)==True:
		print("pre_condition_560 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_561(delta=delta,skoS=skoS)==True:
		print("pre_condition_561 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_562(delta=delta,skoS=skoS)==True:
		print("pre_condition_562 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_563(delta=delta,skoS=skoS)==True:
		print("pre_condition_563 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_564(delta=delta,skoS=skoS)==True:
		print("pre_condition_564 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_565(delta=delta,skoS=skoS)==True:
		print("pre_condition_565 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_566(delta=delta,skoS=skoS)==True:
		print("pre_condition_566 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_567(delta=delta,skoS=skoS)==True:
		print("pre_condition_567 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_568(delta=delta,skoS=skoS)==True:
		print("pre_condition_568 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_569(delta=delta,skoS=skoS)==True:
		print("pre_condition_569 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_570(delta=delta,skoS=skoS)==True:
		print("pre_condition_570 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_571(delta=delta,skoS=skoS)==True:
		print("pre_condition_571 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_572(delta=delta,skoS=skoS)==True:
		print("pre_condition_572 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_573(delta=delta,skoS=skoS)==True:
		print("pre_condition_573 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_574(delta=delta,skoS=skoS)==True:
		print("pre_condition_574 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_575(delta=delta,skoS=skoS)==True:
		print("pre_condition_575 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_576(delta=delta,skoS=skoS)==True:
		print("pre_condition_576 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_577(delta=delta,skoS=skoS)==True:
		print("pre_condition_577 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_578(delta=delta,skoS=skoS)==True:
		print("pre_condition_578 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_579(delta=delta,skoS=skoS)==True:
		print("pre_condition_579 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_580(delta=delta,skoS=skoS)==True:
		print("pre_condition_580 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_581(delta=delta,skoS=skoS)==True:
		print("pre_condition_581 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_582(delta=delta,skoS=skoS)==True:
		print("pre_condition_582 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_583(delta=delta,skoS=skoS)==True:
		print("pre_condition_583 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_584(delta=delta,skoS=skoS)==True:
		print("pre_condition_584 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_585(delta=delta,skoS=skoS)==True:
		print("pre_condition_585 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_586(delta=delta,skoS=skoS)==True:
		print("pre_condition_586 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_587(delta=delta,skoS=skoS)==True:
		print("pre_condition_587 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_588(delta=delta,skoS=skoS)==True:
		print("pre_condition_588 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_589(delta=delta,skoS=skoS)==True:
		print("pre_condition_589 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_590(delta=delta,skoS=skoS)==True:
		print("pre_condition_590 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_591(delta=delta,skoS=skoS)==True:
		print("pre_condition_591 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_592(delta=delta,skoS=skoS)==True:
		print("pre_condition_592 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_593(delta=delta,skoS=skoS)==True:
		print("pre_condition_593 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_594(delta=delta,skoS=skoS)==True:
		print("pre_condition_594 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_595(delta=delta,skoS=skoS)==True:
		print("pre_condition_595 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_596(delta=delta,skoS=skoS)==True:
		print("pre_condition_596 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_597(delta=delta,skoS=skoS)==True:
		print("pre_condition_597 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_598(delta=delta,skoS=skoS)==True:
		print("pre_condition_598 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_599(delta=delta,skoS=skoS)==True:
		print("pre_condition_599 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_600(delta=delta,skoS=skoS)==True:
		print("pre_condition_600 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_601(delta=delta,skoS=skoS)==True:
		print("pre_condition_601 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_602(delta=delta,skoS=skoS)==True:
		print("pre_condition_602 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_603(delta=delta,skoS=skoS)==True:
		print("pre_condition_603 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_604(delta=delta,skoS=skoS)==True:
		print("pre_condition_604 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_605(delta=delta,skoS=skoS)==True:
		print("pre_condition_605 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_606(delta=delta,skoS=skoS)==True:
		print("pre_condition_606 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_607(delta=delta,skoS=skoS)==True:
		print("pre_condition_607 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_608(delta=delta,skoS=skoS)==True:
		print("pre_condition_608 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_609(delta=delta,skoS=skoS)==True:
		print("pre_condition_609 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_610(delta=delta,skoS=skoS)==True:
		print("pre_condition_610 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_611(delta=delta,skoS=skoS)==True:
		print("pre_condition_611 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_612(delta=delta,skoS=skoS)==True:
		print("pre_condition_612 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_613(delta=delta,skoS=skoS)==True:
		print("pre_condition_613 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_614(delta=delta,skoS=skoS)==True:
		print("pre_condition_614 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_615(delta=delta,skoS=skoS)==True:
		print("pre_condition_615 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_616(delta=delta,skoS=skoS)==True:
		print("pre_condition_616 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_617(delta=delta,skoS=skoS)==True:
		print("pre_condition_617 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_618(delta=delta,skoS=skoS)==True:
		print("pre_condition_618 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_619(delta=delta,skoS=skoS)==True:
		print("pre_condition_619 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_620(delta=delta,skoS=skoS)==True:
		print("pre_condition_620 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_621(delta=delta,skoS=skoS)==True:
		print("pre_condition_621 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_622(delta=delta,skoS=skoS)==True:
		print("pre_condition_622 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_623(delta=delta,skoS=skoS)==True:
		print("pre_condition_623 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_624(delta=delta,skoS=skoS)==True:
		print("pre_condition_624 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_625(delta=delta,skoS=skoS)==True:
		print("pre_condition_625 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_626(delta=delta,skoS=skoS)==True:
		print("pre_condition_626 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_627(delta=delta,skoS=skoS)==True:
		print("pre_condition_627 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_628(delta=delta,skoS=skoS)==True:
		print("pre_condition_628 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_629(delta=delta,skoS=skoS)==True:
		print("pre_condition_629 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_630(delta=delta,skoS=skoS)==True:
		print("pre_condition_630 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_631(delta=delta,skoS=skoS)==True:
		print("pre_condition_631 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_632(delta=delta,skoS=skoS)==True:
		print("pre_condition_632 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_633(delta=delta,skoS=skoS)==True:
		print("pre_condition_633 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_634(delta=delta,skoS=skoS)==True:
		print("pre_condition_634 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_635(delta=delta,skoS=skoS)==True:
		print("pre_condition_635 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_636(delta=delta,skoS=skoS)==True:
		print("pre_condition_636 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_637(delta=delta,skoS=skoS)==True:
		print("pre_condition_637 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_638(delta=delta,skoS=skoS)==True:
		print("pre_condition_638 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_639(delta=delta,skoS=skoS)==True:
		print("pre_condition_639 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_640(delta=delta,skoS=skoS)==True:
		print("pre_condition_640 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_641(delta=delta,skoS=skoS)==True:
		print("pre_condition_641 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_642(delta=delta,skoS=skoS)==True:
		print("pre_condition_642 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_643(delta=delta,skoS=skoS)==True:
		print("pre_condition_643 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_644(delta=delta,skoS=skoS)==True:
		print("pre_condition_644 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_645(delta=delta,skoS=skoS)==True:
		print("pre_condition_645 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_646(delta=delta,skoS=skoS)==True:
		print("pre_condition_646 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_647(delta=delta,skoS=skoS)==True:
		print("pre_condition_647 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_648(delta=delta,skoS=skoS)==True:
		print("pre_condition_648 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_649(delta=delta,skoS=skoS)==True:
		print("pre_condition_649 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_650(delta=delta,skoS=skoS)==True:
		print("pre_condition_650 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_651(delta=delta,skoS=skoS)==True:
		print("pre_condition_651 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_652(delta=delta,skoS=skoS)==True:
		print("pre_condition_652 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_653(delta=delta,skoS=skoS)==True:
		print("pre_condition_653 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_654(delta=delta,skoS=skoS)==True:
		print("pre_condition_654 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_655(delta=delta,skoS=skoS)==True:
		print("pre_condition_655 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_656(delta=delta,skoS=skoS)==True:
		print("pre_condition_656 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_657(delta=delta,skoS=skoS)==True:
		print("pre_condition_657 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_658(delta=delta,skoS=skoS)==True:
		print("pre_condition_658 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_659(delta=delta,skoS=skoS)==True:
		print("pre_condition_659 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_660(delta=delta,skoS=skoS)==True:
		print("pre_condition_660 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_661(delta=delta,skoS=skoS)==True:
		print("pre_condition_661 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_662(delta=delta,skoS=skoS)==True:
		print("pre_condition_662 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_663(delta=delta,skoS=skoS)==True:
		print("pre_condition_663 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_664(delta=delta,skoS=skoS)==True:
		print("pre_condition_664 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_665(delta=delta,skoS=skoS)==True:
		print("pre_condition_665 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_666(delta=delta,skoS=skoS)==True:
		print("pre_condition_666 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_667(delta=delta,skoS=skoS)==True:
		print("pre_condition_667 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_668(delta=delta,skoS=skoS)==True:
		print("pre_condition_668 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_669(delta=delta,skoS=skoS)==True:
		print("pre_condition_669 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_670(delta=delta,skoS=skoS)==True:
		print("pre_condition_670 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_671(delta=delta,skoS=skoS)==True:
		print("pre_condition_671 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_672(delta=delta,skoS=skoS)==True:
		print("pre_condition_672 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_673(delta=delta,skoS=skoS)==True:
		print("pre_condition_673 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_674(delta=delta,skoS=skoS)==True:
		print("pre_condition_674 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_675(delta=delta,skoS=skoS)==True:
		print("pre_condition_675 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_676(delta=delta,skoS=skoS)==True:
		print("pre_condition_676 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_677(delta=delta,skoS=skoS)==True:
		print("pre_condition_677 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_678(delta=delta,skoS=skoS)==True:
		print("pre_condition_678 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_679(delta=delta,skoS=skoS)==True:
		print("pre_condition_679 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_680(delta=delta,skoS=skoS)==True:
		print("pre_condition_680 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_681(delta=delta,skoS=skoS)==True:
		print("pre_condition_681 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_682(delta=delta,skoS=skoS)==True:
		print("pre_condition_682 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_683(delta=delta,skoS=skoS)==True:
		print("pre_condition_683 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_684(delta=delta,skoS=skoS)==True:
		print("pre_condition_684 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_685(delta=delta,skoS=skoS)==True:
		print("pre_condition_685 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_686(delta=delta,skoS=skoS)==True:
		print("pre_condition_686 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_687(delta=delta,skoS=skoS)==True:
		print("pre_condition_687 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_688(delta=delta,skoS=skoS)==True:
		print("pre_condition_688 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_689(delta=delta,skoS=skoS)==True:
		print("pre_condition_689 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_690(delta=delta,skoS=skoS)==True:
		print("pre_condition_690 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_691(delta=delta,skoS=skoS)==True:
		print("pre_condition_691 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_692(delta=delta,skoS=skoS)==True:
		print("pre_condition_692 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_693(delta=delta,skoS=skoS)==True:
		print("pre_condition_693 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_694(delta=delta,skoS=skoS)==True:
		print("pre_condition_694 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_695(delta=delta,skoS=skoS)==True:
		print("pre_condition_695 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_696(delta=delta,skoS=skoS)==True:
		print("pre_condition_696 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_697(delta=delta,skoS=skoS)==True:
		print("pre_condition_697 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_698(delta=delta,skoS=skoS)==True:
		print("pre_condition_698 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_699(delta=delta,skoS=skoS)==True:
		print("pre_condition_699 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_700(delta=delta,skoS=skoS)==True:
		print("pre_condition_700 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_701(delta=delta,skoS=skoS)==True:
		print("pre_condition_701 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_702(delta=delta,skoS=skoS)==True:
		print("pre_condition_702 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_703(delta=delta,skoS=skoS)==True:
		print("pre_condition_703 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_704(delta=delta,skoS=skoS)==True:
		print("pre_condition_704 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_705(delta=delta,skoS=skoS)==True:
		print("pre_condition_705 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_706(delta=delta,skoS=skoS)==True:
		print("pre_condition_706 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_707(delta=delta,skoS=skoS)==True:
		print("pre_condition_707 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_708(delta=delta,skoS=skoS)==True:
		print("pre_condition_708 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_709(delta=delta,skoS=skoS)==True:
		print("pre_condition_709 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_710(delta=delta,skoS=skoS)==True:
		print("pre_condition_710 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_711(delta=delta,skoS=skoS)==True:
		print("pre_condition_711 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_712(delta=delta,skoS=skoS)==True:
		print("pre_condition_712 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_713(delta=delta,skoS=skoS)==True:
		print("pre_condition_713 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_714(delta=delta,skoS=skoS)==True:
		print("pre_condition_714 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_715(delta=delta,skoS=skoS)==True:
		print("pre_condition_715 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_716(delta=delta,skoS=skoS)==True:
		print("pre_condition_716 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_717(delta=delta,skoS=skoS)==True:
		print("pre_condition_717 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_718(delta=delta,skoS=skoS)==True:
		print("pre_condition_718 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_719(delta=delta,skoS=skoS)==True:
		print("pre_condition_719 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_720(delta=delta,skoS=skoS)==True:
		print("pre_condition_720 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_721(delta=delta,skoS=skoS)==True:
		print("pre_condition_721 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_722(delta=delta,skoS=skoS)==True:
		print("pre_condition_722 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_723(delta=delta,skoS=skoS)==True:
		print("pre_condition_723 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_724(delta=delta,skoS=skoS)==True:
		print("pre_condition_724 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_725(delta=delta,skoS=skoS)==True:
		print("pre_condition_725 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_726(delta=delta,skoS=skoS)==True:
		print("pre_condition_726 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_727(delta=delta,skoS=skoS)==True:
		print("pre_condition_727 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_728(delta=delta,skoS=skoS)==True:
		print("pre_condition_728 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_729(delta=delta,skoS=skoS)==True:
		print("pre_condition_729 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_730(delta=delta,skoS=skoS)==True:
		print("pre_condition_730 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_731(delta=delta,skoS=skoS)==True:
		print("pre_condition_731 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_732(delta=delta,skoS=skoS)==True:
		print("pre_condition_732 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_733(delta=delta,skoS=skoS)==True:
		print("pre_condition_733 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_734(delta=delta,skoS=skoS)==True:
		print("pre_condition_734 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_735(delta=delta,skoS=skoS)==True:
		print("pre_condition_735 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_736(delta=delta,skoS=skoS)==True:
		print("pre_condition_736 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_737(delta=delta,skoS=skoS)==True:
		print("pre_condition_737 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_738(delta=delta,skoS=skoS)==True:
		print("pre_condition_738 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_739(delta=delta,skoS=skoS)==True:
		print("pre_condition_739 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_740(delta=delta,skoS=skoS)==True:
		print("pre_condition_740 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_741(delta=delta,skoS=skoS)==True:
		print("pre_condition_741 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_742(delta=delta,skoS=skoS)==True:
		print("pre_condition_742 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_743(delta=delta,skoS=skoS)==True:
		print("pre_condition_743 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_744(delta=delta,skoS=skoS)==True:
		print("pre_condition_744 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_745(delta=delta,skoS=skoS)==True:
		print("pre_condition_745 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_746(delta=delta,skoS=skoS)==True:
		print("pre_condition_746 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_747(delta=delta,skoS=skoS)==True:
		print("pre_condition_747 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_748(delta=delta,skoS=skoS)==True:
		print("pre_condition_748 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_749(delta=delta,skoS=skoS)==True:
		print("pre_condition_749 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_750(delta=delta,skoS=skoS)==True:
		print("pre_condition_750 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_751(delta=delta,skoS=skoS)==True:
		print("pre_condition_751 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_752(delta=delta,skoS=skoS)==True:
		print("pre_condition_752 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_753(delta=delta,skoS=skoS)==True:
		print("pre_condition_753 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_754(delta=delta,skoS=skoS)==True:
		print("pre_condition_754 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_755(delta=delta,skoS=skoS)==True:
		print("pre_condition_755 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_756(delta=delta,skoS=skoS)==True:
		print("pre_condition_756 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_757(delta=delta,skoS=skoS)==True:
		print("pre_condition_757 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_758(delta=delta,skoS=skoS)==True:
		print("pre_condition_758 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_759(delta=delta,skoS=skoS)==True:
		print("pre_condition_759 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_760(delta=delta,skoS=skoS)==True:
		print("pre_condition_760 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_761(delta=delta,skoS=skoS)==True:
		print("pre_condition_761 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_762(delta=delta,skoS=skoS)==True:
		print("pre_condition_762 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_763(delta=delta,skoS=skoS)==True:
		print("pre_condition_763 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_764(delta=delta,skoS=skoS)==True:
		print("pre_condition_764 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_765(delta=delta,skoS=skoS)==True:
		print("pre_condition_765 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_766(delta=delta,skoS=skoS)==True:
		print("pre_condition_766 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_767(delta=delta,skoS=skoS)==True:
		print("pre_condition_767 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_768(delta=delta,skoS=skoS)==True:
		print("pre_condition_768 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_769(delta=delta,skoS=skoS)==True:
		print("pre_condition_769 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_770(delta=delta,skoS=skoS)==True:
		print("pre_condition_770 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_771(delta=delta,skoS=skoS)==True:
		print("pre_condition_771 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_772(delta=delta,skoS=skoS)==True:
		print("pre_condition_772 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_773(delta=delta,skoS=skoS)==True:
		print("pre_condition_773 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_774(delta=delta,skoS=skoS)==True:
		print("pre_condition_774 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_775(delta=delta,skoS=skoS)==True:
		print("pre_condition_775 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_776(delta=delta,skoS=skoS)==True:
		print("pre_condition_776 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_777(delta=delta,skoS=skoS)==True:
		print("pre_condition_777 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_778(delta=delta,skoS=skoS)==True:
		print("pre_condition_778 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_779(delta=delta,skoS=skoS)==True:
		print("pre_condition_779 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_780(delta=delta,skoS=skoS)==True:
		print("pre_condition_780 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_781(delta=delta,skoS=skoS)==True:
		print("pre_condition_781 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_782(delta=delta,skoS=skoS)==True:
		print("pre_condition_782 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_783(delta=delta,skoS=skoS)==True:
		print("pre_condition_783 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_784(delta=delta,skoS=skoS)==True:
		print("pre_condition_784 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_785(delta=delta,skoS=skoS)==True:
		print("pre_condition_785 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_786(delta=delta,skoS=skoS)==True:
		print("pre_condition_786 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_787(delta=delta,skoS=skoS)==True:
		print("pre_condition_787 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_788(delta=delta,skoS=skoS)==True:
		print("pre_condition_788 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_789(delta=delta,skoS=skoS)==True:
		print("pre_condition_789 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_790(delta=delta,skoS=skoS)==True:
		print("pre_condition_790 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_791(delta=delta,skoS=skoS)==True:
		print("pre_condition_791 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_792(delta=delta,skoS=skoS)==True:
		print("pre_condition_792 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_793(delta=delta,skoS=skoS)==True:
		print("pre_condition_793 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_794(delta=delta,skoS=skoS)==True:
		print("pre_condition_794 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_795(delta=delta,skoS=skoS)==True:
		print("pre_condition_795 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_796(delta=delta,skoS=skoS)==True:
		print("pre_condition_796 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_797(delta=delta,skoS=skoS)==True:
		print("pre_condition_797 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_798(delta=delta,skoS=skoS)==True:
		print("pre_condition_798 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_799(delta=delta,skoS=skoS)==True:
		print("pre_condition_799 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_800(delta=delta,skoS=skoS)==True:
		print("pre_condition_800 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_801(delta=delta,skoS=skoS)==True:
		print("pre_condition_801 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_802(delta=delta,skoS=skoS)==True:
		print("pre_condition_802 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_803(delta=delta,skoS=skoS)==True:
		print("pre_condition_803 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_804(delta=delta,skoS=skoS)==True:
		print("pre_condition_804 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_805(delta=delta,skoS=skoS)==True:
		print("pre_condition_805 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_806(delta=delta,skoS=skoS)==True:
		print("pre_condition_806 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_807(delta=delta,skoS=skoS)==True:
		print("pre_condition_807 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_808(delta=delta,skoS=skoS)==True:
		print("pre_condition_808 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_809(delta=delta,skoS=skoS)==True:
		print("pre_condition_809 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_810(delta=delta,skoS=skoS)==True:
		print("pre_condition_810 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_811(delta=delta,skoS=skoS)==True:
		print("pre_condition_811 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_812(delta=delta,skoS=skoS)==True:
		print("pre_condition_812 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_813(delta=delta,skoS=skoS)==True:
		print("pre_condition_813 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_814(delta=delta,skoS=skoS)==True:
		print("pre_condition_814 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_815(delta=delta,skoS=skoS)==True:
		print("pre_condition_815 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_816(delta=delta,skoS=skoS)==True:
		print("pre_condition_816 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_817(delta=delta,skoS=skoS)==True:
		print("pre_condition_817 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_818(delta=delta,skoS=skoS)==True:
		print("pre_condition_818 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_819(delta=delta,skoS=skoS)==True:
		print("pre_condition_819 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_820(delta=delta,skoS=skoS)==True:
		print("pre_condition_820 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_821(delta=delta,skoS=skoS)==True:
		print("pre_condition_821 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_822(delta=delta,skoS=skoS)==True:
		print("pre_condition_822 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_823(delta=delta,skoS=skoS)==True:
		print("pre_condition_823 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_824(delta=delta,skoS=skoS)==True:
		print("pre_condition_824 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_825(delta=delta,skoS=skoS)==True:
		print("pre_condition_825 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_826(delta=delta,skoS=skoS)==True:
		print("pre_condition_826 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_827(delta=delta,skoS=skoS)==True:
		print("pre_condition_827 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_828(delta=delta,skoS=skoS)==True:
		print("pre_condition_828 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_829(delta=delta,skoS=skoS)==True:
		print("pre_condition_829 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_830(delta=delta,skoS=skoS)==True:
		print("pre_condition_830 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_831(delta=delta,skoS=skoS)==True:
		print("pre_condition_831 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_832(delta=delta,skoS=skoS)==True:
		print("pre_condition_832 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_833(delta=delta,skoS=skoS)==True:
		print("pre_condition_833 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_834(delta=delta,skoS=skoS)==True:
		print("pre_condition_834 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_835(delta=delta,skoS=skoS)==True:
		print("pre_condition_835 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_836(delta=delta,skoS=skoS)==True:
		print("pre_condition_836 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_837(delta=delta,skoS=skoS)==True:
		print("pre_condition_837 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_838(delta=delta,skoS=skoS)==True:
		print("pre_condition_838 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_839(delta=delta,skoS=skoS)==True:
		print("pre_condition_839 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_840(delta=delta,skoS=skoS)==True:
		print("pre_condition_840 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_841(delta=delta,skoS=skoS)==True:
		print("pre_condition_841 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_842(delta=delta,skoS=skoS)==True:
		print("pre_condition_842 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_843(delta=delta,skoS=skoS)==True:
		print("pre_condition_843 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_844(delta=delta,skoS=skoS)==True:
		print("pre_condition_844 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_845(delta=delta,skoS=skoS)==True:
		print("pre_condition_845 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_846(delta=delta,skoS=skoS)==True:
		print("pre_condition_846 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_847(delta=delta,skoS=skoS)==True:
		print("pre_condition_847 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_848(delta=delta,skoS=skoS)==True:
		print("pre_condition_848 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_849(delta=delta,skoS=skoS)==True:
		print("pre_condition_849 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_850(delta=delta,skoS=skoS)==True:
		print("pre_condition_850 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_851(delta=delta,skoS=skoS)==True:
		print("pre_condition_851 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_852(delta=delta,skoS=skoS)==True:
		print("pre_condition_852 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_853(delta=delta,skoS=skoS)==True:
		print("pre_condition_853 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_854(delta=delta,skoS=skoS)==True:
		print("pre_condition_854 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_855(delta=delta,skoS=skoS)==True:
		print("pre_condition_855 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_856(delta=delta,skoS=skoS)==True:
		print("pre_condition_856 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_857(delta=delta,skoS=skoS)==True:
		print("pre_condition_857 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_858(delta=delta,skoS=skoS)==True:
		print("pre_condition_858 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_859(delta=delta,skoS=skoS)==True:
		print("pre_condition_859 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_860(delta=delta,skoS=skoS)==True:
		print("pre_condition_860 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_861(delta=delta,skoS=skoS)==True:
		print("pre_condition_861 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_862(delta=delta,skoS=skoS)==True:
		print("pre_condition_862 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_863(delta=delta,skoS=skoS)==True:
		print("pre_condition_863 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_864(delta=delta,skoS=skoS)==True:
		print("pre_condition_864 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_865(delta=delta,skoS=skoS)==True:
		print("pre_condition_865 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_866(delta=delta,skoS=skoS)==True:
		print("pre_condition_866 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_867(delta=delta,skoS=skoS)==True:
		print("pre_condition_867 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_868(delta=delta,skoS=skoS)==True:
		print("pre_condition_868 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_869(delta=delta,skoS=skoS)==True:
		print("pre_condition_869 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_870(delta=delta,skoS=skoS)==True:
		print("pre_condition_870 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_871(delta=delta,skoS=skoS)==True:
		print("pre_condition_871 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_872(delta=delta,skoS=skoS)==True:
		print("pre_condition_872 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_873(delta=delta,skoS=skoS)==True:
		print("pre_condition_873 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_874(delta=delta,skoS=skoS)==True:
		print("pre_condition_874 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_875(delta=delta,skoS=skoS)==True:
		print("pre_condition_875 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_876(delta=delta,skoS=skoS)==True:
		print("pre_condition_876 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_877(delta=delta,skoS=skoS)==True:
		print("pre_condition_877 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_878(delta=delta,skoS=skoS)==True:
		print("pre_condition_878 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_879(delta=delta,skoS=skoS)==True:
		print("pre_condition_879 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_880(delta=delta,skoS=skoS)==True:
		print("pre_condition_880 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_881(delta=delta,skoS=skoS)==True:
		print("pre_condition_881 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_882(delta=delta,skoS=skoS)==True:
		print("pre_condition_882 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_883(delta=delta,skoS=skoS)==True:
		print("pre_condition_883 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_884(delta=delta,skoS=skoS)==True:
		print("pre_condition_884 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_885(delta=delta,skoS=skoS)==True:
		print("pre_condition_885 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_886(delta=delta,skoS=skoS)==True:
		print("pre_condition_886 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_887(delta=delta,skoS=skoS)==True:
		print("pre_condition_887 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_888(delta=delta,skoS=skoS)==True:
		print("pre_condition_888 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_889(delta=delta,skoS=skoS)==True:
		print("pre_condition_889 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_890(delta=delta,skoS=skoS)==True:
		print("pre_condition_890 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_891(delta=delta,skoS=skoS)==True:
		print("pre_condition_891 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_892(delta=delta,skoS=skoS)==True:
		print("pre_condition_892 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_893(delta=delta,skoS=skoS)==True:
		print("pre_condition_893 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_894(delta=delta,skoS=skoS)==True:
		print("pre_condition_894 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_895(delta=delta,skoS=skoS)==True:
		print("pre_condition_895 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)
	
	
	if pre_condition_896(delta=delta,skoS=skoS)==True:
		print("pre_condition_896 SAT")
		print('delta = 35888059530608641/590295810358705651712')
		print('skoS = 217/100')
		print('skoCOSS = 255/2048')
		print('skoSINS = -127/128')
		exit(0)


	print("UNKNOWN")
	exit(0)
