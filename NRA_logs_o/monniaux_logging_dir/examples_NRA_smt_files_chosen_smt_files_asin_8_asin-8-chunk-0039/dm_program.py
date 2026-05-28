import sympy
from sympy import *

def pre_condition_0(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= skoX) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta >= -skoX) & (delta >= skoS2**2 - 2) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (pi*skoS2 + pi/2 + 1/20 >= skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 2), Symbol('pi')), Rational(1, 20)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= skoX) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta >= -skoX) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 5/4) & (delta >= skoS2**2 - 2) & (delta - skoX >= -5/4) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (3*pi*skoS2/2 + 3*pi/4 + 3/40 >= skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(5, 4)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-5, 4)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(3, 2), Symbol('pi'), Symbol('skoS2')), Mul(Rational(3, 4), Symbol('pi')), Rational(3, 40)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 5/4) & (delta >= skoS2**2 - 2) & (delta - skoX >= -3/4) & (delta >= 2 - skoS2**2) & (pi*skoS2/2 + pi/4 - 9/40 <= 3*pi*skoS2/2 + 3*pi/4 + 3/40)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(5, 4)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-3, 4)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), LessThan(Add(Mul(Rational(1, 2), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 4), Symbol('pi')), Rational(-9, 40)), Add(Mul(Rational(3, 2), Symbol('pi'), Symbol('skoS2')), Mul(Rational(3, 4), Symbol('pi')), Rational(3, 40))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_4(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 9/16) & (delta >= skoS2**2 - 2) & (delta - skoX >= -9/16) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (5*pi*skoS2/4 + 5*pi/8 + 1/16 >= skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(9, 16)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-9, 16)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(5, 4), Symbol('pi'), Symbol('skoS2')), Mul(Rational(5, 8), Symbol('pi')), Rational(1, 16)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_5(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 3/4) & (delta >= skoS2**2 - 2) & (delta - skoX >= -9/16) & (delta >= 2 - skoS2**2) & (pi*skoS2/2 + pi/4 - 9/40 <= 5*pi*skoS2/4 + 5*pi/8 + 1/16)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(3, 4)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-9, 16)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), LessThan(Add(Mul(Rational(1, 2), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 4), Symbol('pi')), Rational(-9, 40)), Add(Mul(Rational(5, 4), Symbol('pi'), Symbol('skoS2')), Mul(Rational(5, 8), Symbol('pi')), Rational(1, 16))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_6(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 17/64) & (delta >= skoS2**2 - 2) & (delta - skoX >= -17/64) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (9*pi*skoS2/8 + 9*pi/16 + 9/160 >= skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(17, 64)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-17, 64)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(9, 8), Symbol('pi'), Symbol('skoS2')), Mul(Rational(9, 16), Symbol('pi')), Rational(9, 160)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_7(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 7/16) & (delta >= skoS2**2 - 2) & (delta - skoX >= -17/64) & (delta >= 2 - skoS2**2) & (3*pi*skoS2/4 + 3*pi/8 - 19/80 <= 9*pi*skoS2/8 + 9*pi/16 + 9/160)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(7, 16)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-17, 64)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), LessThan(Add(Mul(Rational(3, 4), Symbol('pi'), Symbol('skoS2')), Mul(Rational(3, 8), Symbol('pi')), Rational(-19, 80)), Add(Mul(Rational(9, 8), Symbol('pi'), Symbol('skoS2')), Mul(Rational(9, 16), Symbol('pi')), Rational(9, 160))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_8(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 33/256) & (delta >= skoS2**2 - 2) & (delta - skoX >= -33/256) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (17*pi*skoS2/16 + 17*pi/32 + 17/320 >= skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(33, 256)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-33, 256)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(17, 16), Symbol('pi'), Symbol('skoS2')), Mul(Rational(17, 32), Symbol('pi')), Rational(17, 320)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_9(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 15/64) & (delta >= skoS2**2 - 2) & (delta - skoX >= -33/256) & (delta >= 2 - skoS2**2) & (7*pi*skoS2/8 + 7*pi/16 - 39/160 <= 17*pi*skoS2/16 + 17*pi/32 + 17/320)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(15, 64)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-33, 256)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), LessThan(Add(Mul(Rational(7, 8), Symbol('pi'), Symbol('skoS2')), Mul(Rational(7, 16), Symbol('pi')), Rational(-39, 160)), Add(Mul(Rational(17, 16), Symbol('pi'), Symbol('skoS2')), Mul(Rational(17, 32), Symbol('pi')), Rational(17, 320))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_10(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 65/1024) & (delta >= skoS2**2 - 2) & (delta - skoX >= -65/1024) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (33*pi*skoS2/32 + 33*pi/64 + 33/640 >= skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(65, 1024)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-65, 1024)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(33, 32), Symbol('pi'), Symbol('skoS2')), Mul(Rational(33, 64), Symbol('pi')), Rational(33, 640)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_11(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 31/256) & (delta >= skoS2**2 - 2) & (delta - skoX >= -65/1024) & (delta >= 2 - skoS2**2) & (15*pi*skoS2/16 + 15*pi/32 - 79/320 <= 33*pi*skoS2/32 + 33*pi/64 + 33/640)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(31, 256)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-65, 1024)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), LessThan(Add(Mul(Rational(15, 16), Symbol('pi'), Symbol('skoS2')), Mul(Rational(15, 32), Symbol('pi')), Rational(-79, 320)), Add(Mul(Rational(33, 32), Symbol('pi'), Symbol('skoS2')), Mul(Rational(33, 64), Symbol('pi')), Rational(33, 640))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_12(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 129/4096) & (delta >= skoS2**2 - 2) & (delta - skoX >= -129/4096) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (65*pi*skoS2/64 + 65*pi/128 + 13/256 >= skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(129, 4096)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-129, 4096)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(65, 64), Symbol('pi'), Symbol('skoS2')), Mul(Rational(65, 128), Symbol('pi')), Rational(13, 256)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_13(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 63/1024) & (delta >= skoS2**2 - 2) & (delta - skoX >= -129/4096) & (delta >= 2 - skoS2**2) & (31*pi*skoS2/32 + 31*pi/64 - 159/640 <= 65*pi*skoS2/64 + 65*pi/128 + 13/256)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(63, 1024)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-129, 4096)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), LessThan(Add(Mul(Rational(31, 32), Symbol('pi'), Symbol('skoS2')), Mul(Rational(31, 64), Symbol('pi')), Rational(-159, 640)), Add(Mul(Rational(65, 64), Symbol('pi'), Symbol('skoS2')), Mul(Rational(65, 128), Symbol('pi')), Rational(13, 256))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_14(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 257/16384) & (delta >= skoS2**2 - 2) & (delta - skoX >= -257/16384) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (129*pi*skoS2/128 + 129*pi/256 + 129/2560 >= skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(257, 16384)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-257, 16384)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(129, 128), Symbol('pi'), Symbol('skoS2')), Mul(Rational(129, 256), Symbol('pi')), Rational(129, 2560)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_15(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 127/4096) & (delta >= skoS2**2 - 2) & (delta - skoX >= -257/16384) & (delta >= 2 - skoS2**2) & (63*pi*skoS2/64 + 63*pi/128 - 319/1280 <= 129*pi*skoS2/128 + 129*pi/256 + 129/2560)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(127, 4096)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-257, 16384)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), LessThan(Add(Mul(Rational(63, 64), Symbol('pi'), Symbol('skoS2')), Mul(Rational(63, 128), Symbol('pi')), Rational(-319, 1280)), Add(Mul(Rational(129, 128), Symbol('pi'), Symbol('skoS2')), Mul(Rational(129, 256), Symbol('pi')), Rational(129, 2560))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_16(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 513/65536) & (delta >= skoS2**2 - 2) & (delta - skoX >= -513/65536) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (257*pi*skoS2/256 + 257*pi/512 + 257/5120 >= skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(513, 65536)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-513, 65536)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(257, 256), Symbol('pi'), Symbol('skoS2')), Mul(Rational(257, 512), Symbol('pi')), Rational(257, 5120)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_17(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 255/16384) & (delta >= skoS2**2 - 2) & (delta - skoX >= -513/65536) & (delta >= 2 - skoS2**2) & (127*pi*skoS2/128 + 127*pi/256 - 639/2560 <= 257*pi*skoS2/256 + 257*pi/512 + 257/5120)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(255, 16384)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-513, 65536)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), LessThan(Add(Mul(Rational(127, 128), Symbol('pi'), Symbol('skoS2')), Mul(Rational(127, 256), Symbol('pi')), Rational(-639, 2560)), Add(Mul(Rational(257, 256), Symbol('pi'), Symbol('skoS2')), Mul(Rational(257, 512), Symbol('pi')), Rational(257, 5120))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_18(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 777/16384) & (delta >= skoS2**2 - 2) & (delta - skoX >= -777/16384) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (131*pi*skoS2/128 + 131*pi/256 + 131/2560 >= skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(777, 16384)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-777, 16384)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(131, 128), Symbol('pi'), Symbol('skoS2')), Mul(Rational(131, 256), Symbol('pi')), Rational(131, 2560)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_19(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 63/1024) & (delta >= skoS2**2 - 2) & (delta - skoX >= -777/16384) & (delta >= 2 - skoS2**2) & (31*pi*skoS2/32 + 31*pi/64 - 159/640 <= 131*pi*skoS2/128 + 131*pi/256 + 131/2560)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(63, 1024)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-777, 16384)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), LessThan(Add(Mul(Rational(31, 32), Symbol('pi'), Symbol('skoS2')), Mul(Rational(31, 64), Symbol('pi')), Rational(-159, 640)), Add(Mul(Rational(131, 128), Symbol('pi'), Symbol('skoS2')), Mul(Rational(131, 256), Symbol('pi')), Rational(131, 2560))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_20(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 3633/65536) & (delta >= skoS2**2 - 2) & (delta - skoX >= -3633/65536) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (263*pi*skoS2/256 + 263*pi/512 + 263/5120 >= skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(3633, 65536)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-3633, 65536)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(263, 256), Symbol('pi'), Symbol('skoS2')), Mul(Rational(263, 512), Symbol('pi')), Rational(263, 5120)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_21(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 63/1024) & (delta >= skoS2**2 - 2) & (delta - skoX >= -3633/65536) & (delta >= 2 - skoS2**2) & (31*pi*skoS2/32 + 31*pi/64 - 159/640 <= 263*pi*skoS2/256 + 263*pi/512 + 263/5120)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(63, 1024)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-3633, 65536)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), LessThan(Add(Mul(Rational(31, 32), Symbol('pi'), Symbol('skoS2')), Mul(Rational(31, 64), Symbol('pi')), Rational(-159, 640)), Add(Mul(Rational(263, 256), Symbol('pi'), Symbol('skoS2')), Mul(Rational(263, 512), Symbol('pi')), Rational(263, 5120))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_22(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 15585/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= -15585/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (527*pi*skoS2/512 + 527*pi/1024 + 527/10240 >= skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(15585, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-15585, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(527, 512), Symbol('pi'), Symbol('skoS2')), Mul(Rational(527, 1024), Symbol('pi')), Rational(527, 10240)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_23(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 63/1024) & (delta >= skoS2**2 - 2) & (delta - skoX >= -15585/262144) & (delta >= 2 - skoS2**2) & (31*pi*skoS2/32 + 31*pi/64 - 159/640 <= 527*pi*skoS2/512 + 527*pi/1024 + 527/10240)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(63, 1024)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-15585, 262144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), LessThan(Add(Mul(Rational(31, 32), Symbol('pi'), Symbol('skoS2')), Mul(Rational(31, 64), Symbol('pi')), Rational(-159, 640)), Add(Mul(Rational(527, 512), Symbol('pi'), Symbol('skoS2')), Mul(Rational(527, 1024), Symbol('pi')), Rational(527, 10240))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_24(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 64449/1048576) & (delta >= skoS2**2 - 2) & (delta - skoX >= -64449/1048576) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (1055*pi*skoS2/1024 + 1055*pi/2048 + 211/4096 >= skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(64449, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-64449, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(1055, 1024), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1055, 2048), Symbol('pi')), Rational(211, 4096)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_25(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 63/1024) & (delta >= skoS2**2 - 2) & (delta - skoX >= -64449/1048576) & (delta >= 2 - skoS2**2) & (31*pi*skoS2/32 + 31*pi/64 - 159/640 <= 1055*pi*skoS2/1024 + 1055*pi/2048 + 211/4096)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(63, 1024)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-64449, 1048576)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), LessThan(Add(Mul(Rational(31, 32), Symbol('pi'), Symbol('skoS2')), Mul(Rational(31, 64), Symbol('pi')), Rational(-159, 640)), Add(Mul(Rational(1055, 1024), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1055, 2048), Symbol('pi')), Rational(211, 4096))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_26(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 64449/1048576) & (delta >= skoS2**2 - 2) & (delta - skoX >= -64449/1048576) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (1055*pi*skoS2/1024 + 1055*pi/2048 + 211/4096 >= skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(64449, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-64449, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(1055, 1024), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1055, 2048), Symbol('pi')), Rational(211, 4096)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_27(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 63/1024) & (delta >= skoS2**2 - 2) & (delta - skoX >= -64449/1048576) & (delta >= 2 - skoS2**2) & (31*pi*skoS2/32 + 31*pi/64 - 159/640 <= 1055*pi*skoS2/1024 + 1055*pi/2048 + 211/4096)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(63, 1024)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-64449, 1048576)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), LessThan(Add(Mul(Rational(31, 32), Symbol('pi'), Symbol('skoS2')), Mul(Rational(31, 64), Symbol('pi')), Rational(-159, 640)), Add(Mul(Rational(1055, 1024), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1055, 2048), Symbol('pi')), Rational(211, 4096))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_28(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 64449/1048576) & (delta >= skoS2**2 - 2) & (delta - skoX >= -64449/1048576) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (1055*pi*skoS2/1024 + 1055*pi/2048 + 211/4096 >= skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(64449, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-64449, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(1055, 1024), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1055, 2048), Symbol('pi')), Rational(211, 4096)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_29(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 63/1024) & (delta >= skoS2**2 - 2) & (delta - skoX >= -64449/1048576) & (delta >= 2 - skoS2**2) & (31*pi*skoS2/32 + 31*pi/64 - 159/640 <= 1055*pi*skoS2/1024 + 1055*pi/2048 + 211/4096)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(63, 1024)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-64449, 1048576)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), LessThan(Add(Mul(Rational(31, 32), Symbol('pi'), Symbol('skoS2')), Mul(Rational(31, 64), Symbol('pi')), Rational(-159, 640)), Add(Mul(Rational(1055, 1024), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1055, 2048), Symbol('pi')), Rational(211, 4096))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_30(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 64449/1048576) & (delta >= skoS2**2 - 2) & (delta - skoX >= -64449/1048576) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (1055*pi*skoS2/1024 + 1055*pi/2048 + 211/4096 >= skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(64449, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-64449, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(1055, 1024), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1055, 2048), Symbol('pi')), Rational(211, 4096)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_31(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 63/1024) & (delta >= skoS2**2 - 2) & (delta - skoX >= -64449/1048576) & (delta >= 2 - skoS2**2) & (31*pi*skoS2/32 + 31*pi/64 - 159/640 <= 1055*pi*skoS2/1024 + 1055*pi/2048 + 211/4096)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(63, 1024)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-64449, 1048576)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), LessThan(Add(Mul(Rational(31, 32), Symbol('pi'), Symbol('skoS2')), Mul(Rational(31, 64), Symbol('pi')), Rational(-159, 640)), Add(Mul(Rational(1055, 1024), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1055, 2048), Symbol('pi')), Rational(211, 4096))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_32(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 64449/1048576) & (delta >= skoS2**2 - 2) & (delta - skoX >= -64449/1048576) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (1055*pi*skoS2/1024 + 1055*pi/2048 + 211/4096 >= skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(64449, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-64449, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(1055, 1024), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1055, 2048), Symbol('pi')), Rational(211, 4096)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_33(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 63/1024) & (delta >= skoS2**2 - 2) & (delta - skoX >= -64449/1048576) & (delta >= 2 - skoS2**2) & (31*pi*skoS2/32 + 31*pi/64 - 159/640 <= 1055*pi*skoS2/1024 + 1055*pi/2048 + 211/4096)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(63, 1024)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-64449, 1048576)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), LessThan(Add(Mul(Rational(31, 32), Symbol('pi'), Symbol('skoS2')), Mul(Rational(31, 64), Symbol('pi')), Rational(-159, 640)), Add(Mul(Rational(1055, 1024), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1055, 2048), Symbol('pi')), Rational(211, 4096))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_34(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 64449/1048576) & (delta >= skoS2**2 - 2) & (delta - skoX >= -64449/1048576) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (1055*pi*skoS2/1024 + 1055*pi/2048 + 211/4096 >= skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(64449, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-64449, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(1055, 1024), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1055, 2048), Symbol('pi')), Rational(211, 4096)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_35(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 63/1024) & (delta >= skoS2**2 - 2) & (delta - skoX >= -64449/1048576) & (delta >= 2 - skoS2**2) & (31*pi*skoS2/32 + 31*pi/64 - 159/640 <= 1055*pi*skoS2/1024 + 1055*pi/2048 + 211/4096)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(63, 1024)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-64449, 1048576)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), LessThan(Add(Mul(Rational(31, 32), Symbol('pi'), Symbol('skoS2')), Mul(Rational(31, 64), Symbol('pi')), Rational(-159, 640)), Add(Mul(Rational(1055, 1024), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1055, 2048), Symbol('pi')), Rational(211, 4096))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_36(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 64449/1048576) & (delta >= skoS2**2 - 2) & (delta - skoX >= -64449/1048576) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (1055*pi*skoS2/1024 + 1055*pi/2048 + 211/4096 >= skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(64449, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-64449, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(1055, 1024), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1055, 2048), Symbol('pi')), Rational(211, 4096)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_37(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 63/1024) & (delta >= skoS2**2 - 2) & (delta - skoX >= -64449/1048576) & (delta >= 2 - skoS2**2) & (31*pi*skoS2/32 + 31*pi/64 - 159/640 <= 1055*pi*skoS2/1024 + 1055*pi/2048 + 211/4096)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(63, 1024)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-64449, 1048576)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), LessThan(Add(Mul(Rational(31, 32), Symbol('pi'), Symbol('skoS2')), Mul(Rational(31, 64), Symbol('pi')), Rational(-159, 640)), Add(Mul(Rational(1055, 1024), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1055, 2048), Symbol('pi')), Rational(211, 4096))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_38(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 64449/1048576) & (delta >= skoS2**2 - 2) & (delta - skoX >= -64449/1048576) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (1055*pi*skoS2/1024 + 1055*pi/2048 + 211/4096 >= skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(64449, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-64449, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(1055, 1024), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1055, 2048), Symbol('pi')), Rational(211, 4096)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_39(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 63/1024) & (delta >= skoS2**2 - 2) & (delta - skoX >= -64449/1048576) & (delta >= 2 - skoS2**2) & (31*pi*skoS2/32 + 31*pi/64 - 159/640 <= 1055*pi*skoS2/1024 + 1055*pi/2048 + 211/4096)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(63, 1024)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-64449, 1048576)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), LessThan(Add(Mul(Rational(31, 32), Symbol('pi'), Symbol('skoS2')), Mul(Rational(31, 64), Symbol('pi')), Rational(-159, 640)), Add(Mul(Rational(1055, 1024), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1055, 2048), Symbol('pi')), Rational(211, 4096))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_40(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 64449/1048576) & (delta >= skoS2**2 - 2) & (delta - skoX >= -64449/1048576) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (1055*pi*skoS2/1024 + 1055*pi/2048 + 211/4096 >= skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(64449, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-64449, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(1055, 1024), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1055, 2048), Symbol('pi')), Rational(211, 4096)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_41(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 63/1024) & (delta >= skoS2**2 - 2) & (delta - skoX >= -64449/1048576) & (delta >= 2 - skoS2**2) & (31*pi*skoS2/32 + 31*pi/64 - 159/640 <= 1055*pi*skoS2/1024 + 1055*pi/2048 + 211/4096)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(63, 1024)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-64449, 1048576)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), LessThan(Add(Mul(Rational(31, 32), Symbol('pi'), Symbol('skoS2')), Mul(Rational(31, 64), Symbol('pi')), Rational(-159, 640)), Add(Mul(Rational(1055, 1024), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1055, 2048), Symbol('pi')), Rational(211, 4096))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_42(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 64449/1048576) & (delta >= skoS2**2 - 2) & (delta - skoX >= -64449/1048576) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (1055*pi*skoS2/1024 + 1055*pi/2048 + 211/4096 >= skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(64449, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-64449, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(1055, 1024), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1055, 2048), Symbol('pi')), Rational(211, 4096)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_43(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 63/1024) & (delta >= skoS2**2 - 2) & (delta - skoX >= -64449/1048576) & (delta >= 2 - skoS2**2) & (31*pi*skoS2/32 + 31*pi/64 - 159/640 <= 1055*pi*skoS2/1024 + 1055*pi/2048 + 211/4096)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(63, 1024)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-64449, 1048576)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), LessThan(Add(Mul(Rational(31, 32), Symbol('pi'), Symbol('skoS2')), Mul(Rational(31, 64), Symbol('pi')), Rational(-159, 640)), Add(Mul(Rational(1055, 1024), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1055, 2048), Symbol('pi')), Rational(211, 4096))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_44(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 64449/1048576) & (delta >= skoS2**2 - 2) & (delta - skoX >= -64449/1048576) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (1055*pi*skoS2/1024 + 1055*pi/2048 + 211/4096 >= skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(64449, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-64449, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(1055, 1024), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1055, 2048), Symbol('pi')), Rational(211, 4096)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_45(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 63/1024) & (delta >= skoS2**2 - 2) & (delta - skoX >= -64449/1048576) & (delta >= 2 - skoS2**2) & (31*pi*skoS2/32 + 31*pi/64 - 159/640 <= 1055*pi*skoS2/1024 + 1055*pi/2048 + 211/4096)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(63, 1024)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-64449, 1048576)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), LessThan(Add(Mul(Rational(31, 32), Symbol('pi'), Symbol('skoS2')), Mul(Rational(31, 64), Symbol('pi')), Rational(-159, 640)), Add(Mul(Rational(1055, 1024), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1055, 2048), Symbol('pi')), Rational(211, 4096))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_46(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 64449/1048576) & (delta >= skoS2**2 - 2) & (delta - skoX >= -64449/1048576) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (1055*pi*skoS2/1024 + 1055*pi/2048 + 211/4096 >= skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(64449, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-64449, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(1055, 1024), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1055, 2048), Symbol('pi')), Rational(211, 4096)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_47(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 63/1024) & (delta >= skoS2**2 - 2) & (delta - skoX >= -64449/1048576) & (delta >= 2 - skoS2**2) & (31*pi*skoS2/32 + 31*pi/64 - 159/640 <= 1055*pi*skoS2/1024 + 1055*pi/2048 + 211/4096)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(63, 1024)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-64449, 1048576)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), LessThan(Add(Mul(Rational(31, 32), Symbol('pi'), Symbol('skoS2')), Mul(Rational(31, 64), Symbol('pi')), Rational(-159, 640)), Add(Mul(Rational(1055, 1024), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1055, 2048), Symbol('pi')), Rational(211, 4096))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_48(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 64449/1048576) & (delta >= skoS2**2 - 2) & (delta - skoX >= -64449/1048576) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (1055*pi*skoS2/1024 + 1055*pi/2048 + 211/4096 >= skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(64449, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-64449, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(1055, 1024), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1055, 2048), Symbol('pi')), Rational(211, 4096)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_49(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 63/1024) & (delta >= skoS2**2 - 2) & (delta - skoX >= -64449/1048576) & (delta >= 2 - skoS2**2) & (31*pi*skoS2/32 + 31*pi/64 - 159/640 <= 1055*pi*skoS2/1024 + 1055*pi/2048 + 211/4096)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(63, 1024)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-64449, 1048576)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), LessThan(Add(Mul(Rational(31, 32), Symbol('pi'), Symbol('skoS2')), Mul(Rational(31, 64), Symbol('pi')), Rational(-159, 640)), Add(Mul(Rational(1055, 1024), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1055, 2048), Symbol('pi')), Rational(211, 4096))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_50(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 64449/1048576) & (delta >= skoS2**2 - 2) & (delta - skoX >= -64449/1048576) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (1055*pi*skoS2/1024 + 1055*pi/2048 + 211/4096 >= skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(64449, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-64449, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(1055, 1024), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1055, 2048), Symbol('pi')), Rational(211, 4096)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_51(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 63/1024) & (delta >= skoS2**2 - 2) & (delta - skoX >= -64449/1048576) & (delta >= 2 - skoS2**2) & (31*pi*skoS2/32 + 31*pi/64 - 159/640 <= 1055*pi*skoS2/1024 + 1055*pi/2048 + 211/4096)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(63, 1024)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-64449, 1048576)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), LessThan(Add(Mul(Rational(31, 32), Symbol('pi'), Symbol('skoS2')), Mul(Rational(31, 64), Symbol('pi')), Rational(-159, 640)), Add(Mul(Rational(1055, 1024), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1055, 2048), Symbol('pi')), Rational(211, 4096))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_52(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 64449/1048576) & (delta >= skoS2**2 - 2) & (delta - skoX >= -64449/1048576) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (1055*pi*skoS2/1024 + 1055*pi/2048 + 211/4096 >= skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(64449, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-64449, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(1055, 1024), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1055, 2048), Symbol('pi')), Rational(211, 4096)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_53(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 63/1024) & (delta >= skoS2**2 - 2) & (delta - skoX >= -64449/1048576) & (delta >= 2 - skoS2**2) & (31*pi*skoS2/32 + 31*pi/64 - 159/640 <= 1055*pi*skoS2/1024 + 1055*pi/2048 + 211/4096)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(63, 1024)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-64449, 1048576)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), LessThan(Add(Mul(Rational(31, 32), Symbol('pi'), Symbol('skoS2')), Mul(Rational(31, 64), Symbol('pi')), Rational(-159, 640)), Add(Mul(Rational(1055, 1024), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1055, 2048), Symbol('pi')), Rational(211, 4096))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_54(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 64449/1048576) & (delta >= skoS2**2 - 2) & (delta - skoX >= -64449/1048576) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (1055*pi*skoS2/1024 + 1055*pi/2048 + 211/4096 >= skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(64449, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-64449, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(1055, 1024), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1055, 2048), Symbol('pi')), Rational(211, 4096)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_55(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 63/1024) & (delta >= skoS2**2 - 2) & (delta - skoX >= -64449/1048576) & (delta >= 2 - skoS2**2) & (31*pi*skoS2/32 + 31*pi/64 - 159/640 <= 1055*pi*skoS2/1024 + 1055*pi/2048 + 211/4096)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(63, 1024)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-64449, 1048576)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), LessThan(Add(Mul(Rational(31, 32), Symbol('pi'), Symbol('skoS2')), Mul(Rational(31, 64), Symbol('pi')), Rational(-159, 640)), Add(Mul(Rational(1055, 1024), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1055, 2048), Symbol('pi')), Rational(211, 4096))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_56(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 64449/1048576) & (delta >= skoS2**2 - 2) & (delta - skoX >= -64449/1048576) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (1055*pi*skoS2/1024 + 1055*pi/2048 + 211/4096 >= skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(64449, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-64449, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(1055, 1024), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1055, 2048), Symbol('pi')), Rational(211, 4096)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_57(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 63/1024) & (delta >= skoS2**2 - 2) & (delta - skoX >= -64449/1048576) & (delta >= 2 - skoS2**2) & (31*pi*skoS2/32 + 31*pi/64 - 159/640 <= 1055*pi*skoS2/1024 + 1055*pi/2048 + 211/4096)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(63, 1024)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-64449, 1048576)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), LessThan(Add(Mul(Rational(31, 32), Symbol('pi'), Symbol('skoS2')), Mul(Rational(31, 64), Symbol('pi')), Rational(-159, 640)), Add(Mul(Rational(1055, 1024), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1055, 2048), Symbol('pi')), Rational(211, 4096))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_58(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 64449/1048576) & (delta >= skoS2**2 - 2) & (delta - skoX >= -64449/1048576) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (1055*pi*skoS2/1024 + 1055*pi/2048 + 211/4096 >= skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(64449, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-64449, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(1055, 1024), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1055, 2048), Symbol('pi')), Rational(211, 4096)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_59(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 63/1024) & (delta >= skoS2**2 - 2) & (delta - skoX >= -64449/1048576) & (delta >= 2 - skoS2**2) & (31*pi*skoS2/32 + 31*pi/64 - 159/640 <= 1055*pi*skoS2/1024 + 1055*pi/2048 + 211/4096)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(63, 1024)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-64449, 1048576)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), LessThan(Add(Mul(Rational(31, 32), Symbol('pi'), Symbol('skoS2')), Mul(Rational(31, 64), Symbol('pi')), Rational(-159, 640)), Add(Mul(Rational(1055, 1024), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1055, 2048), Symbol('pi')), Rational(211, 4096))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_60(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 64449/1048576) & (delta >= skoS2**2 - 2) & (delta - skoX >= -64449/1048576) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (1055*pi*skoS2/1024 + 1055*pi/2048 + 211/4096 >= skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(64449, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-64449, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(1055, 1024), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1055, 2048), Symbol('pi')), Rational(211, 4096)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_61(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 63/1024) & (delta >= skoS2**2 - 2) & (delta - skoX >= -64449/1048576) & (delta >= 2 - skoS2**2) & (31*pi*skoS2/32 + 31*pi/64 - 159/640 <= 1055*pi*skoS2/1024 + 1055*pi/2048 + 211/4096)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(63, 1024)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-64449, 1048576)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), LessThan(Add(Mul(Rational(31, 32), Symbol('pi'), Symbol('skoS2')), Mul(Rational(31, 64), Symbol('pi')), Rational(-159, 640)), Add(Mul(Rational(1055, 1024), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1055, 2048), Symbol('pi')), Rational(211, 4096))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_62(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 64449/1048576) & (delta >= skoS2**2 - 2) & (delta - skoX >= -64449/1048576) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (1055*pi*skoS2/1024 + 1055*pi/2048 + 211/4096 >= skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(64449, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-64449, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(1055, 1024), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1055, 2048), Symbol('pi')), Rational(211, 4096)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_63(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 63/1024) & (delta >= skoS2**2 - 2) & (delta - skoX >= -64449/1048576) & (delta >= 2 - skoS2**2) & (31*pi*skoS2/32 + 31*pi/64 - 159/640 <= 1055*pi*skoS2/1024 + 1055*pi/2048 + 211/4096)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(63, 1024)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-64449, 1048576)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), LessThan(Add(Mul(Rational(31, 32), Symbol('pi'), Symbol('skoS2')), Mul(Rational(31, 64), Symbol('pi')), Rational(-159, 640)), Add(Mul(Rational(1055, 1024), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1055, 2048), Symbol('pi')), Rational(211, 4096))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_64(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 64449/1048576) & (delta >= skoS2**2 - 2) & (delta - skoX >= -64449/1048576) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (1055*pi*skoS2/1024 + 1055*pi/2048 + 211/4096 >= skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(64449, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-64449, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(1055, 1024), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1055, 2048), Symbol('pi')), Rational(211, 4096)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_65(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 63/1024) & (delta >= skoS2**2 - 2) & (delta - skoX >= -64449/1048576) & (delta >= 2 - skoS2**2) & (31*pi*skoS2/32 + 31*pi/64 - 159/640 <= 1055*pi*skoS2/1024 + 1055*pi/2048 + 211/4096)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(63, 1024)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-64449, 1048576)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), LessThan(Add(Mul(Rational(31, 32), Symbol('pi'), Symbol('skoS2')), Mul(Rational(31, 64), Symbol('pi')), Rational(-159, 640)), Add(Mul(Rational(1055, 1024), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1055, 2048), Symbol('pi')), Rational(211, 4096))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_66(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 64449/1048576) & (delta >= skoS2**2 - 2) & (delta - skoX >= -64449/1048576) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (1055*pi*skoS2/1024 + 1055*pi/2048 + 211/4096 >= skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(64449, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-64449, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(1055, 1024), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1055, 2048), Symbol('pi')), Rational(211, 4096)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_67(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 63/1024) & (delta >= skoS2**2 - 2) & (delta - skoX >= -64449/1048576) & (delta >= 2 - skoS2**2) & (31*pi*skoS2/32 + 31*pi/64 - 159/640 <= 1055*pi*skoS2/1024 + 1055*pi/2048 + 211/4096)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(63, 1024)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-64449, 1048576)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), LessThan(Add(Mul(Rational(31, 32), Symbol('pi'), Symbol('skoS2')), Mul(Rational(31, 64), Symbol('pi')), Rational(-159, 640)), Add(Mul(Rational(1055, 1024), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1055, 2048), Symbol('pi')), Rational(211, 4096))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_68(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 64449/1048576) & (delta >= skoS2**2 - 2) & (delta - skoX >= -64449/1048576) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (1055*pi*skoS2/1024 + 1055*pi/2048 + 211/4096 >= skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(64449, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-64449, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(1055, 1024), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1055, 2048), Symbol('pi')), Rational(211, 4096)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_69(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 63/1024) & (delta >= skoS2**2 - 2) & (delta - skoX >= -64449/1048576) & (delta >= 2 - skoS2**2) & (31*pi*skoS2/32 + 31*pi/64 - 159/640 <= 1055*pi*skoS2/1024 + 1055*pi/2048 + 211/4096)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(63, 1024)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-64449, 1048576)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), LessThan(Add(Mul(Rational(31, 32), Symbol('pi'), Symbol('skoS2')), Mul(Rational(31, 64), Symbol('pi')), Rational(-159, 640)), Add(Mul(Rational(1055, 1024), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1055, 2048), Symbol('pi')), Rational(211, 4096))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_70(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 64449/1048576) & (delta >= skoS2**2 - 2) & (delta - skoX >= -64449/1048576) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (1055*pi*skoS2/1024 + 1055*pi/2048 + 211/4096 >= skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(64449, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-64449, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(1055, 1024), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1055, 2048), Symbol('pi')), Rational(211, 4096)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_71(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 63/1024) & (delta >= skoS2**2 - 2) & (delta - skoX >= -64449/1048576) & (delta >= 2 - skoS2**2) & (31*pi*skoS2/32 + 31*pi/64 - 159/640 <= 1055*pi*skoS2/1024 + 1055*pi/2048 + 211/4096)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(63, 1024)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-64449, 1048576)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), LessThan(Add(Mul(Rational(31, 32), Symbol('pi'), Symbol('skoS2')), Mul(Rational(31, 64), Symbol('pi')), Rational(-159, 640)), Add(Mul(Rational(1055, 1024), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1055, 2048), Symbol('pi')), Rational(211, 4096))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_72(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 64449/1048576) & (delta >= skoS2**2 - 2) & (delta - skoX >= -64449/1048576) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (1055*pi*skoS2/1024 + 1055*pi/2048 + 211/4096 >= skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(64449, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-64449, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(1055, 1024), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1055, 2048), Symbol('pi')), Rational(211, 4096)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_73(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 63/1024) & (delta >= skoS2**2 - 2) & (delta - skoX >= -64449/1048576) & (delta >= 2 - skoS2**2) & (31*pi*skoS2/32 + 31*pi/64 - 159/640 <= 1055*pi*skoS2/1024 + 1055*pi/2048 + 211/4096)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(63, 1024)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-64449, 1048576)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), LessThan(Add(Mul(Rational(31, 32), Symbol('pi'), Symbol('skoS2')), Mul(Rational(31, 64), Symbol('pi')), Rational(-159, 640)), Add(Mul(Rational(1055, 1024), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1055, 2048), Symbol('pi')), Rational(211, 4096))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_74(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 64449/1048576) & (delta >= skoS2**2 - 2) & (delta - skoX >= -64449/1048576) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (1055*pi*skoS2/1024 + 1055*pi/2048 + 211/4096 >= skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(64449, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-64449, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(1055, 1024), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1055, 2048), Symbol('pi')), Rational(211, 4096)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_75(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 63/1024) & (delta >= skoS2**2 - 2) & (delta - skoX >= -64449/1048576) & (delta >= 2 - skoS2**2) & (31*pi*skoS2/32 + 31*pi/64 - 159/640 <= 1055*pi*skoS2/1024 + 1055*pi/2048 + 211/4096)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(63, 1024)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-64449, 1048576)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), LessThan(Add(Mul(Rational(31, 32), Symbol('pi'), Symbol('skoS2')), Mul(Rational(31, 64), Symbol('pi')), Rational(-159, 640)), Add(Mul(Rational(1055, 1024), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1055, 2048), Symbol('pi')), Rational(211, 4096))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_76(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoSM >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (delta + skoX >= 64449/1048576) & (delta >= skoS2**2 - 2) & (delta - skoX >= -64449/1048576) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (1055*pi*skoS2/1024 + 1055*pi/2048 + 211/4096 >= skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), GreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(64449, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-64449, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(1055, 1024), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1055, 2048), Symbol('pi')), Rational(211, 4096)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(delta:sympy.Rational, skoX:sympy.Rational, skoS2:sympy.Rational, pi:sympy.Rational, skoSP:sympy.Rational, skoSM:sympy.Rational):
	# (0 <= delta) & (0 <= skoS2) & (0 <= skoSM) & (0 <= skoSP) & (1 > skoX) & (31415927/10000000 > pi) & (pi > 15707963/5000000) & (skoX > 0) & (skoS2**2 - 2 <= delta) & (skoSM**2 + skoX - 1 <= delta) & (2 - skoS2**2 <= delta) & (-skoSP**2 + skoX + 1 <= delta) & (skoSP**2 - skoX - 1 <= delta) & (-skoSM**2 - skoX + 1 <= delta) & (skoSP*(-pi*skoS2 - pi/2 - 1/20) <= skoSM*(-pi*skoS2 - pi/2 + 1/20) + 1/5)

	post_cond =  And(LessThan(Integer(0), Symbol('delta')), LessThan(Integer(0), Symbol('skoS2')), LessThan(Integer(0), Symbol('skoSM')), LessThan(Integer(0), Symbol('skoSP')), StrictGreaterThan(Integer(1), Symbol('skoX')), StrictGreaterThan(Rational(31415927, 10000000), Symbol('pi')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), LessThan(Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Symbol('delta')), LessThan(Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1)), Symbol('delta')), LessThan(Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Symbol('delta')), LessThan(Add(Mul(Integer(-1), Pow(Symbol('skoSP'), Integer(2))), Symbol('skoX'), Integer(1)), Symbol('delta')), LessThan(Add(Pow(Symbol('skoSP'), Integer(2)), Mul(Integer(-1), Symbol('skoX')), Integer(-1)), Symbol('delta')), LessThan(Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)), Symbol('delta')), LessThan(Mul(Symbol('skoSP'), Add(Mul(Integer(-1), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 2), Symbol('pi')), Rational(-1, 20))), Add(Mul(Symbol('skoSM'), Add(Mul(Integer(-1), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 2), Symbol('pi')), Rational(1, 20))), Rational(1, 5))))

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
		print('skoSP = 1')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_1(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_1 SAT")
		print('delta = 2')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 1')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_2(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_2 SAT")
		print('delta = 1/2')
		print('skoS2 = 3/2')
		print('skoSM = 1/2')
		print('skoSP = 3/2')
		print('skoX = 7/8')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_3(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_3 SAT")
		print('delta = 1/2')
		print('skoS2 = 3/2')
		print('skoSM = 1/2')
		print('skoSP = 3/2')
		print('skoX = 7/8')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_4(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_4 SAT")
		print('delta = 1/2')
		print('skoS2 = 3/2')
		print('skoSM = 1/2')
		print('skoSP = 5/4')
		print('skoX = 5/8')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_5(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_5 SAT")
		print('delta = 1/2')
		print('skoS2 = 3/2')
		print('skoSM = 1/2')
		print('skoSP = 5/4')
		print('skoX = 5/8')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_6(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_6 SAT")
		print('delta = 17/64')
		print('skoS2 = 3/2')
		print('skoSM = 3/4')
		print('skoSP = 9/8')
		print('skoX = 9/32')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_7(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_7 SAT")
		print('delta = 17/64')
		print('skoS2 = 3/2')
		print('skoSM = 3/4')
		print('skoSP = 9/8')
		print('skoX = 9/32')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_8(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_8 SAT")
		print('delta = 1/8')
		print('skoS2 = 11/8')
		print('skoSM = 7/8')
		print('skoSP = 17/16')
		print('skoX = 17/128')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_9(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_9 SAT")
		print('delta = 1/8')
		print('skoS2 = 11/8')
		print('skoSM = 7/8')
		print('skoSP = 17/16')
		print('skoX = 17/128')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_10(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_10 SAT")
		print('delta = 1/16')
		print('skoS2 = 45/32')
		print('skoSM = 15/16')
		print('skoSP = 33/32')
		print('skoX = 33/512')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_11(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_11 SAT")
		print('delta = 1/16')
		print('skoS2 = 45/32')
		print('skoSM = 15/16')
		print('skoSP = 33/32')
		print('skoX = 33/512')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_12(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_12 SAT")
		print('delta = 1/32')
		print('skoS2 = 45/32')
		print('skoSM = 31/32')
		print('skoSP = 65/64')
		print('skoX = 65/2048')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_13(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_13 SAT")
		print('delta = 1/32')
		print('skoS2 = 45/32')
		print('skoSM = 31/32')
		print('skoSP = 65/64')
		print('skoX = 65/2048')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_14(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_14 SAT")
		print('delta = 1/64')
		print('skoS2 = 181/128')
		print('skoSM = 63/64')
		print('skoSP = 129/128')
		print('skoX = 129/8192')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_15(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_15 SAT")
		print('delta = 1/64')
		print('skoS2 = 181/128')
		print('skoSM = 63/64')
		print('skoSP = 129/128')
		print('skoX = 129/8192')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_16(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_16 SAT")
		print('delta = 1/128')
		print('skoS2 = 181/128')
		print('skoSM = 127/128')
		print('skoSP = 257/256')
		print('skoX = 257/32768')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_17(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_17 SAT")
		print('delta = 1/128')
		print('skoS2 = 181/128')
		print('skoSM = 127/128')
		print('skoSP = 257/256')
		print('skoX = 257/32768')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_18(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_18 SAT")
		print('delta = 1/64')
		print('skoS2 = 181/128')
		print('skoSM = 31/32')
		print('skoSP = 131/128')
		print('skoX = 97/2048')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_19(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_19 SAT")
		print('delta = 1/64')
		print('skoS2 = 181/128')
		print('skoSM = 31/32')
		print('skoSP = 131/128')
		print('skoX = 97/2048')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_20(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_20 SAT")
		print('delta = 1/128')
		print('skoS2 = 181/128')
		print('skoSM = 31/32')
		print('skoSP = 263/256')
		print('skoX = 227/4096')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_21(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_21 SAT")
		print('delta = 1/128')
		print('skoS2 = 181/128')
		print('skoSM = 31/32')
		print('skoSP = 263/256')
		print('skoX = 227/4096')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_22(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_22 SAT")
		print('delta = 1/256')
		print('skoS2 = 181/128')
		print('skoSM = 31/32')
		print('skoSP = 527/512')
		print('skoX = 487/8192')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_23(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_23 SAT")
		print('delta = 1/256')
		print('skoS2 = 181/128')
		print('skoSM = 31/32')
		print('skoSP = 527/512')
		print('skoX = 487/8192')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_24(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_24 SAT")
		print('delta = 1/512')
		print('skoS2 = 181/128')
		print('skoSM = 31/32')
		print('skoSP = 1055/1024')
		print('skoX = 1007/16384')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_25(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_25 SAT")
		print('delta = 1/512')
		print('skoS2 = 181/128')
		print('skoSM = 31/32')
		print('skoSP = 1055/1024')
		print('skoX = 1007/16384')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_26(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_26 SAT")
		print('delta = 1/1024')
		print('skoS2 = 181/128')
		print('skoSM = 31/32')
		print('skoSP = 1055/1024')
		print('skoX = 287953299221512191/4611686018427387904')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_27(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_27 SAT")
		print('delta = 1/1024')
		print('skoS2 = 181/128')
		print('skoSM = 31/32')
		print('skoSP = 1055/1024')
		print('skoX = 287953299221512191/4611686018427387904')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_28(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_28 SAT")
		print('delta = 1/1024')
		print('skoS2 = 181/128')
		print('skoSM = 31/32')
		print('skoSP = 1055/1024')
		print('skoX = 287953299221512191/4611686018427387904')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_29(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_29 SAT")
		print('delta = 1/1024')
		print('skoS2 = 181/128')
		print('skoSM = 31/32')
		print('skoSP = 1055/1024')
		print('skoX = 287953299221512191/4611686018427387904')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_30(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_30 SAT")
		print('delta = 1/1024')
		print('skoS2 = 181/128')
		print('skoSM = 31/32')
		print('skoSP = 1055/1024')
		print('skoX = 287953299221512191/4611686018427387904')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_31(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_31 SAT")
		print('delta = 1/1024')
		print('skoS2 = 181/128')
		print('skoSM = 31/32')
		print('skoSP = 1055/1024')
		print('skoX = 287953299221512191/4611686018427387904')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_32(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_32 SAT")
		print('delta = 1/1024')
		print('skoS2 = 181/128')
		print('skoSM = 31/32')
		print('skoSP = 1055/1024')
		print('skoX = 287953299221512191/4611686018427387904')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_33(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_33 SAT")
		print('delta = 1/1024')
		print('skoS2 = 181/128')
		print('skoSM = 31/32')
		print('skoSP = 1055/1024')
		print('skoX = 287953299221512191/4611686018427387904')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_34(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_34 SAT")
		print('delta = 1/1024')
		print('skoS2 = 181/128')
		print('skoSM = 31/32')
		print('skoSP = 1055/1024')
		print('skoX = 287953299221512191/4611686018427387904')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_35(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_35 SAT")
		print('delta = 1/1024')
		print('skoS2 = 181/128')
		print('skoSM = 31/32')
		print('skoSP = 1055/1024')
		print('skoX = 287953299221512191/4611686018427387904')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_36(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_36 SAT")
		print('delta = 1/1024')
		print('skoS2 = 181/128')
		print('skoSM = 31/32')
		print('skoSP = 1055/1024')
		print('skoX = 287953299221512191/4611686018427387904')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_37(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_37 SAT")
		print('delta = 1/1024')
		print('skoS2 = 181/128')
		print('skoSM = 31/32')
		print('skoSP = 1055/1024')
		print('skoX = 287953299221512191/4611686018427387904')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_38(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_38 SAT")
		print('delta = 1/1024')
		print('skoS2 = 181/128')
		print('skoSM = 31/32')
		print('skoSP = 1055/1024')
		print('skoX = 287953299221512191/4611686018427387904')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_39(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_39 SAT")
		print('delta = 1/1024')
		print('skoS2 = 181/128')
		print('skoSM = 31/32')
		print('skoSP = 1055/1024')
		print('skoX = 287953299221512191/4611686018427387904')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_40(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_40 SAT")
		print('delta = 1/1024')
		print('skoS2 = 181/128')
		print('skoSM = 31/32')
		print('skoSP = 1055/1024')
		print('skoX = 287953299221512191/4611686018427387904')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_41(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_41 SAT")
		print('delta = 1/1024')
		print('skoS2 = 181/128')
		print('skoSM = 31/32')
		print('skoSP = 1055/1024')
		print('skoX = 287953299221512191/4611686018427387904')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_42(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_42 SAT")
		print('delta = 1/1024')
		print('skoS2 = 181/128')
		print('skoSM = 31/32')
		print('skoSP = 1055/1024')
		print('skoX = 287953299221512191/4611686018427387904')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_43(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_43 SAT")
		print('delta = 1/1024')
		print('skoS2 = 181/128')
		print('skoSM = 31/32')
		print('skoSP = 1055/1024')
		print('skoX = 287953299221512191/4611686018427387904')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_44(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_44 SAT")
		print('delta = 1/1024')
		print('skoS2 = 181/128')
		print('skoSM = 31/32')
		print('skoSP = 1055/1024')
		print('skoX = 287953299221512191/4611686018427387904')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_45(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_45 SAT")
		print('delta = 1/1024')
		print('skoS2 = 181/128')
		print('skoSM = 31/32')
		print('skoSP = 1055/1024')
		print('skoX = 287953299221512191/4611686018427387904')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_46(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_46 SAT")
		print('delta = 1/1024')
		print('skoS2 = 181/128')
		print('skoSM = 31/32')
		print('skoSP = 1055/1024')
		print('skoX = 287953299221512191/4611686018427387904')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_47(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_47 SAT")
		print('delta = 1/1024')
		print('skoS2 = 181/128')
		print('skoSM = 31/32')
		print('skoSP = 1055/1024')
		print('skoX = 287953299221512191/4611686018427387904')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_48(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_48 SAT")
		print('delta = 1/1024')
		print('skoS2 = 181/128')
		print('skoSM = 31/32')
		print('skoSP = 1055/1024')
		print('skoX = 287953299221512191/4611686018427387904')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_49(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_49 SAT")
		print('delta = 1/1024')
		print('skoS2 = 181/128')
		print('skoSM = 31/32')
		print('skoSP = 1055/1024')
		print('skoX = 287953299221512191/4611686018427387904')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_50(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_50 SAT")
		print('delta = 1/1024')
		print('skoS2 = 181/128')
		print('skoSM = 31/32')
		print('skoSP = 1055/1024')
		print('skoX = 287953299221512191/4611686018427387904')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_51(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_51 SAT")
		print('delta = 1/1024')
		print('skoS2 = 181/128')
		print('skoSM = 31/32')
		print('skoSP = 1055/1024')
		print('skoX = 287953299221512191/4611686018427387904')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_52(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_52 SAT")
		print('delta = 1/1024')
		print('skoS2 = 181/128')
		print('skoSM = 31/32')
		print('skoSP = 1055/1024')
		print('skoX = 287953299221512191/4611686018427387904')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_53(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_53 SAT")
		print('delta = 1/1024')
		print('skoS2 = 181/128')
		print('skoSM = 31/32')
		print('skoSP = 1055/1024')
		print('skoX = 287953299221512191/4611686018427387904')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_54(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_54 SAT")
		print('delta = 1/1024')
		print('skoS2 = 181/128')
		print('skoSM = 31/32')
		print('skoSP = 1055/1024')
		print('skoX = 287953299221512191/4611686018427387904')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_55(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_55 SAT")
		print('delta = 1/1024')
		print('skoS2 = 181/128')
		print('skoSM = 31/32')
		print('skoSP = 1055/1024')
		print('skoX = 287953299221512191/4611686018427387904')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_56(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_56 SAT")
		print('delta = 1/1024')
		print('skoS2 = 181/128')
		print('skoSM = 31/32')
		print('skoSP = 1055/1024')
		print('skoX = 287953299221512191/4611686018427387904')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_57(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_57 SAT")
		print('delta = 1/1024')
		print('skoS2 = 181/128')
		print('skoSM = 31/32')
		print('skoSP = 1055/1024')
		print('skoX = 287953299221512191/4611686018427387904')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_58(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_58 SAT")
		print('delta = 1/1024')
		print('skoS2 = 181/128')
		print('skoSM = 31/32')
		print('skoSP = 1055/1024')
		print('skoX = 287953299221512191/4611686018427387904')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_59(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_59 SAT")
		print('delta = 1/1024')
		print('skoS2 = 181/128')
		print('skoSM = 31/32')
		print('skoSP = 1055/1024')
		print('skoX = 287953299221512191/4611686018427387904')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_60(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_60 SAT")
		print('delta = 1/1024')
		print('skoS2 = 181/128')
		print('skoSM = 31/32')
		print('skoSP = 1055/1024')
		print('skoX = 287953299221512191/4611686018427387904')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_61(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_61 SAT")
		print('delta = 1/1024')
		print('skoS2 = 181/128')
		print('skoSM = 31/32')
		print('skoSP = 1055/1024')
		print('skoX = 287953299221512191/4611686018427387904')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_62(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_62 SAT")
		print('delta = 1/1024')
		print('skoS2 = 181/128')
		print('skoSM = 31/32')
		print('skoSP = 1055/1024')
		print('skoX = 287953299221512191/4611686018427387904')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_63(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_63 SAT")
		print('delta = 1/1024')
		print('skoS2 = 181/128')
		print('skoSM = 31/32')
		print('skoSP = 1055/1024')
		print('skoX = 287953299221512191/4611686018427387904')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_64(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_64 SAT")
		print('delta = 1/1024')
		print('skoS2 = 181/128')
		print('skoSM = 31/32')
		print('skoSP = 1055/1024')
		print('skoX = 287953299221512191/4611686018427387904')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_65(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_65 SAT")
		print('delta = 1/1024')
		print('skoS2 = 181/128')
		print('skoSM = 31/32')
		print('skoSP = 1055/1024')
		print('skoX = 287953299221512191/4611686018427387904')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_66(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_66 SAT")
		print('delta = 1/1024')
		print('skoS2 = 181/128')
		print('skoSM = 31/32')
		print('skoSP = 1055/1024')
		print('skoX = 287953299221512191/4611686018427387904')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_67(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_67 SAT")
		print('delta = 1/1024')
		print('skoS2 = 181/128')
		print('skoSM = 31/32')
		print('skoSP = 1055/1024')
		print('skoX = 287953299221512191/4611686018427387904')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_68(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_68 SAT")
		print('delta = 1/1024')
		print('skoS2 = 181/128')
		print('skoSM = 31/32')
		print('skoSP = 1055/1024')
		print('skoX = 287953299221512191/4611686018427387904')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_69(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_69 SAT")
		print('delta = 1/1024')
		print('skoS2 = 181/128')
		print('skoSM = 31/32')
		print('skoSP = 1055/1024')
		print('skoX = 287953299221512191/4611686018427387904')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_70(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_70 SAT")
		print('delta = 1/1024')
		print('skoS2 = 181/128')
		print('skoSM = 31/32')
		print('skoSP = 1055/1024')
		print('skoX = 287953299221512191/4611686018427387904')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_71(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_71 SAT")
		print('delta = 1/1024')
		print('skoS2 = 181/128')
		print('skoSM = 31/32')
		print('skoSP = 1055/1024')
		print('skoX = 287953299221512191/4611686018427387904')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_72(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_72 SAT")
		print('delta = 1/1024')
		print('skoS2 = 181/128')
		print('skoSM = 31/32')
		print('skoSP = 1055/1024')
		print('skoX = 287953299221512191/4611686018427387904')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_73(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_73 SAT")
		print('delta = 1/1024')
		print('skoS2 = 181/128')
		print('skoSM = 31/32')
		print('skoSP = 1055/1024')
		print('skoX = 287953299221512191/4611686018427387904')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_74(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_74 SAT")
		print('delta = 1/1024')
		print('skoS2 = 181/128')
		print('skoSM = 31/32')
		print('skoSP = 1055/1024')
		print('skoX = 287953299221512191/4611686018427387904')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_75(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_75 SAT")
		print('delta = 1/1024')
		print('skoS2 = 181/128')
		print('skoSM = 31/32')
		print('skoSP = 1055/1024')
		print('skoX = 287953299221512191/4611686018427387904')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_76(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_76 SAT")
		print('delta = 1/1024')
		print('skoS2 = 181/128')
		print('skoSM = 31/32')
		print('skoSP = 1055/1024')
		print('skoX = 287953299221512191/4611686018427387904')
		print('pi = 26353589/8388608')
		exit(0)


	print("UNKNOWN")
	exit(0)
