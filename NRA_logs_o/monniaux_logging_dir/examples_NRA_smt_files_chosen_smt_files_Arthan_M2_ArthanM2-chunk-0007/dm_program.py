import sympy
from sympy import *

def pre_condition_0(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & ((delta < skoSINS**2 - 63/64) | (delta < 63/64 - skoSINS**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-63, 64))), StrictLessThan(Symbol('delta'), Add(Rational(63, 64), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2)))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & ((delta < skoSINS**2 - 63/64) | (delta < 63/64 - skoSINS**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-63, 64))), StrictLessThan(Symbol('delta'), Add(Rational(63, 64), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2)))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & ((delta < skoSINS**2 - 1) | (delta < 1 - skoSINS**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Integer(1), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2)))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & ((delta < skoSINS**2 - 1) | (delta < 1 - skoSINS**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Integer(1), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2)))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_4(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & ((delta < skoSINS**2) | (delta < -skoSINS**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoSINS'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_5(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & ((delta < skoSINS**2) | (delta < -skoSINS**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoSINS'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_6(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & ((delta < skoSINS**2 + 3) | (delta < -skoSINS**2 - 3))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(3))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-3)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_7(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & ((delta < skoSINS**2 + 3) | (delta < -skoSINS**2 - 3))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(3))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-3)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_8(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & ((delta < skoSINS**2 + 8) | (delta < -skoSINS**2 - 8))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(8))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-8)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_9(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & ((delta < skoSINS**2 + 8) | (delta < -skoSINS**2 - 8))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(8))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-8)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_10(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & ((delta < skoSINS**2 + 15) | (delta < -skoSINS**2 - 15))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(15))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-15)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_11(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & ((delta < skoSINS**2 + 15) | (delta < -skoSINS**2 - 15))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(15))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-15)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_12(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & ((delta < skoSINS**2 + 24) | (delta < -skoSINS**2 - 24))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(24))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-24)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_13(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & ((delta < skoSINS**2 + 24) | (delta < -skoSINS**2 - 24))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(24))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-24)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_14(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & ((delta < skoSINS**2 + 35) | (delta < -skoSINS**2 - 35))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(35))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-35)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_15(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & ((delta < skoSINS**2 + 35) | (delta < -skoSINS**2 - 35))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(35))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-35)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_16(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & ((delta < skoSINS**2 + 48) | (delta < -skoSINS**2 - 48))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(48))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-48)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_17(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & ((delta < skoSINS**2 + 48) | (delta < -skoSINS**2 - 48))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(48))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-48)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_18(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & ((delta < skoSINS**2 + 63) | (delta < -skoSINS**2 - 63))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(63))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-63)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_19(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & ((delta < skoSINS**2 + 63) | (delta < -skoSINS**2 - 63))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(63))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-63)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_20(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & ((delta < skoSINS**2 + 80) | (delta < -skoSINS**2 - 80))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(80))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-80)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_21(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & ((delta < skoSINS**2 + 80) | (delta < -skoSINS**2 - 80))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(80))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-80)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_22(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & ((delta < skoSINS**2 + 99) | (delta < -skoSINS**2 - 99))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(99))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-99)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_23(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & ((delta < skoSINS**2 + 99) | (delta < -skoSINS**2 - 99))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(99))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-99)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_24(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & ((delta < skoSINS**2 + 120) | (delta < -skoSINS**2 - 120))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(120))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-120)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_25(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & ((delta < skoSINS**2 + 120) | (delta < -skoSINS**2 - 120))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(120))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-120)))))