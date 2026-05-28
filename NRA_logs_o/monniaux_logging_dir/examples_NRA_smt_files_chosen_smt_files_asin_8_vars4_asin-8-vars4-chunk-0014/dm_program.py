import sympy
from sympy import *

def pre_condition_0(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < -3/4) | (delta - skoX < 3/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-3, 4)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(3, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < -3/4) | (delta - skoX < 3/4))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-3, 4)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(3, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 3) | (delta - skoX < -3))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(3)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-3))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 3) | (delta - skoX < -3))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(3)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-3))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_4(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 8) | (delta - skoX < -8))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(8)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-8))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_5(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 8) | (delta - skoX < -8))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(8)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-8))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_6(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 15) | (delta - skoX < -15))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(15)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-15))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_7(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 15) | (delta - skoX < -15))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(15)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-15))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_8(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 24) | (delta - skoX < -24))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(24)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-24))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_9(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 24) | (delta - skoX < -24))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(24)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-24))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_10(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 35) | (delta - skoX < -35))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(35)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-35))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_11(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 35) | (delta - skoX < -35))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(35)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-35))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_12(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 48) | (delta - skoX < -48))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(48)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-48))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_13(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 48) | (delta - skoX < -48))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(48)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-48))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_14(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 63) | (delta - skoX < -63))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(63)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-63))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_15(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 63) | (delta - skoX < -63))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(63)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-63))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_16(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 80) | (delta - skoX < -80))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(80)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-80))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_17(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 80) | (delta - skoX < -80))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(80)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-80))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_18(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 99) | (delta - skoX < -99))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(99)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-99))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_19(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 99) | (delta - skoX < -99))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(99)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-99))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_20(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 120) | (delta - skoX < -120))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(120)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-120))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_21(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 120) | (delta - skoX < -120))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(120)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-120))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_22(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 143) | (delta - skoX < -143))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(143)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-143))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_23(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 143) | (delta - skoX < -143))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(143)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-143))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_24(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 168) | (delta - skoX < -168))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(168)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-168))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_25(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 168) | (delta - skoX < -168))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(168)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-168))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_26(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 195) | (delta - skoX < -195))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(195)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-195))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_27(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 195) | (delta - skoX < -195))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(195)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-195))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_28(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 224) | (delta - skoX < -224))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(224)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-224))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_29(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 224) | (delta - skoX < -224))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(224)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-224))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_30(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 255) | (delta - skoX < -255))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(255)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-255))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_31(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 255) | (delta - skoX < -255))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(255)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-255))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_32(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 288) | (delta - skoX < -288))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(288)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-288))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_33(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 288) | (delta - skoX < -288))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(288)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-288))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_34(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 323) | (delta - skoX < -323))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(323)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-323))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_35(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 323) | (delta - skoX < -323))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(323)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-323))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_36(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 360) | (delta - skoX < -360))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(360)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-360))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_37(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 360) | (delta - skoX < -360))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(360)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-360))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_38(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 399) | (delta - skoX < -399))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(399)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-399))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_39(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 399) | (delta - skoX < -399))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(399)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-399))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_40(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 440) | (delta - skoX < -440))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(440)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-440))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_41(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 440) | (delta - skoX < -440))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(440)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-440))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_42(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 483) | (delta - skoX < -483))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(483)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-483))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_43(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 483) | (delta - skoX < -483))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(483)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-483))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_44(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 528) | (delta - skoX < -528))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(528)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-528))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_45(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 528) | (delta - skoX < -528))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(528)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-528))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_46(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 575) | (delta - skoX < -575))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(575)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-575))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_47(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 575) | (delta - skoX < -575))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(575)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-575))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_48(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 624) | (delta - skoX < -624))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(624)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-624))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_49(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 624) | (delta - skoX < -624))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(624)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-624))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_50(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 675) | (delta - skoX < -675))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(675)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-675))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_51(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 675) | (delta - skoX < -675))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(675)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-675))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_52(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 728) | (delta - skoX < -728))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(728)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-728))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_53(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 728) | (delta - skoX < -728))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(728)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-728))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_54(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 783) | (delta - skoX < -783))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(783)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-783))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_55(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 783) | (delta - skoX < -783))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(783)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-783))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_56(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 840) | (delta - skoX < -840))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(840)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-840))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_57(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 840) | (delta - skoX < -840))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(840)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-840))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_58(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 899) | (delta - skoX < -899))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(899)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-899))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_59(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 899) | (delta - skoX < -899))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(899)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-899))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_60(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 960) | (delta - skoX < -960))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(960)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-960))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_61(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 960) | (delta - skoX < -960))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(960)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-960))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_62(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 1023) | (delta - skoX < -1023))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(1023)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-1023))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_63(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 1023) | (delta - skoX < -1023))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(1023)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-1023))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_64(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 1088) | (delta - skoX < -1088))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(1088)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-1088))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_65(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 1088) | (delta - skoX < -1088))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(1088)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-1088))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_66(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 1155) | (delta - skoX < -1155))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(1155)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-1155))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_67(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 1155) | (delta - skoX < -1155))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(1155)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-1155))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_68(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 1224) | (delta - skoX < -1224))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(1224)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-1224))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_69(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 1224) | (delta - skoX < -1224))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(1224)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-1224))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_70(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 1295) | (delta - skoX < -1295))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(1295)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-1295))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_71(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 1295) | (delta - skoX < -1295))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(1295)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-1295))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_72(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 1368) | (delta - skoX < -1368))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(1368)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-1368))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_73(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 1368) | (delta - skoX < -1368))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(1368)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-1368))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_74(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 1443) | (delta - skoX < -1443))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(1443)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-1443))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_75(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 1443) | (delta - skoX < -1443))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(1443)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-1443))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_76(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 1520) | (delta - skoX < -1520))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(1520)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-1520))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_77(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 1520) | (delta - skoX < -1520))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(1520)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-1520))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_78(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 1599) | (delta - skoX < -1599))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(1599)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-1599))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_79(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 1599) | (delta - skoX < -1599))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(1599)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-1599))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_80(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 1680) | (delta - skoX < -1680))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(1680)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-1680))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_81(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 1680) | (delta - skoX < -1680))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(1680)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-1680))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_82(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 1763) | (delta - skoX < -1763))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(1763)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-1763))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_83(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 1763) | (delta - skoX < -1763))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(1763)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-1763))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_84(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 1848) | (delta - skoX < -1848))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(1848)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-1848))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_85(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 1848) | (delta - skoX < -1848))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(1848)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-1848))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_86(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 1935) | (delta - skoX < -1935))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(1935)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-1935))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_87(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 1935) | (delta - skoX < -1935))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(1935)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-1935))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_88(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 2024) | (delta - skoX < -2024))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(2024)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-2024))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_89(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 2024) | (delta - skoX < -2024))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(2024)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-2024))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_90(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 2115) | (delta - skoX < -2115))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(2115)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-2115))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_91(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 2115) | (delta - skoX < -2115))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(2115)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-2115))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_92(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 2208) | (delta - skoX < -2208))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(2208)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-2208))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_93(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 2208) | (delta - skoX < -2208))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(2208)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-2208))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_94(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 2303) | (delta - skoX < -2303))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(2303)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-2303))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_95(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 2303) | (delta - skoX < -2303))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(2303)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-2303))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_96(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 2400) | (delta - skoX < -2400))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(2400)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-2400))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_97(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 2400) | (delta - skoX < -2400))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(2400)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-2400))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_98(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 2499) | (delta - skoX < -2499))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(2499)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-2499))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_99(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 2499) | (delta - skoX < -2499))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(2499)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-2499))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_100(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 2600) | (delta - skoX < -2600))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(2600)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-2600))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_101(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 2600) | (delta - skoX < -2600))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(2600)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-2600))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_102(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 2703) | (delta - skoX < -2703))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(2703)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-2703))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_103(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 2703) | (delta - skoX < -2703))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(2703)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-2703))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_104(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 2808) | (delta - skoX < -2808))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(2808)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-2808))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_105(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 2808) | (delta - skoX < -2808))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(2808)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-2808))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_106(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 2915) | (delta - skoX < -2915))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(2915)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-2915))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_107(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 2915) | (delta - skoX < -2915))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(2915)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-2915))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_108(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 3024) | (delta - skoX < -3024))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(3024)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-3024))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_109(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 3024) | (delta - skoX < -3024))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(3024)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-3024))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_110(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 3135) | (delta - skoX < -3135))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(3135)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-3135))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_111(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 3135) | (delta - skoX < -3135))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(3135)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-3135))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_112(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 3248) | (delta - skoX < -3248))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(3248)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-3248))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_113(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 3248) | (delta - skoX < -3248))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(3248)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-3248))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_114(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 3363) | (delta - skoX < -3363))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(3363)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-3363))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_115(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 3363) | (delta - skoX < -3363))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(3363)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-3363))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_116(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 3480) | (delta - skoX < -3480))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(3480)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-3480))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_117(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 3480) | (delta - skoX < -3480))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(3480)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-3480))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_118(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 3599) | (delta - skoX < -3599))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(3599)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-3599))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_119(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 3599) | (delta - skoX < -3599))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(3599)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-3599))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_120(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 3720) | (delta - skoX < -3720))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(3720)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-3720))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_121(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 3720) | (delta - skoX < -3720))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(3720)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-3720))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_122(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 3843) | (delta - skoX < -3843))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(3843)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-3843))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_123(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 3843) | (delta - skoX < -3843))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(3843)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-3843))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_124(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 3968) | (delta - skoX < -3968))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(3968)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-3968))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_125(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 3968) | (delta - skoX < -3968))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(3968)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-3968))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_126(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 4095) | (delta - skoX < -4095))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(4095)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-4095))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_127(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 4095) | (delta - skoX < -4095))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(4095)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-4095))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_128(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 4224) | (delta - skoX < -4224))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(4224)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-4224))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_129(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 4224) | (delta - skoX < -4224))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(4224)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-4224))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_130(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 4355) | (delta - skoX < -4355))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(4355)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-4355))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_131(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 4355) | (delta - skoX < -4355))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(4355)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-4355))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_132(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 4488) | (delta - skoX < -4488))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(4488)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-4488))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_133(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 4488) | (delta - skoX < -4488))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(4488)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-4488))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_134(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 4623) | (delta - skoX < -4623))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(4623)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-4623))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_135(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 4623) | (delta - skoX < -4623))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(4623)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-4623))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_136(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 4760) | (delta - skoX < -4760))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(4760)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-4760))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_137(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 4760) | (delta - skoX < -4760))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(4760)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-4760))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_138(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 4899) | (delta - skoX < -4899))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(4899)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-4899))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_139(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 4899) | (delta - skoX < -4899))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(4899)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-4899))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_140(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 5040) | (delta - skoX < -5040))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(5040)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-5040))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_141(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 5040) | (delta - skoX < -5040))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(5040)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-5040))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_142(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 5183) | (delta - skoX < -5183))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(5183)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-5183))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_143(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 5183) | (delta - skoX < -5183))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(5183)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-5183))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_144(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 5328) | (delta - skoX < -5328))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(5328)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-5328))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_145(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 5328) | (delta - skoX < -5328))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(5328)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-5328))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_146(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 5475) | (delta - skoX < -5475))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(5475)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-5475))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_147(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 5475) | (delta - skoX < -5475))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(5475)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-5475))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_148(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 5624) | (delta - skoX < -5624))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(5624)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-5624))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_149(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 5624) | (delta - skoX < -5624))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(5624)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-5624))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_150(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 5775) | (delta - skoX < -5775))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(5775)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-5775))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_151(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 5775) | (delta - skoX < -5775))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(5775)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-5775))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_152(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 5928) | (delta - skoX < -5928))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(5928)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-5928))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_153(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 5928) | (delta - skoX < -5928))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(5928)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-5928))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_154(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 6083) | (delta - skoX < -6083))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(6083)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-6083))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_155(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 6083) | (delta - skoX < -6083))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(6083)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-6083))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_156(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 6240) | (delta - skoX < -6240))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(6240)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-6240))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_157(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 6240) | (delta - skoX < -6240))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(6240)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-6240))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_158(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 6399) | (delta - skoX < -6399))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(6399)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-6399))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_159(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 6399) | (delta - skoX < -6399))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(6399)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-6399))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_160(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 167961277/26244) | (delta - skoX < -167961277/26244))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Rational(167961277, 26244)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-167961277, 26244))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_161(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 167961277/26244) | (delta - skoX < -167961277/26244))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Rational(167961277, 26244)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-167961277, 26244))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_162(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 35586647722042483105064473217649/5559566406250000000000000000) | (delta - skoX < -35586647722042483105064473217649/5559566406250000000000000000))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Rational(35586647722042483105064473217649, 5559566406250000000000000000)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-35586647722042483105064473217649, 5559566406250000000000000000))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_163(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 35586647722042483105064473217649/5559566406250000000000000000) | (delta - skoX < -35586647722042483105064473217649/5559566406250000000000000000))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Rational(35586647722042483105064473217649, 5559566406250000000000000000)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-35586647722042483105064473217649, 5559566406250000000000000000))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_164(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 6560) | (delta - skoX < -6560))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(6560)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-6560))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_165(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 6560) | (delta - skoX < -6560))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(6560)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-6560))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_166(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 6723) | (delta - skoX < -6723))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(6723)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-6723))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_167(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 6723) | (delta - skoX < -6723))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(6723)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-6723))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_168(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 6888) | (delta - skoX < -6888))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(6888)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-6888))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_169(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 6888) | (delta - skoX < -6888))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(6888)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-6888))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_170(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 7055) | (delta - skoX < -7055))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(7055)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-7055))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_171(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 7055) | (delta - skoX < -7055))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(7055)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-7055))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_172(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 7224) | (delta - skoX < -7224))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(7224)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-7224))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_173(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 7224) | (delta - skoX < -7224))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(7224)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-7224))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_174(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 7395) | (delta - skoX < -7395))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(7395)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-7395))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_175(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 7395) | (delta - skoX < -7395))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(7395)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-7395))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_176(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 7568) | (delta - skoX < -7568))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(7568)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-7568))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_177(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 7568) | (delta - skoX < -7568))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(7568)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-7568))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_178(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 7743) | (delta - skoX < -7743))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(7743)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-7743))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_179(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 7743) | (delta - skoX < -7743))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(7743)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-7743))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_180(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 7920) | (delta - skoX < -7920))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(7920)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-7920))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_181(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 7920) | (delta - skoX < -7920))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(7920)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-7920))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_182(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 8099) | (delta - skoX < -8099))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(8099)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-8099))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_183(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 8099) | (delta - skoX < -8099))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(8099)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-8099))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_184(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 8280) | (delta - skoX < -8280))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(8280)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-8280))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_185(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 8280) | (delta - skoX < -8280))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(8280)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-8280))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_186(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 8463) | (delta - skoX < -8463))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(8463)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-8463))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_187(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 8463) | (delta - skoX < -8463))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(8463)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-8463))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_188(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 8648) | (delta - skoX < -8648))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(8648)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-8648))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_189(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 8648) | (delta - skoX < -8648))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(8648)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-8648))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_190(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 8835) | (delta - skoX < -8835))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(8835)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-8835))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_191(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 8835) | (delta - skoX < -8835))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(8835)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-8835))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_192(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 9024) | (delta - skoX < -9024))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(9024)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-9024))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_193(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 9024) | (delta - skoX < -9024))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(9024)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-9024))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_194(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 9215) | (delta - skoX < -9215))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(9215)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-9215))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_195(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 9215) | (delta - skoX < -9215))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(9215)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-9215))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_196(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 9408) | (delta - skoX < -9408))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(9408)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-9408))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_197(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 9408) | (delta - skoX < -9408))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(9408)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-9408))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_198(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 9603) | (delta - skoX < -9603))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(9603)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-9603))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_199(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 9603) | (delta - skoX < -9603))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(9603)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-9603))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_200(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < 9800) | (delta - skoX < -9800))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(9800)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-9800))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(delta:sympy.Rational, skoX:sympy.Rational, skoS2:sympy.Rational, skoSP:sympy.Rational, skoSM:sympy.Rational):
	# (0 <= delta) & (1 > skoX) & (skoS2 > 0) & (skoSM > 0) & (skoSP > 0) & (skoX > 0) & (skoS2**2 - 2 <= delta) & (2 - skoS2**2 <= delta) & ~((-skoSP**2 + skoX + 1 <= delta) & (skoSP**2 - skoX - 1 <= delta))

	post_cond =  And(LessThan(Integer(0), Symbol('delta')), StrictGreaterThan(Integer(1), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoSP'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), LessThan(Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Symbol('delta')), LessThan(Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Symbol('delta')), Not(And(LessThan(Add(Mul(Integer(-1), Pow(Symbol('skoSP'), Integer(2))), Symbol('skoX'), Integer(1)), Symbol('delta')), LessThan(Add(Pow(Symbol('skoSP'), Integer(2)), Mul(Integer(-1), Symbol('skoX')), Integer(-1)), Symbol('delta')))))

	eval = post_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'skoSP':skoSP, 'skoSM':skoSM })

	return eval == sympy.logic.boolalg.BooleanTrue





if __name__=="__main__":
	
	ip_0=int(input("enter integer numerator of delta:\n"))
	ip_1=int(input("enter integer denominator of delta:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	delta=sympy.Rational(ip_0,ip_1)
	
	
	ip_0=int(input("enter integer numerator of skoX:\n"))
	ip_1=int(input("enter integer denominator of skoX:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	skoX=sympy.Rational(ip_0,ip_1)
	
	
	ip_0=int(input("enter integer numerator of skoS2:\n"))
	ip_1=int(input("enter integer denominator of skoS2:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	skoS2=sympy.Rational(ip_0,ip_1)
	
	
	
	
	if pre_condition_0(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_0 SAT")
		print('delta = 3/2')
		print('skoX = 7/8')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 1/2')
		exit(0)
	
	
	if pre_condition_1(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_1 SAT")
		print('delta = 3/2')
		print('skoX = 7/8')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 1/2')
		exit(0)
	
	
	if pre_condition_2(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_2 SAT")
		print('delta = 1')
		print('skoX = 1/8')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 2')
		exit(0)
	
	
	if pre_condition_3(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_3 SAT")
		print('delta = 1')
		print('skoX = 1/8')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 2')
		exit(0)
	
	
	if pre_condition_4(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_4 SAT")
		print('delta = 3')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 3')
		exit(0)
	
	
	if pre_condition_5(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_5 SAT")
		print('delta = 3')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 3')
		exit(0)
	
	
	if pre_condition_6(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_6 SAT")
		print('delta = 8')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 4')
		exit(0)
	
	
	if pre_condition_7(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_7 SAT")
		print('delta = 8')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 4')
		exit(0)
	
	
	if pre_condition_8(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_8 SAT")
		print('delta = 15')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 5')
		exit(0)
	
	
	if pre_condition_9(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_9 SAT")
		print('delta = 15')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 5')
		exit(0)
	
	
	if pre_condition_10(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_10 SAT")
		print('delta = 24')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 6')
		exit(0)
	
	
	if pre_condition_11(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_11 SAT")
		print('delta = 24')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 6')
		exit(0)
	
	
	if pre_condition_12(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_12 SAT")
		print('delta = 35')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 7')
		exit(0)
	
	
	if pre_condition_13(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_13 SAT")
		print('delta = 35')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 7')
		exit(0)
	
	
	if pre_condition_14(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_14 SAT")
		print('delta = 48')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 8')
		exit(0)
	
	
	if pre_condition_15(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_15 SAT")
		print('delta = 48')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 8')
		exit(0)
	
	
	if pre_condition_16(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_16 SAT")
		print('delta = 63')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 9')
		exit(0)
	
	
	if pre_condition_17(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_17 SAT")
		print('delta = 63')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 9')
		exit(0)
	
	
	if pre_condition_18(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_18 SAT")
		print('delta = 80')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 10')
		exit(0)
	
	
	if pre_condition_19(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_19 SAT")
		print('delta = 80')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 10')
		exit(0)
	
	
	if pre_condition_20(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_20 SAT")
		print('delta = 99')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 11')
		exit(0)
	
	
	if pre_condition_21(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_21 SAT")
		print('delta = 99')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 11')
		exit(0)
	
	
	if pre_condition_22(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_22 SAT")
		print('delta = 120')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 12')
		exit(0)
	
	
	if pre_condition_23(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_23 SAT")
		print('delta = 120')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 12')
		exit(0)
	
	
	if pre_condition_24(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_24 SAT")
		print('delta = 143')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 13')
		exit(0)
	
	
	if pre_condition_25(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_25 SAT")
		print('delta = 143')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 13')
		exit(0)
	
	
	if pre_condition_26(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_26 SAT")
		print('delta = 168')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 14')
		exit(0)
	
	
	if pre_condition_27(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_27 SAT")
		print('delta = 168')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 14')
		exit(0)
	
	
	if pre_condition_28(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_28 SAT")
		print('delta = 195')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 15')
		exit(0)
	
	
	if pre_condition_29(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_29 SAT")
		print('delta = 195')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 15')
		exit(0)
	
	
	if pre_condition_30(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_30 SAT")
		print('delta = 224')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 16')
		exit(0)
	
	
	if pre_condition_31(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_31 SAT")
		print('delta = 224')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 16')
		exit(0)
	
	
	if pre_condition_32(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_32 SAT")
		print('delta = 255')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 17')
		exit(0)
	
	
	if pre_condition_33(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_33 SAT")
		print('delta = 255')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 17')
		exit(0)
	
	
	if pre_condition_34(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_34 SAT")
		print('delta = 288')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 18')
		exit(0)
	
	
	if pre_condition_35(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_35 SAT")
		print('delta = 288')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 18')
		exit(0)
	
	
	if pre_condition_36(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_36 SAT")
		print('delta = 323')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 19')
		exit(0)
	
	
	if pre_condition_37(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_37 SAT")
		print('delta = 323')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 19')
		exit(0)
	
	
	if pre_condition_38(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_38 SAT")
		print('delta = 360')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 20')
		exit(0)
	
	
	if pre_condition_39(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_39 SAT")
		print('delta = 360')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 20')
		exit(0)
	
	
	if pre_condition_40(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_40 SAT")
		print('delta = 399')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 21')
		exit(0)
	
	
	if pre_condition_41(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_41 SAT")
		print('delta = 399')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 21')
		exit(0)
	
	
	if pre_condition_42(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_42 SAT")
		print('delta = 440')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 22')
		exit(0)
	
	
	if pre_condition_43(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_43 SAT")
		print('delta = 440')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 22')
		exit(0)
	
	
	if pre_condition_44(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_44 SAT")
		print('delta = 483')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 23')
		exit(0)
	
	
	if pre_condition_45(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_45 SAT")
		print('delta = 483')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 23')
		exit(0)
	
	
	if pre_condition_46(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_46 SAT")
		print('delta = 528')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 24')
		exit(0)
	
	
	if pre_condition_47(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_47 SAT")
		print('delta = 528')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 24')
		exit(0)
	
	
	if pre_condition_48(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_48 SAT")
		print('delta = 575')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 25')
		exit(0)
	
	
	if pre_condition_49(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_49 SAT")
		print('delta = 575')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 25')
		exit(0)
	
	
	if pre_condition_50(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_50 SAT")
		print('delta = 624')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 26')
		exit(0)
	
	
	if pre_condition_51(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_51 SAT")
		print('delta = 624')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 26')
		exit(0)
	
	
	if pre_condition_52(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_52 SAT")
		print('delta = 675')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 27')
		exit(0)
	
	
	if pre_condition_53(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_53 SAT")
		print('delta = 675')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 27')
		exit(0)
	
	
	if pre_condition_54(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_54 SAT")
		print('delta = 728')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 28')
		exit(0)
	
	
	if pre_condition_55(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_55 SAT")
		print('delta = 728')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 28')
		exit(0)
	
	
	if pre_condition_56(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_56 SAT")
		print('delta = 783')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 29')
		exit(0)
	
	
	if pre_condition_57(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_57 SAT")
		print('delta = 783')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 29')
		exit(0)
	
	
	if pre_condition_58(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_58 SAT")
		print('delta = 840')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 30')
		exit(0)
	
	
	if pre_condition_59(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_59 SAT")
		print('delta = 840')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 30')
		exit(0)
	
	
	if pre_condition_60(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_60 SAT")
		print('delta = 899')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 31')
		exit(0)
	
	
	if pre_condition_61(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_61 SAT")
		print('delta = 899')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 31')
		exit(0)
	
	
	if pre_condition_62(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_62 SAT")
		print('delta = 960')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 32')
		exit(0)
	
	
	if pre_condition_63(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_63 SAT")
		print('delta = 960')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 32')
		exit(0)
	
	
	if pre_condition_64(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_64 SAT")
		print('delta = 1023')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 33')
		exit(0)
	
	
	if pre_condition_65(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_65 SAT")
		print('delta = 1023')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 33')
		exit(0)
	
	
	if pre_condition_66(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_66 SAT")
		print('delta = 1088')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 34')
		exit(0)
	
	
	if pre_condition_67(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_67 SAT")
		print('delta = 1088')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 34')
		exit(0)
	
	
	if pre_condition_68(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_68 SAT")
		print('delta = 1155')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 35')
		exit(0)
	
	
	if pre_condition_69(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_69 SAT")
		print('delta = 1155')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 35')
		exit(0)
	
	
	if pre_condition_70(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_70 SAT")
		print('delta = 1224')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 36')
		exit(0)
	
	
	if pre_condition_71(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_71 SAT")
		print('delta = 1224')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 36')
		exit(0)
	
	
	if pre_condition_72(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_72 SAT")
		print('delta = 1295')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 37')
		exit(0)
	
	
	if pre_condition_73(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_73 SAT")
		print('delta = 1295')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 37')
		exit(0)
	
	
	if pre_condition_74(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_74 SAT")
		print('delta = 1368')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 38')
		exit(0)
	
	
	if pre_condition_75(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_75 SAT")
		print('delta = 1368')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 38')
		exit(0)
	
	
	if pre_condition_76(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_76 SAT")
		print('delta = 1443')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 39')
		exit(0)
	
	
	if pre_condition_77(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_77 SAT")
		print('delta = 1443')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 39')
		exit(0)
	
	
	if pre_condition_78(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_78 SAT")
		print('delta = 1520')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 40')
		exit(0)
	
	
	if pre_condition_79(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_79 SAT")
		print('delta = 1520')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 40')
		exit(0)
	
	
	if pre_condition_80(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_80 SAT")
		print('delta = 1599')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 41')
		exit(0)
	
	
	if pre_condition_81(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_81 SAT")
		print('delta = 1599')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 41')
		exit(0)
	
	
	if pre_condition_82(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_82 SAT")
		print('delta = 1680')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 42')
		exit(0)
	
	
	if pre_condition_83(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_83 SAT")
		print('delta = 1680')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 42')
		exit(0)
	
	
	if pre_condition_84(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_84 SAT")
		print('delta = 1763')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 43')
		exit(0)
	
	
	if pre_condition_85(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_85 SAT")
		print('delta = 1763')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 43')
		exit(0)
	
	
	if pre_condition_86(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_86 SAT")
		print('delta = 1848')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 44')
		exit(0)
	
	
	if pre_condition_87(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_87 SAT")
		print('delta = 1848')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 44')
		exit(0)
	
	
	if pre_condition_88(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_88 SAT")
		print('delta = 1935')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 45')
		exit(0)
	
	
	if pre_condition_89(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_89 SAT")
		print('delta = 1935')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 45')
		exit(0)
	
	
	if pre_condition_90(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_90 SAT")
		print('delta = 2024')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 46')
		exit(0)
	
	
	if pre_condition_91(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_91 SAT")
		print('delta = 2024')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 46')
		exit(0)
	
	
	if pre_condition_92(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_92 SAT")
		print('delta = 2115')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 47')
		exit(0)
	
	
	if pre_condition_93(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_93 SAT")
		print('delta = 2115')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 47')
		exit(0)
	
	
	if pre_condition_94(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_94 SAT")
		print('delta = 2208')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 48')
		exit(0)
	
	
	if pre_condition_95(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_95 SAT")
		print('delta = 2208')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 48')
		exit(0)
	
	
	if pre_condition_96(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_96 SAT")
		print('delta = 2303')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 49')
		exit(0)
	
	
	if pre_condition_97(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_97 SAT")
		print('delta = 2303')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 49')
		exit(0)
	
	
	if pre_condition_98(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_98 SAT")
		print('delta = 2400')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 50')
		exit(0)
	
	
	if pre_condition_99(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_99 SAT")
		print('delta = 2400')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 50')
		exit(0)
	
	
	if pre_condition_100(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_100 SAT")
		print('delta = 2499')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 51')
		exit(0)
	
	
	if pre_condition_101(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_101 SAT")
		print('delta = 2499')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 51')
		exit(0)
	
	
	if pre_condition_102(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_102 SAT")
		print('delta = 2600')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 52')
		exit(0)
	
	
	if pre_condition_103(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_103 SAT")
		print('delta = 2600')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 52')
		exit(0)
	
	
	if pre_condition_104(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_104 SAT")
		print('delta = 2703')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 53')
		exit(0)
	
	
	if pre_condition_105(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_105 SAT")
		print('delta = 2703')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 53')
		exit(0)
	
	
	if pre_condition_106(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_106 SAT")
		print('delta = 2808')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 54')
		exit(0)
	
	
	if pre_condition_107(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_107 SAT")
		print('delta = 2808')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 54')
		exit(0)
	
	
	if pre_condition_108(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_108 SAT")
		print('delta = 2915')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 55')
		exit(0)
	
	
	if pre_condition_109(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_109 SAT")
		print('delta = 2915')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 55')
		exit(0)
	
	
	if pre_condition_110(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_110 SAT")
		print('delta = 3024')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 56')
		exit(0)
	
	
	if pre_condition_111(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_111 SAT")
		print('delta = 3024')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 56')
		exit(0)
	
	
	if pre_condition_112(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_112 SAT")
		print('delta = 3135')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 57')
		exit(0)
	
	
	if pre_condition_113(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_113 SAT")
		print('delta = 3135')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 57')
		exit(0)
	
	
	if pre_condition_114(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_114 SAT")
		print('delta = 3248')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 58')
		exit(0)
	
	
	if pre_condition_115(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_115 SAT")
		print('delta = 3248')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 58')
		exit(0)
	
	
	if pre_condition_116(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_116 SAT")
		print('delta = 3363')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 59')
		exit(0)
	
	
	if pre_condition_117(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_117 SAT")
		print('delta = 3363')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 59')
		exit(0)
	
	
	if pre_condition_118(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_118 SAT")
		print('delta = 3480')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 60')
		exit(0)
	
	
	if pre_condition_119(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_119 SAT")
		print('delta = 3480')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 60')
		exit(0)
	
	
	if pre_condition_120(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_120 SAT")
		print('delta = 3599')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 61')
		exit(0)
	
	
	if pre_condition_121(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_121 SAT")
		print('delta = 3599')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 61')
		exit(0)
	
	
	if pre_condition_122(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_122 SAT")
		print('delta = 3720')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 62')
		exit(0)
	
	
	if pre_condition_123(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_123 SAT")
		print('delta = 3720')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 62')
		exit(0)
	
	
	if pre_condition_124(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_124 SAT")
		print('delta = 3843')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 63')
		exit(0)
	
	
	if pre_condition_125(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_125 SAT")
		print('delta = 3843')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 63')
		exit(0)
	
	
	if pre_condition_126(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_126 SAT")
		print('delta = 3968')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 64')
		exit(0)
	
	
	if pre_condition_127(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_127 SAT")
		print('delta = 3968')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 64')
		exit(0)
	
	
	if pre_condition_128(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_128 SAT")
		print('delta = 4095')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 65')
		exit(0)
	
	
	if pre_condition_129(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_129 SAT")
		print('delta = 4095')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 65')
		exit(0)
	
	
	if pre_condition_130(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_130 SAT")
		print('delta = 4224')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 66')
		exit(0)
	
	
	if pre_condition_131(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_131 SAT")
		print('delta = 4224')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 66')
		exit(0)
	
	
	if pre_condition_132(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_132 SAT")
		print('delta = 4355')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 67')
		exit(0)
	
	
	if pre_condition_133(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_133 SAT")
		print('delta = 4355')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 67')
		exit(0)
	
	
	if pre_condition_134(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_134 SAT")
		print('delta = 4488')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 68')
		exit(0)
	
	
	if pre_condition_135(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_135 SAT")
		print('delta = 4488')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 68')
		exit(0)
	
	
	if pre_condition_136(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_136 SAT")
		print('delta = 4623')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 69')
		exit(0)
	
	
	if pre_condition_137(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_137 SAT")
		print('delta = 4623')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 69')
		exit(0)
	
	
	if pre_condition_138(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_138 SAT")
		print('delta = 4760')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 70')
		exit(0)
	
	
	if pre_condition_139(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_139 SAT")
		print('delta = 4760')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 70')
		exit(0)
	
	
	if pre_condition_140(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_140 SAT")
		print('delta = 4899')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 71')
		exit(0)
	
	
	if pre_condition_141(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_141 SAT")
		print('delta = 4899')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 71')
		exit(0)
	
	
	if pre_condition_142(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_142 SAT")
		print('delta = 5040')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 72')
		exit(0)
	
	
	if pre_condition_143(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_143 SAT")
		print('delta = 5040')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 72')
		exit(0)
	
	
	if pre_condition_144(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_144 SAT")
		print('delta = 5183')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 73')
		exit(0)
	
	
	if pre_condition_145(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_145 SAT")
		print('delta = 5183')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 73')
		exit(0)
	
	
	if pre_condition_146(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_146 SAT")
		print('delta = 5328')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 74')
		exit(0)
	
	
	if pre_condition_147(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_147 SAT")
		print('delta = 5328')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 74')
		exit(0)
	
	
	if pre_condition_148(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_148 SAT")
		print('delta = 5475')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 75')
		exit(0)
	
	
	if pre_condition_149(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_149 SAT")
		print('delta = 5475')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 75')
		exit(0)
	
	
	if pre_condition_150(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_150 SAT")
		print('delta = 5624')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 76')
		exit(0)
	
	
	if pre_condition_151(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_151 SAT")
		print('delta = 5624')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 76')
		exit(0)
	
	
	if pre_condition_152(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_152 SAT")
		print('delta = 5775')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 77')
		exit(0)
	
	
	if pre_condition_153(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_153 SAT")
		print('delta = 5775')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 77')
		exit(0)
	
	
	if pre_condition_154(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_154 SAT")
		print('delta = 5928')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 78')
		exit(0)
	
	
	if pre_condition_155(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_155 SAT")
		print('delta = 5928')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 78')
		exit(0)
	
	
	if pre_condition_156(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_156 SAT")
		print('delta = 6083')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 79')
		exit(0)
	
	
	if pre_condition_157(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_157 SAT")
		print('delta = 6083')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 79')
		exit(0)
	
	
	if pre_condition_158(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_158 SAT")
		print('delta = 6240')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 80')
		exit(0)
	
	
	if pre_condition_159(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_159 SAT")
		print('delta = 6240')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 80')
		exit(0)
	
	
	if pre_condition_160(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_160 SAT")
		print('delta = 12797/2')
		print('skoX = 1/2')
		print('skoS2 = 1/2')
		print('skoSM = 1/2')
		print('skoSP = 12961/162')
		exit(0)
	
	
	if pre_condition_161(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_161 SAT")
		print('delta = 12797/2')
		print('skoX = 1/2')
		print('skoS2 = 1/2')
		print('skoSM = 1/2')
		print('skoSP = 12961/162')
		exit(0)
	
	
	if pre_condition_162(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_162 SAT")
		print('delta = 799935961553117/125000000000')
		print('skoX = 1/2')
		print('skoS2 = 1/2')
		print('skoSM = 1/2')
		print('skoSP = 5965920489618407/74562500000000')
		exit(0)
	
	
	if pre_condition_163(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_163 SAT")
		print('delta = 799935961553117/125000000000')
		print('skoX = 1/2')
		print('skoS2 = 1/2')
		print('skoSM = 1/2')
		print('skoSP = 5965920489618407/74562500000000')
		exit(0)
	
	
	if pre_condition_164(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_164 SAT")
		print('delta = 6400')
		print('skoX = 63/64')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 81')
		exit(0)
	
	
	if pre_condition_165(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_165 SAT")
		print('delta = 6400')
		print('skoX = 63/64')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 81')
		exit(0)
	
	
	if pre_condition_166(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_166 SAT")
		print('delta = 6560')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 82')
		exit(0)
	
	
	if pre_condition_167(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_167 SAT")
		print('delta = 6560')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 82')
		exit(0)
	
	
	if pre_condition_168(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_168 SAT")
		print('delta = 6723')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 83')
		exit(0)
	
	
	if pre_condition_169(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_169 SAT")
		print('delta = 6723')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 83')
		exit(0)
	
	
	if pre_condition_170(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_170 SAT")
		print('delta = 6888')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 84')
		exit(0)
	
	
	if pre_condition_171(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_171 SAT")
		print('delta = 6888')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 84')
		exit(0)
	
	
	if pre_condition_172(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_172 SAT")
		print('delta = 7055')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 85')
		exit(0)
	
	
	if pre_condition_173(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_173 SAT")
		print('delta = 7055')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 85')
		exit(0)
	
	
	if pre_condition_174(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_174 SAT")
		print('delta = 7224')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 86')
		exit(0)
	
	
	if pre_condition_175(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_175 SAT")
		print('delta = 7224')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 86')
		exit(0)
	
	
	if pre_condition_176(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_176 SAT")
		print('delta = 7395')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 87')
		exit(0)
	
	
	if pre_condition_177(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_177 SAT")
		print('delta = 7395')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 87')
		exit(0)
	
	
	if pre_condition_178(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_178 SAT")
		print('delta = 7568')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 88')
		exit(0)
	
	
	if pre_condition_179(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_179 SAT")
		print('delta = 7568')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 88')
		exit(0)
	
	
	if pre_condition_180(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_180 SAT")
		print('delta = 7743')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 89')
		exit(0)
	
	
	if pre_condition_181(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_181 SAT")
		print('delta = 7743')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 89')
		exit(0)
	
	
	if pre_condition_182(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_182 SAT")
		print('delta = 7920')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 90')
		exit(0)
	
	
	if pre_condition_183(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_183 SAT")
		print('delta = 7920')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 90')
		exit(0)
	
	
	if pre_condition_184(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_184 SAT")
		print('delta = 8099')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 91')
		exit(0)
	
	
	if pre_condition_185(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_185 SAT")
		print('delta = 8099')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 91')
		exit(0)
	
	
	if pre_condition_186(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_186 SAT")
		print('delta = 8280')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 92')
		exit(0)
	
	
	if pre_condition_187(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_187 SAT")
		print('delta = 8280')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 92')
		exit(0)
	
	
	if pre_condition_188(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_188 SAT")
		print('delta = 8463')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 93')
		exit(0)
	
	
	if pre_condition_189(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_189 SAT")
		print('delta = 8463')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 93')
		exit(0)
	
	
	if pre_condition_190(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_190 SAT")
		print('delta = 8648')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 94')
		exit(0)
	
	
	if pre_condition_191(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_191 SAT")
		print('delta = 8648')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 94')
		exit(0)
	
	
	if pre_condition_192(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_192 SAT")
		print('delta = 8835')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 95')
		exit(0)
	
	
	if pre_condition_193(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_193 SAT")
		print('delta = 8835')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 95')
		exit(0)
	
	
	if pre_condition_194(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_194 SAT")
		print('delta = 9024')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 96')
		exit(0)
	
	
	if pre_condition_195(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_195 SAT")
		print('delta = 9024')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 96')
		exit(0)
	
	
	if pre_condition_196(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_196 SAT")
		print('delta = 9215')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 97')
		exit(0)
	
	
	if pre_condition_197(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_197 SAT")
		print('delta = 9215')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 97')
		exit(0)
	
	
	if pre_condition_198(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_198 SAT")
		print('delta = 9408')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 98')
		exit(0)
	
	
	if pre_condition_199(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_199 SAT")
		print('delta = 9408')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 98')
		exit(0)
	
	
	if pre_condition_200(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_200 SAT")
		print('delta = 9603')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1/2')
		print('skoSP = 99')
		exit(0)


	print("UNKNOWN")
	exit(0)
