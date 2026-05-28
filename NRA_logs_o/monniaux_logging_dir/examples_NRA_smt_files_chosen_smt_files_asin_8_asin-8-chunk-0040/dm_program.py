import sympy
from sympy import *

def pre_condition_0(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= -3/4) & (delta >= skoS2**2 - 2) & (delta - skoX >= 3/4) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (pi*skoS2/2 + pi/4 + 1/40 <= skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-3, 4)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(3, 4)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), LessThan(Add(Mul(Rational(1, 2), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 4), Symbol('pi')), Rational(1, 40)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= skoX) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -3/4) & (delta >= skoS2**2 - 2) & (delta - skoX >= 3/4) & (delta >= 2 - skoS2**2) & (pi*skoS2 + pi/2 - 1/4 >= pi*skoS2/2 + pi/4 + 1/40)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-3, 4)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(3, 4)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Add(Mul(Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 2), Symbol('pi')), Rational(-1, 4)), Add(Mul(Rational(1, 2), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 4), Symbol('pi')), Rational(1, 40))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= -7/16) & (delta >= skoS2**2 - 2) & (delta - skoX >= 7/16) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (3*pi*skoS2/4 + 3*pi/8 + 3/80 <= skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-7, 16)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(7, 16)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), LessThan(Add(Mul(Rational(3, 4), Symbol('pi'), Symbol('skoS2')), Mul(Rational(3, 8), Symbol('pi')), Rational(3, 80)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= skoX) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -7/16) & (delta >= skoS2**2 - 2) & (delta - skoX >= 7/16) & (delta >= 2 - skoS2**2) & (pi*skoS2 + pi/2 - 1/4 >= 3*pi*skoS2/4 + 3*pi/8 + 3/80)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-7, 16)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(7, 16)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Add(Mul(Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 2), Symbol('pi')), Rational(-1, 4)), Add(Mul(Rational(3, 4), Symbol('pi'), Symbol('skoS2')), Mul(Rational(3, 8), Symbol('pi')), Rational(3, 80))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_4(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= skoX) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta >= -skoX) & (delta >= skoS2**2 - 2) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (pi*skoS2 + pi/2 + 1/20 <= skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), LessThan(Add(Mul(Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 2), Symbol('pi')), Rational(1, 20)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_5(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= skoX) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -17/64) & (delta >= skoS2**2 - 2) & (delta - skoX >= 17/64) & (delta >= 2 - skoS2**2) & (pi*skoS2 + pi/2 + 1/20 <= 9*pi*skoS2/8 + 9*pi/16 - 41/160)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-17, 64)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(17, 64)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), LessThan(Add(Mul(Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 2), Symbol('pi')), Rational(1, 20)), Add(Mul(Rational(9, 8), Symbol('pi'), Symbol('skoS2')), Mul(Rational(9, 16), Symbol('pi')), Rational(-41, 160))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_6(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= -15/64) & (delta >= skoS2**2 - 2) & (delta - skoX >= 15/64) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (7*pi*skoS2/8 + 7*pi/16 + 7/160 <= skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-15, 64)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(15, 64)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), LessThan(Add(Mul(Rational(7, 8), Symbol('pi'), Symbol('skoS2')), Mul(Rational(7, 16), Symbol('pi')), Rational(7, 160)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_7(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= skoX) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -15/64) & (delta >= skoS2**2 - 2) & (delta - skoX >= 15/64) & (delta >= 2 - skoS2**2) & (pi*skoS2 + pi/2 - 1/4 >= 7*pi*skoS2/8 + 7*pi/16 + 7/160)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-15, 64)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(15, 64)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Add(Mul(Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 2), Symbol('pi')), Rational(-1, 4)), Add(Mul(Rational(7, 8), Symbol('pi'), Symbol('skoS2')), Mul(Rational(7, 16), Symbol('pi')), Rational(7, 160))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_8(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= -31/256) & (delta >= skoS2**2 - 2) & (delta - skoX >= 31/256) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (15*pi*skoS2/16 + 15*pi/32 + 3/64 <= skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-31, 256)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(31, 256)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), LessThan(Add(Mul(Rational(15, 16), Symbol('pi'), Symbol('skoS2')), Mul(Rational(15, 32), Symbol('pi')), Rational(3, 64)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_9(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= skoX) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -31/256) & (delta >= skoS2**2 - 2) & (delta - skoX >= 31/256) & (delta >= 2 - skoS2**2) & (pi*skoS2 + pi/2 - 1/4 >= 15*pi*skoS2/16 + 15*pi/32 + 3/64)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-31, 256)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(31, 256)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Add(Mul(Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 2), Symbol('pi')), Rational(-1, 4)), Add(Mul(Rational(15, 16), Symbol('pi'), Symbol('skoS2')), Mul(Rational(15, 32), Symbol('pi')), Rational(3, 64))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_10(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= -375/4096) & (delta >= skoS2**2 - 2) & (delta - skoX >= 375/4096) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (61*pi*skoS2/64 + 61*pi/128 + 61/1280 <= skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-375, 4096)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(375, 4096)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), LessThan(Add(Mul(Rational(61, 64), Symbol('pi'), Symbol('skoS2')), Mul(Rational(61, 128), Symbol('pi')), Rational(61, 1280)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_11(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= skoX) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -375/4096) & (delta >= skoS2**2 - 2) & (delta - skoX >= 375/4096) & (delta >= 2 - skoS2**2) & (pi*skoS2 + pi/2 - 1/4 >= 61*pi*skoS2/64 + 61*pi/128 + 61/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-375, 4096)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(375, 4096)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Add(Mul(Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 2), Symbol('pi')), Rational(-1, 4)), Add(Mul(Rational(61, 64), Symbol('pi'), Symbol('skoS2')), Mul(Rational(61, 128), Symbol('pi')), Rational(61, 1280))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_12(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= -183/1024) & (delta >= skoS2**2 - 2) & (delta - skoX >= 183/1024) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (29*pi*skoS2/32 + 29*pi/64 + 29/640 <= skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-183, 1024)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(183, 1024)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), LessThan(Add(Mul(Rational(29, 32), Symbol('pi'), Symbol('skoS2')), Mul(Rational(29, 64), Symbol('pi')), Rational(29, 640)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_13(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= skoX) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -183/1024) & (delta >= skoS2**2 - 2) & (delta - skoX >= 183/1024) & (delta >= 2 - skoS2**2) & (pi*skoS2 + pi/2 - 1/4 >= 29*pi*skoS2/32 + 29*pi/64 + 29/640)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-183, 1024)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(183, 1024)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Add(Mul(Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 2), Symbol('pi')), Rational(-1, 4)), Add(Mul(Rational(29, 32), Symbol('pi'), Symbol('skoS2')), Mul(Rational(29, 64), Symbol('pi')), Rational(29, 640))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_14(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= -615/4096) & (delta >= skoS2**2 - 2) & (delta - skoX >= 615/4096) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (59*pi*skoS2/64 + 59*pi/128 + 59/1280 <= skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-615, 4096)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(615, 4096)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), LessThan(Add(Mul(Rational(59, 64), Symbol('pi'), Symbol('skoS2')), Mul(Rational(59, 128), Symbol('pi')), Rational(59, 1280)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_15(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= skoX) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -615/4096) & (delta >= skoS2**2 - 2) & (delta - skoX >= 615/4096) & (delta >= 2 - skoS2**2) & (pi*skoS2 + pi/2 - 1/4 >= 59*pi*skoS2/64 + 59*pi/128 + 59/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-615, 4096)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(615, 4096)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Add(Mul(Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 2), Symbol('pi')), Rational(-1, 4)), Add(Mul(Rational(59, 64), Symbol('pi'), Symbol('skoS2')), Mul(Rational(59, 128), Symbol('pi')), Rational(59, 1280))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_16(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= -2223/16384) & (delta >= skoS2**2 - 2) & (delta - skoX >= 2223/16384) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (119*pi*skoS2/128 + 119*pi/256 + 119/2560 <= skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-2223, 16384)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(2223, 16384)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), LessThan(Add(Mul(Rational(119, 128), Symbol('pi'), Symbol('skoS2')), Mul(Rational(119, 256), Symbol('pi')), Rational(119, 2560)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_17(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= skoX) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -2223/16384) & (delta >= skoS2**2 - 2) & (delta - skoX >= 2223/16384) & (delta >= 2 - skoS2**2) & (pi*skoS2 + pi/2 - 1/4 >= 119*pi*skoS2/128 + 119*pi/256 + 119/2560)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-2223, 16384)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(2223, 16384)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Add(Mul(Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 2), Symbol('pi')), Rational(-1, 4)), Add(Mul(Rational(119, 128), Symbol('pi'), Symbol('skoS2')), Mul(Rational(119, 256), Symbol('pi')), Rational(119, 2560))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_18(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= -8415/65536) & (delta >= skoS2**2 - 2) & (delta - skoX >= 8415/65536) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (239*pi*skoS2/256 + 239*pi/512 + 239/5120 <= skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-8415, 65536)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(8415, 65536)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), LessThan(Add(Mul(Rational(239, 256), Symbol('pi'), Symbol('skoS2')), Mul(Rational(239, 512), Symbol('pi')), Rational(239, 5120)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_19(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= skoX) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -8415/65536) & (delta >= skoS2**2 - 2) & (delta - skoX >= 8415/65536) & (delta >= 2 - skoS2**2) & (pi*skoS2 + pi/2 - 1/4 >= 239*pi*skoS2/256 + 239*pi/512 + 239/5120)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-8415, 65536)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(8415, 65536)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Add(Mul(Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 2), Symbol('pi')), Rational(-1, 4)), Add(Mul(Rational(239, 256), Symbol('pi'), Symbol('skoS2')), Mul(Rational(239, 512), Symbol('pi')), Rational(239, 5120))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_20(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (479*pi*skoS2/512 + 479*pi/1024 + 479/10240 <= skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), LessThan(Add(Mul(Rational(479, 512), Symbol('pi'), Symbol('skoS2')), Mul(Rational(479, 1024), Symbol('pi')), Rational(479, 10240)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_21(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= skoX) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= 2 - skoS2**2) & (pi*skoS2 + pi/2 - 1/4 >= 479*pi*skoS2/512 + 479*pi/1024 + 479/10240)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Add(Mul(Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 2), Symbol('pi')), Rational(-1, 4)), Add(Mul(Rational(479, 512), Symbol('pi'), Symbol('skoS2')), Mul(Rational(479, 1024), Symbol('pi')), Rational(479, 10240))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_22(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= -132727/1048576) & (delta >= skoS2**2 - 2) & (delta - skoX >= 132727/1048576) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (957*pi*skoS2/1024 + 957*pi/2048 + 957/20480 <= skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-132727, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(132727, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), LessThan(Add(Mul(Rational(957, 1024), Symbol('pi'), Symbol('skoS2')), Mul(Rational(957, 2048), Symbol('pi')), Rational(957, 20480)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_23(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= skoX) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -132727/1048576) & (delta >= skoS2**2 - 2) & (delta - skoX >= 132727/1048576) & (delta >= 2 - skoS2**2) & (pi*skoS2 + pi/2 - 1/4 >= 957*pi*skoS2/1024 + 957*pi/2048 + 957/20480)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-132727, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(132727, 1048576)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Add(Mul(Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 2), Symbol('pi')), Rational(-1, 4)), Add(Mul(Rational(957, 1024), Symbol('pi'), Symbol('skoS2')), Mul(Rational(957, 2048), Symbol('pi')), Rational(957, 20480))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_24(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= -534735/4194304) & (delta >= skoS2**2 - 2) & (delta - skoX >= 534735/4194304) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (1913*pi*skoS2/2048 + 1913*pi/4096 + 1913/40960 <= skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-534735, 4194304)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(534735, 4194304)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), LessThan(Add(Mul(Rational(1913, 2048), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1913, 4096), Symbol('pi')), Rational(1913, 40960)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_25(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= skoX) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -534735/4194304) & (delta >= skoS2**2 - 2) & (delta - skoX >= 534735/4194304) & (delta >= 2 - skoS2**2) & (pi*skoS2 + pi/2 - 1/4 >= 1913*pi*skoS2/2048 + 1913*pi/4096 + 1913/40960)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-534735, 4194304)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(534735, 4194304)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Add(Mul(Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 2), Symbol('pi')), Rational(-1, 4)), Add(Mul(Rational(1913, 2048), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1913, 4096), Symbol('pi')), Rational(1913, 40960))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_26(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= -2131287/16777216) & (delta >= skoS2**2 - 2) & (delta - skoX >= 2131287/16777216) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (3827*pi*skoS2/4096 + 3827*pi/8192 + 3827/81920 <= skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-2131287, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(2131287, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), LessThan(Add(Mul(Rational(3827, 4096), Symbol('pi'), Symbol('skoS2')), Mul(Rational(3827, 8192), Symbol('pi')), Rational(3827, 81920)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_27(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= skoX) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -2131287/16777216) & (delta >= skoS2**2 - 2) & (delta - skoX >= 2131287/16777216) & (delta >= 2 - skoS2**2) & (pi*skoS2 + pi/2 - 1/4 >= 3827*pi*skoS2/4096 + 3827*pi/8192 + 3827/81920)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-2131287, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(2131287, 16777216)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Add(Mul(Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 2), Symbol('pi')), Rational(-1, 4)), Add(Mul(Rational(3827, 4096), Symbol('pi'), Symbol('skoS2')), Mul(Rational(3827, 8192), Symbol('pi')), Rational(3827, 81920))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_28(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= -8540455/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= 8540455/67108864) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (7653*pi*skoS2/8192 + 7653*pi/16384 + 7653/163840 <= skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-8540455, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(8540455, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), LessThan(Add(Mul(Rational(7653, 8192), Symbol('pi'), Symbol('skoS2')), Mul(Rational(7653, 16384), Symbol('pi')), Rational(7653, 163840)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_29(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= skoX) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -8540455/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= 8540455/67108864) & (delta >= 2 - skoS2**2) & (pi*skoS2 + pi/2 - 1/4 >= 7653*pi*skoS2/8192 + 7653*pi/16384 + 7653/163840)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-8540455, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(8540455, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Add(Mul(Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 2), Symbol('pi')), Rational(-1, 4)), Add(Mul(Rational(7653, 8192), Symbol('pi'), Symbol('skoS2')), Mul(Rational(7653, 16384), Symbol('pi')), Rational(7653, 163840))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_30(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= -42290284792860090659718398281252863/332306998946228968225951765070086144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 42290284792860090659718398281252863/332306998946228968225951765070086144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (538531999191662591*pi*skoS2/576460752303423488 + 538531999191662591*pi/1152921504606846976 + 538531999191662591/11529215046068469760 <= skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-42290284792860090659718398281252863, 332306998946228968225951765070086144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(42290284792860090659718398281252863, 332306998946228968225951765070086144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), LessThan(Add(Mul(Rational(538531999191662591, 576460752303423488), Symbol('pi'), Symbol('skoS2')), Mul(Rational(538531999191662591, 1152921504606846976), Symbol('pi')), Rational(538531999191662591, 11529215046068469760)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_31(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= skoX) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -42290284792860090659718398281252863/332306998946228968225951765070086144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 42290284792860090659718398281252863/332306998946228968225951765070086144) & (delta >= 2 - skoS2**2) & (pi*skoS2 + pi/2 - 1/4 >= 538531999191662591*pi*skoS2/576460752303423488 + 538531999191662591*pi/1152921504606846976 + 538531999191662591/11529215046068469760)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-42290284792860090659718398281252863, 332306998946228968225951765070086144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(42290284792860090659718398281252863, 332306998946228968225951765070086144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Add(Mul(Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 2), Symbol('pi')), Rational(-1, 4)), Add(Mul(Rational(538531999191662591, 576460752303423488), Symbol('pi'), Symbol('skoS2')), Mul(Rational(538531999191662591, 1152921504606846976), Symbol('pi')), Rational(538531999191662591, 11529215046068469760))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_32(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= -8540455/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= 8540455/67108864) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (7653*pi*skoS2/8192 + 7653*pi/16384 + 7653/163840 <= skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-8540455, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(8540455, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), LessThan(Add(Mul(Rational(7653, 8192), Symbol('pi'), Symbol('skoS2')), Mul(Rational(7653, 16384), Symbol('pi')), Rational(7653, 163840)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_33(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= skoX) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -8540455/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= 8540455/67108864) & (delta >= 2 - skoS2**2) & (pi*skoS2 + pi/2 - 1/4 >= 7653*pi*skoS2/8192 + 7653*pi/16384 + 7653/163840)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-8540455, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(8540455, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Add(Mul(Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 2), Symbol('pi')), Rational(-1, 4)), Add(Mul(Rational(7653, 8192), Symbol('pi'), Symbol('skoS2')), Mul(Rational(7653, 16384), Symbol('pi')), Rational(7653, 163840))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_34(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= -42290284792860090659718398281252863/332306998946228968225951765070086144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 42290284792860090659718398281252863/332306998946228968225951765070086144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (538531999191662591*pi*skoS2/576460752303423488 + 538531999191662591*pi/1152921504606846976 + 538531999191662591/11529215046068469760 <= skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-42290284792860090659718398281252863, 332306998946228968225951765070086144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(42290284792860090659718398281252863, 332306998946228968225951765070086144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), LessThan(Add(Mul(Rational(538531999191662591, 576460752303423488), Symbol('pi'), Symbol('skoS2')), Mul(Rational(538531999191662591, 1152921504606846976), Symbol('pi')), Rational(538531999191662591, 11529215046068469760)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_35(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= skoX) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -42290284792860090659718398281252863/332306998946228968225951765070086144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 42290284792860090659718398281252863/332306998946228968225951765070086144) & (delta >= 2 - skoS2**2) & (pi*skoS2 + pi/2 - 1/4 >= 538531999191662591*pi*skoS2/576460752303423488 + 538531999191662591*pi/1152921504606846976 + 538531999191662591/11529215046068469760)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-42290284792860090659718398281252863, 332306998946228968225951765070086144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(42290284792860090659718398281252863, 332306998946228968225951765070086144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Add(Mul(Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 2), Symbol('pi')), Rational(-1, 4)), Add(Mul(Rational(538531999191662591, 576460752303423488), Symbol('pi'), Symbol('skoS2')), Mul(Rational(538531999191662591, 1152921504606846976), Symbol('pi')), Rational(538531999191662591, 11529215046068469760))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_36(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= -8540455/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= 8540455/67108864) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (7653*pi*skoS2/8192 + 7653*pi/16384 + 7653/163840 <= skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-8540455, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(8540455, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), LessThan(Add(Mul(Rational(7653, 8192), Symbol('pi'), Symbol('skoS2')), Mul(Rational(7653, 16384), Symbol('pi')), Rational(7653, 163840)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_37(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= skoX) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -8540455/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= 8540455/67108864) & (delta >= 2 - skoS2**2) & (pi*skoS2 + pi/2 - 1/4 >= 7653*pi*skoS2/8192 + 7653*pi/16384 + 7653/163840)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-8540455, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(8540455, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Add(Mul(Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 2), Symbol('pi')), Rational(-1, 4)), Add(Mul(Rational(7653, 8192), Symbol('pi'), Symbol('skoS2')), Mul(Rational(7653, 16384), Symbol('pi')), Rational(7653, 163840))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_38(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= -42290284792860090659718398281252863/332306998946228968225951765070086144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 42290284792860090659718398281252863/332306998946228968225951765070086144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (538531999191662591*pi*skoS2/576460752303423488 + 538531999191662591*pi/1152921504606846976 + 538531999191662591/11529215046068469760 <= skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-42290284792860090659718398281252863, 332306998946228968225951765070086144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(42290284792860090659718398281252863, 332306998946228968225951765070086144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), LessThan(Add(Mul(Rational(538531999191662591, 576460752303423488), Symbol('pi'), Symbol('skoS2')), Mul(Rational(538531999191662591, 1152921504606846976), Symbol('pi')), Rational(538531999191662591, 11529215046068469760)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_39(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= skoX) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -42290284792860090659718398281252863/332306998946228968225951765070086144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 42290284792860090659718398281252863/332306998946228968225951765070086144) & (delta >= 2 - skoS2**2) & (pi*skoS2 + pi/2 - 1/4 >= 538531999191662591*pi*skoS2/576460752303423488 + 538531999191662591*pi/1152921504606846976 + 538531999191662591/11529215046068469760)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-42290284792860090659718398281252863, 332306998946228968225951765070086144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(42290284792860090659718398281252863, 332306998946228968225951765070086144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Add(Mul(Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 2), Symbol('pi')), Rational(-1, 4)), Add(Mul(Rational(538531999191662591, 576460752303423488), Symbol('pi'), Symbol('skoS2')), Mul(Rational(538531999191662591, 1152921504606846976), Symbol('pi')), Rational(538531999191662591, 11529215046068469760))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_40(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= -8540455/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= 8540455/67108864) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (7653*pi*skoS2/8192 + 7653*pi/16384 + 7653/163840 <= skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-8540455, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(8540455, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), LessThan(Add(Mul(Rational(7653, 8192), Symbol('pi'), Symbol('skoS2')), Mul(Rational(7653, 16384), Symbol('pi')), Rational(7653, 163840)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_41(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= skoX) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -8540455/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= 8540455/67108864) & (delta >= 2 - skoS2**2) & (pi*skoS2 + pi/2 - 1/4 >= 7653*pi*skoS2/8192 + 7653*pi/16384 + 7653/163840)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-8540455, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(8540455, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Add(Mul(Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 2), Symbol('pi')), Rational(-1, 4)), Add(Mul(Rational(7653, 8192), Symbol('pi'), Symbol('skoS2')), Mul(Rational(7653, 16384), Symbol('pi')), Rational(7653, 163840))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_42(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= -42290284792860090659718398281252863/332306998946228968225951765070086144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 42290284792860090659718398281252863/332306998946228968225951765070086144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (538531999191662591*pi*skoS2/576460752303423488 + 538531999191662591*pi/1152921504606846976 + 538531999191662591/11529215046068469760 <= skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-42290284792860090659718398281252863, 332306998946228968225951765070086144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(42290284792860090659718398281252863, 332306998946228968225951765070086144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), LessThan(Add(Mul(Rational(538531999191662591, 576460752303423488), Symbol('pi'), Symbol('skoS2')), Mul(Rational(538531999191662591, 1152921504606846976), Symbol('pi')), Rational(538531999191662591, 11529215046068469760)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_43(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= skoX) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -42290284792860090659718398281252863/332306998946228968225951765070086144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 42290284792860090659718398281252863/332306998946228968225951765070086144) & (delta >= 2 - skoS2**2) & (pi*skoS2 + pi/2 - 1/4 >= 538531999191662591*pi*skoS2/576460752303423488 + 538531999191662591*pi/1152921504606846976 + 538531999191662591/11529215046068469760)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-42290284792860090659718398281252863, 332306998946228968225951765070086144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(42290284792860090659718398281252863, 332306998946228968225951765070086144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Add(Mul(Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 2), Symbol('pi')), Rational(-1, 4)), Add(Mul(Rational(538531999191662591, 576460752303423488), Symbol('pi'), Symbol('skoS2')), Mul(Rational(538531999191662591, 1152921504606846976), Symbol('pi')), Rational(538531999191662591, 11529215046068469760))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_44(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= -8540455/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= 8540455/67108864) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (7653*pi*skoS2/8192 + 7653*pi/16384 + 7653/163840 <= skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-8540455, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(8540455, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), LessThan(Add(Mul(Rational(7653, 8192), Symbol('pi'), Symbol('skoS2')), Mul(Rational(7653, 16384), Symbol('pi')), Rational(7653, 163840)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_45(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= skoX) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -8540455/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= 8540455/67108864) & (delta >= 2 - skoS2**2) & (pi*skoS2 + pi/2 - 1/4 >= 7653*pi*skoS2/8192 + 7653*pi/16384 + 7653/163840)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-8540455, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(8540455, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Add(Mul(Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 2), Symbol('pi')), Rational(-1, 4)), Add(Mul(Rational(7653, 8192), Symbol('pi'), Symbol('skoS2')), Mul(Rational(7653, 16384), Symbol('pi')), Rational(7653, 163840))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_46(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= -42290284792860090659718398281252863/332306998946228968225951765070086144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 42290284792860090659718398281252863/332306998946228968225951765070086144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (538531999191662591*pi*skoS2/576460752303423488 + 538531999191662591*pi/1152921504606846976 + 538531999191662591/11529215046068469760 <= skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-42290284792860090659718398281252863, 332306998946228968225951765070086144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(42290284792860090659718398281252863, 332306998946228968225951765070086144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), LessThan(Add(Mul(Rational(538531999191662591, 576460752303423488), Symbol('pi'), Symbol('skoS2')), Mul(Rational(538531999191662591, 1152921504606846976), Symbol('pi')), Rational(538531999191662591, 11529215046068469760)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_47(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= skoX) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -42290284792860090659718398281252863/332306998946228968225951765070086144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 42290284792860090659718398281252863/332306998946228968225951765070086144) & (delta >= 2 - skoS2**2) & (pi*skoS2 + pi/2 - 1/4 >= 538531999191662591*pi*skoS2/576460752303423488 + 538531999191662591*pi/1152921504606846976 + 538531999191662591/11529215046068469760)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-42290284792860090659718398281252863, 332306998946228968225951765070086144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(42290284792860090659718398281252863, 332306998946228968225951765070086144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Add(Mul(Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 2), Symbol('pi')), Rational(-1, 4)), Add(Mul(Rational(538531999191662591, 576460752303423488), Symbol('pi'), Symbol('skoS2')), Mul(Rational(538531999191662591, 1152921504606846976), Symbol('pi')), Rational(538531999191662591, 11529215046068469760))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_48(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= -8540455/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= 8540455/67108864) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (7653*pi*skoS2/8192 + 7653*pi/16384 + 7653/163840 <= skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-8540455, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(8540455, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), LessThan(Add(Mul(Rational(7653, 8192), Symbol('pi'), Symbol('skoS2')), Mul(Rational(7653, 16384), Symbol('pi')), Rational(7653, 163840)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_49(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= skoX) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -8540455/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= 8540455/67108864) & (delta >= 2 - skoS2**2) & (pi*skoS2 + pi/2 - 1/4 >= 7653*pi*skoS2/8192 + 7653*pi/16384 + 7653/163840)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-8540455, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(8540455, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Add(Mul(Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 2), Symbol('pi')), Rational(-1, 4)), Add(Mul(Rational(7653, 8192), Symbol('pi'), Symbol('skoS2')), Mul(Rational(7653, 16384), Symbol('pi')), Rational(7653, 163840))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_50(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= -42290284792860090659718398281252863/332306998946228968225951765070086144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 42290284792860090659718398281252863/332306998946228968225951765070086144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (538531999191662591*pi*skoS2/576460752303423488 + 538531999191662591*pi/1152921504606846976 + 538531999191662591/11529215046068469760 <= skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-42290284792860090659718398281252863, 332306998946228968225951765070086144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(42290284792860090659718398281252863, 332306998946228968225951765070086144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), LessThan(Add(Mul(Rational(538531999191662591, 576460752303423488), Symbol('pi'), Symbol('skoS2')), Mul(Rational(538531999191662591, 1152921504606846976), Symbol('pi')), Rational(538531999191662591, 11529215046068469760)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_51(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= skoX) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -42290284792860090659718398281252863/332306998946228968225951765070086144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 42290284792860090659718398281252863/332306998946228968225951765070086144) & (delta >= 2 - skoS2**2) & (pi*skoS2 + pi/2 - 1/4 >= 538531999191662591*pi*skoS2/576460752303423488 + 538531999191662591*pi/1152921504606846976 + 538531999191662591/11529215046068469760)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-42290284792860090659718398281252863, 332306998946228968225951765070086144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(42290284792860090659718398281252863, 332306998946228968225951765070086144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Add(Mul(Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 2), Symbol('pi')), Rational(-1, 4)), Add(Mul(Rational(538531999191662591, 576460752303423488), Symbol('pi'), Symbol('skoS2')), Mul(Rational(538531999191662591, 1152921504606846976), Symbol('pi')), Rational(538531999191662591, 11529215046068469760))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_52(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= -8540455/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= 8540455/67108864) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (7653*pi*skoS2/8192 + 7653*pi/16384 + 7653/163840 <= skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-8540455, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(8540455, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), LessThan(Add(Mul(Rational(7653, 8192), Symbol('pi'), Symbol('skoS2')), Mul(Rational(7653, 16384), Symbol('pi')), Rational(7653, 163840)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_53(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= skoX) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -8540455/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= 8540455/67108864) & (delta >= 2 - skoS2**2) & (pi*skoS2 + pi/2 - 1/4 >= 7653*pi*skoS2/8192 + 7653*pi/16384 + 7653/163840)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-8540455, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(8540455, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Add(Mul(Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 2), Symbol('pi')), Rational(-1, 4)), Add(Mul(Rational(7653, 8192), Symbol('pi'), Symbol('skoS2')), Mul(Rational(7653, 16384), Symbol('pi')), Rational(7653, 163840))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_54(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= -42290284792860090659718398281252863/332306998946228968225951765070086144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 42290284792860090659718398281252863/332306998946228968225951765070086144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (538531999191662591*pi*skoS2/576460752303423488 + 538531999191662591*pi/1152921504606846976 + 538531999191662591/11529215046068469760 <= skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-42290284792860090659718398281252863, 332306998946228968225951765070086144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(42290284792860090659718398281252863, 332306998946228968225951765070086144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), LessThan(Add(Mul(Rational(538531999191662591, 576460752303423488), Symbol('pi'), Symbol('skoS2')), Mul(Rational(538531999191662591, 1152921504606846976), Symbol('pi')), Rational(538531999191662591, 11529215046068469760)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_55(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= skoX) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -42290284792860090659718398281252863/332306998946228968225951765070086144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 42290284792860090659718398281252863/332306998946228968225951765070086144) & (delta >= 2 - skoS2**2) & (pi*skoS2 + pi/2 - 1/4 >= 538531999191662591*pi*skoS2/576460752303423488 + 538531999191662591*pi/1152921504606846976 + 538531999191662591/11529215046068469760)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-42290284792860090659718398281252863, 332306998946228968225951765070086144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(42290284792860090659718398281252863, 332306998946228968225951765070086144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Add(Mul(Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 2), Symbol('pi')), Rational(-1, 4)), Add(Mul(Rational(538531999191662591, 576460752303423488), Symbol('pi'), Symbol('skoS2')), Mul(Rational(538531999191662591, 1152921504606846976), Symbol('pi')), Rational(538531999191662591, 11529215046068469760))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_56(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= -8540455/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= 8540455/67108864) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (7653*pi*skoS2/8192 + 7653*pi/16384 + 7653/163840 <= skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-8540455, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(8540455, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), LessThan(Add(Mul(Rational(7653, 8192), Symbol('pi'), Symbol('skoS2')), Mul(Rational(7653, 16384), Symbol('pi')), Rational(7653, 163840)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_57(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= skoX) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -8540455/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= 8540455/67108864) & (delta >= 2 - skoS2**2) & (pi*skoS2 + pi/2 - 1/4 >= 7653*pi*skoS2/8192 + 7653*pi/16384 + 7653/163840)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-8540455, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(8540455, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Add(Mul(Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 2), Symbol('pi')), Rational(-1, 4)), Add(Mul(Rational(7653, 8192), Symbol('pi'), Symbol('skoS2')), Mul(Rational(7653, 16384), Symbol('pi')), Rational(7653, 163840))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_58(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= -42290284792860090659718398281252863/332306998946228968225951765070086144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 42290284792860090659718398281252863/332306998946228968225951765070086144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (538531999191662591*pi*skoS2/576460752303423488 + 538531999191662591*pi/1152921504606846976 + 538531999191662591/11529215046068469760 <= skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-42290284792860090659718398281252863, 332306998946228968225951765070086144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(42290284792860090659718398281252863, 332306998946228968225951765070086144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), LessThan(Add(Mul(Rational(538531999191662591, 576460752303423488), Symbol('pi'), Symbol('skoS2')), Mul(Rational(538531999191662591, 1152921504606846976), Symbol('pi')), Rational(538531999191662591, 11529215046068469760)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_59(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= skoX) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -42290284792860090659718398281252863/332306998946228968225951765070086144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 42290284792860090659718398281252863/332306998946228968225951765070086144) & (delta >= 2 - skoS2**2) & (pi*skoS2 + pi/2 - 1/4 >= 538531999191662591*pi*skoS2/576460752303423488 + 538531999191662591*pi/1152921504606846976 + 538531999191662591/11529215046068469760)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-42290284792860090659718398281252863, 332306998946228968225951765070086144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(42290284792860090659718398281252863, 332306998946228968225951765070086144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Add(Mul(Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 2), Symbol('pi')), Rational(-1, 4)), Add(Mul(Rational(538531999191662591, 576460752303423488), Symbol('pi'), Symbol('skoS2')), Mul(Rational(538531999191662591, 1152921504606846976), Symbol('pi')), Rational(538531999191662591, 11529215046068469760))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_60(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= -8540455/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= 8540455/67108864) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (7653*pi*skoS2/8192 + 7653*pi/16384 + 7653/163840 <= skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-8540455, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(8540455, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), LessThan(Add(Mul(Rational(7653, 8192), Symbol('pi'), Symbol('skoS2')), Mul(Rational(7653, 16384), Symbol('pi')), Rational(7653, 163840)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_61(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= skoX) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -8540455/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= 8540455/67108864) & (delta >= 2 - skoS2**2) & (pi*skoS2 + pi/2 - 1/4 >= 7653*pi*skoS2/8192 + 7653*pi/16384 + 7653/163840)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-8540455, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(8540455, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Add(Mul(Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 2), Symbol('pi')), Rational(-1, 4)), Add(Mul(Rational(7653, 8192), Symbol('pi'), Symbol('skoS2')), Mul(Rational(7653, 16384), Symbol('pi')), Rational(7653, 163840))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_62(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= -42290284792860090659718398281252863/332306998946228968225951765070086144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 42290284792860090659718398281252863/332306998946228968225951765070086144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (538531999191662591*pi*skoS2/576460752303423488 + 538531999191662591*pi/1152921504606846976 + 538531999191662591/11529215046068469760 <= skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-42290284792860090659718398281252863, 332306998946228968225951765070086144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(42290284792860090659718398281252863, 332306998946228968225951765070086144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), LessThan(Add(Mul(Rational(538531999191662591, 576460752303423488), Symbol('pi'), Symbol('skoS2')), Mul(Rational(538531999191662591, 1152921504606846976), Symbol('pi')), Rational(538531999191662591, 11529215046068469760)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_63(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= skoX) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -42290284792860090659718398281252863/332306998946228968225951765070086144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 42290284792860090659718398281252863/332306998946228968225951765070086144) & (delta >= 2 - skoS2**2) & (pi*skoS2 + pi/2 - 1/4 >= 538531999191662591*pi*skoS2/576460752303423488 + 538531999191662591*pi/1152921504606846976 + 538531999191662591/11529215046068469760)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-42290284792860090659718398281252863, 332306998946228968225951765070086144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(42290284792860090659718398281252863, 332306998946228968225951765070086144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Add(Mul(Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 2), Symbol('pi')), Rational(-1, 4)), Add(Mul(Rational(538531999191662591, 576460752303423488), Symbol('pi'), Symbol('skoS2')), Mul(Rational(538531999191662591, 1152921504606846976), Symbol('pi')), Rational(538531999191662591, 11529215046068469760))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(delta:sympy.Rational, skoX:sympy.Rational, skoS2:sympy.Rational, pi:sympy.Rational, skoSP:sympy.Rational, skoSM:sympy.Rational):
	# (0 <= delta) & (0 <= skoS2) & (0 <= skoSM) & (0 <= skoSP) & (1 > skoX) & (31415927/10000000 > pi) & (pi > 15707963/5000000) & (skoX > 0) & (skoS2**2 - 2 <= delta) & (skoSM**2 + skoX - 1 <= delta) & (2 - skoS2**2 <= delta) & (-skoSP**2 + skoX + 1 <= delta) & (skoSP**2 - skoX - 1 <= delta) & (-skoSM**2 - skoX + 1 <= delta) & (skoSP*(pi*skoS2 + pi/2 + 1/20) <= skoSM*(pi*skoS2 + pi/2 - 1/20) - 1/5)

	post_cond =  And(LessThan(Integer(0), Symbol('delta')), LessThan(Integer(0), Symbol('skoS2')), LessThan(Integer(0), Symbol('skoSM')), LessThan(Integer(0), Symbol('skoSP')), StrictGreaterThan(Integer(1), Symbol('skoX')), StrictGreaterThan(Rational(31415927, 10000000), Symbol('pi')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), LessThan(Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Symbol('delta')), LessThan(Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1)), Symbol('delta')), LessThan(Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Symbol('delta')), LessThan(Add(Mul(Integer(-1), Pow(Symbol('skoSP'), Integer(2))), Symbol('skoX'), Integer(1)), Symbol('delta')), LessThan(Add(Pow(Symbol('skoSP'), Integer(2)), Mul(Integer(-1), Symbol('skoX')), Integer(-1)), Symbol('delta')), LessThan(Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)), Symbol('delta')), LessThan(Mul(Symbol('skoSP'), Add(Mul(Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 2), Symbol('pi')), Rational(1, 20))), Add(Mul(Symbol('skoSM'), Add(Mul(Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 2), Symbol('pi')), Rational(-1, 20))), Rational(-1, 5))))

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
		print('skoSM = 1')
		print('skoSP = 1/2')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_1(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_1 SAT")
		print('delta = 2')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 1/2')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_2(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_2 SAT")
		print('delta = 1')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 3/4')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_3(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_3 SAT")
		print('delta = 1')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 3/4')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_4(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_4 SAT")
		print('delta = 1')
		print('skoS2 = 1')
		print('skoSM = 9/8')
		print('skoSP = 1')
		print('skoX = 5/8')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_5(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_5 SAT")
		print('delta = 1')
		print('skoS2 = 1')
		print('skoSM = 9/8')
		print('skoSP = 1')
		print('skoX = 5/8')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_6(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_6 SAT")
		print('delta = 1')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 7/8')
		print('skoX = 3/4')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_7(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_7 SAT")
		print('delta = 1')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 7/8')
		print('skoX = 3/4')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_8(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_8 SAT")
		print('delta = 1')
		print('skoS2 = 3/2')
		print('skoSM = 1')
		print('skoSP = 15/16')
		print('skoX = 7/8')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_9(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_9 SAT")
		print('delta = 1')
		print('skoS2 = 3/2')
		print('skoSM = 1')
		print('skoSP = 15/16')
		print('skoX = 7/8')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_10(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_10 SAT")
		print('delta = 35/32')
		print('skoS2 = 7/4')
		print('skoSM = 1')
		print('skoSP = 61/64')
		print('skoX = 63/64')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_11(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_11 SAT")
		print('delta = 35/32')
		print('skoS2 = 7/4')
		print('skoSM = 1')
		print('skoSP = 61/64')
		print('skoX = 63/64')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_12(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_12 SAT")
		print('delta = 1')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 29/32')
		print('skoX = 13/16')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_13(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_13 SAT")
		print('delta = 1')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 29/32')
		print('skoX = 13/16')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_14(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_14 SAT")
		print('delta = 1')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 59/64')
		print('skoX = 27/32')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_15(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_15 SAT")
		print('delta = 1')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 59/64')
		print('skoX = 27/32')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_16(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_16 SAT")
		print('delta = 1')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 119/128')
		print('skoX = 55/64')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_17(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_17 SAT")
		print('delta = 1')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 119/128')
		print('skoX = 55/64')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_18(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_18 SAT")
		print('delta = 1')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 239/256')
		print('skoX = 111/128')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_19(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_19 SAT")
		print('delta = 1')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 239/256')
		print('skoX = 111/128')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_20(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_20 SAT")
		print('delta = 1')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		print('skoX = 7/8')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_21(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_21 SAT")
		print('delta = 1')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		print('skoX = 7/8')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_22(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_22 SAT")
		print('delta = 9/8')
		print('skoS2 = 61/64')
		print('skoSM = 1')
		print('skoSP = 957/1024')
		print('skoX = 511/512')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_23(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_23 SAT")
		print('delta = 9/8')
		print('skoS2 = 61/64')
		print('skoSM = 1')
		print('skoSP = 957/1024')
		print('skoX = 511/512')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_24(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_24 SAT")
		print('delta = 9/8')
		print('skoS2 = 15/16')
		print('skoSM = 1')
		print('skoSP = 1913/2048')
		print('skoX = 1021/1024')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_25(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_25 SAT")
		print('delta = 9/8')
		print('skoS2 = 15/16')
		print('skoSM = 1')
		print('skoSP = 1913/2048')
		print('skoX = 1021/1024')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_26(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_26 SAT")
		print('delta = 9/8')
		print('skoS2 = 241/256')
		print('skoSM = 1')
		print('skoSP = 3827/4096')
		print('skoX = 2043/2048')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_27(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_27 SAT")
		print('delta = 9/8')
		print('skoS2 = 241/256')
		print('skoSM = 1')
		print('skoSP = 3827/4096')
		print('skoX = 2043/2048')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_28(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_28 SAT")
		print('delta = 9/8')
		print('skoS2 = 15/16')
		print('skoSM = 1')
		print('skoSP = 7653/8192')
		print('skoX = 2043/2048')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_29(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_29 SAT")
		print('delta = 9/8')
		print('skoS2 = 15/16')
		print('skoSM = 1')
		print('skoSP = 7653/8192')
		print('skoX = 2043/2048')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_30(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_30 SAT")
		print('delta = 9/8')
		print('skoS2 = 31388019/33554432')
		print('skoSM = 1')
		print('skoSP = 538531999191662591/576460752303423488')
		print('skoX = 287578198252716031/288230376151711744')
		print('pi = 56593901693316947/18014398509481984')
		exit(0)
	
	
	if pre_condition_31(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_31 SAT")
		print('delta = 9/8')
		print('skoS2 = 31388019/33554432')
		print('skoSM = 1')
		print('skoSP = 538531999191662591/576460752303423488')
		print('skoX = 287578198252716031/288230376151711744')
		print('pi = 56593901693316947/18014398509481984')
		exit(0)
	
	
	if pre_condition_32(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_32 SAT")
		print('delta = 9/8')
		print('skoS2 = 15/16')
		print('skoSM = 1')
		print('skoSP = 7653/8192')
		print('skoX = 287578198252716031/288230376151711744')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_33(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_33 SAT")
		print('delta = 9/8')
		print('skoS2 = 15/16')
		print('skoSM = 1')
		print('skoSP = 7653/8192')
		print('skoX = 287578198252716031/288230376151711744')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_34(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_34 SAT")
		print('delta = 9/8')
		print('skoS2 = 31388019/33554432')
		print('skoSM = 1')
		print('skoSP = 538531999191662591/576460752303423488')
		print('skoX = 287578198252716031/288230376151711744')
		print('pi = 56593901693316947/18014398509481984')
		exit(0)
	
	
	if pre_condition_35(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_35 SAT")
		print('delta = 9/8')
		print('skoS2 = 31388019/33554432')
		print('skoSM = 1')
		print('skoSP = 538531999191662591/576460752303423488')
		print('skoX = 287578198252716031/288230376151711744')
		print('pi = 56593901693316947/18014398509481984')
		exit(0)
	
	
	if pre_condition_36(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_36 SAT")
		print('delta = 9/8')
		print('skoS2 = 15/16')
		print('skoSM = 1')
		print('skoSP = 7653/8192')
		print('skoX = 287578198252716031/288230376151711744')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_37(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_37 SAT")
		print('delta = 9/8')
		print('skoS2 = 15/16')
		print('skoSM = 1')
		print('skoSP = 7653/8192')
		print('skoX = 287578198252716031/288230376151711744')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_38(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_38 SAT")
		print('delta = 9/8')
		print('skoS2 = 31388019/33554432')
		print('skoSM = 1')
		print('skoSP = 538531999191662591/576460752303423488')
		print('skoX = 287578198252716031/288230376151711744')
		print('pi = 56593901693316947/18014398509481984')
		exit(0)
	
	
	if pre_condition_39(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_39 SAT")
		print('delta = 9/8')
		print('skoS2 = 31388019/33554432')
		print('skoSM = 1')
		print('skoSP = 538531999191662591/576460752303423488')
		print('skoX = 287578198252716031/288230376151711744')
		print('pi = 56593901693316947/18014398509481984')
		exit(0)
	
	
	if pre_condition_40(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_40 SAT")
		print('delta = 9/8')
		print('skoS2 = 15/16')
		print('skoSM = 1')
		print('skoSP = 7653/8192')
		print('skoX = 287578198252716031/288230376151711744')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_41(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_41 SAT")
		print('delta = 9/8')
		print('skoS2 = 15/16')
		print('skoSM = 1')
		print('skoSP = 7653/8192')
		print('skoX = 287578198252716031/288230376151711744')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_42(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_42 SAT")
		print('delta = 9/8')
		print('skoS2 = 31388019/33554432')
		print('skoSM = 1')
		print('skoSP = 538531999191662591/576460752303423488')
		print('skoX = 287578198252716031/288230376151711744')
		print('pi = 56593901693316947/18014398509481984')
		exit(0)
	
	
	if pre_condition_43(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_43 SAT")
		print('delta = 9/8')
		print('skoS2 = 31388019/33554432')
		print('skoSM = 1')
		print('skoSP = 538531999191662591/576460752303423488')
		print('skoX = 287578198252716031/288230376151711744')
		print('pi = 56593901693316947/18014398509481984')
		exit(0)
	
	
	if pre_condition_44(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_44 SAT")
		print('delta = 9/8')
		print('skoS2 = 15/16')
		print('skoSM = 1')
		print('skoSP = 7653/8192')
		print('skoX = 287578198252716031/288230376151711744')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_45(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_45 SAT")
		print('delta = 9/8')
		print('skoS2 = 15/16')
		print('skoSM = 1')
		print('skoSP = 7653/8192')
		print('skoX = 287578198252716031/288230376151711744')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_46(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_46 SAT")
		print('delta = 9/8')
		print('skoS2 = 31388019/33554432')
		print('skoSM = 1')
		print('skoSP = 538531999191662591/576460752303423488')
		print('skoX = 287578198252716031/288230376151711744')
		print('pi = 56593901693316947/18014398509481984')
		exit(0)
	
	
	if pre_condition_47(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_47 SAT")
		print('delta = 9/8')
		print('skoS2 = 31388019/33554432')
		print('skoSM = 1')
		print('skoSP = 538531999191662591/576460752303423488')
		print('skoX = 287578198252716031/288230376151711744')
		print('pi = 56593901693316947/18014398509481984')
		exit(0)
	
	
	if pre_condition_48(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_48 SAT")
		print('delta = 9/8')
		print('skoS2 = 15/16')
		print('skoSM = 1')
		print('skoSP = 7653/8192')
		print('skoX = 287578198252716031/288230376151711744')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_49(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_49 SAT")
		print('delta = 9/8')
		print('skoS2 = 15/16')
		print('skoSM = 1')
		print('skoSP = 7653/8192')
		print('skoX = 287578198252716031/288230376151711744')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_50(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_50 SAT")
		print('delta = 9/8')
		print('skoS2 = 31388019/33554432')
		print('skoSM = 1')
		print('skoSP = 538531999191662591/576460752303423488')
		print('skoX = 287578198252716031/288230376151711744')
		print('pi = 56593901693316947/18014398509481984')
		exit(0)
	
	
	if pre_condition_51(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_51 SAT")
		print('delta = 9/8')
		print('skoS2 = 31388019/33554432')
		print('skoSM = 1')
		print('skoSP = 538531999191662591/576460752303423488')
		print('skoX = 287578198252716031/288230376151711744')
		print('pi = 56593901693316947/18014398509481984')
		exit(0)
	
	
	if pre_condition_52(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_52 SAT")
		print('delta = 9/8')
		print('skoS2 = 15/16')
		print('skoSM = 1')
		print('skoSP = 7653/8192')
		print('skoX = 287578198252716031/288230376151711744')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_53(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_53 SAT")
		print('delta = 9/8')
		print('skoS2 = 15/16')
		print('skoSM = 1')
		print('skoSP = 7653/8192')
		print('skoX = 287578198252716031/288230376151711744')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_54(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_54 SAT")
		print('delta = 9/8')
		print('skoS2 = 31388019/33554432')
		print('skoSM = 1')
		print('skoSP = 538531999191662591/576460752303423488')
		print('skoX = 287578198252716031/288230376151711744')
		print('pi = 56593901693316947/18014398509481984')
		exit(0)
	
	
	if pre_condition_55(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_55 SAT")
		print('delta = 9/8')
		print('skoS2 = 31388019/33554432')
		print('skoSM = 1')
		print('skoSP = 538531999191662591/576460752303423488')
		print('skoX = 287578198252716031/288230376151711744')
		print('pi = 56593901693316947/18014398509481984')
		exit(0)
	
	
	if pre_condition_56(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_56 SAT")
		print('delta = 9/8')
		print('skoS2 = 15/16')
		print('skoSM = 1')
		print('skoSP = 7653/8192')
		print('skoX = 287578198252716031/288230376151711744')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_57(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_57 SAT")
		print('delta = 9/8')
		print('skoS2 = 15/16')
		print('skoSM = 1')
		print('skoSP = 7653/8192')
		print('skoX = 287578198252716031/288230376151711744')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_58(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_58 SAT")
		print('delta = 9/8')
		print('skoS2 = 31388019/33554432')
		print('skoSM = 1')
		print('skoSP = 538531999191662591/576460752303423488')
		print('skoX = 287578198252716031/288230376151711744')
		print('pi = 56593901693316947/18014398509481984')
		exit(0)
	
	
	if pre_condition_59(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_59 SAT")
		print('delta = 9/8')
		print('skoS2 = 31388019/33554432')
		print('skoSM = 1')
		print('skoSP = 538531999191662591/576460752303423488')
		print('skoX = 287578198252716031/288230376151711744')
		print('pi = 56593901693316947/18014398509481984')
		exit(0)
	
	
	if pre_condition_60(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_60 SAT")
		print('delta = 9/8')
		print('skoS2 = 15/16')
		print('skoSM = 1')
		print('skoSP = 7653/8192')
		print('skoX = 287578198252716031/288230376151711744')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_61(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_61 SAT")
		print('delta = 9/8')
		print('skoS2 = 15/16')
		print('skoSM = 1')
		print('skoSP = 7653/8192')
		print('skoX = 287578198252716031/288230376151711744')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_62(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_62 SAT")
		print('delta = 9/8')
		print('skoS2 = 31388019/33554432')
		print('skoSM = 1')
		print('skoSP = 538531999191662591/576460752303423488')
		print('skoX = 287578198252716031/288230376151711744')
		print('pi = 56593901693316947/18014398509481984')
		exit(0)
	
	
	if pre_condition_63(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_63 SAT")
		print('delta = 9/8')
		print('skoS2 = 31388019/33554432')
		print('skoSM = 1')
		print('skoSP = 538531999191662591/576460752303423488')
		print('skoX = 287578198252716031/288230376151711744')
		print('pi = 56593901693316947/18014398509481984')
		exit(0)


	print("UNKNOWN")
	exit(0)
