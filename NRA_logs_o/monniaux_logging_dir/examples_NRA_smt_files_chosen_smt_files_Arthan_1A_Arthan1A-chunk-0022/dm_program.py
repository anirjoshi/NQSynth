import sympy
from sympy import *

def pre_condition_0(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2) | (delta < -skoSINS**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoSINS'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 1/8) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -1/64) | (delta < 1/64))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(1, 8)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-1, 64)), StrictLessThan(Symbol('delta'), Rational(1, 64))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 - 1) | (delta < 1 - skoSINS**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Integer(1), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2)))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -1) | (delta < 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Integer(-1)), StrictLessThan(Symbol('delta'), Integer(1))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_4(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 3) | (delta < -skoSINS**2 - 3))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(3))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-3)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_5(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 1/8) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -193/64) | (delta < 193/64))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(1, 8)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-193, 64)), StrictLessThan(Symbol('delta'), Rational(193, 64))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_6(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 8) | (delta < -skoSINS**2 - 8))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(8))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-8)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_7(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -33/4) | (delta < 33/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-33, 4)), StrictLessThan(Symbol('delta'), Rational(33, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_8(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 15) | (delta < -skoSINS**2 - 15))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(15))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-15)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_9(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -15) | (delta < 15))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Integer(-15)), StrictLessThan(Symbol('delta'), Integer(15))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_10(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 24) | (delta < -skoSINS**2 - 24))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(24))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-24)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_11(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 1/8) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -1537/64) | (delta < 1537/64))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(1, 8)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-1537, 64)), StrictLessThan(Symbol('delta'), Rational(1537, 64))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_12(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 35) | (delta < -skoSINS**2 - 35))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(35))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-35)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_13(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -36) | (delta < 36))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Integer(-36)), StrictLessThan(Symbol('delta'), Integer(36))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_14(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 48) | (delta < -skoSINS**2 - 48))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(48))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-48)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_15(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -49) | (delta < 49))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Integer(-49)), StrictLessThan(Symbol('delta'), Integer(49))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_16(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 63) | (delta < -skoSINS**2 - 63))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(63))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-63)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_17(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 1) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -64) | (delta < 64))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(1)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Integer(-64)), StrictLessThan(Symbol('delta'), Integer(64))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_18(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 80) | (delta < -skoSINS**2 - 80))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(80))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-80)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_19(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 1) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -81) | (delta < 81))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(1)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Integer(-81)), StrictLessThan(Symbol('delta'), Integer(81))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_20(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 99) | (delta < -skoSINS**2 - 99))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(99))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-99)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_21(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -99) | (delta < 99))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Integer(-99)), StrictLessThan(Symbol('delta'), Integer(99))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_22(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 120) | (delta < -skoSINS**2 - 120))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(120))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-120)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_23(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 1/8) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -7681/64) | (delta < 7681/64))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(1, 8)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-7681, 64)), StrictLessThan(Symbol('delta'), Rational(7681, 64))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_24(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 143) | (delta < -skoSINS**2 - 143))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(143))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-143)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_25(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -144) | (delta < 144))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Integer(-144)), StrictLessThan(Symbol('delta'), Integer(144))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_26(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 168) | (delta < -skoSINS**2 - 168))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(168))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-168)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_27(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 1) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -169) | (delta < 169))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(1)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Integer(-169)), StrictLessThan(Symbol('delta'), Integer(169))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_28(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 195) | (delta < -skoSINS**2 - 195))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(195))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-195)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_29(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -196) | (delta < 196))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Integer(-196)), StrictLessThan(Symbol('delta'), Integer(196))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_30(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 224) | (delta < -skoSINS**2 - 224))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(224))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-224)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_31(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 1) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -225) | (delta < 225))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(1)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Integer(-225)), StrictLessThan(Symbol('delta'), Integer(225))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_32(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 255) | (delta < -skoSINS**2 - 255))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(255))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-255)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_33(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -256) | (delta < 256))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Integer(-256)), StrictLessThan(Symbol('delta'), Integer(256))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_34(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 288) | (delta < -skoSINS**2 - 288))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(288))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-288)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_35(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -289) | (delta < 289))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Integer(-289)), StrictLessThan(Symbol('delta'), Integer(289))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_36(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 323) | (delta < -skoSINS**2 - 323))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(323))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-323)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_37(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -324) | (delta < 324))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Integer(-324)), StrictLessThan(Symbol('delta'), Integer(324))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_38(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 360) | (delta < -skoSINS**2 - 360))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(360))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-360)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_39(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -361) | (delta < 361))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Integer(-361)), StrictLessThan(Symbol('delta'), Integer(361))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_40(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 399) | (delta < -skoSINS**2 - 399))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(399))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-399)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_41(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -400) | (delta < 400))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Integer(-400)), StrictLessThan(Symbol('delta'), Integer(400))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_42(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 440) | (delta < -skoSINS**2 - 440))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(440))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-440)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_43(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -441) | (delta < 441))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Integer(-441)), StrictLessThan(Symbol('delta'), Integer(441))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_44(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 483) | (delta < -skoSINS**2 - 483))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(483))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-483)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_45(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -483) | (delta < 483))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Integer(-483)), StrictLessThan(Symbol('delta'), Integer(483))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_46(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 528) | (delta < -skoSINS**2 - 528))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(528))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-528)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_47(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 1/8) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -33793/64) | (delta < 33793/64))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(1, 8)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-33793, 64)), StrictLessThan(Symbol('delta'), Rational(33793, 64))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_48(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 575) | (delta < -skoSINS**2 - 575))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(575))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-575)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_49(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -576) | (delta < 576))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Integer(-576)), StrictLessThan(Symbol('delta'), Integer(576))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_50(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 624) | (delta < -skoSINS**2 - 624))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(624))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-624)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_51(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 1) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -625) | (delta < 625))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(1)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Integer(-625)), StrictLessThan(Symbol('delta'), Integer(625))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_52(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 675) | (delta < -skoSINS**2 - 675))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(675))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-675)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_53(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -676) | (delta < 676))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Integer(-676)), StrictLessThan(Symbol('delta'), Integer(676))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_54(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 728) | (delta < -skoSINS**2 - 728))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(728))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-728)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_55(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -729) | (delta < 729))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Integer(-729)), StrictLessThan(Symbol('delta'), Integer(729))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_56(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 783) | (delta < -skoSINS**2 - 783))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(783))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-783)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_57(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -783) | (delta < 783))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Integer(-783)), StrictLessThan(Symbol('delta'), Integer(783))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_58(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 840) | (delta < -skoSINS**2 - 840))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(840))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-840)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_59(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 1/8) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -53761/64) | (delta < 53761/64))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(1, 8)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-53761, 64)), StrictLessThan(Symbol('delta'), Rational(53761, 64))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_60(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 899) | (delta < -skoSINS**2 - 899))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(899))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-899)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_61(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 1) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -900) | (delta < 900))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(1)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Integer(-900)), StrictLessThan(Symbol('delta'), Integer(900))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_62(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 960) | (delta < -skoSINS**2 - 960))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(960))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-960)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_63(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -960) | (delta < 960))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Integer(-960)), StrictLessThan(Symbol('delta'), Integer(960))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_64(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 1023) | (delta < -skoSINS**2 - 1023))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(1023))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-1023)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_65(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 1/8) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -65473/64) | (delta < 65473/64))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(1, 8)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-65473, 64)), StrictLessThan(Symbol('delta'), Rational(65473, 64))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_66(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 1088) | (delta < -skoSINS**2 - 1088))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(1088))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-1088)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_67(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -1089) | (delta < 1089))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Integer(-1089)), StrictLessThan(Symbol('delta'), Integer(1089))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_68(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 1155) | (delta < -skoSINS**2 - 1155))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(1155))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-1155)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_69(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 1) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -1156) | (delta < 1156))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(1)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Integer(-1156)), StrictLessThan(Symbol('delta'), Integer(1156))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_70(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 1224) | (delta < -skoSINS**2 - 1224))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(1224))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-1224)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_71(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -1225) | (delta < 1225))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Integer(-1225)), StrictLessThan(Symbol('delta'), Integer(1225))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_72(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 1295) | (delta < -skoSINS**2 - 1295))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(1295))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-1295)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_73(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 1) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -1296) | (delta < 1296))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(1)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Integer(-1296)), StrictLessThan(Symbol('delta'), Integer(1296))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_74(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 1368) | (delta < -skoSINS**2 - 1368))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(1368))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-1368)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_75(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -1368) | (delta < 1368))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Integer(-1368)), StrictLessThan(Symbol('delta'), Integer(1368))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_76(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 1443) | (delta < -skoSINS**2 - 1443))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(1443))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-1443)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_77(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 1/8) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -92353/64) | (delta < 92353/64))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(1, 8)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-92353, 64)), StrictLessThan(Symbol('delta'), Rational(92353, 64))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_78(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 1520) | (delta < -skoSINS**2 - 1520))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(1520))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-1520)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_79(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -1521) | (delta < 1521))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Integer(-1521)), StrictLessThan(Symbol('delta'), Integer(1521))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_80(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 1599) | (delta < -skoSINS**2 - 1599))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(1599))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-1599)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_81(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -1600) | (delta < 1600))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Integer(-1600)), StrictLessThan(Symbol('delta'), Integer(1600))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_82(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 1680) | (delta < -skoSINS**2 - 1680))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(1680))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-1680)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_83(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -1681) | (delta < 1681))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Integer(-1681)), StrictLessThan(Symbol('delta'), Integer(1681))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_84(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 1763) | (delta < -skoSINS**2 - 1763))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(1763))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-1763)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_85(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -1763) | (delta < 1763))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Integer(-1763)), StrictLessThan(Symbol('delta'), Integer(1763))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_86(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 1848) | (delta < -skoSINS**2 - 1848))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(1848))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-1848)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_87(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 1/8) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -118273/64) | (delta < 118273/64))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(1, 8)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-118273, 64)), StrictLessThan(Symbol('delta'), Rational(118273, 64))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_88(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 1935) | (delta < -skoSINS**2 - 1935))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(1935))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-1935)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_89(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -1936) | (delta < 1936))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Integer(-1936)), StrictLessThan(Symbol('delta'), Integer(1936))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_90(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 2024) | (delta < -skoSINS**2 - 2024))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(2024))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-2024)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_91(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -2024) | (delta < 2024))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Integer(-2024)), StrictLessThan(Symbol('delta'), Integer(2024))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_92(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 2115) | (delta < -skoSINS**2 - 2115))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(2115))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-2115)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_93(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 1/8) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -135361/64) | (delta < 135361/64))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(1, 8)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-135361, 64)), StrictLessThan(Symbol('delta'), Rational(135361, 64))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_94(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 2208) | (delta < -skoSINS**2 - 2208))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(2208))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-2208)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_95(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 1) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -2209) | (delta < 2209))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(1)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Integer(-2209)), StrictLessThan(Symbol('delta'), Integer(2209))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_96(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 2303) | (delta < -skoSINS**2 - 2303))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(2303))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-2303)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_97(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -2303) | (delta < 2303))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Integer(-2303)), StrictLessThan(Symbol('delta'), Integer(2303))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_98(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 2400) | (delta < -skoSINS**2 - 2400))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(2400))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-2400)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_99(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 1/8) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -153601/64) | (delta < 153601/64))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(1, 8)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-153601, 64)), StrictLessThan(Symbol('delta'), Rational(153601, 64))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_100(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 2499) | (delta < -skoSINS**2 - 2499))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(2499))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-2499)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_101(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -2499) | (delta < 2499))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Integer(-2499)), StrictLessThan(Symbol('delta'), Integer(2499))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_102(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 2600) | (delta < -skoSINS**2 - 2600))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(2600))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-2600)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_103(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 1/8) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -166401/64) | (delta < 166401/64))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(1, 8)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-166401, 64)), StrictLessThan(Symbol('delta'), Rational(166401, 64))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_104(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 2703) | (delta < -skoSINS**2 - 2703))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(2703))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-2703)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_105(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 1) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -2704) | (delta < 2704))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(1)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Integer(-2704)), StrictLessThan(Symbol('delta'), Integer(2704))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_106(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 2808) | (delta < -skoSINS**2 - 2808))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(2808))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-2808)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_107(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 1) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -2809) | (delta < 2809))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(1)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Integer(-2809)), StrictLessThan(Symbol('delta'), Integer(2809))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_108(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 2915) | (delta < -skoSINS**2 - 2915))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(2915))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-2915)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_109(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 1) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -2916) | (delta < 2916))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(1)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Integer(-2916)), StrictLessThan(Symbol('delta'), Integer(2916))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_110(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 3024) | (delta < -skoSINS**2 - 3024))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(3024))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-3024)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_111(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 1) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -3025) | (delta < 3025))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(1)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Integer(-3025)), StrictLessThan(Symbol('delta'), Integer(3025))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_112(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 3135) | (delta < -skoSINS**2 - 3135))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(3135))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-3135)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_113(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -3136) | (delta < 3136))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Integer(-3136)), StrictLessThan(Symbol('delta'), Integer(3136))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_114(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 3248) | (delta < -skoSINS**2 - 3248))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(3248))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-3248)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_115(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -3249) | (delta < 3249))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Integer(-3249)), StrictLessThan(Symbol('delta'), Integer(3249))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_116(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 3363) | (delta < -skoSINS**2 - 3363))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(3363))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-3363)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_117(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -3364) | (delta < 3364))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Integer(-3364)), StrictLessThan(Symbol('delta'), Integer(3364))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_118(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 3480) | (delta < -skoSINS**2 - 3480))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(3480))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-3480)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_119(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -3480) | (delta < 3480))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Integer(-3480)), StrictLessThan(Symbol('delta'), Integer(3480))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_120(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 3599) | (delta < -skoSINS**2 - 3599))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(3599))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-3599)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_121(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 1/8) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -230337/64) | (delta < 230337/64))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(1, 8)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-230337, 64)), StrictLessThan(Symbol('delta'), Rational(230337, 64))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_122(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 3720) | (delta < -skoSINS**2 - 3720))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(3720))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-3720)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_123(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 1) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -3721) | (delta < 3721))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(1)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Integer(-3721)), StrictLessThan(Symbol('delta'), Integer(3721))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_124(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 3843) | (delta < -skoSINS**2 - 3843))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(3843))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-3843)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_125(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 1) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -3844) | (delta < 3844))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(1)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Integer(-3844)), StrictLessThan(Symbol('delta'), Integer(3844))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_126(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 3968) | (delta < -skoSINS**2 - 3968))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(3968))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-3968)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_127(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -3969) | (delta < 3969))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Integer(-3969)), StrictLessThan(Symbol('delta'), Integer(3969))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_128(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 4095) | (delta < -skoSINS**2 - 4095))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(4095))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-4095)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_129(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -4095) | (delta < 4095))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Integer(-4095)), StrictLessThan(Symbol('delta'), Integer(4095))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_130(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 4224) | (delta < -skoSINS**2 - 4224))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(4224))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-4224)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_131(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 1/8) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -270337/64) | (delta < 270337/64))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(1, 8)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-270337, 64)), StrictLessThan(Symbol('delta'), Rational(270337, 64))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_132(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 4355) | (delta < -skoSINS**2 - 4355))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(4355))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-4355)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_133(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -4355) | (delta < 4355))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Integer(-4355)), StrictLessThan(Symbol('delta'), Integer(4355))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_134(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 4488) | (delta < -skoSINS**2 - 4488))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(4488))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-4488)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_135(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 1/8) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -287233/64) | (delta < 287233/64))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(1, 8)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-287233, 64)), StrictLessThan(Symbol('delta'), Rational(287233, 64))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_136(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 4623) | (delta < -skoSINS**2 - 4623))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(4623))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-4623)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_137(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 1) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -4624) | (delta < 4624))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(1)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Integer(-4624)), StrictLessThan(Symbol('delta'), Integer(4624))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_138(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 4760) | (delta < -skoSINS**2 - 4760))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(4760))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-4760)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_139(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 1) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -4761) | (delta < 4761))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(1)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Integer(-4761)), StrictLessThan(Symbol('delta'), Integer(4761))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_140(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 4899) | (delta < -skoSINS**2 - 4899))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(4899))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-4899)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_141(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 1) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -4900) | (delta < 4900))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(1)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Integer(-4900)), StrictLessThan(Symbol('delta'), Integer(4900))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_142(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 5040) | (delta < -skoSINS**2 - 5040))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(5040))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-5040)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_143(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -5041) | (delta < 5041))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Integer(-5041)), StrictLessThan(Symbol('delta'), Integer(5041))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_144(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 5183) | (delta < -skoSINS**2 - 5183))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(5183))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-5183)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_145(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -5184) | (delta < 5184))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Integer(-5184)), StrictLessThan(Symbol('delta'), Integer(5184))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_146(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 5328) | (delta < -skoSINS**2 - 5328))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(5328))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-5328)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_147(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 1) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -5329) | (delta < 5329))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(1)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Integer(-5329)), StrictLessThan(Symbol('delta'), Integer(5329))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_148(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 5475) | (delta < -skoSINS**2 - 5475))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(5475))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-5475)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_149(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 1) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -5476) | (delta < 5476))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(1)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Integer(-5476)), StrictLessThan(Symbol('delta'), Integer(5476))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_150(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 5624) | (delta < -skoSINS**2 - 5624))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(5624))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-5624)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_151(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -5624) | (delta < 5624))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Integer(-5624)), StrictLessThan(Symbol('delta'), Integer(5624))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_152(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 5775) | (delta < -skoSINS**2 - 5775))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(5775))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-5775)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_153(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 1/8) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -369601/64) | (delta < 369601/64))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(1, 8)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-369601, 64)), StrictLessThan(Symbol('delta'), Rational(369601, 64))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_154(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 5928) | (delta < -skoSINS**2 - 5928))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(5928))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-5928)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_155(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -5929) | (delta < 5929))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Integer(-5929)), StrictLessThan(Symbol('delta'), Integer(5929))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_156(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 6083) | (delta < -skoSINS**2 - 6083))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(6083))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-6083)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_157(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 1) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -6084) | (delta < 6084))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(1)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Integer(-6084)), StrictLessThan(Symbol('delta'), Integer(6084))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_158(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 6240) | (delta < -skoSINS**2 - 6240))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(6240))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-6240)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_159(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -6240) | (delta < 6240))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Integer(-6240)), StrictLessThan(Symbol('delta'), Integer(6240))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_160(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 6399) | (delta < -skoSINS**2 - 6399))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(6399))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-6399)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_161(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 1/8) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -409537/64) | (delta < 409537/64))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(1, 8)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-409537, 64)), StrictLessThan(Symbol('delta'), Rational(409537, 64))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_162(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 6560) | (delta < -skoSINS**2 - 6560))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(6560))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-6560)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_163(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -6560) | (delta < 6560))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Integer(-6560)), StrictLessThan(Symbol('delta'), Integer(6560))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_164(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 6723) | (delta < -skoSINS**2 - 6723))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(6723))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-6723)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_165(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 1/8) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -430273/64) | (delta < 430273/64))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(1, 8)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-430273, 64)), StrictLessThan(Symbol('delta'), Rational(430273, 64))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_166(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 6888) | (delta < -skoSINS**2 - 6888))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(6888))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-6888)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_167(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -6889) | (delta < 6889))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Integer(-6889)), StrictLessThan(Symbol('delta'), Integer(6889))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_168(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 7055) | (delta < -skoSINS**2 - 7055))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(7055))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-7055)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_169(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -7056) | (delta < 7056))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Integer(-7056)), StrictLessThan(Symbol('delta'), Integer(7056))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_170(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 7224) | (delta < -skoSINS**2 - 7224))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(7224))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-7224)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_171(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -7224) | (delta < 7224))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Integer(-7224)), StrictLessThan(Symbol('delta'), Integer(7224))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_172(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 7395) | (delta < -skoSINS**2 - 7395))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(7395))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-7395)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_173(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 1/8) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -473281/64) | (delta < 473281/64))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(1, 8)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-473281, 64)), StrictLessThan(Symbol('delta'), Rational(473281, 64))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_174(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 7568) | (delta < -skoSINS**2 - 7568))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(7568))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-7568)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_175(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 1) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -7569) | (delta < 7569))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(1)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Integer(-7569)), StrictLessThan(Symbol('delta'), Integer(7569))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_176(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 7743) | (delta < -skoSINS**2 - 7743))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(7743))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-7743)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_177(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 1) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -7744) | (delta < 7744))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(1)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Integer(-7744)), StrictLessThan(Symbol('delta'), Integer(7744))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(delta:sympy.Rational, skoS:sympy.Rational, pi:sympy.Rational, skoCOSS:sympy.Rational, skoSINS:sympy.Rational):
	# (0 <= delta) & (0 <= skoCOSS) & (0 <= skoS) & (skoSINS <= skoS) & (31415927/10000000 > pi) & (pi > 15707963/5000000) & (pi/2 > skoS) & ~((skoCOSS**2 + skoSINS**2 - 1 <= delta) & (-skoCOSS**2 - skoSINS**2 + 1 <= delta))

	post_cond =  And(LessThan(Integer(0), Symbol('delta')), LessThan(Integer(0), Symbol('skoCOSS')), LessThan(Integer(0), Symbol('skoS')), LessThan(Symbol('skoSINS'), Symbol('skoS')), StrictGreaterThan(Rational(31415927, 10000000), Symbol('pi')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Mul(Rational(1, 2), Symbol('pi')), Symbol('skoS')), Not(And(LessThan(Add(Pow(Symbol('skoCOSS'), Integer(2)), Pow(Symbol('skoSINS'), Integer(2)), Integer(-1)), Symbol('delta')), LessThan(Add(Mul(Integer(-1), Pow(Symbol('skoCOSS'), Integer(2))), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(1)), Symbol('delta')))))

	eval = post_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi, 'skoCOSS':skoCOSS, 'skoSINS':skoSINS })

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
	
	
	ip_0=int(input("enter integer numerator of pi:\n"))
	ip_1=int(input("enter integer denominator of pi:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	pi=sympy.Rational(ip_0,ip_1)
	
	
	
	
	if pre_condition_0(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_0 SAT")
		print('delta = 1/128')
		print('skoCOSS = 1')
		print('skoS = 1')
		print('skoSINS = 1/8')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_1(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_1 SAT")
		print('delta = 1/128')
		print('skoCOSS = 1')
		print('skoS = 1')
		print('skoSINS = 1/8')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_2(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_2 SAT")
		print('delta = 1/64')
		print('skoCOSS = 0')
		print('skoS = 62831851/40000000')
		print('skoSINS = 0')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_3(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_3 SAT")
		print('delta = 1/64')
		print('skoCOSS = 0')
		print('skoS = 62831851/40000000')
		print('skoSINS = 0')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_4(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_4 SAT")
		print('delta = 2')
		print('skoCOSS = 2')
		print('skoS = 1')
		print('skoSINS = 1/8')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_5(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_5 SAT")
		print('delta = 2')
		print('skoCOSS = 2')
		print('skoS = 1')
		print('skoSINS = 1/8')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_6(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_6 SAT")
		print('delta = 4')
		print('skoCOSS = 3')
		print('skoS = 1/16')
		print('skoSINS = -1/2')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_7(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_7 SAT")
		print('delta = 4')
		print('skoCOSS = 3')
		print('skoS = 1/16')
		print('skoSINS = -1/2')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_8(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_8 SAT")
		print('delta = 9')
		print('skoCOSS = 4')
		print('skoS = 1')
		print('skoSINS = 0')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_9(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_9 SAT")
		print('delta = 9')
		print('skoCOSS = 4')
		print('skoS = 1')
		print('skoSINS = 0')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_10(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_10 SAT")
		print('delta = 16')
		print('skoCOSS = 5')
		print('skoS = 1')
		print('skoSINS = 1/8')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_11(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_11 SAT")
		print('delta = 16')
		print('skoCOSS = 5')
		print('skoS = 1')
		print('skoSINS = 1/8')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_12(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_12 SAT")
		print('delta = 26')
		print('skoCOSS = 6')
		print('skoS = 1')
		print('skoSINS = -1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_13(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_13 SAT")
		print('delta = 26')
		print('skoCOSS = 6')
		print('skoS = 1')
		print('skoSINS = -1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_14(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_14 SAT")
		print('delta = 37')
		print('skoCOSS = 7')
		print('skoS = 1')
		print('skoSINS = -1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_15(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_15 SAT")
		print('delta = 37')
		print('skoCOSS = 7')
		print('skoS = 1')
		print('skoSINS = -1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_16(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_16 SAT")
		print('delta = 50')
		print('skoCOSS = 8')
		print('skoS = 3/2')
		print('skoSINS = 1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_17(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_17 SAT")
		print('delta = 50')
		print('skoCOSS = 8')
		print('skoS = 3/2')
		print('skoSINS = 1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_18(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_18 SAT")
		print('delta = 65')
		print('skoCOSS = 9')
		print('skoS = 3/2')
		print('skoSINS = 1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_19(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_19 SAT")
		print('delta = 65')
		print('skoCOSS = 9')
		print('skoS = 3/2')
		print('skoSINS = 1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_20(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_20 SAT")
		print('delta = 82')
		print('skoCOSS = 10')
		print('skoS = 1')
		print('skoSINS = 0')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_21(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_21 SAT")
		print('delta = 82')
		print('skoCOSS = 10')
		print('skoS = 1')
		print('skoSINS = 0')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_22(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_22 SAT")
		print('delta = 100')
		print('skoCOSS = 11')
		print('skoS = 1')
		print('skoSINS = 1/8')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_23(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_23 SAT")
		print('delta = 100')
		print('skoCOSS = 11')
		print('skoS = 1')
		print('skoSINS = 1/8')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_24(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_24 SAT")
		print('delta = 122')
		print('skoCOSS = 12')
		print('skoS = 1')
		print('skoSINS = -1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_25(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_25 SAT")
		print('delta = 122')
		print('skoCOSS = 12')
		print('skoS = 1')
		print('skoSINS = -1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_26(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_26 SAT")
		print('delta = 145')
		print('skoCOSS = 13')
		print('skoS = 3/2')
		print('skoSINS = 1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_27(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_27 SAT")
		print('delta = 145')
		print('skoCOSS = 13')
		print('skoS = 3/2')
		print('skoSINS = 1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_28(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_28 SAT")
		print('delta = 170')
		print('skoCOSS = 14')
		print('skoS = 1')
		print('skoSINS = -1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_29(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_29 SAT")
		print('delta = 170')
		print('skoCOSS = 14')
		print('skoS = 1')
		print('skoSINS = -1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_30(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_30 SAT")
		print('delta = 197')
		print('skoCOSS = 15')
		print('skoS = 3/2')
		print('skoSINS = 1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_31(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_31 SAT")
		print('delta = 197')
		print('skoCOSS = 15')
		print('skoS = 3/2')
		print('skoSINS = 1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_32(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_32 SAT")
		print('delta = 226')
		print('skoCOSS = 16')
		print('skoS = 1')
		print('skoSINS = -1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_33(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_33 SAT")
		print('delta = 226')
		print('skoCOSS = 16')
		print('skoS = 1')
		print('skoSINS = -1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_34(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_34 SAT")
		print('delta = 257')
		print('skoCOSS = 17')
		print('skoS = 1')
		print('skoSINS = -1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_35(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_35 SAT")
		print('delta = 257')
		print('skoCOSS = 17')
		print('skoS = 1')
		print('skoSINS = -1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_36(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_36 SAT")
		print('delta = 290')
		print('skoCOSS = 18')
		print('skoS = 1')
		print('skoSINS = -1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_37(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_37 SAT")
		print('delta = 290')
		print('skoCOSS = 18')
		print('skoS = 1')
		print('skoSINS = -1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_38(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_38 SAT")
		print('delta = 325')
		print('skoCOSS = 19')
		print('skoS = 1')
		print('skoSINS = -1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_39(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_39 SAT")
		print('delta = 325')
		print('skoCOSS = 19')
		print('skoS = 1')
		print('skoSINS = -1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_40(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_40 SAT")
		print('delta = 362')
		print('skoCOSS = 20')
		print('skoS = 1')
		print('skoSINS = -1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_41(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_41 SAT")
		print('delta = 362')
		print('skoCOSS = 20')
		print('skoS = 1')
		print('skoSINS = -1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_42(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_42 SAT")
		print('delta = 401')
		print('skoCOSS = 21')
		print('skoS = 1')
		print('skoSINS = -1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_43(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_43 SAT")
		print('delta = 401')
		print('skoCOSS = 21')
		print('skoS = 1')
		print('skoSINS = -1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_44(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_44 SAT")
		print('delta = 442')
		print('skoCOSS = 22')
		print('skoS = 1')
		print('skoSINS = 0')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_45(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_45 SAT")
		print('delta = 442')
		print('skoCOSS = 22')
		print('skoS = 1')
		print('skoSINS = 0')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_46(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_46 SAT")
		print('delta = 484')
		print('skoCOSS = 23')
		print('skoS = 1')
		print('skoSINS = 1/8')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_47(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_47 SAT")
		print('delta = 484')
		print('skoCOSS = 23')
		print('skoS = 1')
		print('skoSINS = 1/8')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_48(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_48 SAT")
		print('delta = 530')
		print('skoCOSS = 24')
		print('skoS = 1')
		print('skoSINS = -1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_49(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_49 SAT")
		print('delta = 530')
		print('skoCOSS = 24')
		print('skoS = 1')
		print('skoSINS = -1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_50(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_50 SAT")
		print('delta = 577')
		print('skoCOSS = 25')
		print('skoS = 3/2')
		print('skoSINS = 1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_51(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_51 SAT")
		print('delta = 577')
		print('skoCOSS = 25')
		print('skoS = 3/2')
		print('skoSINS = 1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_52(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_52 SAT")
		print('delta = 626')
		print('skoCOSS = 26')
		print('skoS = 1')
		print('skoSINS = -1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_53(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_53 SAT")
		print('delta = 626')
		print('skoCOSS = 26')
		print('skoS = 1')
		print('skoSINS = -1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_54(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_54 SAT")
		print('delta = 677')
		print('skoCOSS = 27')
		print('skoS = 1')
		print('skoSINS = -1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_55(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_55 SAT")
		print('delta = 677')
		print('skoCOSS = 27')
		print('skoS = 1')
		print('skoSINS = -1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_56(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_56 SAT")
		print('delta = 730')
		print('skoCOSS = 28')
		print('skoS = 1')
		print('skoSINS = 0')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_57(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_57 SAT")
		print('delta = 730')
		print('skoCOSS = 28')
		print('skoS = 1')
		print('skoSINS = 0')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_58(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_58 SAT")
		print('delta = 784')
		print('skoCOSS = 29')
		print('skoS = 1')
		print('skoSINS = 1/8')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_59(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_59 SAT")
		print('delta = 784')
		print('skoCOSS = 29')
		print('skoS = 1')
		print('skoSINS = 1/8')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_60(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_60 SAT")
		print('delta = 842')
		print('skoCOSS = 30')
		print('skoS = 3/2')
		print('skoSINS = 1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_61(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_61 SAT")
		print('delta = 842')
		print('skoCOSS = 30')
		print('skoS = 3/2')
		print('skoSINS = 1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_62(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_62 SAT")
		print('delta = 901')
		print('skoCOSS = 31')
		print('skoS = 1')
		print('skoSINS = 0')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_63(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_63 SAT")
		print('delta = 901')
		print('skoCOSS = 31')
		print('skoS = 1')
		print('skoSINS = 0')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_64(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_64 SAT")
		print('delta = 961')
		print('skoCOSS = 32')
		print('skoS = 1')
		print('skoSINS = 1/8')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_65(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_65 SAT")
		print('delta = 961')
		print('skoCOSS = 32')
		print('skoS = 1')
		print('skoSINS = 1/8')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_66(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_66 SAT")
		print('delta = 1025')
		print('skoCOSS = 33')
		print('skoS = 1')
		print('skoSINS = -1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_67(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_67 SAT")
		print('delta = 1025')
		print('skoCOSS = 33')
		print('skoS = 1')
		print('skoSINS = -1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_68(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_68 SAT")
		print('delta = 1090')
		print('skoCOSS = 34')
		print('skoS = 3/2')
		print('skoSINS = 1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_69(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_69 SAT")
		print('delta = 1090')
		print('skoCOSS = 34')
		print('skoS = 3/2')
		print('skoSINS = 1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_70(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_70 SAT")
		print('delta = 1157')
		print('skoCOSS = 35')
		print('skoS = 1')
		print('skoSINS = -1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_71(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_71 SAT")
		print('delta = 1157')
		print('skoCOSS = 35')
		print('skoS = 1')
		print('skoSINS = -1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_72(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_72 SAT")
		print('delta = 1226')
		print('skoCOSS = 36')
		print('skoS = 3/2')
		print('skoSINS = 1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_73(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_73 SAT")
		print('delta = 1226')
		print('skoCOSS = 36')
		print('skoS = 3/2')
		print('skoSINS = 1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_74(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_74 SAT")
		print('delta = 1297')
		print('skoCOSS = 37')
		print('skoS = 1')
		print('skoSINS = 0')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_75(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_75 SAT")
		print('delta = 1297')
		print('skoCOSS = 37')
		print('skoS = 1')
		print('skoSINS = 0')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_76(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_76 SAT")
		print('delta = 1369')
		print('skoCOSS = 38')
		print('skoS = 1')
		print('skoSINS = 1/8')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_77(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_77 SAT")
		print('delta = 1369')
		print('skoCOSS = 38')
		print('skoS = 1')
		print('skoSINS = 1/8')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_78(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_78 SAT")
		print('delta = 1445')
		print('skoCOSS = 39')
		print('skoS = 1')
		print('skoSINS = -1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_79(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_79 SAT")
		print('delta = 1445')
		print('skoCOSS = 39')
		print('skoS = 1')
		print('skoSINS = -1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_80(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_80 SAT")
		print('delta = 1522')
		print('skoCOSS = 40')
		print('skoS = 1')
		print('skoSINS = -1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_81(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_81 SAT")
		print('delta = 1522')
		print('skoCOSS = 40')
		print('skoS = 1')
		print('skoSINS = -1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_82(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_82 SAT")
		print('delta = 1601')
		print('skoCOSS = 41')
		print('skoS = 1')
		print('skoSINS = -1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_83(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_83 SAT")
		print('delta = 1601')
		print('skoCOSS = 41')
		print('skoS = 1')
		print('skoSINS = -1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_84(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_84 SAT")
		print('delta = 1682')
		print('skoCOSS = 42')
		print('skoS = 1')
		print('skoSINS = 0')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_85(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_85 SAT")
		print('delta = 1682')
		print('skoCOSS = 42')
		print('skoS = 1')
		print('skoSINS = 0')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_86(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_86 SAT")
		print('delta = 1764')
		print('skoCOSS = 43')
		print('skoS = 1')
		print('skoSINS = 1/8')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_87(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_87 SAT")
		print('delta = 1764')
		print('skoCOSS = 43')
		print('skoS = 1')
		print('skoSINS = 1/8')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_88(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_88 SAT")
		print('delta = 1850')
		print('skoCOSS = 44')
		print('skoS = 1')
		print('skoSINS = -1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_89(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_89 SAT")
		print('delta = 1850')
		print('skoCOSS = 44')
		print('skoS = 1')
		print('skoSINS = -1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_90(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_90 SAT")
		print('delta = 1937')
		print('skoCOSS = 45')
		print('skoS = 1')
		print('skoSINS = 0')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_91(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_91 SAT")
		print('delta = 1937')
		print('skoCOSS = 45')
		print('skoS = 1')
		print('skoSINS = 0')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_92(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_92 SAT")
		print('delta = 2025')
		print('skoCOSS = 46')
		print('skoS = 1')
		print('skoSINS = 1/8')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_93(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_93 SAT")
		print('delta = 2025')
		print('skoCOSS = 46')
		print('skoS = 1')
		print('skoSINS = 1/8')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_94(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_94 SAT")
		print('delta = 2117')
		print('skoCOSS = 47')
		print('skoS = 3/2')
		print('skoSINS = 1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_95(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_95 SAT")
		print('delta = 2117')
		print('skoCOSS = 47')
		print('skoS = 3/2')
		print('skoSINS = 1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_96(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_96 SAT")
		print('delta = 2210')
		print('skoCOSS = 48')
		print('skoS = 1')
		print('skoSINS = 0')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_97(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_97 SAT")
		print('delta = 2210')
		print('skoCOSS = 48')
		print('skoS = 1')
		print('skoSINS = 0')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_98(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_98 SAT")
		print('delta = 2304')
		print('skoCOSS = 49')
		print('skoS = 1')
		print('skoSINS = 1/8')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_99(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_99 SAT")
		print('delta = 2304')
		print('skoCOSS = 49')
		print('skoS = 1')
		print('skoSINS = 1/8')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_100(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_100 SAT")
		print('delta = 2401')
		print('skoCOSS = 50')
		print('skoS = 1')
		print('skoSINS = 0')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_101(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_101 SAT")
		print('delta = 2401')
		print('skoCOSS = 50')
		print('skoS = 1')
		print('skoSINS = 0')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_102(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_102 SAT")
		print('delta = 2500')
		print('skoCOSS = 51')
		print('skoS = 1')
		print('skoSINS = 1/8')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_103(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_103 SAT")
		print('delta = 2500')
		print('skoCOSS = 51')
		print('skoS = 1')
		print('skoSINS = 1/8')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_104(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_104 SAT")
		print('delta = 2602')
		print('skoCOSS = 52')
		print('skoS = 3/2')
		print('skoSINS = 1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_105(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_105 SAT")
		print('delta = 2602')
		print('skoCOSS = 52')
		print('skoS = 3/2')
		print('skoSINS = 1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_106(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_106 SAT")
		print('delta = 2705')
		print('skoCOSS = 53')
		print('skoS = 3/2')
		print('skoSINS = 1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_107(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_107 SAT")
		print('delta = 2705')
		print('skoCOSS = 53')
		print('skoS = 3/2')
		print('skoSINS = 1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_108(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_108 SAT")
		print('delta = 2810')
		print('skoCOSS = 54')
		print('skoS = 3/2')
		print('skoSINS = 1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_109(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_109 SAT")
		print('delta = 2810')
		print('skoCOSS = 54')
		print('skoS = 3/2')
		print('skoSINS = 1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_110(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_110 SAT")
		print('delta = 2917')
		print('skoCOSS = 55')
		print('skoS = 3/2')
		print('skoSINS = 1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_111(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_111 SAT")
		print('delta = 2917')
		print('skoCOSS = 55')
		print('skoS = 3/2')
		print('skoSINS = 1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_112(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_112 SAT")
		print('delta = 3026')
		print('skoCOSS = 56')
		print('skoS = 1')
		print('skoSINS = -1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_113(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_113 SAT")
		print('delta = 3026')
		print('skoCOSS = 56')
		print('skoS = 1')
		print('skoSINS = -1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_114(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_114 SAT")
		print('delta = 3137')
		print('skoCOSS = 57')
		print('skoS = 1')
		print('skoSINS = -1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_115(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_115 SAT")
		print('delta = 3137')
		print('skoCOSS = 57')
		print('skoS = 1')
		print('skoSINS = -1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_116(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_116 SAT")
		print('delta = 3250')
		print('skoCOSS = 58')
		print('skoS = 1')
		print('skoSINS = -1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_117(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_117 SAT")
		print('delta = 3250')
		print('skoCOSS = 58')
		print('skoS = 1')
		print('skoSINS = -1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_118(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_118 SAT")
		print('delta = 3365')
		print('skoCOSS = 59')
		print('skoS = 1')
		print('skoSINS = 0')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_119(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_119 SAT")
		print('delta = 3365')
		print('skoCOSS = 59')
		print('skoS = 1')
		print('skoSINS = 0')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_120(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_120 SAT")
		print('delta = 3481')
		print('skoCOSS = 60')
		print('skoS = 1')
		print('skoSINS = 1/8')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_121(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_121 SAT")
		print('delta = 3481')
		print('skoCOSS = 60')
		print('skoS = 1')
		print('skoSINS = 1/8')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_122(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_122 SAT")
		print('delta = 3601')
		print('skoCOSS = 61')
		print('skoS = 3/2')
		print('skoSINS = 1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_123(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_123 SAT")
		print('delta = 3601')
		print('skoCOSS = 61')
		print('skoS = 3/2')
		print('skoSINS = 1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_124(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_124 SAT")
		print('delta = 3722')
		print('skoCOSS = 62')
		print('skoS = 3/2')
		print('skoSINS = 1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_125(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_125 SAT")
		print('delta = 3722')
		print('skoCOSS = 62')
		print('skoS = 3/2')
		print('skoSINS = 1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_126(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_126 SAT")
		print('delta = 3845')
		print('skoCOSS = 63')
		print('skoS = 1')
		print('skoSINS = -1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_127(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_127 SAT")
		print('delta = 3845')
		print('skoCOSS = 63')
		print('skoS = 1')
		print('skoSINS = -1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_128(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_128 SAT")
		print('delta = 3970')
		print('skoCOSS = 64')
		print('skoS = 1')
		print('skoSINS = 0')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_129(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_129 SAT")
		print('delta = 3970')
		print('skoCOSS = 64')
		print('skoS = 1')
		print('skoSINS = 0')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_130(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_130 SAT")
		print('delta = 4096')
		print('skoCOSS = 65')
		print('skoS = 1')
		print('skoSINS = 1/8')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_131(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_131 SAT")
		print('delta = 4096')
		print('skoCOSS = 65')
		print('skoS = 1')
		print('skoSINS = 1/8')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_132(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_132 SAT")
		print('delta = 4225')
		print('skoCOSS = 66')
		print('skoS = 1')
		print('skoSINS = 0')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_133(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_133 SAT")
		print('delta = 4225')
		print('skoCOSS = 66')
		print('skoS = 1')
		print('skoSINS = 0')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_134(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_134 SAT")
		print('delta = 4356')
		print('skoCOSS = 67')
		print('skoS = 1')
		print('skoSINS = 1/8')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_135(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_135 SAT")
		print('delta = 4356')
		print('skoCOSS = 67')
		print('skoS = 1')
		print('skoSINS = 1/8')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_136(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_136 SAT")
		print('delta = 4490')
		print('skoCOSS = 68')
		print('skoS = 3/2')
		print('skoSINS = 1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_137(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_137 SAT")
		print('delta = 4490')
		print('skoCOSS = 68')
		print('skoS = 3/2')
		print('skoSINS = 1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_138(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_138 SAT")
		print('delta = 4625')
		print('skoCOSS = 69')
		print('skoS = 3/2')
		print('skoSINS = 1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_139(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_139 SAT")
		print('delta = 4625')
		print('skoCOSS = 69')
		print('skoS = 3/2')
		print('skoSINS = 1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_140(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_140 SAT")
		print('delta = 4762')
		print('skoCOSS = 70')
		print('skoS = 3/2')
		print('skoSINS = 1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_141(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_141 SAT")
		print('delta = 4762')
		print('skoCOSS = 70')
		print('skoS = 3/2')
		print('skoSINS = 1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_142(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_142 SAT")
		print('delta = 4901')
		print('skoCOSS = 71')
		print('skoS = 1')
		print('skoSINS = -1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_143(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_143 SAT")
		print('delta = 4901')
		print('skoCOSS = 71')
		print('skoS = 1')
		print('skoSINS = -1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_144(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_144 SAT")
		print('delta = 5042')
		print('skoCOSS = 72')
		print('skoS = 1')
		print('skoSINS = -1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_145(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_145 SAT")
		print('delta = 5042')
		print('skoCOSS = 72')
		print('skoS = 1')
		print('skoSINS = -1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_146(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_146 SAT")
		print('delta = 5185')
		print('skoCOSS = 73')
		print('skoS = 3/2')
		print('skoSINS = 1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_147(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_147 SAT")
		print('delta = 5185')
		print('skoCOSS = 73')
		print('skoS = 3/2')
		print('skoSINS = 1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_148(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_148 SAT")
		print('delta = 5330')
		print('skoCOSS = 74')
		print('skoS = 3/2')
		print('skoSINS = 1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_149(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_149 SAT")
		print('delta = 5330')
		print('skoCOSS = 74')
		print('skoS = 3/2')
		print('skoSINS = 1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_150(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_150 SAT")
		print('delta = 5477')
		print('skoCOSS = 75')
		print('skoS = 1')
		print('skoSINS = 0')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_151(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_151 SAT")
		print('delta = 5477')
		print('skoCOSS = 75')
		print('skoS = 1')
		print('skoSINS = 0')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_152(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_152 SAT")
		print('delta = 5625')
		print('skoCOSS = 76')
		print('skoS = 1')
		print('skoSINS = 1/8')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_153(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_153 SAT")
		print('delta = 5625')
		print('skoCOSS = 76')
		print('skoS = 1')
		print('skoSINS = 1/8')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_154(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_154 SAT")
		print('delta = 5777')
		print('skoCOSS = 77')
		print('skoS = 1')
		print('skoSINS = -1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_155(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_155 SAT")
		print('delta = 5777')
		print('skoCOSS = 77')
		print('skoS = 1')
		print('skoSINS = -1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_156(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_156 SAT")
		print('delta = 5930')
		print('skoCOSS = 78')
		print('skoS = 3/2')
		print('skoSINS = 1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_157(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_157 SAT")
		print('delta = 5930')
		print('skoCOSS = 78')
		print('skoS = 3/2')
		print('skoSINS = 1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_158(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_158 SAT")
		print('delta = 6085')
		print('skoCOSS = 79')
		print('skoS = 1')
		print('skoSINS = 0')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_159(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_159 SAT")
		print('delta = 6085')
		print('skoCOSS = 79')
		print('skoS = 1')
		print('skoSINS = 0')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_160(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_160 SAT")
		print('delta = 6241')
		print('skoCOSS = 80')
		print('skoS = 1')
		print('skoSINS = 1/8')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_161(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_161 SAT")
		print('delta = 6241')
		print('skoCOSS = 80')
		print('skoS = 1')
		print('skoSINS = 1/8')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_162(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_162 SAT")
		print('delta = 6400')
		print('skoCOSS = 81')
		print('skoS = 1')
		print('skoSINS = 0')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_163(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_163 SAT")
		print('delta = 6400')
		print('skoCOSS = 81')
		print('skoS = 1')
		print('skoSINS = 0')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_164(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_164 SAT")
		print('delta = 6561')
		print('skoCOSS = 82')
		print('skoS = 1')
		print('skoSINS = 1/8')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_165(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_165 SAT")
		print('delta = 6561')
		print('skoCOSS = 82')
		print('skoS = 1')
		print('skoSINS = 1/8')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_166(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_166 SAT")
		print('delta = 6725')
		print('skoCOSS = 83')
		print('skoS = 1')
		print('skoSINS = -1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_167(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_167 SAT")
		print('delta = 6725')
		print('skoCOSS = 83')
		print('skoS = 1')
		print('skoSINS = -1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_168(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_168 SAT")
		print('delta = 6890')
		print('skoCOSS = 84')
		print('skoS = 1')
		print('skoSINS = -1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_169(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_169 SAT")
		print('delta = 6890')
		print('skoCOSS = 84')
		print('skoS = 1')
		print('skoSINS = -1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_170(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_170 SAT")
		print('delta = 7057')
		print('skoCOSS = 85')
		print('skoS = 1')
		print('skoSINS = 0')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_171(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_171 SAT")
		print('delta = 7057')
		print('skoCOSS = 85')
		print('skoS = 1')
		print('skoSINS = 0')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_172(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_172 SAT")
		print('delta = 7225')
		print('skoCOSS = 86')
		print('skoS = 1')
		print('skoSINS = 1/8')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_173(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_173 SAT")
		print('delta = 7225')
		print('skoCOSS = 86')
		print('skoS = 1')
		print('skoSINS = 1/8')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_174(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_174 SAT")
		print('delta = 7397')
		print('skoCOSS = 87')
		print('skoS = 3/2')
		print('skoSINS = 1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_175(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_175 SAT")
		print('delta = 7397')
		print('skoCOSS = 87')
		print('skoS = 3/2')
		print('skoSINS = 1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_176(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_176 SAT")
		print('delta = 7570')
		print('skoCOSS = 88')
		print('skoS = 3/2')
		print('skoSINS = 1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_177(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_177 SAT")
		print('delta = 7570')
		print('skoCOSS = 88')
		print('skoS = 3/2')
		print('skoSINS = 1')
		print('pi = 26353589/8388608')
		exit(0)


	print("UNKNOWN")
	exit(0)
