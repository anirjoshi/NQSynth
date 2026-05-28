import sympy
from sympy import *

def pre_condition_0(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 63/64) & (delta >= 63/64 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-63, 64))), GreaterThan(Symbol('delta'), Add(Rational(63, 64), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 63/64) & (delta >= 63/64 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-63, 64))), GreaterThan(Symbol('delta'), Add(Rational(63, 64), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 127/4096) & (delta >= 127/4096 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-127, 4096))), GreaterThan(Symbol('delta'), Add(Rational(127, 4096), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 127/4096) & (delta >= 127/4096 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-127, 4096))), GreaterThan(Symbol('delta'), Add(Rational(127, 4096), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_4(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 3/4) & (delta >= 3/4 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-3, 4))), GreaterThan(Symbol('delta'), Add(Rational(3, 4), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_5(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 3/4) & (delta >= 3/4 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-3, 4))), GreaterThan(Symbol('delta'), Add(Rational(3, 4), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_6(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 15/16) & (delta >= 15/16 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-15, 16))), GreaterThan(Symbol('delta'), Add(Rational(15, 16), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_7(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 15/16) & (delta >= 15/16 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-15, 16))), GreaterThan(Symbol('delta'), Add(Rational(15, 16), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_8(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 61567/65536) & (delta >= 61567/65536 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-61567, 65536))), GreaterThan(Symbol('delta'), Add(Rational(61567, 65536), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_9(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 61567/65536) & (delta >= 61567/65536 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-61567, 65536))), GreaterThan(Symbol('delta'), Add(Rational(61567, 65536), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_10(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 247/256) & (delta >= 247/256 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-247, 256))), GreaterThan(Symbol('delta'), Add(Rational(247, 256), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_11(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 247/256) & (delta >= 247/256 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-247, 256))), GreaterThan(Symbol('delta'), Add(Rational(247, 256), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_12(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 999/1024) & (delta >= 999/1024 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-999, 1024))), GreaterThan(Symbol('delta'), Add(Rational(999, 1024), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_13(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 999/1024) & (delta >= 999/1024 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-999, 1024))), GreaterThan(Symbol('delta'), Add(Rational(999, 1024), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_14(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 64015/65536) & (delta >= 64015/65536 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-64015, 65536))), GreaterThan(Symbol('delta'), Add(Rational(64015, 65536), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_15(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 64015/65536) & (delta >= 64015/65536 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-64015, 65536))), GreaterThan(Symbol('delta'), Add(Rational(64015, 65536), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_16(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4015/4096) & (delta >= 4015/4096 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4015, 4096))), GreaterThan(Symbol('delta'), Add(Rational(4015, 4096), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_17(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4015/4096) & (delta >= 4015/4096 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4015, 4096))), GreaterThan(Symbol('delta'), Add(Rational(4015, 4096), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_18(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_19(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_20(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_21(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_22(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_23(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_24(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_25(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_26(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_27(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_28(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_29(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_30(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_31(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_32(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_33(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_34(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_35(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_36(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_37(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_38(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_39(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_40(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_41(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_42(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_43(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_44(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_45(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_46(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_47(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_48(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_49(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_50(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_51(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_52(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_53(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_54(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_55(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_56(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_57(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_58(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_59(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_60(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_61(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_62(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_63(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_64(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_65(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_66(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_67(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_68(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_69(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_70(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_71(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_72(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_73(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_74(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_75(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_76(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_77(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_78(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_79(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_80(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_81(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_82(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_83(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_84(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_85(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_86(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_87(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_88(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_89(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_90(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_91(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_92(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_93(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_94(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_95(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_96(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_97(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_98(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_99(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_100(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_101(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_102(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_103(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_104(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_105(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_106(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_107(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_108(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_109(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_110(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_111(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_112(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_113(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_114(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_115(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_116(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_117(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_118(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_119(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_120(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_121(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_122(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_123(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_124(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_125(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_126(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_127(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_128(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_129(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_130(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_131(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_132(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_133(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_134(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_135(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_136(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_137(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_138(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_139(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_140(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_141(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_142(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_143(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_144(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_145(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_146(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_147(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_148(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_149(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_150(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_151(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_152(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_153(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_154(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_155(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_156(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_157(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_158(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_159(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_160(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_161(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_162(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_163(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_164(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_165(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_166(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_167(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_168(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_169(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_170(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_171(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_172(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_173(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_174(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_175(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_176(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_177(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_178(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_179(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_180(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_181(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_182(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_183(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_184(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_185(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_186(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_187(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_188(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_189(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_190(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_191(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_192(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_193(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_194(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_195(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_196(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_197(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_198(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_199(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_200(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_201(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_202(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (delta >= skoSINS**2 - 4096335/4194304) & (delta >= 4096335/4194304 - skoSINS**2) & ((delta < skoM) | (delta < -skoM)) & ((delta < skoM**2) | (delta < -skoM**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4096335, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4096335, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoM')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM')))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoM'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(delta:sympy.Rational, skoSINS:sympy.Rational, skoM:sympy.Rational, skoCOSS:sympy.Rational, skoS:sympy.Rational):
	# (0 <= delta) & (2 <= skoM) & (2 <= skoS) & (skoCOSS**2 + skoSINS**2 - 1 <= delta) & ~((skoM <= delta) & (-skoM <= delta)) & (-skoCOSS**2 - skoSINS**2 + 1 <= delta) & ~((skoM**2 <= delta) & (-skoM**2 <= delta))

	post_cond =  And(LessThan(Integer(0), Symbol('delta')), LessThan(Integer(2), Symbol('skoM')), LessThan(Integer(2), Symbol('skoS')), LessThan(Add(Pow(Symbol('skoCOSS'), Integer(2)), Pow(Symbol('skoSINS'), Integer(2)), Integer(-1)), Symbol('delta')), Not(And(LessThan(Symbol('skoM'), Symbol('delta')), LessThan(Mul(Integer(-1), Symbol('skoM')), Symbol('delta')))), LessThan(Add(Mul(Integer(-1), Pow(Symbol('skoCOSS'), Integer(2))), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(1)), Symbol('delta')), Not(And(LessThan(Pow(Symbol('skoM'), Integer(2)), Symbol('delta')), LessThan(Mul(Integer(-1), Pow(Symbol('skoM'), Integer(2))), Symbol('delta')))))

	eval = post_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM, 'skoCOSS':skoCOSS, 'skoS':skoS })

	return eval == sympy.logic.boolalg.BooleanTrue





if __name__=="__main__":
	
	ip_0=int(input("enter integer numerator of delta:\n"))
	ip_1=int(input("enter integer denominator of delta:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	delta=sympy.Rational(ip_0,ip_1)
	
	
	ip_0=int(input("enter integer numerator of skoSINS:\n"))
	ip_1=int(input("enter integer denominator of skoSINS:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	skoSINS=sympy.Rational(ip_0,ip_1)
	
	
	ip_0=int(input("enter integer numerator of skoM:\n"))
	ip_1=int(input("enter integer denominator of skoM:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	skoM=sympy.Rational(ip_0,ip_1)
	
	
	
	
	if pre_condition_0(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_0 SAT")
		print('delta = 1')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = 1/8')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_1(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_1 SAT")
		print('delta = 1')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = 1/8')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_2(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_2 SAT")
		print('delta = 127/4096')
		print('skoM = 4')
		print('skoS = 2')
		print('skoCOSS = 63/64')
		print('skoSINS = 0')
		exit(0)
	
	
	if pre_condition_3(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_3 SAT")
		print('delta = 127/4096')
		print('skoM = 4')
		print('skoS = 2')
		print('skoCOSS = 63/64')
		print('skoSINS = 0')
		exit(0)
	
	
	if pre_condition_4(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_4 SAT")
		print('delta = 1/4')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -1/2')
		print('skoSINS = -3/4')
		exit(0)
	
	
	if pre_condition_5(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_5 SAT")
		print('delta = 1/4')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -1/2')
		print('skoSINS = -3/4')
		exit(0)
	
	
	if pre_condition_6(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_6 SAT")
		print('delta = 1/16')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -1/4')
		print('skoSINS = 15/16')
		exit(0)
	
	
	if pre_condition_7(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_7 SAT")
		print('delta = 1/16')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -1/4')
		print('skoSINS = 15/16')
		exit(0)
	
	
	if pre_condition_8(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_8 SAT")
		print('delta = 127/131072')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -63/256')
		print('skoSINS = 31/32')
		exit(0)
	
	
	if pre_condition_9(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_9 SAT")
		print('delta = 127/131072')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -63/256')
		print('skoSINS = 31/32')
		exit(0)
	
	
	if pre_condition_10(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_10 SAT")
		print('delta = 1/128')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -3/16')
		print('skoSINS = 63/64')
		exit(0)
	
	
	if pre_condition_11(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_11 SAT")
		print('delta = 1/128')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -3/16')
		print('skoSINS = 63/64')
		exit(0)
	
	
	if pre_condition_12(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_12 SAT")
		print('delta = 1/256')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -5/32')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_13(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_13 SAT")
		print('delta = 1/256')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -5/32')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_14(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_14 SAT")
		print('delta = 1/1024')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -39/256')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_15(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_15 SAT")
		print('delta = 1/1024')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -39/256')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_16(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_16 SAT")
		print('delta = 1/512')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -9/64')
		print('skoSINS = 507/512')
		exit(0)
	
	
	if pre_condition_17(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_17 SAT")
		print('delta = 1/512')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -9/64')
		print('skoSINS = 507/512')
		exit(0)
	
	
	if pre_condition_18(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_18 SAT")
		print('delta = 1/16384')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_19(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_19 SAT")
		print('delta = 1/16384')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_20(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_20 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_21(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_21 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_22(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_22 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_23(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_23 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_24(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_24 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_25(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_25 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_26(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_26 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_27(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_27 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_28(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_28 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_29(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_29 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_30(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_30 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_31(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_31 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_32(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_32 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_33(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_33 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_34(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_34 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_35(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_35 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_36(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_36 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_37(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_37 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_38(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_38 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_39(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_39 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_40(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_40 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_41(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_41 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_42(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_42 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_43(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_43 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_44(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_44 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_45(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_45 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_46(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_46 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_47(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_47 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_48(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_48 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_49(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_49 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_50(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_50 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_51(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_51 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_52(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_52 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_53(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_53 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_54(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_54 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_55(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_55 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_56(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_56 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_57(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_57 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_58(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_58 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_59(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_59 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_60(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_60 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_61(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_61 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_62(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_62 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_63(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_63 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_64(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_64 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_65(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_65 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_66(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_66 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_67(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_67 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_68(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_68 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_69(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_69 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_70(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_70 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_71(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_71 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_72(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_72 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_73(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_73 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_74(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_74 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_75(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_75 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_76(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_76 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_77(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_77 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_78(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_78 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_79(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_79 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_80(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_80 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_81(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_81 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_82(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_82 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_83(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_83 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_84(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_84 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_85(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_85 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_86(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_86 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_87(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_87 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_88(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_88 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_89(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_89 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_90(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_90 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_91(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_91 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_92(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_92 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_93(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_93 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_94(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_94 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_95(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_95 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_96(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_96 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_97(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_97 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_98(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_98 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_99(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_99 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_100(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_100 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_101(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_101 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_102(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_102 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_103(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_103 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_104(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_104 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_105(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_105 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_106(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_106 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_107(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_107 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_108(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_108 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_109(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_109 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_110(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_110 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_111(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_111 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_112(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_112 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_113(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_113 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_114(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_114 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_115(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_115 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_116(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_116 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_117(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_117 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_118(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_118 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_119(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_119 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_120(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_120 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_121(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_121 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_122(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_122 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_123(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_123 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_124(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_124 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_125(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_125 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_126(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_126 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_127(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_127 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_128(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_128 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_129(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_129 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_130(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_130 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_131(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_131 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_132(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_132 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_133(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_133 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_134(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_134 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_135(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_135 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_136(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_136 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_137(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_137 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_138(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_138 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_139(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_139 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_140(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_140 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_141(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_141 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_142(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_142 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_143(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_143 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_144(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_144 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_145(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_145 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_146(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_146 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_147(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_147 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_148(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_148 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_149(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_149 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_150(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_150 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_151(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_151 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_152(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_152 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_153(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_153 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_154(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_154 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_155(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_155 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_156(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_156 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_157(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_157 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_158(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_158 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_159(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_159 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_160(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_160 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_161(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_161 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_162(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_162 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_163(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_163 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_164(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_164 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_165(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_165 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_166(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_166 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_167(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_167 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_168(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_168 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_169(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_169 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_170(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_170 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_171(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_171 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_172(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_172 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_173(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_173 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_174(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_174 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_175(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_175 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_176(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_176 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_177(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_177 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_178(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_178 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_179(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_179 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_180(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_180 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_181(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_181 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_182(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_182 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_183(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_183 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_184(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_184 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_185(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_185 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_186(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_186 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_187(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_187 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_188(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_188 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_189(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_189 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_190(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_190 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_191(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_191 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_192(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_192 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_193(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_193 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_194(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_194 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_195(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_195 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_196(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_196 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_197(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_197 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_198(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_198 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_199(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_199 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_200(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_200 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_201(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_201 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)
	
	
	if pre_condition_202(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_202 SAT")
		print('delta = 4140348473345/72057594037927936')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = -313/2048')
		print('skoSINS = 253/256')
		exit(0)


	print("UNKNOWN")
	exit(0)
