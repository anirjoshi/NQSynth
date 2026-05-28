import sympy
from sympy import *

def pre_condition_0(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 - 63/64) | (delta < 63/64 - skoSINS**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-63, 64))), StrictLessThan(Symbol('delta'), Add(Rational(63, 64), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2)))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -47/64) | (delta < 47/64))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-47, 64)), StrictLessThan(Symbol('delta'), Rational(47, 64))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 - 1) | (delta < 1 - skoSINS**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Integer(1), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2)))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -1) | (delta < 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Integer(-1)), StrictLessThan(Symbol('delta'), Integer(1))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_4(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2) | (delta < -skoSINS**2))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Pow(Symbol('skoSINS'), Integer(2))), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_5(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -4) | (delta < 4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Integer(-4)), StrictLessThan(Symbol('delta'), Integer(4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_6(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 3) | (delta < -skoSINS**2 - 3))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(3))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-3)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_7(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -7) | (delta < 7))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Integer(-7)), StrictLessThan(Symbol('delta'), Integer(7))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_8(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 8) | (delta < -skoSINS**2 - 8))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(8))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-8)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_9(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -33/4) | (delta < 33/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-33, 4)), StrictLessThan(Symbol('delta'), Rational(33, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_10(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 15) | (delta < -skoSINS**2 - 15))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(15))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-15)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_11(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -61/4) | (delta < 61/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-61, 4)), StrictLessThan(Symbol('delta'), Rational(61, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_12(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 24) | (delta < -skoSINS**2 - 24))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(24))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-24)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_13(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -97/4) | (delta < 97/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-97, 4)), StrictLessThan(Symbol('delta'), Rational(97, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_14(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 35) | (delta < -skoSINS**2 - 35))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(35))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-35)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_15(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -141/4) | (delta < 141/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-141, 4)), StrictLessThan(Symbol('delta'), Rational(141, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_16(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 48) | (delta < -skoSINS**2 - 48))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(48))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-48)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_17(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -193/4) | (delta < 193/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-193, 4)), StrictLessThan(Symbol('delta'), Rational(193, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_18(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 63) | (delta < -skoSINS**2 - 63))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(63))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-63)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_19(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -253/4) | (delta < 253/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-253, 4)), StrictLessThan(Symbol('delta'), Rational(253, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_20(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 80) | (delta < -skoSINS**2 - 80))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(80))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-80)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_21(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -321/4) | (delta < 321/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-321, 4)), StrictLessThan(Symbol('delta'), Rational(321, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_22(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 99) | (delta < -skoSINS**2 - 99))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(99))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-99)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_23(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -397/4) | (delta < 397/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-397, 4)), StrictLessThan(Symbol('delta'), Rational(397, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_24(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 120) | (delta < -skoSINS**2 - 120))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(120))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-120)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_25(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -481/4) | (delta < 481/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-481, 4)), StrictLessThan(Symbol('delta'), Rational(481, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_26(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 143) | (delta < -skoSINS**2 - 143))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(143))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-143)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_27(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -573/4) | (delta < 573/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-573, 4)), StrictLessThan(Symbol('delta'), Rational(573, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_28(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 168) | (delta < -skoSINS**2 - 168))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(168))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-168)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_29(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -673/4) | (delta < 673/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-673, 4)), StrictLessThan(Symbol('delta'), Rational(673, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_30(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 195) | (delta < -skoSINS**2 - 195))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(195))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-195)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_31(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -781/4) | (delta < 781/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-781, 4)), StrictLessThan(Symbol('delta'), Rational(781, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_32(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 224) | (delta < -skoSINS**2 - 224))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(224))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-224)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_33(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -897/4) | (delta < 897/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-897, 4)), StrictLessThan(Symbol('delta'), Rational(897, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_34(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 255) | (delta < -skoSINS**2 - 255))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(255))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-255)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_35(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -1021/4) | (delta < 1021/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-1021, 4)), StrictLessThan(Symbol('delta'), Rational(1021, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_36(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 288) | (delta < -skoSINS**2 - 288))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(288))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-288)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_37(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -1153/4) | (delta < 1153/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-1153, 4)), StrictLessThan(Symbol('delta'), Rational(1153, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_38(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 323) | (delta < -skoSINS**2 - 323))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(323))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-323)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_39(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -1293/4) | (delta < 1293/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-1293, 4)), StrictLessThan(Symbol('delta'), Rational(1293, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_40(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 360) | (delta < -skoSINS**2 - 360))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(360))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-360)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_41(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -1441/4) | (delta < 1441/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-1441, 4)), StrictLessThan(Symbol('delta'), Rational(1441, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_42(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 399) | (delta < -skoSINS**2 - 399))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(399))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-399)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_43(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -1597/4) | (delta < 1597/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-1597, 4)), StrictLessThan(Symbol('delta'), Rational(1597, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_44(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 440) | (delta < -skoSINS**2 - 440))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(440))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-440)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_45(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -1761/4) | (delta < 1761/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-1761, 4)), StrictLessThan(Symbol('delta'), Rational(1761, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_46(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 483) | (delta < -skoSINS**2 - 483))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(483))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-483)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_47(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -1933/4) | (delta < 1933/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-1933, 4)), StrictLessThan(Symbol('delta'), Rational(1933, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_48(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 528) | (delta < -skoSINS**2 - 528))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(528))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-528)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_49(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -2113/4) | (delta < 2113/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-2113, 4)), StrictLessThan(Symbol('delta'), Rational(2113, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_50(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 575) | (delta < -skoSINS**2 - 575))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(575))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-575)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_51(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -2301/4) | (delta < 2301/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-2301, 4)), StrictLessThan(Symbol('delta'), Rational(2301, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_52(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 624) | (delta < -skoSINS**2 - 624))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(624))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-624)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_53(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -2497/4) | (delta < 2497/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-2497, 4)), StrictLessThan(Symbol('delta'), Rational(2497, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_54(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 675) | (delta < -skoSINS**2 - 675))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(675))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-675)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_55(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -2701/4) | (delta < 2701/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-2701, 4)), StrictLessThan(Symbol('delta'), Rational(2701, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_56(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 728) | (delta < -skoSINS**2 - 728))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(728))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-728)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_57(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -2913/4) | (delta < 2913/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-2913, 4)), StrictLessThan(Symbol('delta'), Rational(2913, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_58(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 783) | (delta < -skoSINS**2 - 783))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(783))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-783)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_59(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -3133/4) | (delta < 3133/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-3133, 4)), StrictLessThan(Symbol('delta'), Rational(3133, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_60(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 840) | (delta < -skoSINS**2 - 840))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(840))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-840)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_61(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -3361/4) | (delta < 3361/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-3361, 4)), StrictLessThan(Symbol('delta'), Rational(3361, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_62(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 899) | (delta < -skoSINS**2 - 899))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(899))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-899)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_63(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -3597/4) | (delta < 3597/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-3597, 4)), StrictLessThan(Symbol('delta'), Rational(3597, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_64(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 960) | (delta < -skoSINS**2 - 960))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(960))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-960)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_65(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -3841/4) | (delta < 3841/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-3841, 4)), StrictLessThan(Symbol('delta'), Rational(3841, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_66(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 1023) | (delta < -skoSINS**2 - 1023))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(1023))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-1023)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_67(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -4093/4) | (delta < 4093/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-4093, 4)), StrictLessThan(Symbol('delta'), Rational(4093, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_68(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 1088) | (delta < -skoSINS**2 - 1088))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(1088))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-1088)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_69(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -4353/4) | (delta < 4353/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-4353, 4)), StrictLessThan(Symbol('delta'), Rational(4353, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_70(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 1155) | (delta < -skoSINS**2 - 1155))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(1155))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-1155)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_71(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -4621/4) | (delta < 4621/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-4621, 4)), StrictLessThan(Symbol('delta'), Rational(4621, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_72(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 1224) | (delta < -skoSINS**2 - 1224))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(1224))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-1224)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_73(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -4897/4) | (delta < 4897/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-4897, 4)), StrictLessThan(Symbol('delta'), Rational(4897, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_74(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 1295) | (delta < -skoSINS**2 - 1295))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(1295))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-1295)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_75(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -5181/4) | (delta < 5181/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-5181, 4)), StrictLessThan(Symbol('delta'), Rational(5181, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_76(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 1368) | (delta < -skoSINS**2 - 1368))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(1368))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-1368)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_77(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -5473/4) | (delta < 5473/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-5473, 4)), StrictLessThan(Symbol('delta'), Rational(5473, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_78(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 1443) | (delta < -skoSINS**2 - 1443))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(1443))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-1443)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_79(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -5773/4) | (delta < 5773/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-5773, 4)), StrictLessThan(Symbol('delta'), Rational(5773, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_80(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 1520) | (delta < -skoSINS**2 - 1520))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(1520))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-1520)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_81(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -6081/4) | (delta < 6081/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-6081, 4)), StrictLessThan(Symbol('delta'), Rational(6081, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_82(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 1599) | (delta < -skoSINS**2 - 1599))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(1599))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-1599)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_83(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -6397/4) | (delta < 6397/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-6397, 4)), StrictLessThan(Symbol('delta'), Rational(6397, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_84(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 1680) | (delta < -skoSINS**2 - 1680))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(1680))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-1680)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_85(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -6721/4) | (delta < 6721/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-6721, 4)), StrictLessThan(Symbol('delta'), Rational(6721, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_86(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 1763) | (delta < -skoSINS**2 - 1763))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(1763))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-1763)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_87(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -7053/4) | (delta < 7053/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-7053, 4)), StrictLessThan(Symbol('delta'), Rational(7053, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_88(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 1848) | (delta < -skoSINS**2 - 1848))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(1848))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-1848)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_89(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -7393/4) | (delta < 7393/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-7393, 4)), StrictLessThan(Symbol('delta'), Rational(7393, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_90(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 1935) | (delta < -skoSINS**2 - 1935))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(1935))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-1935)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_91(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -7741/4) | (delta < 7741/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-7741, 4)), StrictLessThan(Symbol('delta'), Rational(7741, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_92(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 2024) | (delta < -skoSINS**2 - 2024))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(2024))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-2024)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_93(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -8097/4) | (delta < 8097/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-8097, 4)), StrictLessThan(Symbol('delta'), Rational(8097, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_94(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 2115) | (delta < -skoSINS**2 - 2115))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(2115))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-2115)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_95(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -8461/4) | (delta < 8461/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-8461, 4)), StrictLessThan(Symbol('delta'), Rational(8461, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_96(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 2208) | (delta < -skoSINS**2 - 2208))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(2208))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-2208)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_97(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -8833/4) | (delta < 8833/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-8833, 4)), StrictLessThan(Symbol('delta'), Rational(8833, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_98(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 2303) | (delta < -skoSINS**2 - 2303))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(2303))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-2303)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_99(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -9213/4) | (delta < 9213/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-9213, 4)), StrictLessThan(Symbol('delta'), Rational(9213, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_100(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 2400) | (delta < -skoSINS**2 - 2400))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(2400))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-2400)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_101(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -9601/4) | (delta < 9601/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-9601, 4)), StrictLessThan(Symbol('delta'), Rational(9601, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_102(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 2499) | (delta < -skoSINS**2 - 2499))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(2499))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-2499)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_103(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -9997/4) | (delta < 9997/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-9997, 4)), StrictLessThan(Symbol('delta'), Rational(9997, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_104(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 2600) | (delta < -skoSINS**2 - 2600))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(2600))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-2600)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_105(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -10401/4) | (delta < 10401/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-10401, 4)), StrictLessThan(Symbol('delta'), Rational(10401, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_106(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 2703) | (delta < -skoSINS**2 - 2703))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(2703))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-2703)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_107(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -10813/4) | (delta < 10813/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-10813, 4)), StrictLessThan(Symbol('delta'), Rational(10813, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_108(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 2808) | (delta < -skoSINS**2 - 2808))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(2808))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-2808)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_109(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -11233/4) | (delta < 11233/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-11233, 4)), StrictLessThan(Symbol('delta'), Rational(11233, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_110(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 2915) | (delta < -skoSINS**2 - 2915))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(2915))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-2915)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_111(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -11661/4) | (delta < 11661/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-11661, 4)), StrictLessThan(Symbol('delta'), Rational(11661, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_112(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 3024) | (delta < -skoSINS**2 - 3024))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(3024))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-3024)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_113(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -12097/4) | (delta < 12097/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-12097, 4)), StrictLessThan(Symbol('delta'), Rational(12097, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_114(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 3135) | (delta < -skoSINS**2 - 3135))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(3135))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-3135)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_115(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -12541/4) | (delta < 12541/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-12541, 4)), StrictLessThan(Symbol('delta'), Rational(12541, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_116(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 3248) | (delta < -skoSINS**2 - 3248))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(3248))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-3248)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_117(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -12993/4) | (delta < 12993/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-12993, 4)), StrictLessThan(Symbol('delta'), Rational(12993, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_118(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 3363) | (delta < -skoSINS**2 - 3363))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(3363))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-3363)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_119(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -13453/4) | (delta < 13453/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-13453, 4)), StrictLessThan(Symbol('delta'), Rational(13453, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_120(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 3480) | (delta < -skoSINS**2 - 3480))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(3480))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-3480)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_121(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -13921/4) | (delta < 13921/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-13921, 4)), StrictLessThan(Symbol('delta'), Rational(13921, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_122(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 3599) | (delta < -skoSINS**2 - 3599))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(3599))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-3599)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_123(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -14397/4) | (delta < 14397/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-14397, 4)), StrictLessThan(Symbol('delta'), Rational(14397, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_124(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 3720) | (delta < -skoSINS**2 - 3720))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(3720))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-3720)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_125(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -14881/4) | (delta < 14881/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-14881, 4)), StrictLessThan(Symbol('delta'), Rational(14881, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_126(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 3843) | (delta < -skoSINS**2 - 3843))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(3843))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-3843)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_127(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -15373/4) | (delta < 15373/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-15373, 4)), StrictLessThan(Symbol('delta'), Rational(15373, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_128(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 3968) | (delta < -skoSINS**2 - 3968))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(3968))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-3968)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_129(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -15873/4) | (delta < 15873/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-15873, 4)), StrictLessThan(Symbol('delta'), Rational(15873, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_130(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 4095) | (delta < -skoSINS**2 - 4095))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(4095))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-4095)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_131(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -16381/4) | (delta < 16381/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-16381, 4)), StrictLessThan(Symbol('delta'), Rational(16381, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_132(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 4224) | (delta < -skoSINS**2 - 4224))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(4224))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-4224)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_133(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -16897/4) | (delta < 16897/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-16897, 4)), StrictLessThan(Symbol('delta'), Rational(16897, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_134(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 4355) | (delta < -skoSINS**2 - 4355))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(4355))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-4355)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_135(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -17421/4) | (delta < 17421/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-17421, 4)), StrictLessThan(Symbol('delta'), Rational(17421, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_136(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 4488) | (delta < -skoSINS**2 - 4488))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(4488))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-4488)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_137(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -17953/4) | (delta < 17953/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-17953, 4)), StrictLessThan(Symbol('delta'), Rational(17953, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_138(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 4623) | (delta < -skoSINS**2 - 4623))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(4623))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-4623)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_139(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -18493/4) | (delta < 18493/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-18493, 4)), StrictLessThan(Symbol('delta'), Rational(18493, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_140(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 4760) | (delta < -skoSINS**2 - 4760))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(4760))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-4760)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_141(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -19041/4) | (delta < 19041/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-19041, 4)), StrictLessThan(Symbol('delta'), Rational(19041, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_142(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 4899) | (delta < -skoSINS**2 - 4899))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(4899))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-4899)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_143(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -19597/4) | (delta < 19597/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-19597, 4)), StrictLessThan(Symbol('delta'), Rational(19597, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_144(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 5040) | (delta < -skoSINS**2 - 5040))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(5040))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-5040)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_145(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -20161/4) | (delta < 20161/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-20161, 4)), StrictLessThan(Symbol('delta'), Rational(20161, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_146(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 5183) | (delta < -skoSINS**2 - 5183))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(5183))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-5183)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_147(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -20733/4) | (delta < 20733/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-20733, 4)), StrictLessThan(Symbol('delta'), Rational(20733, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_148(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 5328) | (delta < -skoSINS**2 - 5328))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(5328))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-5328)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_149(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -21313/4) | (delta < 21313/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-21313, 4)), StrictLessThan(Symbol('delta'), Rational(21313, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_150(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 5475) | (delta < -skoSINS**2 - 5475))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(5475))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-5475)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_151(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -21901/4) | (delta < 21901/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-21901, 4)), StrictLessThan(Symbol('delta'), Rational(21901, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_152(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 5624) | (delta < -skoSINS**2 - 5624))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(5624))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-5624)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_153(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -22497/4) | (delta < 22497/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-22497, 4)), StrictLessThan(Symbol('delta'), Rational(22497, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_154(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 5775) | (delta < -skoSINS**2 - 5775))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(5775))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-5775)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_155(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -23101/4) | (delta < 23101/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-23101, 4)), StrictLessThan(Symbol('delta'), Rational(23101, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_156(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 5928) | (delta < -skoSINS**2 - 5928))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(5928))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-5928)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_157(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -23713/4) | (delta < 23713/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-23713, 4)), StrictLessThan(Symbol('delta'), Rational(23713, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_158(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 6083) | (delta < -skoSINS**2 - 6083))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(6083))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-6083)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_159(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -24333/4) | (delta < 24333/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-24333, 4)), StrictLessThan(Symbol('delta'), Rational(24333, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_160(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 6240) | (delta < -skoSINS**2 - 6240))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(6240))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-6240)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_161(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -24961/4) | (delta < 24961/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-24961, 4)), StrictLessThan(Symbol('delta'), Rational(24961, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_162(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 6399) | (delta < -skoSINS**2 - 6399))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(6399))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-6399)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_163(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -25597/4) | (delta < 25597/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-25597, 4)), StrictLessThan(Symbol('delta'), Rational(25597, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_164(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 6560) | (delta < -skoSINS**2 - 6560))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(6560))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-6560)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_165(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -26241/4) | (delta < 26241/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-26241, 4)), StrictLessThan(Symbol('delta'), Rational(26241, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_166(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 6723) | (delta < -skoSINS**2 - 6723))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(6723))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-6723)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_167(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -26893/4) | (delta < 26893/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-26893, 4)), StrictLessThan(Symbol('delta'), Rational(26893, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_168(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 6888) | (delta < -skoSINS**2 - 6888))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(6888))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-6888)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_169(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -27553/4) | (delta < 27553/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-27553, 4)), StrictLessThan(Symbol('delta'), Rational(27553, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_170(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 7055) | (delta < -skoSINS**2 - 7055))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(7055))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-7055)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_171(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -28221/4) | (delta < 28221/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-28221, 4)), StrictLessThan(Symbol('delta'), Rational(28221, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_172(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 7224) | (delta < -skoSINS**2 - 7224))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(7224))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-7224)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_173(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -28897/4) | (delta < 28897/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-28897, 4)), StrictLessThan(Symbol('delta'), Rational(28897, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_174(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 7395) | (delta < -skoSINS**2 - 7395))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(7395))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-7395)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_175(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -29581/4) | (delta < 29581/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-29581, 4)), StrictLessThan(Symbol('delta'), Rational(29581, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_176(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 7568) | (delta < -skoSINS**2 - 7568))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(7568))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-7568)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_177(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -30273/4) | (delta < 30273/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-30273, 4)), StrictLessThan(Symbol('delta'), Rational(30273, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_178(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 7743) | (delta < -skoSINS**2 - 7743))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(7743))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-7743)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_179(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -30973/4) | (delta < 30973/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-30973, 4)), StrictLessThan(Symbol('delta'), Rational(30973, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_180(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 7920) | (delta < -skoSINS**2 - 7920))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(7920))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-7920)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_181(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -31681/4) | (delta < 31681/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-31681, 4)), StrictLessThan(Symbol('delta'), Rational(31681, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_182(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 8099) | (delta < -skoSINS**2 - 8099))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(8099))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-8099)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_183(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -32397/4) | (delta < 32397/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-32397, 4)), StrictLessThan(Symbol('delta'), Rational(32397, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_184(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 8280) | (delta < -skoSINS**2 - 8280))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(8280))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-8280)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_185(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -33121/4) | (delta < 33121/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-33121, 4)), StrictLessThan(Symbol('delta'), Rational(33121, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_186(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 8463) | (delta < -skoSINS**2 - 8463))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(8463))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-8463)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_187(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -33853/4) | (delta < 33853/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-33853, 4)), StrictLessThan(Symbol('delta'), Rational(33853, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_188(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 8648) | (delta < -skoSINS**2 - 8648))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(8648))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-8648)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_189(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -34593/4) | (delta < 34593/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-34593, 4)), StrictLessThan(Symbol('delta'), Rational(34593, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_190(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 8835) | (delta < -skoSINS**2 - 8835))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(8835))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-8835)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_191(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -35341/4) | (delta < 35341/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-35341, 4)), StrictLessThan(Symbol('delta'), Rational(35341, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_192(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 9024) | (delta < -skoSINS**2 - 9024))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(9024))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-9024)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_193(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -36097/4) | (delta < 36097/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-36097, 4)), StrictLessThan(Symbol('delta'), Rational(36097, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_194(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 9215) | (delta < -skoSINS**2 - 9215))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(9215))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-9215)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_195(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -36861/4) | (delta < 36861/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-36861, 4)), StrictLessThan(Symbol('delta'), Rational(36861, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_196(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 9408) | (delta < -skoSINS**2 - 9408))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(9408))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-9408)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_197(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -37633/4) | (delta < 37633/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-37633, 4)), StrictLessThan(Symbol('delta'), Rational(37633, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_198(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 9603) | (delta < -skoSINS**2 - 9603))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(9603))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-9603)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_199(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -38413/4) | (delta < 38413/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-38413, 4)), StrictLessThan(Symbol('delta'), Rational(38413, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_200(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 9800) | (delta < -skoSINS**2 - 9800))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(9800))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-9800)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_201(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -39201/4) | (delta < 39201/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-39201, 4)), StrictLessThan(Symbol('delta'), Rational(39201, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_202(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 9999) | (delta < -skoSINS**2 - 9999))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(9999))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-9999)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_203(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -39997/4) | (delta < 39997/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-39997, 4)), StrictLessThan(Symbol('delta'), Rational(39997, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_204(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 10200) | (delta < -skoSINS**2 - 10200))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(10200))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-10200)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_205(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -40801/4) | (delta < 40801/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-40801, 4)), StrictLessThan(Symbol('delta'), Rational(40801, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_206(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 10403) | (delta < -skoSINS**2 - 10403))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(10403))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-10403)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_207(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -41613/4) | (delta < 41613/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-41613, 4)), StrictLessThan(Symbol('delta'), Rational(41613, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_208(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 10608) | (delta < -skoSINS**2 - 10608))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(10608))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-10608)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_209(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -42433/4) | (delta < 42433/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-42433, 4)), StrictLessThan(Symbol('delta'), Rational(42433, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_210(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 10815) | (delta < -skoSINS**2 - 10815))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(10815))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-10815)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_211(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -43261/4) | (delta < 43261/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-43261, 4)), StrictLessThan(Symbol('delta'), Rational(43261, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_212(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 11024) | (delta < -skoSINS**2 - 11024))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(11024))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-11024)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_213(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -44097/4) | (delta < 44097/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-44097, 4)), StrictLessThan(Symbol('delta'), Rational(44097, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_214(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 11235) | (delta < -skoSINS**2 - 11235))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(11235))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-11235)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_215(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -44941/4) | (delta < 44941/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-44941, 4)), StrictLessThan(Symbol('delta'), Rational(44941, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_216(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 11448) | (delta < -skoSINS**2 - 11448))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(11448))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-11448)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_217(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -45793/4) | (delta < 45793/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-45793, 4)), StrictLessThan(Symbol('delta'), Rational(45793, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_218(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 11663) | (delta < -skoSINS**2 - 11663))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(11663))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-11663)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_219(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -46653/4) | (delta < 46653/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-46653, 4)), StrictLessThan(Symbol('delta'), Rational(46653, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_220(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 11880) | (delta < -skoSINS**2 - 11880))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(11880))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-11880)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_221(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -47521/4) | (delta < 47521/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-47521, 4)), StrictLessThan(Symbol('delta'), Rational(47521, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_222(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 12099) | (delta < -skoSINS**2 - 12099))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(12099))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-12099)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_223(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -48397/4) | (delta < 48397/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-48397, 4)), StrictLessThan(Symbol('delta'), Rational(48397, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_224(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 12320) | (delta < -skoSINS**2 - 12320))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(12320))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-12320)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_225(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -49281/4) | (delta < 49281/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-49281, 4)), StrictLessThan(Symbol('delta'), Rational(49281, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_226(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 12543) | (delta < -skoSINS**2 - 12543))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(12543))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-12543)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_227(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -50173/4) | (delta < 50173/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-50173, 4)), StrictLessThan(Symbol('delta'), Rational(50173, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_228(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 12768) | (delta < -skoSINS**2 - 12768))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(12768))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-12768)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_229(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -51073/4) | (delta < 51073/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-51073, 4)), StrictLessThan(Symbol('delta'), Rational(51073, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_230(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 12995) | (delta < -skoSINS**2 - 12995))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(12995))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-12995)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_231(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -51981/4) | (delta < 51981/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-51981, 4)), StrictLessThan(Symbol('delta'), Rational(51981, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_232(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 13224) | (delta < -skoSINS**2 - 13224))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(13224))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-13224)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_233(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -52897/4) | (delta < 52897/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-52897, 4)), StrictLessThan(Symbol('delta'), Rational(52897, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_234(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 13455) | (delta < -skoSINS**2 - 13455))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(13455))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-13455)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_235(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -53821/4) | (delta < 53821/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-53821, 4)), StrictLessThan(Symbol('delta'), Rational(53821, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_236(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 13688) | (delta < -skoSINS**2 - 13688))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(13688))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-13688)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_237(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -54753/4) | (delta < 54753/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-54753, 4)), StrictLessThan(Symbol('delta'), Rational(54753, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_238(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 13923) | (delta < -skoSINS**2 - 13923))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(13923))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-13923)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_239(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -55693/4) | (delta < 55693/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-55693, 4)), StrictLessThan(Symbol('delta'), Rational(55693, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_240(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 14160) | (delta < -skoSINS**2 - 14160))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(14160))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-14160)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_241(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -56641/4) | (delta < 56641/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-56641, 4)), StrictLessThan(Symbol('delta'), Rational(56641, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_242(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 14399) | (delta < -skoSINS**2 - 14399))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(14399))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-14399)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_243(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -57597/4) | (delta < 57597/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-57597, 4)), StrictLessThan(Symbol('delta'), Rational(57597, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_244(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 14640) | (delta < -skoSINS**2 - 14640))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(14640))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-14640)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_245(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -58561/4) | (delta < 58561/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-58561, 4)), StrictLessThan(Symbol('delta'), Rational(58561, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_246(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 14883) | (delta < -skoSINS**2 - 14883))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(14883))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-14883)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_247(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -59533/4) | (delta < 59533/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-59533, 4)), StrictLessThan(Symbol('delta'), Rational(59533, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_248(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 15128) | (delta < -skoSINS**2 - 15128))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(15128))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-15128)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_249(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -60513/4) | (delta < 60513/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-60513, 4)), StrictLessThan(Symbol('delta'), Rational(60513, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_250(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 15375) | (delta < -skoSINS**2 - 15375))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(15375))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-15375)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_251(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -61501/4) | (delta < 61501/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-61501, 4)), StrictLessThan(Symbol('delta'), Rational(61501, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_252(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 15624) | (delta < -skoSINS**2 - 15624))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(15624))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-15624)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_253(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -62497/4) | (delta < 62497/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-62497, 4)), StrictLessThan(Symbol('delta'), Rational(62497, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_254(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 15875) | (delta < -skoSINS**2 - 15875))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(15875))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-15875)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_255(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -63501/4) | (delta < 63501/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-63501, 4)), StrictLessThan(Symbol('delta'), Rational(63501, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_256(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 16128) | (delta < -skoSINS**2 - 16128))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(16128))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-16128)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_257(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -64513/4) | (delta < 64513/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-64513, 4)), StrictLessThan(Symbol('delta'), Rational(64513, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_258(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 16383) | (delta < -skoSINS**2 - 16383))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(16383))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-16383)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_259(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -65533/4) | (delta < 65533/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-65533, 4)), StrictLessThan(Symbol('delta'), Rational(65533, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_260(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 16640) | (delta < -skoSINS**2 - 16640))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(16640))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-16640)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_261(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -66561/4) | (delta < 66561/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-66561, 4)), StrictLessThan(Symbol('delta'), Rational(66561, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_262(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 16899) | (delta < -skoSINS**2 - 16899))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(16899))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-16899)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_263(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -67597/4) | (delta < 67597/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-67597, 4)), StrictLessThan(Symbol('delta'), Rational(67597, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_264(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 17160) | (delta < -skoSINS**2 - 17160))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(17160))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-17160)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_265(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -68641/4) | (delta < 68641/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-68641, 4)), StrictLessThan(Symbol('delta'), Rational(68641, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_266(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 17423) | (delta < -skoSINS**2 - 17423))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(17423))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-17423)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_267(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -69693/4) | (delta < 69693/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-69693, 4)), StrictLessThan(Symbol('delta'), Rational(69693, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_268(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 17688) | (delta < -skoSINS**2 - 17688))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(17688))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-17688)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_269(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -70753/4) | (delta < 70753/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-70753, 4)), StrictLessThan(Symbol('delta'), Rational(70753, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_270(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 17955) | (delta < -skoSINS**2 - 17955))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(17955))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-17955)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_271(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -71821/4) | (delta < 71821/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-71821, 4)), StrictLessThan(Symbol('delta'), Rational(71821, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_272(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 18224) | (delta < -skoSINS**2 - 18224))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(18224))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-18224)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_273(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -72897/4) | (delta < 72897/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-72897, 4)), StrictLessThan(Symbol('delta'), Rational(72897, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_274(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 18495) | (delta < -skoSINS**2 - 18495))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(18495))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-18495)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_275(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -73981/4) | (delta < 73981/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-73981, 4)), StrictLessThan(Symbol('delta'), Rational(73981, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_276(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 18768) | (delta < -skoSINS**2 - 18768))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(18768))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-18768)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_277(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -75073/4) | (delta < 75073/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-75073, 4)), StrictLessThan(Symbol('delta'), Rational(75073, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_278(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 19043) | (delta < -skoSINS**2 - 19043))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(19043))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-19043)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_279(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -76173/4) | (delta < 76173/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-76173, 4)), StrictLessThan(Symbol('delta'), Rational(76173, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_280(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 19320) | (delta < -skoSINS**2 - 19320))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(19320))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-19320)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_281(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -77281/4) | (delta < 77281/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-77281, 4)), StrictLessThan(Symbol('delta'), Rational(77281, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_282(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 19599) | (delta < -skoSINS**2 - 19599))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(19599))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-19599)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_283(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -78397/4) | (delta < 78397/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-78397, 4)), StrictLessThan(Symbol('delta'), Rational(78397, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_284(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 19880) | (delta < -skoSINS**2 - 19880))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(19880))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-19880)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_285(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -79521/4) | (delta < 79521/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-79521, 4)), StrictLessThan(Symbol('delta'), Rational(79521, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_286(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 20163) | (delta < -skoSINS**2 - 20163))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(20163))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-20163)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_287(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -80653/4) | (delta < 80653/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-80653, 4)), StrictLessThan(Symbol('delta'), Rational(80653, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_288(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 20448) | (delta < -skoSINS**2 - 20448))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(20448))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-20448)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_289(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -81793/4) | (delta < 81793/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-81793, 4)), StrictLessThan(Symbol('delta'), Rational(81793, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_290(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 20735) | (delta < -skoSINS**2 - 20735))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(20735))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-20735)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_291(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -82941/4) | (delta < 82941/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-82941, 4)), StrictLessThan(Symbol('delta'), Rational(82941, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_292(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 21024) | (delta < -skoSINS**2 - 21024))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(21024))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-21024)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_293(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -84097/4) | (delta < 84097/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-84097, 4)), StrictLessThan(Symbol('delta'), Rational(84097, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_294(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 21315) | (delta < -skoSINS**2 - 21315))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(21315))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-21315)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_295(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -85261/4) | (delta < 85261/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-85261, 4)), StrictLessThan(Symbol('delta'), Rational(85261, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_296(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 21608) | (delta < -skoSINS**2 - 21608))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(21608))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-21608)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_297(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -86433/4) | (delta < 86433/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-86433, 4)), StrictLessThan(Symbol('delta'), Rational(86433, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_298(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 21903) | (delta < -skoSINS**2 - 21903))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(21903))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-21903)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_299(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -87613/4) | (delta < 87613/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-87613, 4)), StrictLessThan(Symbol('delta'), Rational(87613, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_300(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 22200) | (delta < -skoSINS**2 - 22200))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(22200))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-22200)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_301(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -88801/4) | (delta < 88801/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-88801, 4)), StrictLessThan(Symbol('delta'), Rational(88801, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_302(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 22499) | (delta < -skoSINS**2 - 22499))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(22499))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-22499)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_303(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -89997/4) | (delta < 89997/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-89997, 4)), StrictLessThan(Symbol('delta'), Rational(89997, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_304(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 22800) | (delta < -skoSINS**2 - 22800))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(22800))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-22800)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_305(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -91201/4) | (delta < 91201/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-91201, 4)), StrictLessThan(Symbol('delta'), Rational(91201, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_306(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 23103) | (delta < -skoSINS**2 - 23103))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(23103))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-23103)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_307(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -92413/4) | (delta < 92413/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-92413, 4)), StrictLessThan(Symbol('delta'), Rational(92413, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_308(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 23408) | (delta < -skoSINS**2 - 23408))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(23408))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-23408)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_309(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -93633/4) | (delta < 93633/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-93633, 4)), StrictLessThan(Symbol('delta'), Rational(93633, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_310(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 23715) | (delta < -skoSINS**2 - 23715))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(23715))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-23715)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_311(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -94861/4) | (delta < 94861/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-94861, 4)), StrictLessThan(Symbol('delta'), Rational(94861, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_312(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 24024) | (delta < -skoSINS**2 - 24024))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(24024))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-24024)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_313(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -96097/4) | (delta < 96097/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-96097, 4)), StrictLessThan(Symbol('delta'), Rational(96097, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_314(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 24335) | (delta < -skoSINS**2 - 24335))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(24335))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-24335)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_315(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -97341/4) | (delta < 97341/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-97341, 4)), StrictLessThan(Symbol('delta'), Rational(97341, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_316(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 24648) | (delta < -skoSINS**2 - 24648))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(24648))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-24648)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_317(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -98593/4) | (delta < 98593/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-98593, 4)), StrictLessThan(Symbol('delta'), Rational(98593, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_318(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 24963) | (delta < -skoSINS**2 - 24963))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(24963))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-24963)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_319(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -99853/4) | (delta < 99853/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-99853, 4)), StrictLessThan(Symbol('delta'), Rational(99853, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_320(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 25280) | (delta < -skoSINS**2 - 25280))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(25280))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-25280)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_321(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -101121/4) | (delta < 101121/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-101121, 4)), StrictLessThan(Symbol('delta'), Rational(101121, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_322(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 25599) | (delta < -skoSINS**2 - 25599))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(25599))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-25599)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_323(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -102397/4) | (delta < 102397/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-102397, 4)), StrictLessThan(Symbol('delta'), Rational(102397, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_324(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 25920) | (delta < -skoSINS**2 - 25920))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(25920))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-25920)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_325(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -103681/4) | (delta < 103681/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-103681, 4)), StrictLessThan(Symbol('delta'), Rational(103681, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_326(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 26243) | (delta < -skoSINS**2 - 26243))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(26243))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-26243)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_327(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -104973/4) | (delta < 104973/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-104973, 4)), StrictLessThan(Symbol('delta'), Rational(104973, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_328(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 26568) | (delta < -skoSINS**2 - 26568))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(26568))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-26568)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_329(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -106273/4) | (delta < 106273/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-106273, 4)), StrictLessThan(Symbol('delta'), Rational(106273, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_330(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 26895) | (delta < -skoSINS**2 - 26895))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(26895))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-26895)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_331(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -107581/4) | (delta < 107581/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-107581, 4)), StrictLessThan(Symbol('delta'), Rational(107581, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_332(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 27224) | (delta < -skoSINS**2 - 27224))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(27224))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-27224)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_333(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -108897/4) | (delta < 108897/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-108897, 4)), StrictLessThan(Symbol('delta'), Rational(108897, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_334(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 27555) | (delta < -skoSINS**2 - 27555))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(27555))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-27555)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_335(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -110221/4) | (delta < 110221/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-110221, 4)), StrictLessThan(Symbol('delta'), Rational(110221, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_336(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 27888) | (delta < -skoSINS**2 - 27888))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(27888))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-27888)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_337(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -111553/4) | (delta < 111553/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-111553, 4)), StrictLessThan(Symbol('delta'), Rational(111553, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_338(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 28223) | (delta < -skoSINS**2 - 28223))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(28223))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-28223)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_339(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -112893/4) | (delta < 112893/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-112893, 4)), StrictLessThan(Symbol('delta'), Rational(112893, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_340(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 28560) | (delta < -skoSINS**2 - 28560))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(28560))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-28560)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_341(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -114241/4) | (delta < 114241/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-114241, 4)), StrictLessThan(Symbol('delta'), Rational(114241, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_342(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 28899) | (delta < -skoSINS**2 - 28899))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(28899))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-28899)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_343(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -115597/4) | (delta < 115597/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-115597, 4)), StrictLessThan(Symbol('delta'), Rational(115597, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_344(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 29240) | (delta < -skoSINS**2 - 29240))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(29240))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-29240)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_345(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -116961/4) | (delta < 116961/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-116961, 4)), StrictLessThan(Symbol('delta'), Rational(116961, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_346(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 29583) | (delta < -skoSINS**2 - 29583))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(29583))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-29583)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_347(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -118333/4) | (delta < 118333/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-118333, 4)), StrictLessThan(Symbol('delta'), Rational(118333, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_348(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 29928) | (delta < -skoSINS**2 - 29928))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(29928))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-29928)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_349(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -119713/4) | (delta < 119713/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-119713, 4)), StrictLessThan(Symbol('delta'), Rational(119713, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_350(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 30275) | (delta < -skoSINS**2 - 30275))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(30275))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-30275)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_351(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -121101/4) | (delta < 121101/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-121101, 4)), StrictLessThan(Symbol('delta'), Rational(121101, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_352(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 30624) | (delta < -skoSINS**2 - 30624))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(30624))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-30624)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_353(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -122497/4) | (delta < 122497/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-122497, 4)), StrictLessThan(Symbol('delta'), Rational(122497, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_354(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 30975) | (delta < -skoSINS**2 - 30975))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(30975))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-30975)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_355(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -123901/4) | (delta < 123901/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-123901, 4)), StrictLessThan(Symbol('delta'), Rational(123901, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_356(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 31328) | (delta < -skoSINS**2 - 31328))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(31328))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-31328)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_357(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -125313/4) | (delta < 125313/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-125313, 4)), StrictLessThan(Symbol('delta'), Rational(125313, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_358(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 31683) | (delta < -skoSINS**2 - 31683))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(31683))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-31683)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_359(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -126733/4) | (delta < 126733/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-126733, 4)), StrictLessThan(Symbol('delta'), Rational(126733, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_360(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 32040) | (delta < -skoSINS**2 - 32040))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(32040))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-32040)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_361(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -128161/4) | (delta < 128161/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-128161, 4)), StrictLessThan(Symbol('delta'), Rational(128161, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_362(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 32399) | (delta < -skoSINS**2 - 32399))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(32399))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-32399)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_363(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -129597/4) | (delta < 129597/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-129597, 4)), StrictLessThan(Symbol('delta'), Rational(129597, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_364(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 32760) | (delta < -skoSINS**2 - 32760))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(32760))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-32760)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_365(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -131041/4) | (delta < 131041/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-131041, 4)), StrictLessThan(Symbol('delta'), Rational(131041, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_366(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 33123) | (delta < -skoSINS**2 - 33123))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(33123))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-33123)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_367(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -132493/4) | (delta < 132493/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-132493, 4)), StrictLessThan(Symbol('delta'), Rational(132493, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_368(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 33488) | (delta < -skoSINS**2 - 33488))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(33488))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-33488)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_369(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -133953/4) | (delta < 133953/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-133953, 4)), StrictLessThan(Symbol('delta'), Rational(133953, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_370(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 33855) | (delta < -skoSINS**2 - 33855))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(33855))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-33855)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_371(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -135421/4) | (delta < 135421/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-135421, 4)), StrictLessThan(Symbol('delta'), Rational(135421, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_372(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 34224) | (delta < -skoSINS**2 - 34224))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(34224))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-34224)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_373(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -136897/4) | (delta < 136897/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-136897, 4)), StrictLessThan(Symbol('delta'), Rational(136897, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_374(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 34595) | (delta < -skoSINS**2 - 34595))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(34595))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-34595)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_375(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -138381/4) | (delta < 138381/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-138381, 4)), StrictLessThan(Symbol('delta'), Rational(138381, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_376(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 34968) | (delta < -skoSINS**2 - 34968))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(34968))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-34968)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_377(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -139873/4) | (delta < 139873/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-139873, 4)), StrictLessThan(Symbol('delta'), Rational(139873, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_378(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 35343) | (delta < -skoSINS**2 - 35343))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(35343))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-35343)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_379(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -141373/4) | (delta < 141373/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-141373, 4)), StrictLessThan(Symbol('delta'), Rational(141373, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_380(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 35720) | (delta < -skoSINS**2 - 35720))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(35720))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-35720)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_381(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -142881/4) | (delta < 142881/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-142881, 4)), StrictLessThan(Symbol('delta'), Rational(142881, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_382(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 36099) | (delta < -skoSINS**2 - 36099))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(36099))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-36099)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_383(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -144397/4) | (delta < 144397/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-144397, 4)), StrictLessThan(Symbol('delta'), Rational(144397, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_384(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 36480) | (delta < -skoSINS**2 - 36480))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(36480))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-36480)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_385(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -145921/4) | (delta < 145921/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-145921, 4)), StrictLessThan(Symbol('delta'), Rational(145921, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_386(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 36863) | (delta < -skoSINS**2 - 36863))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(36863))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-36863)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_387(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -147453/4) | (delta < 147453/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-147453, 4)), StrictLessThan(Symbol('delta'), Rational(147453, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_388(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 37248) | (delta < -skoSINS**2 - 37248))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(37248))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-37248)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_389(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -148993/4) | (delta < 148993/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-148993, 4)), StrictLessThan(Symbol('delta'), Rational(148993, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_390(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 37635) | (delta < -skoSINS**2 - 37635))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(37635))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-37635)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_391(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -150541/4) | (delta < 150541/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-150541, 4)), StrictLessThan(Symbol('delta'), Rational(150541, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_392(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 38024) | (delta < -skoSINS**2 - 38024))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(38024))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-38024)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_393(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -152097/4) | (delta < 152097/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-152097, 4)), StrictLessThan(Symbol('delta'), Rational(152097, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_394(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 38415) | (delta < -skoSINS**2 - 38415))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(38415))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-38415)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_395(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -153661/4) | (delta < 153661/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-153661, 4)), StrictLessThan(Symbol('delta'), Rational(153661, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_396(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 38808) | (delta < -skoSINS**2 - 38808))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(38808))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-38808)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_397(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -155233/4) | (delta < 155233/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-155233, 4)), StrictLessThan(Symbol('delta'), Rational(155233, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_398(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 39203) | (delta < -skoSINS**2 - 39203))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(39203))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-39203)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_399(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -156813/4) | (delta < 156813/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-156813, 4)), StrictLessThan(Symbol('delta'), Rational(156813, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_400(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 39600) | (delta < -skoSINS**2 - 39600))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(39600))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-39600)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_401(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -158401/4) | (delta < 158401/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-158401, 4)), StrictLessThan(Symbol('delta'), Rational(158401, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_402(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 39999) | (delta < -skoSINS**2 - 39999))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(39999))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-39999)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_403(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -159997/4) | (delta < 159997/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-159997, 4)), StrictLessThan(Symbol('delta'), Rational(159997, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_404(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 40400) | (delta < -skoSINS**2 - 40400))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(40400))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-40400)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_405(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -161601/4) | (delta < 161601/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-161601, 4)), StrictLessThan(Symbol('delta'), Rational(161601, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_406(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 40803) | (delta < -skoSINS**2 - 40803))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(40803))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-40803)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_407(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -163213/4) | (delta < 163213/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-163213, 4)), StrictLessThan(Symbol('delta'), Rational(163213, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_408(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 41208) | (delta < -skoSINS**2 - 41208))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(41208))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-41208)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_409(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -164833/4) | (delta < 164833/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-164833, 4)), StrictLessThan(Symbol('delta'), Rational(164833, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_410(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 41615) | (delta < -skoSINS**2 - 41615))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(41615))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-41615)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_411(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -166461/4) | (delta < 166461/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-166461, 4)), StrictLessThan(Symbol('delta'), Rational(166461, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_412(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 42024) | (delta < -skoSINS**2 - 42024))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(42024))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-42024)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_413(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -168097/4) | (delta < 168097/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-168097, 4)), StrictLessThan(Symbol('delta'), Rational(168097, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_414(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 42435) | (delta < -skoSINS**2 - 42435))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(42435))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-42435)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_415(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -169741/4) | (delta < 169741/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-169741, 4)), StrictLessThan(Symbol('delta'), Rational(169741, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_416(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 42848) | (delta < -skoSINS**2 - 42848))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(42848))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-42848)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_417(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -171393/4) | (delta < 171393/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-171393, 4)), StrictLessThan(Symbol('delta'), Rational(171393, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_418(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 43263) | (delta < -skoSINS**2 - 43263))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(43263))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-43263)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_419(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -173053/4) | (delta < 173053/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-173053, 4)), StrictLessThan(Symbol('delta'), Rational(173053, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_420(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 43680) | (delta < -skoSINS**2 - 43680))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(43680))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-43680)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_421(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -174721/4) | (delta < 174721/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-174721, 4)), StrictLessThan(Symbol('delta'), Rational(174721, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_422(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 44099) | (delta < -skoSINS**2 - 44099))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(44099))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-44099)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_423(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -176397/4) | (delta < 176397/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-176397, 4)), StrictLessThan(Symbol('delta'), Rational(176397, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_424(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 44520) | (delta < -skoSINS**2 - 44520))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(44520))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-44520)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_425(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -178081/4) | (delta < 178081/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-178081, 4)), StrictLessThan(Symbol('delta'), Rational(178081, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_426(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 44943) | (delta < -skoSINS**2 - 44943))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(44943))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-44943)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_427(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -179773/4) | (delta < 179773/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-179773, 4)), StrictLessThan(Symbol('delta'), Rational(179773, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_428(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 45368) | (delta < -skoSINS**2 - 45368))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(45368))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-45368)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_429(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -181473/4) | (delta < 181473/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-181473, 4)), StrictLessThan(Symbol('delta'), Rational(181473, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_430(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 45795) | (delta < -skoSINS**2 - 45795))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(45795))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-45795)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_431(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -183181/4) | (delta < 183181/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-183181, 4)), StrictLessThan(Symbol('delta'), Rational(183181, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_432(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 46224) | (delta < -skoSINS**2 - 46224))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(46224))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-46224)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_433(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -184897/4) | (delta < 184897/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-184897, 4)), StrictLessThan(Symbol('delta'), Rational(184897, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_434(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 46655) | (delta < -skoSINS**2 - 46655))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(46655))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-46655)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_435(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -186621/4) | (delta < 186621/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-186621, 4)), StrictLessThan(Symbol('delta'), Rational(186621, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_436(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 47088) | (delta < -skoSINS**2 - 47088))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(47088))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-47088)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_437(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -188353/4) | (delta < 188353/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-188353, 4)), StrictLessThan(Symbol('delta'), Rational(188353, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_438(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 47523) | (delta < -skoSINS**2 - 47523))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(47523))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-47523)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_439(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -190093/4) | (delta < 190093/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-190093, 4)), StrictLessThan(Symbol('delta'), Rational(190093, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_440(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 47960) | (delta < -skoSINS**2 - 47960))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(47960))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-47960)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_441(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -191841/4) | (delta < 191841/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-191841, 4)), StrictLessThan(Symbol('delta'), Rational(191841, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_442(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 48399) | (delta < -skoSINS**2 - 48399))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(48399))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-48399)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_443(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -193597/4) | (delta < 193597/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-193597, 4)), StrictLessThan(Symbol('delta'), Rational(193597, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_444(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 48840) | (delta < -skoSINS**2 - 48840))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(48840))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-48840)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_445(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -195361/4) | (delta < 195361/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-195361, 4)), StrictLessThan(Symbol('delta'), Rational(195361, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_446(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 49283) | (delta < -skoSINS**2 - 49283))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(49283))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-49283)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_447(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -197133/4) | (delta < 197133/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-197133, 4)), StrictLessThan(Symbol('delta'), Rational(197133, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_448(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 49728) | (delta < -skoSINS**2 - 49728))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(49728))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-49728)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_449(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -198913/4) | (delta < 198913/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-198913, 4)), StrictLessThan(Symbol('delta'), Rational(198913, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_450(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 50175) | (delta < -skoSINS**2 - 50175))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(50175))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-50175)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_451(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -200701/4) | (delta < 200701/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-200701, 4)), StrictLessThan(Symbol('delta'), Rational(200701, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_452(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 50624) | (delta < -skoSINS**2 - 50624))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(50624))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-50624)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_453(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -202497/4) | (delta < 202497/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-202497, 4)), StrictLessThan(Symbol('delta'), Rational(202497, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_454(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 51075) | (delta < -skoSINS**2 - 51075))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(51075))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-51075)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_455(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -204301/4) | (delta < 204301/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-204301, 4)), StrictLessThan(Symbol('delta'), Rational(204301, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_456(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 51528) | (delta < -skoSINS**2 - 51528))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(51528))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-51528)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_457(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -206113/4) | (delta < 206113/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-206113, 4)), StrictLessThan(Symbol('delta'), Rational(206113, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_458(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 51983) | (delta < -skoSINS**2 - 51983))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(51983))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-51983)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_459(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -207933/4) | (delta < 207933/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-207933, 4)), StrictLessThan(Symbol('delta'), Rational(207933, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_460(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 52440) | (delta < -skoSINS**2 - 52440))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(52440))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-52440)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_461(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -209761/4) | (delta < 209761/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-209761, 4)), StrictLessThan(Symbol('delta'), Rational(209761, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_462(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 52899) | (delta < -skoSINS**2 - 52899))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(52899))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-52899)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_463(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -211597/4) | (delta < 211597/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-211597, 4)), StrictLessThan(Symbol('delta'), Rational(211597, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_464(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 53360) | (delta < -skoSINS**2 - 53360))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(53360))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-53360)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_465(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -213441/4) | (delta < 213441/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-213441, 4)), StrictLessThan(Symbol('delta'), Rational(213441, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_466(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 53823) | (delta < -skoSINS**2 - 53823))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(53823))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-53823)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_467(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -215293/4) | (delta < 215293/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-215293, 4)), StrictLessThan(Symbol('delta'), Rational(215293, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_468(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 54288) | (delta < -skoSINS**2 - 54288))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(54288))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-54288)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_469(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -217153/4) | (delta < 217153/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-217153, 4)), StrictLessThan(Symbol('delta'), Rational(217153, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_470(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 54755) | (delta < -skoSINS**2 - 54755))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(54755))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-54755)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_471(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -219021/4) | (delta < 219021/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-219021, 4)), StrictLessThan(Symbol('delta'), Rational(219021, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_472(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 55224) | (delta < -skoSINS**2 - 55224))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(55224))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-55224)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_473(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -220897/4) | (delta < 220897/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-220897, 4)), StrictLessThan(Symbol('delta'), Rational(220897, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_474(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 55695) | (delta < -skoSINS**2 - 55695))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(55695))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-55695)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_475(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -222781/4) | (delta < 222781/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-222781, 4)), StrictLessThan(Symbol('delta'), Rational(222781, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_476(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 56168) | (delta < -skoSINS**2 - 56168))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(56168))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-56168)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_477(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -224673/4) | (delta < 224673/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-224673, 4)), StrictLessThan(Symbol('delta'), Rational(224673, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_478(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 56643) | (delta < -skoSINS**2 - 56643))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(56643))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-56643)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_479(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -226573/4) | (delta < 226573/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-226573, 4)), StrictLessThan(Symbol('delta'), Rational(226573, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_480(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 57120) | (delta < -skoSINS**2 - 57120))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(57120))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-57120)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_481(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -228481/4) | (delta < 228481/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-228481, 4)), StrictLessThan(Symbol('delta'), Rational(228481, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_482(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 57599) | (delta < -skoSINS**2 - 57599))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(57599))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-57599)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_483(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -230397/4) | (delta < 230397/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-230397, 4)), StrictLessThan(Symbol('delta'), Rational(230397, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_484(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 58080) | (delta < -skoSINS**2 - 58080))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(58080))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-58080)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_485(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -232321/4) | (delta < 232321/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-232321, 4)), StrictLessThan(Symbol('delta'), Rational(232321, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_486(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 58563) | (delta < -skoSINS**2 - 58563))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(58563))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-58563)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_487(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -234253/4) | (delta < 234253/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-234253, 4)), StrictLessThan(Symbol('delta'), Rational(234253, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_488(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 59048) | (delta < -skoSINS**2 - 59048))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(59048))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-59048)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_489(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -236193/4) | (delta < 236193/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-236193, 4)), StrictLessThan(Symbol('delta'), Rational(236193, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_490(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 59535) | (delta < -skoSINS**2 - 59535))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(59535))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-59535)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_491(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -238141/4) | (delta < 238141/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-238141, 4)), StrictLessThan(Symbol('delta'), Rational(238141, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_492(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 60024) | (delta < -skoSINS**2 - 60024))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(60024))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-60024)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_493(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -240097/4) | (delta < 240097/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-240097, 4)), StrictLessThan(Symbol('delta'), Rational(240097, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_494(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 60515) | (delta < -skoSINS**2 - 60515))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(60515))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-60515)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_495(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -242061/4) | (delta < 242061/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-242061, 4)), StrictLessThan(Symbol('delta'), Rational(242061, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_496(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 61008) | (delta < -skoSINS**2 - 61008))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(61008))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-61008)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_497(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -244033/4) | (delta < 244033/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-244033, 4)), StrictLessThan(Symbol('delta'), Rational(244033, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_498(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 61503) | (delta < -skoSINS**2 - 61503))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(61503))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-61503)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_499(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -246013/4) | (delta < 246013/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-246013, 4)), StrictLessThan(Symbol('delta'), Rational(246013, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_500(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 62000) | (delta < -skoSINS**2 - 62000))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(62000))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-62000)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_501(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -248001/4) | (delta < 248001/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-248001, 4)), StrictLessThan(Symbol('delta'), Rational(248001, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_502(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 62499) | (delta < -skoSINS**2 - 62499))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(62499))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-62499)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_503(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -249997/4) | (delta < 249997/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-249997, 4)), StrictLessThan(Symbol('delta'), Rational(249997, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_504(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 63000) | (delta < -skoSINS**2 - 63000))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(63000))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-63000)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_505(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -252001/4) | (delta < 252001/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-252001, 4)), StrictLessThan(Symbol('delta'), Rational(252001, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_506(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 63503) | (delta < -skoSINS**2 - 63503))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(63503))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-63503)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_507(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -254013/4) | (delta < 254013/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-254013, 4)), StrictLessThan(Symbol('delta'), Rational(254013, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_508(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 64008) | (delta < -skoSINS**2 - 64008))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(64008))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-64008)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_509(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -256033/4) | (delta < 256033/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-256033, 4)), StrictLessThan(Symbol('delta'), Rational(256033, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_510(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 64515) | (delta < -skoSINS**2 - 64515))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(64515))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-64515)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_511(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -258061/4) | (delta < 258061/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-258061, 4)), StrictLessThan(Symbol('delta'), Rational(258061, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_512(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 65024) | (delta < -skoSINS**2 - 65024))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(65024))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-65024)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_513(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -260097/4) | (delta < 260097/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-260097, 4)), StrictLessThan(Symbol('delta'), Rational(260097, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_514(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 65535) | (delta < -skoSINS**2 - 65535))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(65535))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-65535)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_515(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -262141/4) | (delta < 262141/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-262141, 4)), StrictLessThan(Symbol('delta'), Rational(262141, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_516(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 66048) | (delta < -skoSINS**2 - 66048))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(66048))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-66048)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_517(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -264193/4) | (delta < 264193/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-264193, 4)), StrictLessThan(Symbol('delta'), Rational(264193, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_518(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 66563) | (delta < -skoSINS**2 - 66563))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(66563))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-66563)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_519(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -266253/4) | (delta < 266253/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-266253, 4)), StrictLessThan(Symbol('delta'), Rational(266253, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_520(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 67080) | (delta < -skoSINS**2 - 67080))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(67080))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-67080)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_521(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -268321/4) | (delta < 268321/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-268321, 4)), StrictLessThan(Symbol('delta'), Rational(268321, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_522(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 67599) | (delta < -skoSINS**2 - 67599))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(67599))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-67599)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_523(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -270397/4) | (delta < 270397/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-270397, 4)), StrictLessThan(Symbol('delta'), Rational(270397, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_524(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 68120) | (delta < -skoSINS**2 - 68120))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(68120))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-68120)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_525(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -272481/4) | (delta < 272481/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-272481, 4)), StrictLessThan(Symbol('delta'), Rational(272481, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_526(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 68643) | (delta < -skoSINS**2 - 68643))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(68643))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-68643)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_527(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -274573/4) | (delta < 274573/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-274573, 4)), StrictLessThan(Symbol('delta'), Rational(274573, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_528(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 69168) | (delta < -skoSINS**2 - 69168))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(69168))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-69168)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_529(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -276673/4) | (delta < 276673/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-276673, 4)), StrictLessThan(Symbol('delta'), Rational(276673, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_530(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 69695) | (delta < -skoSINS**2 - 69695))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(69695))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-69695)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_531(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -278781/4) | (delta < 278781/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-278781, 4)), StrictLessThan(Symbol('delta'), Rational(278781, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_532(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 70224) | (delta < -skoSINS**2 - 70224))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(70224))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-70224)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_533(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -280897/4) | (delta < 280897/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-280897, 4)), StrictLessThan(Symbol('delta'), Rational(280897, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_534(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 70755) | (delta < -skoSINS**2 - 70755))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(70755))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-70755)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_535(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -283021/4) | (delta < 283021/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-283021, 4)), StrictLessThan(Symbol('delta'), Rational(283021, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_536(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 71288) | (delta < -skoSINS**2 - 71288))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(71288))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-71288)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_537(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -285153/4) | (delta < 285153/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-285153, 4)), StrictLessThan(Symbol('delta'), Rational(285153, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_538(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 71823) | (delta < -skoSINS**2 - 71823))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(71823))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-71823)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_539(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -287293/4) | (delta < 287293/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-287293, 4)), StrictLessThan(Symbol('delta'), Rational(287293, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_540(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 72360) | (delta < -skoSINS**2 - 72360))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(72360))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-72360)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_541(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -289441/4) | (delta < 289441/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-289441, 4)), StrictLessThan(Symbol('delta'), Rational(289441, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_542(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 72899) | (delta < -skoSINS**2 - 72899))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(72899))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-72899)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_543(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -291597/4) | (delta < 291597/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-291597, 4)), StrictLessThan(Symbol('delta'), Rational(291597, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_544(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 73440) | (delta < -skoSINS**2 - 73440))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(73440))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-73440)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_545(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -293761/4) | (delta < 293761/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-293761, 4)), StrictLessThan(Symbol('delta'), Rational(293761, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_546(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 73983) | (delta < -skoSINS**2 - 73983))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(73983))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-73983)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_547(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -295933/4) | (delta < 295933/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-295933, 4)), StrictLessThan(Symbol('delta'), Rational(295933, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_548(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 74528) | (delta < -skoSINS**2 - 74528))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(74528))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-74528)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_549(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -298113/4) | (delta < 298113/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-298113, 4)), StrictLessThan(Symbol('delta'), Rational(298113, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_550(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 75075) | (delta < -skoSINS**2 - 75075))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(75075))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-75075)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_551(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -300301/4) | (delta < 300301/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-300301, 4)), StrictLessThan(Symbol('delta'), Rational(300301, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_552(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 75624) | (delta < -skoSINS**2 - 75624))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(75624))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-75624)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_553(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -302497/4) | (delta < 302497/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-302497, 4)), StrictLessThan(Symbol('delta'), Rational(302497, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_554(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 76175) | (delta < -skoSINS**2 - 76175))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(76175))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-76175)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_555(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -304701/4) | (delta < 304701/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-304701, 4)), StrictLessThan(Symbol('delta'), Rational(304701, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_556(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 76728) | (delta < -skoSINS**2 - 76728))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(76728))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-76728)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_557(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -306913/4) | (delta < 306913/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-306913, 4)), StrictLessThan(Symbol('delta'), Rational(306913, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_558(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 77283) | (delta < -skoSINS**2 - 77283))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(77283))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-77283)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_559(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -309133/4) | (delta < 309133/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-309133, 4)), StrictLessThan(Symbol('delta'), Rational(309133, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_560(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 77840) | (delta < -skoSINS**2 - 77840))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(77840))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-77840)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_561(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -311361/4) | (delta < 311361/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-311361, 4)), StrictLessThan(Symbol('delta'), Rational(311361, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_562(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 78399) | (delta < -skoSINS**2 - 78399))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(78399))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-78399)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_563(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -313597/4) | (delta < 313597/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-313597, 4)), StrictLessThan(Symbol('delta'), Rational(313597, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_564(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 78960) | (delta < -skoSINS**2 - 78960))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(78960))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-78960)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_565(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -315841/4) | (delta < 315841/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-315841, 4)), StrictLessThan(Symbol('delta'), Rational(315841, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_566(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 79523) | (delta < -skoSINS**2 - 79523))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(79523))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-79523)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_567(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -318093/4) | (delta < 318093/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-318093, 4)), StrictLessThan(Symbol('delta'), Rational(318093, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_568(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 80088) | (delta < -skoSINS**2 - 80088))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(80088))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-80088)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_569(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -320353/4) | (delta < 320353/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-320353, 4)), StrictLessThan(Symbol('delta'), Rational(320353, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_570(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 80655) | (delta < -skoSINS**2 - 80655))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(80655))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-80655)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_571(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -322621/4) | (delta < 322621/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-322621, 4)), StrictLessThan(Symbol('delta'), Rational(322621, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_572(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 81224) | (delta < -skoSINS**2 - 81224))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(81224))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-81224)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_573(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -324897/4) | (delta < 324897/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-324897, 4)), StrictLessThan(Symbol('delta'), Rational(324897, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_574(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 81795) | (delta < -skoSINS**2 - 81795))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(81795))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-81795)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_575(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -327181/4) | (delta < 327181/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-327181, 4)), StrictLessThan(Symbol('delta'), Rational(327181, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_576(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 82368) | (delta < -skoSINS**2 - 82368))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(82368))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-82368)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_577(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -329473/4) | (delta < 329473/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-329473, 4)), StrictLessThan(Symbol('delta'), Rational(329473, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_578(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 82943) | (delta < -skoSINS**2 - 82943))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(82943))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-82943)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_579(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -331773/4) | (delta < 331773/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-331773, 4)), StrictLessThan(Symbol('delta'), Rational(331773, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_580(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 83520) | (delta < -skoSINS**2 - 83520))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(83520))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-83520)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_581(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -334081/4) | (delta < 334081/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-334081, 4)), StrictLessThan(Symbol('delta'), Rational(334081, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_582(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 84099) | (delta < -skoSINS**2 - 84099))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(84099))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-84099)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_583(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -336397/4) | (delta < 336397/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-336397, 4)), StrictLessThan(Symbol('delta'), Rational(336397, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_584(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 84680) | (delta < -skoSINS**2 - 84680))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(84680))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-84680)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_585(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -338721/4) | (delta < 338721/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-338721, 4)), StrictLessThan(Symbol('delta'), Rational(338721, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_586(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 85263) | (delta < -skoSINS**2 - 85263))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(85263))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-85263)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_587(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -341053/4) | (delta < 341053/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-341053, 4)), StrictLessThan(Symbol('delta'), Rational(341053, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_588(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 85848) | (delta < -skoSINS**2 - 85848))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(85848))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-85848)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_589(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -343393/4) | (delta < 343393/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-343393, 4)), StrictLessThan(Symbol('delta'), Rational(343393, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_590(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 86435) | (delta < -skoSINS**2 - 86435))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(86435))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-86435)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_591(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -345741/4) | (delta < 345741/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-345741, 4)), StrictLessThan(Symbol('delta'), Rational(345741, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_592(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 87024) | (delta < -skoSINS**2 - 87024))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(87024))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-87024)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_593(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -348097/4) | (delta < 348097/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-348097, 4)), StrictLessThan(Symbol('delta'), Rational(348097, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_594(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 87615) | (delta < -skoSINS**2 - 87615))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(87615))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-87615)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_595(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -350461/4) | (delta < 350461/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-350461, 4)), StrictLessThan(Symbol('delta'), Rational(350461, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_596(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 88208) | (delta < -skoSINS**2 - 88208))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(88208))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-88208)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_597(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -352833/4) | (delta < 352833/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-352833, 4)), StrictLessThan(Symbol('delta'), Rational(352833, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_598(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 88803) | (delta < -skoSINS**2 - 88803))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(88803))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-88803)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_599(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -355213/4) | (delta < 355213/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-355213, 4)), StrictLessThan(Symbol('delta'), Rational(355213, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_600(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 89400) | (delta < -skoSINS**2 - 89400))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(89400))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-89400)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_601(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -357601/4) | (delta < 357601/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-357601, 4)), StrictLessThan(Symbol('delta'), Rational(357601, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_602(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 89999) | (delta < -skoSINS**2 - 89999))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(89999))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-89999)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_603(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -359997/4) | (delta < 359997/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-359997, 4)), StrictLessThan(Symbol('delta'), Rational(359997, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_604(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 90600) | (delta < -skoSINS**2 - 90600))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(90600))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-90600)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_605(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -362401/4) | (delta < 362401/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-362401, 4)), StrictLessThan(Symbol('delta'), Rational(362401, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_606(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 91203) | (delta < -skoSINS**2 - 91203))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(91203))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-91203)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_607(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -364813/4) | (delta < 364813/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-364813, 4)), StrictLessThan(Symbol('delta'), Rational(364813, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_608(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 91808) | (delta < -skoSINS**2 - 91808))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(91808))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-91808)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_609(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -367233/4) | (delta < 367233/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-367233, 4)), StrictLessThan(Symbol('delta'), Rational(367233, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_610(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta < skoSINS**2 + 92415) | (delta < -skoSINS**2 - 92415))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(92415))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-92415)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_611(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & ((delta <= -369661/4) | (delta < 369661/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), Or(LessThan(Symbol('delta'), Rational(-369661, 4)), StrictLessThan(Symbol('delta'), Rational(369661, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(delta:sympy.Rational, skoS:sympy.Rational, pi:sympy.Rational, skoCOSS:sympy.Rational, skoSINS:sympy.Rational):
	# (0 <= delta) & (31415927/10000000 > pi) & (pi > 15707963/5000000) & (pi/2 > skoS) & ~((skoCOSS**2 + skoSINS**2 - 1 <= delta) & (-skoCOSS**2 - skoSINS**2 + 1 <= delta))

	post_cond =  And(LessThan(Integer(0), Symbol('delta')), StrictGreaterThan(Rational(31415927, 10000000), Symbol('pi')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Mul(Rational(1, 2), Symbol('pi')), Symbol('skoS')), Not(And(LessThan(Add(Pow(Symbol('skoCOSS'), Integer(2)), Pow(Symbol('skoSINS'), Integer(2)), Integer(-1)), Symbol('delta')), LessThan(Add(Mul(Integer(-1), Pow(Symbol('skoCOSS'), Integer(2))), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(1)), Symbol('delta')))))

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
		print('delta = 1/2')
		print('pi = 26353589/8388608')
		print('skoS = 9576373/16777216')
		print('skoCOSS = 1/8')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_1(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_1 SAT")
		print('delta = 1/2')
		print('pi = 26353589/8388608')
		print('skoS = 9576373/16777216')
		print('skoCOSS = 1/8')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_2(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_2 SAT")
		print('delta = 63/64')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 0')
		print('skoSINS = 0')
		exit(0)
	
	
	if pre_condition_3(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_3 SAT")
		print('delta = 63/64')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 0')
		print('skoSINS = 0')
		exit(0)
	
	
	if pre_condition_4(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_4 SAT")
		print('delta = 7/2')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 1')
		print('skoSINS = -2')
		exit(0)
	
	
	if pre_condition_5(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_5 SAT")
		print('delta = 7/2')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 1')
		print('skoSINS = -2')
		exit(0)
	
	
	if pre_condition_6(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_6 SAT")
		print('delta = 5')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 2')
		print('skoSINS = -2')
		exit(0)
	
	
	if pre_condition_7(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_7 SAT")
		print('delta = 5')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 2')
		print('skoSINS = -2')
		exit(0)
	
	
	if pre_condition_8(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_8 SAT")
		print('delta = 8')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 3')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_9(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_9 SAT")
		print('delta = 8')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 3')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_10(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_10 SAT")
		print('delta = 9')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 4')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_11(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_11 SAT")
		print('delta = 9')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 4')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_12(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_12 SAT")
		print('delta = 16')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 5')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_13(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_13 SAT")
		print('delta = 16')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 5')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_14(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_14 SAT")
		print('delta = 25')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 6')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_15(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_15 SAT")
		print('delta = 25')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 6')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_16(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_16 SAT")
		print('delta = 36')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 7')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_17(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_17 SAT")
		print('delta = 36')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 7')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_18(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_18 SAT")
		print('delta = 49')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 8')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_19(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_19 SAT")
		print('delta = 49')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 8')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_20(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_20 SAT")
		print('delta = 64')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 9')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_21(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_21 SAT")
		print('delta = 64')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 9')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_22(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_22 SAT")
		print('delta = 81')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 10')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_23(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_23 SAT")
		print('delta = 81')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 10')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_24(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_24 SAT")
		print('delta = 100')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 11')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_25(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_25 SAT")
		print('delta = 100')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 11')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_26(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_26 SAT")
		print('delta = 121')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 12')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_27(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_27 SAT")
		print('delta = 121')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 12')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_28(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_28 SAT")
		print('delta = 144')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 13')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_29(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_29 SAT")
		print('delta = 144')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 13')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_30(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_30 SAT")
		print('delta = 169')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 14')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_31(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_31 SAT")
		print('delta = 169')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 14')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_32(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_32 SAT")
		print('delta = 196')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 15')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_33(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_33 SAT")
		print('delta = 196')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 15')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_34(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_34 SAT")
		print('delta = 225')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 16')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_35(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_35 SAT")
		print('delta = 225')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 16')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_36(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_36 SAT")
		print('delta = 256')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 17')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_37(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_37 SAT")
		print('delta = 256')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 17')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_38(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_38 SAT")
		print('delta = 289')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 18')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_39(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_39 SAT")
		print('delta = 289')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 18')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_40(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_40 SAT")
		print('delta = 324')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 19')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_41(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_41 SAT")
		print('delta = 324')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 19')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_42(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_42 SAT")
		print('delta = 361')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 20')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_43(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_43 SAT")
		print('delta = 361')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 20')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_44(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_44 SAT")
		print('delta = 400')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 21')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_45(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_45 SAT")
		print('delta = 400')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 21')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_46(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_46 SAT")
		print('delta = 441')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 22')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_47(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_47 SAT")
		print('delta = 441')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 22')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_48(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_48 SAT")
		print('delta = 484')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 23')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_49(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_49 SAT")
		print('delta = 484')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 23')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_50(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_50 SAT")
		print('delta = 529')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 24')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_51(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_51 SAT")
		print('delta = 529')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 24')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_52(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_52 SAT")
		print('delta = 576')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 25')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_53(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_53 SAT")
		print('delta = 576')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 25')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_54(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_54 SAT")
		print('delta = 625')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 26')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_55(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_55 SAT")
		print('delta = 625')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 26')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_56(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_56 SAT")
		print('delta = 676')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 27')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_57(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_57 SAT")
		print('delta = 676')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 27')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_58(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_58 SAT")
		print('delta = 729')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 28')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_59(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_59 SAT")
		print('delta = 729')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 28')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_60(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_60 SAT")
		print('delta = 784')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 29')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_61(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_61 SAT")
		print('delta = 784')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 29')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_62(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_62 SAT")
		print('delta = 841')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 30')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_63(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_63 SAT")
		print('delta = 841')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 30')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_64(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_64 SAT")
		print('delta = 900')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 31')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_65(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_65 SAT")
		print('delta = 900')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 31')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_66(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_66 SAT")
		print('delta = 961')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 32')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_67(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_67 SAT")
		print('delta = 961')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 32')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_68(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_68 SAT")
		print('delta = 1024')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 33')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_69(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_69 SAT")
		print('delta = 1024')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 33')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_70(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_70 SAT")
		print('delta = 1089')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 34')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_71(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_71 SAT")
		print('delta = 1089')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 34')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_72(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_72 SAT")
		print('delta = 1156')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 35')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_73(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_73 SAT")
		print('delta = 1156')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 35')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_74(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_74 SAT")
		print('delta = 1225')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 36')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_75(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_75 SAT")
		print('delta = 1225')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 36')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_76(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_76 SAT")
		print('delta = 1296')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 37')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_77(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_77 SAT")
		print('delta = 1296')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 37')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_78(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_78 SAT")
		print('delta = 1369')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 38')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_79(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_79 SAT")
		print('delta = 1369')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 38')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_80(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_80 SAT")
		print('delta = 1444')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 39')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_81(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_81 SAT")
		print('delta = 1444')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 39')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_82(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_82 SAT")
		print('delta = 1521')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 40')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_83(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_83 SAT")
		print('delta = 1521')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 40')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_84(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_84 SAT")
		print('delta = 1600')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 41')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_85(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_85 SAT")
		print('delta = 1600')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 41')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_86(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_86 SAT")
		print('delta = 1681')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 42')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_87(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_87 SAT")
		print('delta = 1681')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 42')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_88(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_88 SAT")
		print('delta = 1764')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 43')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_89(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_89 SAT")
		print('delta = 1764')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 43')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_90(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_90 SAT")
		print('delta = 1849')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 44')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_91(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_91 SAT")
		print('delta = 1849')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 44')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_92(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_92 SAT")
		print('delta = 1936')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 45')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_93(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_93 SAT")
		print('delta = 1936')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 45')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_94(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_94 SAT")
		print('delta = 2025')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 46')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_95(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_95 SAT")
		print('delta = 2025')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 46')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_96(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_96 SAT")
		print('delta = 2116')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 47')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_97(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_97 SAT")
		print('delta = 2116')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 47')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_98(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_98 SAT")
		print('delta = 2209')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 48')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_99(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_99 SAT")
		print('delta = 2209')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 48')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_100(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_100 SAT")
		print('delta = 2304')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 49')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_101(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_101 SAT")
		print('delta = 2304')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 49')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_102(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_102 SAT")
		print('delta = 2401')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 50')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_103(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_103 SAT")
		print('delta = 2401')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 50')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_104(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_104 SAT")
		print('delta = 2500')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 51')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_105(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_105 SAT")
		print('delta = 2500')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 51')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_106(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_106 SAT")
		print('delta = 2601')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 52')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_107(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_107 SAT")
		print('delta = 2601')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 52')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_108(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_108 SAT")
		print('delta = 2704')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 53')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_109(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_109 SAT")
		print('delta = 2704')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 53')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_110(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_110 SAT")
		print('delta = 2809')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 54')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_111(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_111 SAT")
		print('delta = 2809')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 54')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_112(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_112 SAT")
		print('delta = 2916')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 55')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_113(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_113 SAT")
		print('delta = 2916')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 55')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_114(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_114 SAT")
		print('delta = 3025')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 56')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_115(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_115 SAT")
		print('delta = 3025')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 56')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_116(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_116 SAT")
		print('delta = 3136')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 57')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_117(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_117 SAT")
		print('delta = 3136')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 57')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_118(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_118 SAT")
		print('delta = 3249')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 58')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_119(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_119 SAT")
		print('delta = 3249')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 58')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_120(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_120 SAT")
		print('delta = 3364')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 59')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_121(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_121 SAT")
		print('delta = 3364')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 59')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_122(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_122 SAT")
		print('delta = 3481')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 60')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_123(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_123 SAT")
		print('delta = 3481')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 60')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_124(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_124 SAT")
		print('delta = 3600')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 61')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_125(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_125 SAT")
		print('delta = 3600')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 61')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_126(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_126 SAT")
		print('delta = 3721')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 62')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_127(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_127 SAT")
		print('delta = 3721')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 62')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_128(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_128 SAT")
		print('delta = 3844')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 63')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_129(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_129 SAT")
		print('delta = 3844')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 63')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_130(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_130 SAT")
		print('delta = 3969')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 64')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_131(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_131 SAT")
		print('delta = 3969')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 64')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_132(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_132 SAT")
		print('delta = 4096')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 65')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_133(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_133 SAT")
		print('delta = 4096')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 65')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_134(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_134 SAT")
		print('delta = 4225')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 66')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_135(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_135 SAT")
		print('delta = 4225')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 66')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_136(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_136 SAT")
		print('delta = 4356')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 67')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_137(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_137 SAT")
		print('delta = 4356')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 67')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_138(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_138 SAT")
		print('delta = 4489')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 68')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_139(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_139 SAT")
		print('delta = 4489')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 68')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_140(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_140 SAT")
		print('delta = 4624')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 69')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_141(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_141 SAT")
		print('delta = 4624')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 69')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_142(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_142 SAT")
		print('delta = 4761')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 70')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_143(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_143 SAT")
		print('delta = 4761')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 70')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_144(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_144 SAT")
		print('delta = 4900')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 71')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_145(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_145 SAT")
		print('delta = 4900')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 71')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_146(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_146 SAT")
		print('delta = 5041')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 72')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_147(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_147 SAT")
		print('delta = 5041')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 72')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_148(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_148 SAT")
		print('delta = 5184')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 73')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_149(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_149 SAT")
		print('delta = 5184')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 73')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_150(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_150 SAT")
		print('delta = 5329')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 74')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_151(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_151 SAT")
		print('delta = 5329')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 74')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_152(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_152 SAT")
		print('delta = 5476')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 75')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_153(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_153 SAT")
		print('delta = 5476')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 75')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_154(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_154 SAT")
		print('delta = 5625')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 76')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_155(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_155 SAT")
		print('delta = 5625')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 76')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_156(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_156 SAT")
		print('delta = 5776')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 77')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_157(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_157 SAT")
		print('delta = 5776')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 77')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_158(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_158 SAT")
		print('delta = 5929')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 78')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_159(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_159 SAT")
		print('delta = 5929')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 78')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_160(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_160 SAT")
		print('delta = 6084')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 79')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_161(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_161 SAT")
		print('delta = 6084')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 79')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_162(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_162 SAT")
		print('delta = 6241')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 80')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_163(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_163 SAT")
		print('delta = 6241')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 80')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_164(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_164 SAT")
		print('delta = 6400')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 81')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_165(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_165 SAT")
		print('delta = 6400')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 81')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_166(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_166 SAT")
		print('delta = 6561')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 82')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_167(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_167 SAT")
		print('delta = 6561')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 82')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_168(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_168 SAT")
		print('delta = 6724')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 83')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_169(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_169 SAT")
		print('delta = 6724')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 83')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_170(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_170 SAT")
		print('delta = 6889')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 84')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_171(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_171 SAT")
		print('delta = 6889')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 84')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_172(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_172 SAT")
		print('delta = 7056')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 85')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_173(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_173 SAT")
		print('delta = 7056')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 85')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_174(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_174 SAT")
		print('delta = 7225')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 86')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_175(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_175 SAT")
		print('delta = 7225')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 86')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_176(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_176 SAT")
		print('delta = 7396')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 87')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_177(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_177 SAT")
		print('delta = 7396')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 87')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_178(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_178 SAT")
		print('delta = 7569')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 88')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_179(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_179 SAT")
		print('delta = 7569')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 88')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_180(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_180 SAT")
		print('delta = 7744')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 89')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_181(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_181 SAT")
		print('delta = 7744')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 89')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_182(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_182 SAT")
		print('delta = 7921')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 90')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_183(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_183 SAT")
		print('delta = 7921')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 90')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_184(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_184 SAT")
		print('delta = 8100')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 91')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_185(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_185 SAT")
		print('delta = 8100')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 91')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_186(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_186 SAT")
		print('delta = 8281')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 92')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_187(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_187 SAT")
		print('delta = 8281')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 92')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_188(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_188 SAT")
		print('delta = 8464')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 93')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_189(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_189 SAT")
		print('delta = 8464')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 93')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_190(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_190 SAT")
		print('delta = 8649')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 94')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_191(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_191 SAT")
		print('delta = 8649')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 94')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_192(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_192 SAT")
		print('delta = 8836')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 95')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_193(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_193 SAT")
		print('delta = 8836')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 95')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_194(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_194 SAT")
		print('delta = 9025')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 96')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_195(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_195 SAT")
		print('delta = 9025')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 96')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_196(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_196 SAT")
		print('delta = 9216')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 97')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_197(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_197 SAT")
		print('delta = 9216')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 97')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_198(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_198 SAT")
		print('delta = 9409')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 98')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_199(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_199 SAT")
		print('delta = 9409')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 98')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_200(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_200 SAT")
		print('delta = 9604')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 99')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_201(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_201 SAT")
		print('delta = 9604')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 99')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_202(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_202 SAT")
		print('delta = 9801')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 100')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_203(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_203 SAT")
		print('delta = 9801')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 100')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_204(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_204 SAT")
		print('delta = 10000')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 101')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_205(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_205 SAT")
		print('delta = 10000')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 101')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_206(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_206 SAT")
		print('delta = 10201')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 102')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_207(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_207 SAT")
		print('delta = 10201')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 102')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_208(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_208 SAT")
		print('delta = 10404')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 103')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_209(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_209 SAT")
		print('delta = 10404')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 103')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_210(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_210 SAT")
		print('delta = 10609')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 104')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_211(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_211 SAT")
		print('delta = 10609')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 104')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_212(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_212 SAT")
		print('delta = 10816')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 105')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_213(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_213 SAT")
		print('delta = 10816')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 105')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_214(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_214 SAT")
		print('delta = 11025')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 106')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_215(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_215 SAT")
		print('delta = 11025')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 106')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_216(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_216 SAT")
		print('delta = 11236')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 107')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_217(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_217 SAT")
		print('delta = 11236')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 107')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_218(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_218 SAT")
		print('delta = 11449')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 108')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_219(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_219 SAT")
		print('delta = 11449')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 108')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_220(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_220 SAT")
		print('delta = 11664')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 109')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_221(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_221 SAT")
		print('delta = 11664')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 109')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_222(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_222 SAT")
		print('delta = 11881')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 110')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_223(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_223 SAT")
		print('delta = 11881')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 110')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_224(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_224 SAT")
		print('delta = 12100')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 111')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_225(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_225 SAT")
		print('delta = 12100')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 111')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_226(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_226 SAT")
		print('delta = 12321')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 112')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_227(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_227 SAT")
		print('delta = 12321')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 112')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_228(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_228 SAT")
		print('delta = 12544')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 113')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_229(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_229 SAT")
		print('delta = 12544')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 113')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_230(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_230 SAT")
		print('delta = 12769')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 114')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_231(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_231 SAT")
		print('delta = 12769')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 114')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_232(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_232 SAT")
		print('delta = 12996')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 115')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_233(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_233 SAT")
		print('delta = 12996')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 115')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_234(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_234 SAT")
		print('delta = 13225')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 116')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_235(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_235 SAT")
		print('delta = 13225')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 116')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_236(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_236 SAT")
		print('delta = 13456')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 117')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_237(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_237 SAT")
		print('delta = 13456')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 117')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_238(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_238 SAT")
		print('delta = 13689')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 118')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_239(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_239 SAT")
		print('delta = 13689')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 118')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_240(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_240 SAT")
		print('delta = 13924')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 119')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_241(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_241 SAT")
		print('delta = 13924')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 119')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_242(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_242 SAT")
		print('delta = 14161')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 120')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_243(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_243 SAT")
		print('delta = 14161')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 120')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_244(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_244 SAT")
		print('delta = 14400')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 121')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_245(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_245 SAT")
		print('delta = 14400')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 121')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_246(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_246 SAT")
		print('delta = 14641')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 122')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_247(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_247 SAT")
		print('delta = 14641')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 122')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_248(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_248 SAT")
		print('delta = 14884')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 123')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_249(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_249 SAT")
		print('delta = 14884')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 123')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_250(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_250 SAT")
		print('delta = 15129')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 124')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_251(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_251 SAT")
		print('delta = 15129')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 124')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_252(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_252 SAT")
		print('delta = 15376')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 125')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_253(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_253 SAT")
		print('delta = 15376')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 125')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_254(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_254 SAT")
		print('delta = 15625')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 126')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_255(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_255 SAT")
		print('delta = 15625')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 126')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_256(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_256 SAT")
		print('delta = 15876')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 127')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_257(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_257 SAT")
		print('delta = 15876')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 127')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_258(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_258 SAT")
		print('delta = 16129')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 128')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_259(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_259 SAT")
		print('delta = 16129')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 128')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_260(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_260 SAT")
		print('delta = 16384')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 129')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_261(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_261 SAT")
		print('delta = 16384')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 129')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_262(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_262 SAT")
		print('delta = 16641')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 130')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_263(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_263 SAT")
		print('delta = 16641')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 130')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_264(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_264 SAT")
		print('delta = 16900')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 131')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_265(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_265 SAT")
		print('delta = 16900')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 131')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_266(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_266 SAT")
		print('delta = 17161')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 132')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_267(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_267 SAT")
		print('delta = 17161')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 132')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_268(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_268 SAT")
		print('delta = 17424')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 133')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_269(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_269 SAT")
		print('delta = 17424')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 133')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_270(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_270 SAT")
		print('delta = 17689')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 134')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_271(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_271 SAT")
		print('delta = 17689')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 134')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_272(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_272 SAT")
		print('delta = 17956')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 135')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_273(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_273 SAT")
		print('delta = 17956')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 135')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_274(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_274 SAT")
		print('delta = 18225')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 136')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_275(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_275 SAT")
		print('delta = 18225')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 136')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_276(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_276 SAT")
		print('delta = 18496')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 137')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_277(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_277 SAT")
		print('delta = 18496')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 137')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_278(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_278 SAT")
		print('delta = 18769')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 138')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_279(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_279 SAT")
		print('delta = 18769')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 138')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_280(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_280 SAT")
		print('delta = 19044')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 139')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_281(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_281 SAT")
		print('delta = 19044')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 139')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_282(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_282 SAT")
		print('delta = 19321')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 140')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_283(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_283 SAT")
		print('delta = 19321')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 140')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_284(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_284 SAT")
		print('delta = 19600')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 141')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_285(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_285 SAT")
		print('delta = 19600')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 141')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_286(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_286 SAT")
		print('delta = 19881')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 142')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_287(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_287 SAT")
		print('delta = 19881')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 142')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_288(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_288 SAT")
		print('delta = 20164')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 143')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_289(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_289 SAT")
		print('delta = 20164')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 143')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_290(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_290 SAT")
		print('delta = 20449')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 144')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_291(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_291 SAT")
		print('delta = 20449')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 144')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_292(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_292 SAT")
		print('delta = 20736')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 145')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_293(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_293 SAT")
		print('delta = 20736')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 145')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_294(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_294 SAT")
		print('delta = 21025')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 146')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_295(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_295 SAT")
		print('delta = 21025')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 146')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_296(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_296 SAT")
		print('delta = 21316')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 147')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_297(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_297 SAT")
		print('delta = 21316')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 147')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_298(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_298 SAT")
		print('delta = 21609')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 148')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_299(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_299 SAT")
		print('delta = 21609')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 148')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_300(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_300 SAT")
		print('delta = 21904')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 149')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_301(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_301 SAT")
		print('delta = 21904')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 149')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_302(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_302 SAT")
		print('delta = 22201')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 150')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_303(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_303 SAT")
		print('delta = 22201')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 150')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_304(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_304 SAT")
		print('delta = 22500')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 151')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_305(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_305 SAT")
		print('delta = 22500')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 151')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_306(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_306 SAT")
		print('delta = 22801')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 152')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_307(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_307 SAT")
		print('delta = 22801')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 152')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_308(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_308 SAT")
		print('delta = 23104')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 153')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_309(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_309 SAT")
		print('delta = 23104')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 153')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_310(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_310 SAT")
		print('delta = 23409')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 154')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_311(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_311 SAT")
		print('delta = 23409')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 154')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_312(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_312 SAT")
		print('delta = 23716')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 155')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_313(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_313 SAT")
		print('delta = 23716')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 155')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_314(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_314 SAT")
		print('delta = 24025')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 156')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_315(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_315 SAT")
		print('delta = 24025')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 156')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_316(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_316 SAT")
		print('delta = 24336')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 157')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_317(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_317 SAT")
		print('delta = 24336')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 157')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_318(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_318 SAT")
		print('delta = 24649')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 158')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_319(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_319 SAT")
		print('delta = 24649')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 158')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_320(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_320 SAT")
		print('delta = 24964')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 159')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_321(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_321 SAT")
		print('delta = 24964')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 159')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_322(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_322 SAT")
		print('delta = 25281')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 160')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_323(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_323 SAT")
		print('delta = 25281')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 160')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_324(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_324 SAT")
		print('delta = 25600')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 161')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_325(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_325 SAT")
		print('delta = 25600')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 161')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_326(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_326 SAT")
		print('delta = 25921')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 162')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_327(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_327 SAT")
		print('delta = 25921')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 162')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_328(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_328 SAT")
		print('delta = 26244')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 163')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_329(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_329 SAT")
		print('delta = 26244')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 163')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_330(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_330 SAT")
		print('delta = 26569')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 164')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_331(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_331 SAT")
		print('delta = 26569')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 164')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_332(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_332 SAT")
		print('delta = 26896')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 165')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_333(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_333 SAT")
		print('delta = 26896')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 165')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_334(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_334 SAT")
		print('delta = 27225')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 166')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_335(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_335 SAT")
		print('delta = 27225')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 166')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_336(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_336 SAT")
		print('delta = 27556')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 167')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_337(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_337 SAT")
		print('delta = 27556')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 167')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_338(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_338 SAT")
		print('delta = 27889')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 168')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_339(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_339 SAT")
		print('delta = 27889')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 168')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_340(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_340 SAT")
		print('delta = 28224')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 169')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_341(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_341 SAT")
		print('delta = 28224')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 169')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_342(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_342 SAT")
		print('delta = 28561')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 170')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_343(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_343 SAT")
		print('delta = 28561')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 170')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_344(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_344 SAT")
		print('delta = 28900')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 171')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_345(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_345 SAT")
		print('delta = 28900')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 171')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_346(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_346 SAT")
		print('delta = 29241')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 172')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_347(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_347 SAT")
		print('delta = 29241')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 172')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_348(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_348 SAT")
		print('delta = 29584')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 173')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_349(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_349 SAT")
		print('delta = 29584')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 173')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_350(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_350 SAT")
		print('delta = 29929')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 174')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_351(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_351 SAT")
		print('delta = 29929')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 174')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_352(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_352 SAT")
		print('delta = 30276')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 175')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_353(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_353 SAT")
		print('delta = 30276')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 175')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_354(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_354 SAT")
		print('delta = 30625')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 176')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_355(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_355 SAT")
		print('delta = 30625')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 176')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_356(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_356 SAT")
		print('delta = 30976')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 177')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_357(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_357 SAT")
		print('delta = 30976')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 177')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_358(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_358 SAT")
		print('delta = 31329')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 178')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_359(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_359 SAT")
		print('delta = 31329')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 178')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_360(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_360 SAT")
		print('delta = 31684')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 179')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_361(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_361 SAT")
		print('delta = 31684')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 179')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_362(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_362 SAT")
		print('delta = 32041')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 180')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_363(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_363 SAT")
		print('delta = 32041')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 180')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_364(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_364 SAT")
		print('delta = 32400')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 181')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_365(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_365 SAT")
		print('delta = 32400')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 181')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_366(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_366 SAT")
		print('delta = 32761')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 182')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_367(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_367 SAT")
		print('delta = 32761')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 182')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_368(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_368 SAT")
		print('delta = 33124')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 183')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_369(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_369 SAT")
		print('delta = 33124')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 183')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_370(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_370 SAT")
		print('delta = 33489')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 184')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_371(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_371 SAT")
		print('delta = 33489')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 184')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_372(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_372 SAT")
		print('delta = 33856')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 185')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_373(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_373 SAT")
		print('delta = 33856')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 185')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_374(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_374 SAT")
		print('delta = 34225')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 186')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_375(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_375 SAT")
		print('delta = 34225')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 186')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_376(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_376 SAT")
		print('delta = 34596')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 187')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_377(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_377 SAT")
		print('delta = 34596')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 187')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_378(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_378 SAT")
		print('delta = 34969')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 188')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_379(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_379 SAT")
		print('delta = 34969')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 188')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_380(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_380 SAT")
		print('delta = 35344')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 189')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_381(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_381 SAT")
		print('delta = 35344')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 189')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_382(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_382 SAT")
		print('delta = 35721')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 190')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_383(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_383 SAT")
		print('delta = 35721')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 190')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_384(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_384 SAT")
		print('delta = 36100')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 191')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_385(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_385 SAT")
		print('delta = 36100')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 191')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_386(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_386 SAT")
		print('delta = 36481')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 192')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_387(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_387 SAT")
		print('delta = 36481')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 192')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_388(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_388 SAT")
		print('delta = 36864')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 193')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_389(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_389 SAT")
		print('delta = 36864')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 193')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_390(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_390 SAT")
		print('delta = 37249')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 194')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_391(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_391 SAT")
		print('delta = 37249')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 194')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_392(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_392 SAT")
		print('delta = 37636')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 195')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_393(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_393 SAT")
		print('delta = 37636')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 195')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_394(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_394 SAT")
		print('delta = 38025')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 196')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_395(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_395 SAT")
		print('delta = 38025')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 196')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_396(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_396 SAT")
		print('delta = 38416')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 197')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_397(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_397 SAT")
		print('delta = 38416')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 197')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_398(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_398 SAT")
		print('delta = 38809')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 198')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_399(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_399 SAT")
		print('delta = 38809')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 198')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_400(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_400 SAT")
		print('delta = 39204')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 199')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_401(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_401 SAT")
		print('delta = 39204')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 199')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_402(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_402 SAT")
		print('delta = 39601')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 200')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_403(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_403 SAT")
		print('delta = 39601')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 200')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_404(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_404 SAT")
		print('delta = 40000')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 201')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_405(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_405 SAT")
		print('delta = 40000')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 201')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_406(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_406 SAT")
		print('delta = 40401')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 202')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_407(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_407 SAT")
		print('delta = 40401')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 202')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_408(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_408 SAT")
		print('delta = 40804')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 203')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_409(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_409 SAT")
		print('delta = 40804')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 203')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_410(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_410 SAT")
		print('delta = 41209')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 204')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_411(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_411 SAT")
		print('delta = 41209')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 204')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_412(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_412 SAT")
		print('delta = 41616')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 205')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_413(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_413 SAT")
		print('delta = 41616')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 205')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_414(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_414 SAT")
		print('delta = 42025')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 206')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_415(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_415 SAT")
		print('delta = 42025')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 206')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_416(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_416 SAT")
		print('delta = 42436')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 207')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_417(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_417 SAT")
		print('delta = 42436')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 207')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_418(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_418 SAT")
		print('delta = 42849')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 208')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_419(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_419 SAT")
		print('delta = 42849')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 208')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_420(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_420 SAT")
		print('delta = 43264')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 209')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_421(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_421 SAT")
		print('delta = 43264')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 209')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_422(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_422 SAT")
		print('delta = 43681')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 210')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_423(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_423 SAT")
		print('delta = 43681')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 210')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_424(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_424 SAT")
		print('delta = 44100')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 211')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_425(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_425 SAT")
		print('delta = 44100')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 211')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_426(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_426 SAT")
		print('delta = 44521')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 212')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_427(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_427 SAT")
		print('delta = 44521')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 212')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_428(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_428 SAT")
		print('delta = 44944')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 213')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_429(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_429 SAT")
		print('delta = 44944')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 213')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_430(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_430 SAT")
		print('delta = 45369')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 214')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_431(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_431 SAT")
		print('delta = 45369')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 214')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_432(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_432 SAT")
		print('delta = 45796')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 215')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_433(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_433 SAT")
		print('delta = 45796')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 215')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_434(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_434 SAT")
		print('delta = 46225')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 216')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_435(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_435 SAT")
		print('delta = 46225')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 216')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_436(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_436 SAT")
		print('delta = 46656')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 217')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_437(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_437 SAT")
		print('delta = 46656')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 217')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_438(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_438 SAT")
		print('delta = 47089')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 218')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_439(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_439 SAT")
		print('delta = 47089')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 218')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_440(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_440 SAT")
		print('delta = 47524')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 219')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_441(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_441 SAT")
		print('delta = 47524')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 219')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_442(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_442 SAT")
		print('delta = 47961')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 220')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_443(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_443 SAT")
		print('delta = 47961')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 220')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_444(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_444 SAT")
		print('delta = 48400')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 221')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_445(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_445 SAT")
		print('delta = 48400')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 221')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_446(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_446 SAT")
		print('delta = 48841')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 222')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_447(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_447 SAT")
		print('delta = 48841')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 222')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_448(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_448 SAT")
		print('delta = 49284')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 223')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_449(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_449 SAT")
		print('delta = 49284')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 223')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_450(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_450 SAT")
		print('delta = 49729')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 224')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_451(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_451 SAT")
		print('delta = 49729')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 224')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_452(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_452 SAT")
		print('delta = 50176')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 225')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_453(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_453 SAT")
		print('delta = 50176')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 225')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_454(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_454 SAT")
		print('delta = 50625')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 226')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_455(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_455 SAT")
		print('delta = 50625')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 226')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_456(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_456 SAT")
		print('delta = 51076')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 227')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_457(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_457 SAT")
		print('delta = 51076')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 227')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_458(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_458 SAT")
		print('delta = 51529')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 228')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_459(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_459 SAT")
		print('delta = 51529')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 228')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_460(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_460 SAT")
		print('delta = 51984')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 229')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_461(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_461 SAT")
		print('delta = 51984')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 229')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_462(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_462 SAT")
		print('delta = 52441')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 230')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_463(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_463 SAT")
		print('delta = 52441')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 230')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_464(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_464 SAT")
		print('delta = 52900')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 231')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_465(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_465 SAT")
		print('delta = 52900')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 231')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_466(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_466 SAT")
		print('delta = 53361')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 232')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_467(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_467 SAT")
		print('delta = 53361')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 232')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_468(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_468 SAT")
		print('delta = 53824')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 233')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_469(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_469 SAT")
		print('delta = 53824')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 233')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_470(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_470 SAT")
		print('delta = 54289')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 234')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_471(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_471 SAT")
		print('delta = 54289')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 234')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_472(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_472 SAT")
		print('delta = 54756')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 235')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_473(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_473 SAT")
		print('delta = 54756')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 235')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_474(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_474 SAT")
		print('delta = 55225')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 236')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_475(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_475 SAT")
		print('delta = 55225')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 236')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_476(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_476 SAT")
		print('delta = 55696')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 237')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_477(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_477 SAT")
		print('delta = 55696')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 237')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_478(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_478 SAT")
		print('delta = 56169')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 238')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_479(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_479 SAT")
		print('delta = 56169')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 238')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_480(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_480 SAT")
		print('delta = 56644')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 239')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_481(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_481 SAT")
		print('delta = 56644')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 239')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_482(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_482 SAT")
		print('delta = 57121')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 240')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_483(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_483 SAT")
		print('delta = 57121')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 240')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_484(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_484 SAT")
		print('delta = 57600')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 241')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_485(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_485 SAT")
		print('delta = 57600')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 241')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_486(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_486 SAT")
		print('delta = 58081')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 242')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_487(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_487 SAT")
		print('delta = 58081')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 242')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_488(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_488 SAT")
		print('delta = 58564')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 243')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_489(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_489 SAT")
		print('delta = 58564')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 243')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_490(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_490 SAT")
		print('delta = 59049')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 244')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_491(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_491 SAT")
		print('delta = 59049')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 244')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_492(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_492 SAT")
		print('delta = 59536')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 245')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_493(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_493 SAT")
		print('delta = 59536')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 245')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_494(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_494 SAT")
		print('delta = 60025')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 246')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_495(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_495 SAT")
		print('delta = 60025')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 246')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_496(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_496 SAT")
		print('delta = 60516')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 247')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_497(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_497 SAT")
		print('delta = 60516')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 247')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_498(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_498 SAT")
		print('delta = 61009')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 248')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_499(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_499 SAT")
		print('delta = 61009')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 248')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_500(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_500 SAT")
		print('delta = 61504')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 249')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_501(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_501 SAT")
		print('delta = 61504')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 249')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_502(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_502 SAT")
		print('delta = 62001')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 250')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_503(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_503 SAT")
		print('delta = 62001')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 250')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_504(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_504 SAT")
		print('delta = 62500')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 251')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_505(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_505 SAT")
		print('delta = 62500')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 251')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_506(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_506 SAT")
		print('delta = 63001')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 252')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_507(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_507 SAT")
		print('delta = 63001')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 252')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_508(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_508 SAT")
		print('delta = 63504')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 253')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_509(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_509 SAT")
		print('delta = 63504')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 253')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_510(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_510 SAT")
		print('delta = 64009')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 254')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_511(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_511 SAT")
		print('delta = 64009')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 254')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_512(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_512 SAT")
		print('delta = 64516')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 255')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_513(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_513 SAT")
		print('delta = 64516')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 255')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_514(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_514 SAT")
		print('delta = 65025')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 256')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_515(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_515 SAT")
		print('delta = 65025')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 256')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_516(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_516 SAT")
		print('delta = 65536')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 257')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_517(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_517 SAT")
		print('delta = 65536')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 257')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_518(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_518 SAT")
		print('delta = 66049')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 258')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_519(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_519 SAT")
		print('delta = 66049')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 258')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_520(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_520 SAT")
		print('delta = 66564')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 259')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_521(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_521 SAT")
		print('delta = 66564')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 259')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_522(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_522 SAT")
		print('delta = 67081')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 260')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_523(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_523 SAT")
		print('delta = 67081')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 260')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_524(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_524 SAT")
		print('delta = 67600')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 261')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_525(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_525 SAT")
		print('delta = 67600')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 261')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_526(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_526 SAT")
		print('delta = 68121')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 262')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_527(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_527 SAT")
		print('delta = 68121')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 262')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_528(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_528 SAT")
		print('delta = 68644')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 263')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_529(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_529 SAT")
		print('delta = 68644')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 263')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_530(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_530 SAT")
		print('delta = 69169')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 264')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_531(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_531 SAT")
		print('delta = 69169')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 264')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_532(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_532 SAT")
		print('delta = 69696')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 265')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_533(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_533 SAT")
		print('delta = 69696')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 265')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_534(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_534 SAT")
		print('delta = 70225')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 266')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_535(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_535 SAT")
		print('delta = 70225')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 266')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_536(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_536 SAT")
		print('delta = 70756')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 267')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_537(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_537 SAT")
		print('delta = 70756')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 267')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_538(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_538 SAT")
		print('delta = 71289')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 268')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_539(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_539 SAT")
		print('delta = 71289')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 268')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_540(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_540 SAT")
		print('delta = 71824')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 269')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_541(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_541 SAT")
		print('delta = 71824')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 269')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_542(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_542 SAT")
		print('delta = 72361')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 270')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_543(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_543 SAT")
		print('delta = 72361')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 270')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_544(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_544 SAT")
		print('delta = 72900')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 271')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_545(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_545 SAT")
		print('delta = 72900')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 271')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_546(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_546 SAT")
		print('delta = 73441')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 272')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_547(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_547 SAT")
		print('delta = 73441')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 272')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_548(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_548 SAT")
		print('delta = 73984')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 273')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_549(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_549 SAT")
		print('delta = 73984')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 273')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_550(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_550 SAT")
		print('delta = 74529')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 274')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_551(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_551 SAT")
		print('delta = 74529')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 274')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_552(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_552 SAT")
		print('delta = 75076')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 275')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_553(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_553 SAT")
		print('delta = 75076')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 275')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_554(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_554 SAT")
		print('delta = 75625')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 276')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_555(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_555 SAT")
		print('delta = 75625')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 276')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_556(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_556 SAT")
		print('delta = 76176')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 277')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_557(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_557 SAT")
		print('delta = 76176')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 277')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_558(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_558 SAT")
		print('delta = 76729')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 278')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_559(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_559 SAT")
		print('delta = 76729')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 278')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_560(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_560 SAT")
		print('delta = 77284')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 279')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_561(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_561 SAT")
		print('delta = 77284')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 279')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_562(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_562 SAT")
		print('delta = 77841')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 280')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_563(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_563 SAT")
		print('delta = 77841')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 280')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_564(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_564 SAT")
		print('delta = 78400')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 281')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_565(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_565 SAT")
		print('delta = 78400')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 281')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_566(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_566 SAT")
		print('delta = 78961')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 282')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_567(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_567 SAT")
		print('delta = 78961')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 282')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_568(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_568 SAT")
		print('delta = 79524')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 283')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_569(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_569 SAT")
		print('delta = 79524')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 283')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_570(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_570 SAT")
		print('delta = 80089')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 284')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_571(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_571 SAT")
		print('delta = 80089')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 284')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_572(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_572 SAT")
		print('delta = 80656')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 285')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_573(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_573 SAT")
		print('delta = 80656')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 285')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_574(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_574 SAT")
		print('delta = 81225')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 286')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_575(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_575 SAT")
		print('delta = 81225')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 286')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_576(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_576 SAT")
		print('delta = 81796')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 287')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_577(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_577 SAT")
		print('delta = 81796')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 287')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_578(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_578 SAT")
		print('delta = 82369')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 288')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_579(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_579 SAT")
		print('delta = 82369')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 288')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_580(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_580 SAT")
		print('delta = 82944')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 289')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_581(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_581 SAT")
		print('delta = 82944')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 289')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_582(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_582 SAT")
		print('delta = 83521')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 290')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_583(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_583 SAT")
		print('delta = 83521')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 290')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_584(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_584 SAT")
		print('delta = 84100')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 291')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_585(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_585 SAT")
		print('delta = 84100')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 291')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_586(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_586 SAT")
		print('delta = 84681')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 292')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_587(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_587 SAT")
		print('delta = 84681')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 292')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_588(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_588 SAT")
		print('delta = 85264')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 293')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_589(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_589 SAT")
		print('delta = 85264')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 293')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_590(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_590 SAT")
		print('delta = 85849')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 294')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_591(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_591 SAT")
		print('delta = 85849')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 294')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_592(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_592 SAT")
		print('delta = 86436')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 295')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_593(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_593 SAT")
		print('delta = 86436')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 295')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_594(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_594 SAT")
		print('delta = 87025')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 296')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_595(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_595 SAT")
		print('delta = 87025')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 296')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_596(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_596 SAT")
		print('delta = 87616')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 297')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_597(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_597 SAT")
		print('delta = 87616')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 297')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_598(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_598 SAT")
		print('delta = 88209')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 298')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_599(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_599 SAT")
		print('delta = 88209')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 298')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_600(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_600 SAT")
		print('delta = 88804')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 299')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_601(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_601 SAT")
		print('delta = 88804')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 299')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_602(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_602 SAT")
		print('delta = 89401')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 300')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_603(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_603 SAT")
		print('delta = 89401')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 300')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_604(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_604 SAT")
		print('delta = 90000')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 301')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_605(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_605 SAT")
		print('delta = 90000')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 301')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_606(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_606 SAT")
		print('delta = 90601')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 302')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_607(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_607 SAT")
		print('delta = 90601')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 302')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_608(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_608 SAT")
		print('delta = 91204')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 303')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_609(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_609 SAT")
		print('delta = 91204')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 303')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_610(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_610 SAT")
		print('delta = 91809')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 304')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_611(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_611 SAT")
		print('delta = 91809')
		print('pi = 62831853/20000000')
		print('skoS = 62831851/40000000')
		print('skoCOSS = 304')
		print('skoSINS = 1/2')
		exit(0)


	print("UNKNOWN")
	exit(0)
