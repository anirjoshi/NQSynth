import sympy
from sympy import *

def pre_condition_0(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= skoX) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta >= -skoX) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta < skoSM**2 + skoX - 1) | (delta < -skoSM**2 - skoX + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= skoX) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta >= -skoX) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & ((delta + skoX < -3) | (delta - skoX < 3))

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(-3)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(3))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 9/16) & (delta >= skoS2**2 - 2) & (delta - skoX >= -9/16) & (delta >= 2 - skoS2**2) & ((delta < skoSM**2 + skoX - 1) | (delta < -skoSM**2 - skoX + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(9, 16)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-9, 16)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 9/16) & (delta >= skoS2**2 - 2) & (delta - skoX >= -9/16) & (delta >= 2 - skoS2**2) & ((delta + skoX < 1) | (delta - skoX < -1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(9, 16)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-9, 16)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(1)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-1))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_4(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 5/4) & (delta >= skoS2**2 - 2) & (delta - skoX >= -5/4) & (delta >= 2 - skoS2**2) & ((delta < skoSM**2 + skoX - 1) | (delta < -skoSM**2 - skoX + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(5, 4)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-5, 4)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_5(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 5/4) & (delta >= skoS2**2 - 2) & (delta - skoX >= -5/4) & (delta >= 2 - skoS2**2) & ((delta + skoX < -3) | (delta - skoX < 3))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(5, 4)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-5, 4)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(-3)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(3))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_6(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 57/64) & (delta >= skoS2**2 - 2) & (delta - skoX >= -57/64) & (delta >= 2 - skoS2**2) & ((delta < skoSM**2 + skoX - 1) | (delta < -skoSM**2 - skoX + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(57, 64)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-57, 64)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_7(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 57/64) & (delta >= skoS2**2 - 2) & (delta - skoX >= -57/64) & (delta >= 2 - skoS2**2) & ((delta < skoX) | (delta < -skoX))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(57, 64)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-57, 64)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoX')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_8(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 273/256) & (delta >= skoS2**2 - 2) & (delta - skoX >= -273/256) & (delta >= 2 - skoS2**2) & ((delta < skoSM**2 + skoX - 1) | (delta < -skoSM**2 - skoX + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(273, 256)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-273, 256)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_9(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 273/256) & (delta >= skoS2**2 - 2) & (delta - skoX >= -273/256) & (delta >= 2 - skoS2**2) & ((delta < skoX) | (delta < -skoX))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(273, 256)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-273, 256)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoX')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_10(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 185/256) & (delta >= skoS2**2 - 2) & (delta - skoX >= -185/256) & (delta >= 2 - skoS2**2) & ((delta < skoSM**2 + skoX - 1) | (delta < -skoSM**2 - skoX + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(185, 256)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-185, 256)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_11(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 185/256) & (delta >= skoS2**2 - 2) & (delta - skoX >= -185/256) & (delta >= 2 - skoS2**2) & ((delta < skoX) | (delta < -skoX))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(185, 256)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-185, 256)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoX')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_12(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 657/1024) & (delta >= skoS2**2 - 2) & (delta - skoX >= -657/1024) & (delta >= 2 - skoS2**2) & ((delta < skoSM**2 + skoX - 1) | (delta < -skoSM**2 - skoX + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(657, 1024)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-657, 1024)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_13(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 657/1024) & (delta >= skoS2**2 - 2) & (delta - skoX >= -657/1024) & (delta >= 2 - skoS2**2) & ((delta < skoX) | (delta < -skoX))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(657, 1024)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-657, 1024)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoX')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_14(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 2465/4096) & (delta >= skoS2**2 - 2) & (delta - skoX >= -2465/4096) & (delta >= 2 - skoS2**2) & ((delta < skoSM**2 + skoX - 1) | (delta < -skoSM**2 - skoX + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(2465, 4096)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-2465, 4096)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_15(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 2465/4096) & (delta >= skoS2**2 - 2) & (delta - skoX >= -2465/4096) & (delta >= 2 - skoS2**2) & ((delta < skoX) | (delta < -skoX))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(2465, 4096)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-2465, 4096)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoX')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_16(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 9537/16384) & (delta >= skoS2**2 - 2) & (delta - skoX >= -9537/16384) & (delta >= 2 - skoS2**2) & ((delta < skoSM**2 + skoX - 1) | (delta < -skoSM**2 - skoX + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(9537, 16384)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-9537, 16384)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_17(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 9537/16384) & (delta >= skoS2**2 - 2) & (delta - skoX >= -9537/16384) & (delta >= 2 - skoS2**2) & ((delta < skoX) | (delta < -skoX))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(9537, 16384)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-9537, 16384)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoX')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_18(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 37505/65536) & (delta >= skoS2**2 - 2) & (delta - skoX >= -37505/65536) & (delta >= 2 - skoS2**2) & ((delta < skoSM**2 + skoX - 1) | (delta < -skoSM**2 - skoX + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(37505, 65536)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-37505, 65536)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_19(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 37505/65536) & (delta >= skoS2**2 - 2) & (delta - skoX >= -37505/65536) & (delta >= 2 - skoS2**2) & ((delta < skoX) | (delta < -skoX))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(37505, 65536)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-37505, 65536)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoX')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_20(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 148737/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= -148737/262144) & (delta >= 2 - skoS2**2) & ((delta < skoSM**2 + skoX - 1) | (delta < -skoSM**2 - skoX + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(148737, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-148737, 262144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_21(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 148737/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= -148737/262144) & (delta >= 2 - skoS2**2) & ((delta < skoX) | (delta < -skoX))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(148737, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-148737, 262144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoX')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_22(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 17/64) & (delta >= skoS2**2 - 2) & (delta - skoX >= -17/64) & (delta >= 2 - skoS2**2) & ((delta < skoSM**2 + skoX - 1) | (delta < -skoSM**2 - skoX + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(17, 64)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-17, 64)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_23(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 17/64) & (delta >= skoS2**2 - 2) & (delta - skoX >= -17/64) & (delta >= 2 - skoS2**2) & ((delta < skoX) | (delta < -skoX))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(17, 64)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-17, 64)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoX')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_24(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 33/256) & (delta >= skoS2**2 - 2) & (delta - skoX >= -33/256) & (delta >= 2 - skoS2**2) & ((delta < skoSM**2 + skoX - 1) | (delta < -skoSM**2 - skoX + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(33, 256)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-33, 256)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_25(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 33/256) & (delta >= skoS2**2 - 2) & (delta - skoX >= -33/256) & (delta >= 2 - skoS2**2) & ((delta < skoX) | (delta < -skoX))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(33, 256)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-33, 256)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoX')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_26(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 65/1024) & (delta >= skoS2**2 - 2) & (delta - skoX >= -65/1024) & (delta >= 2 - skoS2**2) & ((delta < skoSM**2 + skoX - 1) | (delta < -skoSM**2 - skoX + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(65, 1024)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-65, 1024)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_27(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 65/1024) & (delta >= skoS2**2 - 2) & (delta - skoX >= -65/1024) & (delta >= 2 - skoS2**2) & ((delta < skoX) | (delta < -skoX))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(65, 1024)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-65, 1024)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoX')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_28(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 129/4096) & (delta >= skoS2**2 - 2) & (delta - skoX >= -129/4096) & (delta >= 2 - skoS2**2) & ((delta < skoSM**2 + skoX - 1) | (delta < -skoSM**2 - skoX + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(129, 4096)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-129, 4096)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_29(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 129/4096) & (delta >= skoS2**2 - 2) & (delta - skoX >= -129/4096) & (delta >= 2 - skoS2**2) & ((delta < skoX) | (delta < -skoX))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(129, 4096)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-129, 4096)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoX')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_30(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 257/16384) & (delta >= skoS2**2 - 2) & (delta - skoX >= -257/16384) & (delta >= 2 - skoS2**2) & ((delta < skoSM**2 + skoX - 1) | (delta < -skoSM**2 - skoX + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(257, 16384)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-257, 16384)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_31(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 257/16384) & (delta >= skoS2**2 - 2) & (delta - skoX >= -257/16384) & (delta >= 2 - skoS2**2) & ((delta < skoX) | (delta < -skoX))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(257, 16384)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-257, 16384)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoX')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_32(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 513/65536) & (delta >= skoS2**2 - 2) & (delta - skoX >= -513/65536) & (delta >= 2 - skoS2**2) & ((delta < skoSM**2 + skoX - 1) | (delta < -skoSM**2 - skoX + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(513, 65536)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-513, 65536)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_33(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 513/65536) & (delta >= skoS2**2 - 2) & (delta - skoX >= -513/65536) & (delta >= 2 - skoS2**2) & ((delta < skoX) | (delta < -skoX))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(513, 65536)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-513, 65536)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoX')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_34(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 1025/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= -1025/262144) & (delta >= 2 - skoS2**2) & ((delta < skoSM**2 + skoX - 1) | (delta < -skoSM**2 - skoX + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(1025, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-1025, 262144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_35(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 1025/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= -1025/262144) & (delta >= 2 - skoS2**2) & ((delta < skoX) | (delta < -skoX))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(1025, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-1025, 262144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoX')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_36(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 2049/1048576) & (delta >= skoS2**2 - 2) & (delta - skoX >= -2049/1048576) & (delta >= 2 - skoS2**2) & ((delta < skoSM**2 + skoX - 1) | (delta < -skoSM**2 - skoX + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(2049, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-2049, 1048576)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_37(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 2049/1048576) & (delta >= skoS2**2 - 2) & (delta - skoX >= -2049/1048576) & (delta >= 2 - skoS2**2) & ((delta < skoX) | (delta < -skoX))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(2049, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-2049, 1048576)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoX')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_38(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 4097/4194304) & (delta >= skoS2**2 - 2) & (delta - skoX >= -4097/4194304) & (delta >= 2 - skoS2**2) & ((delta < skoSM**2 + skoX - 1) | (delta < -skoSM**2 - skoX + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(4097, 4194304)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-4097, 4194304)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_39(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 4097/4194304) & (delta >= skoS2**2 - 2) & (delta - skoX >= -4097/4194304) & (delta >= 2 - skoS2**2) & ((delta < skoX) | (delta < -skoX))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(4097, 4194304)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-4097, 4194304)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoX')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_40(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 4097/4194304) & (delta >= skoS2**2 - 2) & (delta - skoX >= -4097/4194304) & (delta >= 2 - skoS2**2) & ((delta < skoSM**2 + skoX - 1) | (delta < -skoSM**2 - skoX + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(4097, 4194304)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-4097, 4194304)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_41(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 4097/4194304) & (delta >= skoS2**2 - 2) & (delta - skoX >= -4097/4194304) & (delta >= 2 - skoS2**2) & ((delta < skoX) | (delta < -skoX))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(4097, 4194304)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-4097, 4194304)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoX')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_42(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 4097/4194304) & (delta >= skoS2**2 - 2) & (delta - skoX >= -4097/4194304) & (delta >= 2 - skoS2**2) & ((delta < skoSM**2 + skoX - 1) | (delta < -skoSM**2 - skoX + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(4097, 4194304)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-4097, 4194304)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_43(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 4097/4194304) & (delta >= skoS2**2 - 2) & (delta - skoX >= -4097/4194304) & (delta >= 2 - skoS2**2) & ((delta < skoX) | (delta < -skoX))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(4097, 4194304)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-4097, 4194304)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoX')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_44(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 4097/4194304) & (delta >= skoS2**2 - 2) & (delta - skoX >= -4097/4194304) & (delta >= 2 - skoS2**2) & ((delta < skoSM**2 + skoX - 1) | (delta < -skoSM**2 - skoX + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(4097, 4194304)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-4097, 4194304)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_45(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 4097/4194304) & (delta >= skoS2**2 - 2) & (delta - skoX >= -4097/4194304) & (delta >= 2 - skoS2**2) & ((delta < skoX) | (delta < -skoX))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(4097, 4194304)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-4097, 4194304)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoX')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_46(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 4097/4194304) & (delta >= skoS2**2 - 2) & (delta - skoX >= -4097/4194304) & (delta >= 2 - skoS2**2) & ((delta < skoSM**2 + skoX - 1) | (delta < -skoSM**2 - skoX + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(4097, 4194304)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-4097, 4194304)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_47(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 4097/4194304) & (delta >= skoS2**2 - 2) & (delta - skoX >= -4097/4194304) & (delta >= 2 - skoS2**2) & ((delta < skoX) | (delta < -skoX))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(4097, 4194304)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-4097, 4194304)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoX')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_48(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 4097/4194304) & (delta >= skoS2**2 - 2) & (delta - skoX >= -4097/4194304) & (delta >= 2 - skoS2**2) & ((delta < skoSM**2 + skoX - 1) | (delta < -skoSM**2 - skoX + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(4097, 4194304)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-4097, 4194304)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_49(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 4097/4194304) & (delta >= skoS2**2 - 2) & (delta - skoX >= -4097/4194304) & (delta >= 2 - skoS2**2) & ((delta < skoX) | (delta < -skoX))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(4097, 4194304)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-4097, 4194304)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoX')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_50(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 4097/4194304) & (delta >= skoS2**2 - 2) & (delta - skoX >= -4097/4194304) & (delta >= 2 - skoS2**2) & ((delta < skoSM**2 + skoX - 1) | (delta < -skoSM**2 - skoX + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(4097, 4194304)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-4097, 4194304)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_51(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 4097/4194304) & (delta >= skoS2**2 - 2) & (delta - skoX >= -4097/4194304) & (delta >= 2 - skoS2**2) & ((delta < skoX) | (delta < -skoX))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(4097, 4194304)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-4097, 4194304)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoX')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_52(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 4097/4194304) & (delta >= skoS2**2 - 2) & (delta - skoX >= -4097/4194304) & (delta >= 2 - skoS2**2) & ((delta < skoSM**2 + skoX - 1) | (delta < -skoSM**2 - skoX + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(4097, 4194304)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-4097, 4194304)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_53(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 4097/4194304) & (delta >= skoS2**2 - 2) & (delta - skoX >= -4097/4194304) & (delta >= 2 - skoS2**2) & ((delta < skoX) | (delta < -skoX))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(4097, 4194304)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-4097, 4194304)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoX')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_54(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 4097/4194304) & (delta >= skoS2**2 - 2) & (delta - skoX >= -4097/4194304) & (delta >= 2 - skoS2**2) & ((delta < skoSM**2 + skoX - 1) | (delta < -skoSM**2 - skoX + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(4097, 4194304)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-4097, 4194304)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_55(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 4097/4194304) & (delta >= skoS2**2 - 2) & (delta - skoX >= -4097/4194304) & (delta >= 2 - skoS2**2) & ((delta < skoX) | (delta < -skoX))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(4097, 4194304)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-4097, 4194304)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoX')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_56(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 4097/4194304) & (delta >= skoS2**2 - 2) & (delta - skoX >= -4097/4194304) & (delta >= 2 - skoS2**2) & ((delta < skoSM**2 + skoX - 1) | (delta < -skoSM**2 - skoX + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(4097, 4194304)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-4097, 4194304)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_57(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 4097/4194304) & (delta >= skoS2**2 - 2) & (delta - skoX >= -4097/4194304) & (delta >= 2 - skoS2**2) & ((delta < skoX) | (delta < -skoX))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(4097, 4194304)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-4097, 4194304)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoX')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_58(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 4097/4194304) & (delta >= skoS2**2 - 2) & (delta - skoX >= -4097/4194304) & (delta >= 2 - skoS2**2) & ((delta < skoSM**2 + skoX - 1) | (delta < -skoSM**2 - skoX + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(4097, 4194304)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-4097, 4194304)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_59(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 4097/4194304) & (delta >= skoS2**2 - 2) & (delta - skoX >= -4097/4194304) & (delta >= 2 - skoS2**2) & ((delta < skoX) | (delta < -skoX))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(4097, 4194304)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-4097, 4194304)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoX')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_60(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 24585/16777216) & (delta >= skoS2**2 - 2) & (delta - skoX >= -24585/16777216) & (delta >= 2 - skoS2**2) & ((delta < skoSM**2 + skoX - 1) | (delta < -skoSM**2 - skoX + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(24585, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-24585, 16777216)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_61(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 24585/16777216) & (delta >= skoS2**2 - 2) & (delta - skoX >= -24585/16777216) & (delta >= 2 - skoS2**2) & ((delta < skoX) | (delta < -skoX))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(24585, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-24585, 16777216)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoX')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_62(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoSM**2 + skoX - 1) | (delta < -skoSM**2 - skoX + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_63(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoX) | (delta < -skoX))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoX')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_64(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoSM**2 + skoX - 1) | (delta < -skoSM**2 - skoX + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_65(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoX) | (delta < -skoX))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoX')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_66(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoSM**2 + skoX - 1) | (delta < -skoSM**2 - skoX + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_67(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoX) | (delta < -skoX))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoX')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_68(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoSM**2 + skoX - 1) | (delta < -skoSM**2 - skoX + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_69(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoX) | (delta < -skoX))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoX')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_70(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 4097/4194304) & (delta >= skoS2**2 - 2) & (delta - skoX >= -4097/4194304) & (delta >= 2 - skoS2**2) & ((delta < skoSM**2 + skoX - 1) | (delta < -skoSM**2 - skoX + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(4097, 4194304)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-4097, 4194304)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_71(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 4097/4194304) & (delta >= skoS2**2 - 2) & (delta - skoX >= -4097/4194304) & (delta >= 2 - skoS2**2) & ((delta < skoX) | (delta < -skoX))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(4097, 4194304)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-4097, 4194304)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoX')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_72(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoSM**2 + skoX - 1) | (delta < -skoSM**2 - skoX + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_73(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoX) | (delta < -skoX))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoX')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_74(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoSM**2 + skoX - 1) | (delta < -skoSM**2 - skoX + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_75(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoX) | (delta < -skoX))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoX')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_76(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoSM**2 + skoX - 1) | (delta < -skoSM**2 - skoX + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_77(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoX) | (delta < -skoX))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoX')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_78(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoSM**2 + skoX - 1) | (delta < -skoSM**2 - skoX + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_79(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoX) | (delta < -skoX))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoX')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_80(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoSM**2 + skoX - 1) | (delta < -skoSM**2 - skoX + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_81(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoX) | (delta < -skoX))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoX')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_82(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoSM**2 + skoX - 1) | (delta < -skoSM**2 - skoX + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_83(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoX) | (delta < -skoX))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoX')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_84(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoSM**2 + skoX - 1) | (delta < -skoSM**2 - skoX + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_85(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoX) | (delta < -skoX))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoX')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_86(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoSM**2 + skoX - 1) | (delta < -skoSM**2 - skoX + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_87(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoX) | (delta < -skoX))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoX')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_88(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoSM**2 + skoX - 1) | (delta < -skoSM**2 - skoX + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_89(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoX) | (delta < -skoX))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoX')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_90(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoSM**2 + skoX - 1) | (delta < -skoSM**2 - skoX + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_91(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoX) | (delta < -skoX))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoX')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_92(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoSM**2 + skoX - 1) | (delta < -skoSM**2 - skoX + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_93(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoX) | (delta < -skoX))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoX')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_94(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoSM**2 + skoX - 1) | (delta < -skoSM**2 - skoX + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_95(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoX) | (delta < -skoX))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoX')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_96(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoSM**2 + skoX - 1) | (delta < -skoSM**2 - skoX + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_97(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoX) | (delta < -skoX))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoX')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_98(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoSM**2 + skoX - 1) | (delta < -skoSM**2 - skoX + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_99(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoX) | (delta < -skoX))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoX')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_100(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoSM**2 + skoX - 1) | (delta < -skoSM**2 - skoX + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_101(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoX) | (delta < -skoX))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoX')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_102(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoSM**2 + skoX - 1) | (delta < -skoSM**2 - skoX + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_103(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoX) | (delta < -skoX))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoX')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_104(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoSM**2 + skoX - 1) | (delta < -skoSM**2 - skoX + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_105(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoX) | (delta < -skoX))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoX')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_106(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoSM**2 + skoX - 1) | (delta < -skoSM**2 - skoX + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_107(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoX) | (delta < -skoX))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoX')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_108(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoSM**2 + skoX - 1) | (delta < -skoSM**2 - skoX + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_109(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoX) | (delta < -skoX))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoX')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_110(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoSM**2 + skoX - 1) | (delta < -skoSM**2 - skoX + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_111(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoX) | (delta < -skoX))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoX')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_112(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoSM**2 + skoX - 1) | (delta < -skoSM**2 - skoX + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_113(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoX) | (delta < -skoX))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoX')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_114(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoSM**2 + skoX - 1) | (delta < -skoSM**2 - skoX + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_115(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoX) | (delta < -skoX))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoX')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_116(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoSM**2 + skoX - 1) | (delta < -skoSM**2 - skoX + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_117(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoX) | (delta < -skoX))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoX')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_118(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoSM**2 + skoX - 1) | (delta < -skoSM**2 - skoX + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_119(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoX) | (delta < -skoX))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoX')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_120(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoSM**2 + skoX - 1) | (delta < -skoSM**2 - skoX + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_121(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoX) | (delta < -skoX))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoX')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_122(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoSM**2 + skoX - 1) | (delta < -skoSM**2 - skoX + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_123(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoX) | (delta < -skoX))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoX')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_124(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoSM**2 + skoX - 1) | (delta < -skoSM**2 - skoX + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_125(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoX) | (delta < -skoX))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoX')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_126(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoSM**2 + skoX - 1) | (delta < -skoSM**2 - skoX + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_127(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoX) | (delta < -skoX))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoX')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_128(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoSM**2 + skoX - 1) | (delta < -skoSM**2 - skoX + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_129(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoX) | (delta < -skoX))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoX')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_130(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoSM**2 + skoX - 1) | (delta < -skoSM**2 - skoX + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_131(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoX) | (delta < -skoX))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoX')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_132(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoSM**2 + skoX - 1) | (delta < -skoSM**2 - skoX + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_133(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoX) | (delta < -skoX))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoX')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_134(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoSM**2 + skoX - 1) | (delta < -skoSM**2 - skoX + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_135(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoX) | (delta < -skoX))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoX')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_136(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoSM**2 + skoX - 1) | (delta < -skoSM**2 - skoX + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_137(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoX) | (delta < -skoX))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoX')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_138(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoSM**2 + skoX - 1) | (delta < -skoSM**2 - skoX + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_139(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoX) | (delta < -skoX))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoX')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_140(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoSM**2 + skoX - 1) | (delta < -skoSM**2 - skoX + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_141(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoX) | (delta < -skoX))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoX')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_142(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoSM**2 + skoX - 1) | (delta < -skoSM**2 - skoX + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_143(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoX) | (delta < -skoX))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoX')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_144(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoSM**2 + skoX - 1) | (delta < -skoSM**2 - skoX + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_145(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoX) | (delta < -skoX))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoX')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_146(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoSM**2 + skoX - 1) | (delta < -skoSM**2 - skoX + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_147(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoX) | (delta < -skoX))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoX')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_148(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoSM**2 + skoX - 1) | (delta < -skoSM**2 - skoX + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_149(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoX) | (delta < -skoX))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoX')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_150(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoSM**2 + skoX - 1) | (delta < -skoSM**2 - skoX + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_151(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoX) | (delta < -skoX))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoX')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_152(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoSM**2 + skoX - 1) | (delta < -skoSM**2 - skoX + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_153(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoX) | (delta < -skoX))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoX')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_154(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoSM**2 + skoX - 1) | (delta < -skoSM**2 - skoX + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_155(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoX) | (delta < -skoX))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Symbol('skoX')), StrictLessThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_156(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 81945/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81945/67108864) & (delta >= 2 - skoS2**2) & ((delta < skoSM**2 + skoX - 1) | (delta < -skoSM**2 - skoX + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(81945, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81945, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), Or(StrictLessThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), StrictLessThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(delta:sympy.Rational, skoX:sympy.Rational, skoS2:sympy.Rational, pi:sympy.Rational, skoSP:sympy.Rational, skoSM:sympy.Rational):
	# (0 <= delta) & (0 <= skoS2) & (0 <= skoSM) & (0 <= skoSP) & (1 > skoX) & (31415927/10000000 > pi) & (pi > 15707963/5000000) & (skoX > 0) & (skoS2**2 - 2 <= delta) & (2 - skoS2**2 <= delta) & (-skoSP**2 + skoX + 1 <= delta) & (skoSP**2 - skoX - 1 <= delta) & ~((skoSM**2 + skoX - 1 <= delta) & (-skoSM**2 - skoX + 1 <= delta))

	post_cond =  And(LessThan(Integer(0), Symbol('delta')), LessThan(Integer(0), Symbol('skoS2')), LessThan(Integer(0), Symbol('skoSM')), LessThan(Integer(0), Symbol('skoSP')), StrictGreaterThan(Integer(1), Symbol('skoX')), StrictGreaterThan(Rational(31415927, 10000000), Symbol('pi')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), LessThan(Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Symbol('delta')), LessThan(Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Symbol('delta')), LessThan(Add(Mul(Integer(-1), Pow(Symbol('skoSP'), Integer(2))), Symbol('skoX'), Integer(1)), Symbol('delta')), LessThan(Add(Pow(Symbol('skoSP'), Integer(2)), Mul(Integer(-1), Symbol('skoX')), Integer(-1)), Symbol('delta')), Not(And(LessThan(Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1)), Symbol('delta')), LessThan(Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)), Symbol('delta')))))

	eval = post_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi, 'skoSP':skoSP, 'skoSM':skoSM })

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
	
	
	ip_0=int(input("enter integer numerator of pi:\n"))
	ip_1=int(input("enter integer denominator of pi:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	pi=sympy.Rational(ip_0,ip_1)
	
	
	
	
	if pre_condition_0(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_0 SAT")
		print('delta = 2')
		print('skoS2 = 1')
		print('skoSM = 2')
		print('skoSP = 1')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_1(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_1 SAT")
		print('delta = 2')
		print('skoS2 = 1')
		print('skoSM = 2')
		print('skoSP = 1')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_2(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_2 SAT")
		print('delta = 3/8')
		print('skoS2 = 3/2')
		print('skoSM = 0')
		print('skoSP = 5/4')
		print('skoX = 1/2')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_3(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_3 SAT")
		print('delta = 3/8')
		print('skoS2 = 3/2')
		print('skoSM = 0')
		print('skoSP = 5/4')
		print('skoX = 1/2')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_4(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_4 SAT")
		print('delta = 3/8')
		print('skoS2 = 3/2')
		print('skoSM = 2')
		print('skoSP = 3/2')
		print('skoX = 31/32')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_5(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_5 SAT")
		print('delta = 3/8')
		print('skoS2 = 3/2')
		print('skoSM = 2')
		print('skoSP = 3/2')
		print('skoX = 31/32')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_6(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_6 SAT")
		print('delta = 5/16')
		print('skoS2 = 3/2')
		print('skoSM = 1')
		print('skoSP = 11/8')
		print('skoX = 29/32')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_7(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_7 SAT")
		print('delta = 5/16')
		print('skoS2 = 3/2')
		print('skoSM = 1')
		print('skoSP = 11/8')
		print('skoX = 29/32')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_8(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_8 SAT")
		print('delta = 3/32')
		print('skoS2 = 23/16')
		print('skoSM = 1')
		print('skoSP = 23/16')
		print('skoX = 127/128')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_9(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_9 SAT")
		print('delta = 3/32')
		print('skoS2 = 23/16')
		print('skoSM = 1')
		print('skoSP = 23/16')
		print('skoX = 127/128')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_10(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_10 SAT")
		print('delta = 1/8')
		print('skoS2 = 11/8')
		print('skoSM = 1')
		print('skoSP = 21/16')
		print('skoX = 3/4')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_11(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_11 SAT")
		print('delta = 1/8')
		print('skoS2 = 11/8')
		print('skoSM = 1')
		print('skoSP = 21/16')
		print('skoX = 3/4')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_12(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_12 SAT")
		print('delta = 5/64')
		print('skoS2 = 23/16')
		print('skoSM = 1')
		print('skoSP = 41/32')
		print('skoX = 329/512')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_13(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_13 SAT")
		print('delta = 5/64')
		print('skoS2 = 23/16')
		print('skoSM = 1')
		print('skoSP = 41/32')
		print('skoX = 329/512')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_14(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_14 SAT")
		print('delta = 1/32')
		print('skoS2 = 45/32')
		print('skoSM = 1')
		print('skoSP = 81/64')
		print('skoX = 39/64')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_15(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_15 SAT")
		print('delta = 1/32')
		print('skoS2 = 45/32')
		print('skoSM = 1')
		print('skoSP = 81/64')
		print('skoX = 39/64')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_16(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_16 SAT")
		print('delta = 1/64')
		print('skoS2 = 181/128')
		print('skoSM = 1')
		print('skoSP = 161/128')
		print('skoX = 75/128')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_17(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_17 SAT")
		print('delta = 1/64')
		print('skoS2 = 181/128')
		print('skoSM = 1')
		print('skoSP = 161/128')
		print('skoX = 75/128')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_18(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_18 SAT")
		print('delta = 1/128')
		print('skoS2 = 181/128')
		print('skoSM = 1')
		print('skoSP = 321/256')
		print('skoX = 147/256')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_19(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_19 SAT")
		print('delta = 1/128')
		print('skoS2 = 181/128')
		print('skoSM = 1')
		print('skoSP = 321/256')
		print('skoX = 147/256')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_20(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_20 SAT")
		print('delta = 1/256')
		print('skoS2 = 181/128')
		print('skoSM = 1')
		print('skoSP = 641/512')
		print('skoX = 291/512')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_21(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_21 SAT")
		print('delta = 1/256')
		print('skoS2 = 181/128')
		print('skoSM = 1')
		print('skoSP = 641/512')
		print('skoX = 291/512')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_22(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_22 SAT")
		print('delta = 17/64')
		print('skoS2 = 3/2')
		print('skoSM = 1')
		print('skoSP = 9/8')
		print('skoX = 9/32')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_23(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_23 SAT")
		print('delta = 17/64')
		print('skoS2 = 3/2')
		print('skoSM = 1')
		print('skoSP = 9/8')
		print('skoX = 9/32')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_24(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_24 SAT")
		print('delta = 1/8')
		print('skoS2 = 11/8')
		print('skoSM = 1')
		print('skoSP = 17/16')
		print('skoX = 17/128')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_25(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_25 SAT")
		print('delta = 1/8')
		print('skoS2 = 11/8')
		print('skoSM = 1')
		print('skoSP = 17/16')
		print('skoX = 17/128')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_26(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_26 SAT")
		print('delta = 1/16')
		print('skoS2 = 45/32')
		print('skoSM = 1')
		print('skoSP = 33/32')
		print('skoX = 33/512')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_27(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_27 SAT")
		print('delta = 1/16')
		print('skoS2 = 45/32')
		print('skoSM = 1')
		print('skoSP = 33/32')
		print('skoX = 33/512')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_28(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_28 SAT")
		print('delta = 1/32')
		print('skoS2 = 45/32')
		print('skoSM = 1')
		print('skoSP = 65/64')
		print('skoX = 65/2048')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_29(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_29 SAT")
		print('delta = 1/32')
		print('skoS2 = 45/32')
		print('skoSM = 1')
		print('skoSP = 65/64')
		print('skoX = 65/2048')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_30(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_30 SAT")
		print('delta = 1/64')
		print('skoS2 = 181/128')
		print('skoSM = 1')
		print('skoSP = 129/128')
		print('skoX = 129/8192')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_31(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_31 SAT")
		print('delta = 1/64')
		print('skoS2 = 181/128')
		print('skoSM = 1')
		print('skoSP = 129/128')
		print('skoX = 129/8192')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_32(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_32 SAT")
		print('delta = 1/128')
		print('skoS2 = 181/128')
		print('skoSM = 1')
		print('skoSP = 257/256')
		print('skoX = 257/32768')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_33(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_33 SAT")
		print('delta = 1/128')
		print('skoS2 = 181/128')
		print('skoSM = 1')
		print('skoSP = 257/256')
		print('skoX = 257/32768')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_34(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_34 SAT")
		print('delta = 1/256')
		print('skoS2 = 181/128')
		print('skoSM = 1')
		print('skoSP = 513/512')
		print('skoX = 513/131072')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_35(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_35 SAT")
		print('delta = 1/256')
		print('skoS2 = 181/128')
		print('skoSM = 1')
		print('skoSP = 513/512')
		print('skoX = 513/131072')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_36(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_36 SAT")
		print('delta = 1/512')
		print('skoS2 = 181/128')
		print('skoSM = 1')
		print('skoSP = 1025/1024')
		print('skoX = 1025/524288')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_37(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_37 SAT")
		print('delta = 1/512')
		print('skoS2 = 181/128')
		print('skoSM = 1')
		print('skoSP = 1025/1024')
		print('skoX = 1025/524288')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_38(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_38 SAT")
		print('delta = 1/1024')
		print('skoS2 = 181/128')
		print('skoSM = 1')
		print('skoSP = 2049/2048')
		print('skoX = 2049/2097152')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_39(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_39 SAT")
		print('delta = 1/1024')
		print('skoS2 = 181/128')
		print('skoSM = 1')
		print('skoSP = 2049/2048')
		print('skoX = 2049/2097152')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_40(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_40 SAT")
		print('delta = 1/2048')
		print('skoS2 = 181/128')
		print('skoSM = 1')
		print('skoSP = 2049/2048')
		print('skoX = 18023194602504193/36893488147419103232')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_41(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_41 SAT")
		print('delta = 1/2048')
		print('skoS2 = 181/128')
		print('skoSM = 1')
		print('skoSP = 2049/2048')
		print('skoX = 18023194602504193/36893488147419103232')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_42(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_42 SAT")
		print('delta = 1/2048')
		print('skoS2 = 181/128')
		print('skoSM = 1')
		print('skoSP = 2049/2048')
		print('skoX = 18023194602504193/36893488147419103232')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_43(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_43 SAT")
		print('delta = 1/2048')
		print('skoS2 = 181/128')
		print('skoSM = 1')
		print('skoSP = 2049/2048')
		print('skoX = 18023194602504193/36893488147419103232')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_44(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_44 SAT")
		print('delta = 1/2048')
		print('skoS2 = 181/128')
		print('skoSM = 1')
		print('skoSP = 2049/2048')
		print('skoX = 18023194602504193/36893488147419103232')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_45(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_45 SAT")
		print('delta = 1/2048')
		print('skoS2 = 181/128')
		print('skoSM = 1')
		print('skoSP = 2049/2048')
		print('skoX = 18023194602504193/36893488147419103232')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_46(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_46 SAT")
		print('delta = 1/2048')
		print('skoS2 = 181/128')
		print('skoSM = 1')
		print('skoSP = 2049/2048')
		print('skoX = 18023194602504193/36893488147419103232')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_47(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_47 SAT")
		print('delta = 1/2048')
		print('skoS2 = 181/128')
		print('skoSM = 1')
		print('skoSP = 2049/2048')
		print('skoX = 18023194602504193/36893488147419103232')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_48(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_48 SAT")
		print('delta = 1/2048')
		print('skoS2 = 181/128')
		print('skoSM = 1')
		print('skoSP = 2049/2048')
		print('skoX = 18023194602504193/36893488147419103232')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_49(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_49 SAT")
		print('delta = 1/2048')
		print('skoS2 = 181/128')
		print('skoSM = 1')
		print('skoSP = 2049/2048')
		print('skoX = 18023194602504193/36893488147419103232')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_50(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_50 SAT")
		print('delta = 1/2048')
		print('skoS2 = 181/128')
		print('skoSM = 1')
		print('skoSP = 2049/2048')
		print('skoX = 18023194602504193/36893488147419103232')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_51(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_51 SAT")
		print('delta = 1/2048')
		print('skoS2 = 181/128')
		print('skoSM = 1')
		print('skoSP = 2049/2048')
		print('skoX = 18023194602504193/36893488147419103232')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_52(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_52 SAT")
		print('delta = 1/2048')
		print('skoS2 = 181/128')
		print('skoSM = 1')
		print('skoSP = 2049/2048')
		print('skoX = 18023194602504193/36893488147419103232')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_53(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_53 SAT")
		print('delta = 1/2048')
		print('skoS2 = 181/128')
		print('skoSM = 1')
		print('skoSP = 2049/2048')
		print('skoX = 18023194602504193/36893488147419103232')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_54(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_54 SAT")
		print('delta = 1/2048')
		print('skoS2 = 181/128')
		print('skoSM = 1')
		print('skoSP = 2049/2048')
		print('skoX = 18023194602504193/36893488147419103232')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_55(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_55 SAT")
		print('delta = 1/2048')
		print('skoS2 = 181/128')
		print('skoSM = 1')
		print('skoSP = 2049/2048')
		print('skoX = 18023194602504193/36893488147419103232')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_56(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_56 SAT")
		print('delta = 1/2048')
		print('skoS2 = 181/128')
		print('skoSM = 1')
		print('skoSP = 2049/2048')
		print('skoX = 18023194602504193/36893488147419103232')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_57(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_57 SAT")
		print('delta = 1/2048')
		print('skoS2 = 181/128')
		print('skoSM = 1')
		print('skoSP = 2049/2048')
		print('skoX = 18023194602504193/36893488147419103232')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_58(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_58 SAT")
		print('delta = 1/2048')
		print('skoS2 = 181/128')
		print('skoSM = 1')
		print('skoSP = 2049/2048')
		print('skoX = 18023194602504193/36893488147419103232')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_59(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_59 SAT")
		print('delta = 1/2048')
		print('skoS2 = 181/128')
		print('skoSM = 1')
		print('skoSP = 2049/2048')
		print('skoX = 18023194602504193/36893488147419103232')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_60(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_60 SAT")
		print('delta = 1/2048')
		print('skoS2 = 181/128')
		print('skoSM = 1')
		print('skoSP = 4099/4096')
		print('skoX = 3073/2097152')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_61(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_61 SAT")
		print('delta = 1/2048')
		print('skoS2 = 181/128')
		print('skoSM = 1')
		print('skoSP = 4099/4096')
		print('skoX = 3073/2097152')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_62(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_62 SAT")
		print('delta = 1/4096')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 2561/2097152')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_63(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_63 SAT")
		print('delta = 1/4096')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 2561/2097152')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_64(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_64 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_65(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_65 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_66(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_66 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_67(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_67 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_68(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_68 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_69(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_69 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_70(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_70 SAT")
		print('delta = 1/2048')
		print('skoS2 = 181/128')
		print('skoSM = 1')
		print('skoSP = 2049/2048')
		print('skoX = 18023194602504193/36893488147419103232')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_71(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_71 SAT")
		print('delta = 1/2048')
		print('skoS2 = 181/128')
		print('skoSM = 1')
		print('skoSP = 2049/2048')
		print('skoX = 18023194602504193/36893488147419103232')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_72(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_72 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_73(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_73 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_74(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_74 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_75(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_75 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_76(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_76 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_77(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_77 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_78(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_78 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_79(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_79 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_80(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_80 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_81(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_81 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_82(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_82 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_83(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_83 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_84(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_84 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_85(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_85 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_86(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_86 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_87(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_87 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_88(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_88 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_89(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_89 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_90(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_90 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_91(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_91 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_92(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_92 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_93(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_93 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_94(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_94 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_95(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_95 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_96(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_96 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_97(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_97 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_98(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_98 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_99(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_99 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_100(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_100 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_101(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_101 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_102(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_102 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_103(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_103 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_104(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_104 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_105(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_105 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_106(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_106 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_107(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_107 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_108(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_108 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_109(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_109 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_110(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_110 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_111(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_111 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_112(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_112 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_113(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_113 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_114(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_114 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_115(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_115 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_116(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_116 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_117(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_117 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_118(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_118 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_119(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_119 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_120(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_120 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_121(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_121 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_122(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_122 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_123(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_123 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_124(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_124 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_125(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_125 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_126(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_126 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_127(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_127 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_128(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_128 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_129(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_129 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_130(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_130 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_131(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_131 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_132(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_132 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_133(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_133 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_134(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_134 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_135(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_135 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_136(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_136 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_137(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_137 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_138(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_138 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_139(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_139 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_140(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_140 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_141(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_141 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_142(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_142 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_143(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_143 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_144(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_144 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_145(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_145 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_146(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_146 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_147(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_147 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_148(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_148 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_149(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_149 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_150(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_150 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_151(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_151 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_152(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_152 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_153(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_153 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_154(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_154 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_155(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_155 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)
	
	
	if pre_condition_156(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_156 SAT")
		print('delta = 1/8192')
		print('skoS2 = 11585/8192')
		print('skoSM = 1')
		print('skoSP = 8197/8192')
		print('skoX = 162184562166726657/147573952589676412928')
		print('pi = 62831853/20000000')
		exit(0)


	print("UNKNOWN")
	exit(0)
