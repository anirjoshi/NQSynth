import sympy
from sympy import *

def pre_condition_0(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoX*(8*skoSM + 33)/8 < 0) & (pi*skoS2/8 + pi/16 + 1/160 > skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Mul(Rational(1, 8), Symbol('skoX'), Add(Mul(Integer(8), Symbol('skoSM')), Integer(33))), Integer(0)), StrictGreaterThan(Add(Mul(Rational(1, 8), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 16), Symbol('pi')), Rational(1, 160)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (pi*skoS2/8 + pi/16 + 1/160 > -6*pi*skoS2 - 3*pi + 1/10)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(1, 8), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 16), Symbol('pi')), Rational(1, 160)), Add(Mul(Integer(-1), Integer(6), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Integer(3), Symbol('pi')), Rational(1, 10))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoX*(2 - skoSM) > 0) & (6*pi*skoS2 + 3*pi + 3/10 < -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Mul(Symbol('skoX'), Add(Integer(2), Mul(Integer(-1), Symbol('skoSM')))), Integer(0)), StrictLessThan(Add(Mul(Integer(6), Symbol('pi'), Symbol('skoS2')), Mul(Integer(3), Symbol('pi')), Rational(3, 10)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (pi*skoS2/16 + pi/32 - 13/64 < -6*pi*skoS2 - 3*pi - 3/10)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Rational(1, 16), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 32), Symbol('pi')), Rational(-13, 64)), Add(Mul(Integer(-1), Integer(6), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Integer(3), Symbol('pi')), Rational(-3, 10))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_4(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoX*(1 - skoSM) > 0) & (5*pi*skoS2 + 5*pi/2 + 1/4 < -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Mul(Symbol('skoX'), Add(Integer(1), Mul(Integer(-1), Symbol('skoSM')))), Integer(0)), StrictLessThan(Add(Mul(Integer(5), Symbol('pi'), Symbol('skoS2')), Mul(Rational(5, 2), Symbol('pi')), Rational(1, 4)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_5(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (pi*skoS2/2 + pi/4 - 9/40 < -5*pi*skoS2 - 5*pi/2 - 1/4)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Rational(1, 2), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 4), Symbol('pi')), Rational(-9, 40)), Add(Mul(Integer(-1), Integer(5), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(5, 2), Symbol('pi')), Rational(-1, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_6(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoX*(5 - 4*skoSM)/4 > 0) & (21*pi*skoS2/4 + 21*pi/8 + 21/80 < -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Mul(Rational(1, 4), Symbol('skoX'), Add(Integer(5), Mul(Integer(-1), Integer(4), Symbol('skoSM')))), Integer(0)), StrictLessThan(Add(Mul(Rational(21, 4), Symbol('pi'), Symbol('skoS2')), Mul(Rational(21, 8), Symbol('pi')), Rational(21, 80)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_7(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (pi*skoS2 + pi/2 - 1/4 < -21*pi*skoS2/4 - 21*pi/8 - 21/80)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 2), Symbol('pi')), Rational(-1, 4)), Add(Mul(Integer(-1), Rational(21, 4), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(21, 8), Symbol('pi')), Rational(-21, 80))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_8(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoX*(13 - 8*skoSM)/8 > 0) & (45*pi*skoS2/8 + 45*pi/16 + 9/32 < -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Mul(Rational(1, 8), Symbol('skoX'), Add(Integer(13), Mul(Integer(-1), Integer(8), Symbol('skoSM')))), Integer(0)), StrictLessThan(Add(Mul(Rational(45, 8), Symbol('pi'), Symbol('skoS2')), Mul(Rational(45, 16), Symbol('pi')), Rational(9, 32)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_9(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (3*pi*skoS2/2 + 3*pi/4 - 11/40 < -45*pi*skoS2/8 - 45*pi/16 - 9/32)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Rational(3, 2), Symbol('pi'), Symbol('skoS2')), Mul(Rational(3, 4), Symbol('pi')), Rational(-11, 40)), Add(Mul(Integer(-1), Rational(45, 8), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(45, 16), Symbol('pi')), Rational(-9, 32))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_10(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoX*(29 - 16*skoSM)/16 > 0) & (93*pi*skoS2/16 + 93*pi/32 + 93/320 < -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Mul(Rational(1, 16), Symbol('skoX'), Add(Integer(29), Mul(Integer(-1), Integer(16), Symbol('skoSM')))), Integer(0)), StrictLessThan(Add(Mul(Rational(93, 16), Symbol('pi'), Symbol('skoS2')), Mul(Rational(93, 32), Symbol('pi')), Rational(93, 320)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_11(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (7*pi*skoS2/4 + 7*pi/8 - 23/80 < -93*pi*skoS2/16 - 93*pi/32 - 93/320)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Rational(7, 4), Symbol('pi'), Symbol('skoS2')), Mul(Rational(7, 8), Symbol('pi')), Rational(-23, 80)), Add(Mul(Integer(-1), Rational(93, 16), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(93, 32), Symbol('pi')), Rational(-93, 320))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_12(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoX*(3841 - 2048*skoSM)/2048 > 0) & (12033*pi*skoS2/2048 + 12033*pi/4096 + 12033/40960 < -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Mul(Rational(1, 2048), Symbol('skoX'), Add(Integer(3841), Mul(Integer(-1), Integer(2048), Symbol('skoSM')))), Integer(0)), StrictLessThan(Add(Mul(Rational(12033, 2048), Symbol('pi'), Symbol('skoS2')), Mul(Rational(12033, 4096), Symbol('pi')), Rational(12033, 40960)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_13(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (15*pi*skoS2/8 + 15*pi/16 - 47/160 < -12033*pi*skoS2/2048 - 12033*pi/4096 - 12033/40960)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Rational(15, 8), Symbol('pi'), Symbol('skoS2')), Mul(Rational(15, 16), Symbol('pi')), Rational(-47, 160)), Add(Mul(Integer(-1), Rational(12033, 2048), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(12033, 4096), Symbol('pi')), Rational(-12033, 40960))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_14(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoX*(31745 - 16384*skoSM)/16384 > 0) & (97281*pi*skoS2/16384 + 97281*pi/32768 + 97281/327680 < -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Mul(Rational(1, 16384), Symbol('skoX'), Add(Integer(31745), Mul(Integer(-1), Integer(16384), Symbol('skoSM')))), Integer(0)), StrictLessThan(Add(Mul(Rational(97281, 16384), Symbol('pi'), Symbol('skoS2')), Mul(Rational(97281, 32768), Symbol('pi')), Rational(97281, 327680)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_15(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (31*pi*skoS2/16 + 31*pi/32 - 19/64 < -97281*pi*skoS2/16384 - 97281*pi/32768 - 97281/327680)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Rational(31, 16), Symbol('pi'), Symbol('skoS2')), Mul(Rational(31, 32), Symbol('pi')), Rational(-19, 64)), Add(Mul(Integer(-1), Rational(97281, 16384), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(97281, 32768), Symbol('pi')), Rational(-97281, 327680))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_16(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoX*(129025 - 65536*skoSM)/65536 > 0) & (391169*pi*skoS2/65536 + 391169*pi/131072 + 391169/1310720 < -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Mul(Rational(1, 65536), Symbol('skoX'), Add(Integer(129025), Mul(Integer(-1), Integer(65536), Symbol('skoSM')))), Integer(0)), StrictLessThan(Add(Mul(Rational(391169, 65536), Symbol('pi'), Symbol('skoS2')), Mul(Rational(391169, 131072), Symbol('pi')), Rational(391169, 1310720)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_17(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (63*pi*skoS2/32 + 63*pi/64 - 191/640 < -391169*pi*skoS2/65536 - 391169*pi/131072 - 391169/1310720)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Rational(63, 32), Symbol('pi'), Symbol('skoS2')), Mul(Rational(63, 64), Symbol('pi')), Rational(-191, 640)), Add(Mul(Integer(-1), Rational(391169, 65536), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(391169, 131072), Symbol('pi')), Rational(-391169, 1310720))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_18(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoX*(260097 - 131072*skoSM)/131072 > 0) & (784385*pi*skoS2/131072 + 784385*pi/262144 + 156877/524288 < -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Mul(Rational(1, 131072), Symbol('skoX'), Add(Integer(260097), Mul(Integer(-1), Integer(131072), Symbol('skoSM')))), Integer(0)), StrictLessThan(Add(Mul(Rational(784385, 131072), Symbol('pi'), Symbol('skoS2')), Mul(Rational(784385, 262144), Symbol('pi')), Rational(156877, 524288)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_19(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (127*pi*skoS2/64 + 127*pi/128 - 383/1280 < -784385*pi*skoS2/131072 - 784385*pi/262144 - 156877/524288)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Rational(127, 64), Symbol('pi'), Symbol('skoS2')), Mul(Rational(127, 128), Symbol('pi')), Rational(-383, 1280)), Add(Mul(Integer(-1), Rational(784385, 131072), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(784385, 262144), Symbol('pi')), Rational(-156877, 524288))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_20(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoX*(522241 - 262144*skoSM)/262144 > 0) & (1570817*pi*skoS2/262144 + 1570817*pi/524288 + 1570817/5242880 < -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Mul(Rational(1, 262144), Symbol('skoX'), Add(Integer(522241), Mul(Integer(-1), Integer(262144), Symbol('skoSM')))), Integer(0)), StrictLessThan(Add(Mul(Rational(1570817, 262144), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1570817, 524288), Symbol('pi')), Rational(1570817, 5242880)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_21(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (255*pi*skoS2/128 + 255*pi/256 - 767/2560 < -1570817*pi*skoS2/262144 - 1570817*pi/524288 - 1570817/5242880)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Rational(255, 128), Symbol('pi'), Symbol('skoS2')), Mul(Rational(255, 256), Symbol('pi')), Rational(-767, 2560)), Add(Mul(Integer(-1), Rational(1570817, 262144), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(1570817, 524288), Symbol('pi')), Rational(-1570817, 5242880))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_22(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoX*(1046529 - 524288*skoSM)/524288 > 0) & (3143681*pi*skoS2/524288 + 3143681*pi/1048576 + 3143681/10485760 < -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Mul(Rational(1, 524288), Symbol('skoX'), Add(Integer(1046529), Mul(Integer(-1), Integer(524288), Symbol('skoSM')))), Integer(0)), StrictLessThan(Add(Mul(Rational(3143681, 524288), Symbol('pi'), Symbol('skoS2')), Mul(Rational(3143681, 1048576), Symbol('pi')), Rational(3143681, 10485760)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_23(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (511*pi*skoS2/256 + 511*pi/512 - 307/1024 < -3143681*pi*skoS2/524288 - 3143681*pi/1048576 - 3143681/10485760)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Rational(511, 256), Symbol('pi'), Symbol('skoS2')), Mul(Rational(511, 512), Symbol('pi')), Rational(-307, 1024)), Add(Mul(Integer(-1), Rational(3143681, 524288), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(3143681, 1048576), Symbol('pi')), Rational(-3143681, 10485760))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_24(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoX*(2095105 - 1048576*skoSM)/1048576 > 0) & (6289409*pi*skoS2/1048576 + 6289409*pi/2097152 + 6289409/20971520 < -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Mul(Rational(1, 1048576), Symbol('skoX'), Add(Integer(2095105), Mul(Integer(-1), Integer(1048576), Symbol('skoSM')))), Integer(0)), StrictLessThan(Add(Mul(Rational(6289409, 1048576), Symbol('pi'), Symbol('skoS2')), Mul(Rational(6289409, 2097152), Symbol('pi')), Rational(6289409, 20971520)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_25(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (1023*pi*skoS2/512 + 1023*pi/1024 - 3071/10240 < -6289409*pi*skoS2/1048576 - 6289409*pi/2097152 - 6289409/20971520)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Rational(1023, 512), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1023, 1024), Symbol('pi')), Rational(-3071, 10240)), Add(Mul(Integer(-1), Rational(6289409, 1048576), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(6289409, 2097152), Symbol('pi')), Rational(-6289409, 20971520))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_26(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoX*(4192257 - 2097152*skoSM)/2097152 > 0) & (12580865*pi*skoS2/2097152 + 12580865*pi/4194304 + 2516173/8388608 < -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Mul(Rational(1, 2097152), Symbol('skoX'), Add(Integer(4192257), Mul(Integer(-1), Integer(2097152), Symbol('skoSM')))), Integer(0)), StrictLessThan(Add(Mul(Rational(12580865, 2097152), Symbol('pi'), Symbol('skoS2')), Mul(Rational(12580865, 4194304), Symbol('pi')), Rational(2516173, 8388608)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_27(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (2047*pi*skoS2/1024 + 2047*pi/2048 - 6143/20480 < -12580865*pi*skoS2/2097152 - 12580865*pi/4194304 - 2516173/8388608)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Rational(2047, 1024), Symbol('pi'), Symbol('skoS2')), Mul(Rational(2047, 2048), Symbol('pi')), Rational(-6143, 20480)), Add(Mul(Integer(-1), Rational(12580865, 2097152), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(12580865, 4194304), Symbol('pi')), Rational(-2516173, 8388608))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_28(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoX*(8386561 - 4194304*skoSM)/4194304 > 0) & (25163777*pi*skoS2/4194304 + 25163777*pi/8388608 + 25163777/83886080 < -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Mul(Rational(1, 4194304), Symbol('skoX'), Add(Integer(8386561), Mul(Integer(-1), Integer(4194304), Symbol('skoSM')))), Integer(0)), StrictLessThan(Add(Mul(Rational(25163777, 4194304), Symbol('pi'), Symbol('skoS2')), Mul(Rational(25163777, 8388608), Symbol('pi')), Rational(25163777, 83886080)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_29(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (4095*pi*skoS2/2048 + 4095*pi/4096 - 12287/40960 < -25163777*pi*skoS2/4194304 - 25163777*pi/8388608 - 25163777/83886080)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Rational(4095, 2048), Symbol('pi'), Symbol('skoS2')), Mul(Rational(4095, 4096), Symbol('pi')), Rational(-12287, 40960)), Add(Mul(Integer(-1), Rational(25163777, 4194304), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(25163777, 8388608), Symbol('pi')), Rational(-25163777, 83886080))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_30(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoX*(16775169 - 8388608*skoSM)/8388608 > 0) & (50329601*pi*skoS2/8388608 + 50329601*pi/16777216 + 50329601/167772160 < -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Mul(Rational(1, 8388608), Symbol('skoX'), Add(Integer(16775169), Mul(Integer(-1), Integer(8388608), Symbol('skoSM')))), Integer(0)), StrictLessThan(Add(Mul(Rational(50329601, 8388608), Symbol('pi'), Symbol('skoS2')), Mul(Rational(50329601, 16777216), Symbol('pi')), Rational(50329601, 167772160)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_31(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (8191*pi*skoS2/4096 + 8191*pi/8192 - 4915/16384 < -50329601*pi*skoS2/8388608 - 50329601*pi/16777216 - 50329601/167772160)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Rational(8191, 4096), Symbol('pi'), Symbol('skoS2')), Mul(Rational(8191, 8192), Symbol('pi')), Rational(-4915, 16384)), Add(Mul(Integer(-1), Rational(50329601, 8388608), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(50329601, 16777216), Symbol('pi')), Rational(-50329601, 167772160))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_32(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoX*(33552385 - 16777216*skoSM)/16777216 > 0) & (100661249*pi*skoS2/16777216 + 100661249*pi/33554432 + 100661249/335544320 < -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Mul(Rational(1, 16777216), Symbol('skoX'), Add(Integer(33552385), Mul(Integer(-1), Integer(16777216), Symbol('skoSM')))), Integer(0)), StrictLessThan(Add(Mul(Rational(100661249, 16777216), Symbol('pi'), Symbol('skoS2')), Mul(Rational(100661249, 33554432), Symbol('pi')), Rational(100661249, 335544320)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_33(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (16383*pi*skoS2/8192 + 16383*pi/16384 - 49151/163840 < -100661249*pi*skoS2/16777216 - 100661249*pi/33554432 - 100661249/335544320)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Rational(16383, 8192), Symbol('pi'), Symbol('skoS2')), Mul(Rational(16383, 16384), Symbol('pi')), Rational(-49151, 163840)), Add(Mul(Integer(-1), Rational(100661249, 16777216), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(100661249, 33554432), Symbol('pi')), Rational(-100661249, 335544320))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_34(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoX*(67106817 - 33554432*skoSM)/33554432 > 0) & (201324545*pi*skoS2/33554432 + 201324545*pi/67108864 + 40264909/134217728 < -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Mul(Rational(1, 33554432), Symbol('skoX'), Add(Integer(67106817), Mul(Integer(-1), Integer(33554432), Symbol('skoSM')))), Integer(0)), StrictLessThan(Add(Mul(Rational(201324545, 33554432), Symbol('pi'), Symbol('skoS2')), Mul(Rational(201324545, 67108864), Symbol('pi')), Rational(40264909, 134217728)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_35(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (32767*pi*skoS2/16384 + 32767*pi/32768 - 98303/327680 < -201324545*pi*skoS2/33554432 - 201324545*pi/67108864 - 40264909/134217728)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Rational(32767, 16384), Symbol('pi'), Symbol('skoS2')), Mul(Rational(32767, 32768), Symbol('pi')), Rational(-98303, 327680)), Add(Mul(Integer(-1), Rational(201324545, 33554432), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(201324545, 67108864), Symbol('pi')), Rational(-40264909, 134217728))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_36(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoX*(134215681 - 67108864*skoSM)/67108864 > 0) & (402651137*pi*skoS2/67108864 + 402651137*pi/134217728 + 402651137/1342177280 < -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Mul(Rational(1, 67108864), Symbol('skoX'), Add(Integer(134215681), Mul(Integer(-1), Integer(67108864), Symbol('skoSM')))), Integer(0)), StrictLessThan(Add(Mul(Rational(402651137, 67108864), Symbol('pi'), Symbol('skoS2')), Mul(Rational(402651137, 134217728), Symbol('pi')), Rational(402651137, 1342177280)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_37(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (65535*pi*skoS2/32768 + 65535*pi/65536 - 196607/655360 < -402651137*pi*skoS2/67108864 - 402651137*pi/134217728 - 402651137/1342177280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Rational(65535, 32768), Symbol('pi'), Symbol('skoS2')), Mul(Rational(65535, 65536), Symbol('pi')), Rational(-196607, 655360)), Add(Mul(Integer(-1), Rational(402651137, 67108864), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(402651137, 134217728), Symbol('pi')), Rational(-402651137, 1342177280))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_38(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoX*(268433409 - 134217728*skoSM)/134217728 > 0) & (805304321*pi*skoS2/134217728 + 805304321*pi/268435456 + 805304321/2684354560 < -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Mul(Rational(1, 134217728), Symbol('skoX'), Add(Integer(268433409), Mul(Integer(-1), Integer(134217728), Symbol('skoSM')))), Integer(0)), StrictLessThan(Add(Mul(Rational(805304321, 134217728), Symbol('pi'), Symbol('skoS2')), Mul(Rational(805304321, 268435456), Symbol('pi')), Rational(805304321, 2684354560)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_39(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (131071*pi*skoS2/65536 + 131071*pi/131072 - 78643/262144 < -805304321*pi*skoS2/134217728 - 805304321*pi/268435456 - 805304321/2684354560)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Rational(131071, 65536), Symbol('pi'), Symbol('skoS2')), Mul(Rational(131071, 131072), Symbol('pi')), Rational(-78643, 262144)), Add(Mul(Integer(-1), Rational(805304321, 134217728), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(805304321, 268435456), Symbol('pi')), Rational(-805304321, 2684354560))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_40(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoX*(536868865 - 268435456*skoSM)/268435456 > 0) & (1610610689*pi*skoS2/268435456 + 1610610689*pi/536870912 + 1610610689/5368709120 < -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Mul(Rational(1, 268435456), Symbol('skoX'), Add(Integer(536868865), Mul(Integer(-1), Integer(268435456), Symbol('skoSM')))), Integer(0)), StrictLessThan(Add(Mul(Rational(1610610689, 268435456), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1610610689, 536870912), Symbol('pi')), Rational(1610610689, 5368709120)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_41(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (262143*pi*skoS2/131072 + 262143*pi/262144 - 786431/2621440 < -1610610689*pi*skoS2/268435456 - 1610610689*pi/536870912 - 1610610689/5368709120)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Rational(262143, 131072), Symbol('pi'), Symbol('skoS2')), Mul(Rational(262143, 262144), Symbol('pi')), Rational(-786431, 2621440)), Add(Mul(Integer(-1), Rational(1610610689, 268435456), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(1610610689, 536870912), Symbol('pi')), Rational(-1610610689, 5368709120))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_42(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoX*(1073739777 - 536870912*skoSM)/536870912 > 0) & (3221223425*pi*skoS2/536870912 + 3221223425*pi/1073741824 + 644244685/2147483648 < -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Mul(Rational(1, 536870912), Symbol('skoX'), Add(Integer(1073739777), Mul(Integer(-1), Integer(536870912), Symbol('skoSM')))), Integer(0)), StrictLessThan(Add(Mul(Rational(3221223425, 536870912), Symbol('pi'), Symbol('skoS2')), Mul(Rational(3221223425, 1073741824), Symbol('pi')), Rational(644244685, 2147483648)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_43(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (524287*pi*skoS2/262144 + 524287*pi/524288 - 1572863/5242880 < -3221223425*pi*skoS2/536870912 - 3221223425*pi/1073741824 - 644244685/2147483648)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Rational(524287, 262144), Symbol('pi'), Symbol('skoS2')), Mul(Rational(524287, 524288), Symbol('pi')), Rational(-1572863, 5242880)), Add(Mul(Integer(-1), Rational(3221223425, 536870912), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(3221223425, 1073741824), Symbol('pi')), Rational(-644244685, 2147483648))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_44(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoX*(2147481601 - 1073741824*skoSM)/1073741824 > 0) & (6442448897*pi*skoS2/1073741824 + 6442448897*pi/2147483648 + 6442448897/21474836480 < -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Mul(Rational(1, 1073741824), Symbol('skoX'), Add(Integer(2147481601), Mul(Integer(-1), Integer(1073741824), Symbol('skoSM')))), Integer(0)), StrictLessThan(Add(Mul(Rational(6442448897, 1073741824), Symbol('pi'), Symbol('skoS2')), Mul(Rational(6442448897, 2147483648), Symbol('pi')), Rational(6442448897, 21474836480)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_45(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (1048575*pi*skoS2/524288 + 1048575*pi/1048576 - 3145727/10485760 < -6442448897*pi*skoS2/1073741824 - 6442448897*pi/2147483648 - 6442448897/21474836480)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Rational(1048575, 524288), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1048575, 1048576), Symbol('pi')), Rational(-3145727, 10485760)), Add(Mul(Integer(-1), Rational(6442448897, 1073741824), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(6442448897, 2147483648), Symbol('pi')), Rational(-6442448897, 21474836480))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_46(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoX*(4294965249 - 2147483648*skoSM)/2147483648 > 0) & (12884899841*pi*skoS2/2147483648 + 12884899841*pi/4294967296 + 12884899841/42949672960 < -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Mul(Rational(1, 2147483648), Symbol('skoX'), Add(Integer(4294965249), Mul(Integer(-1), Integer(2147483648), Symbol('skoSM')))), Integer(0)), StrictLessThan(Add(Mul(Rational(12884899841, 2147483648), Symbol('pi'), Symbol('skoS2')), Mul(Rational(12884899841, 4294967296), Symbol('pi')), Rational(12884899841, 42949672960)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_47(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (2097151*pi*skoS2/1048576 + 2097151*pi/2097152 - 1258291/4194304 < -12884899841*pi*skoS2/2147483648 - 12884899841*pi/4294967296 - 12884899841/42949672960)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Rational(2097151, 1048576), Symbol('pi'), Symbol('skoS2')), Mul(Rational(2097151, 2097152), Symbol('pi')), Rational(-1258291, 4194304)), Add(Mul(Integer(-1), Rational(12884899841, 2147483648), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(12884899841, 4294967296), Symbol('pi')), Rational(-12884899841, 42949672960))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_48(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoX*(8589932545 - 4294967296*skoSM)/4294967296 > 0) & (25769801729*pi*skoS2/4294967296 + 25769801729*pi/8589934592 + 25769801729/85899345920 < -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Mul(Rational(1, 4294967296), Symbol('skoX'), Add(Integer(8589932545), Mul(Integer(-1), Integer(4294967296), Symbol('skoSM')))), Integer(0)), StrictLessThan(Add(Mul(Rational(25769801729, 4294967296), Symbol('pi'), Symbol('skoS2')), Mul(Rational(25769801729, 8589934592), Symbol('pi')), Rational(25769801729, 85899345920)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_49(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (4194303*pi*skoS2/2097152 + 4194303*pi/4194304 - 12582911/41943040 < -25769801729*pi*skoS2/4294967296 - 25769801729*pi/8589934592 - 25769801729/85899345920)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Rational(4194303, 2097152), Symbol('pi'), Symbol('skoS2')), Mul(Rational(4194303, 4194304), Symbol('pi')), Rational(-12582911, 41943040)), Add(Mul(Integer(-1), Rational(25769801729, 4294967296), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(25769801729, 8589934592), Symbol('pi')), Rational(-25769801729, 85899345920))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_50(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoX*(17179867137 - 8589934592*skoSM)/8589934592 > 0) & (51539605505*pi*skoS2/8589934592 + 51539605505*pi/17179869184 + 10307921101/34359738368 < -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Mul(Rational(1, 8589934592), Symbol('skoX'), Add(Integer(17179867137), Mul(Integer(-1), Integer(8589934592), Symbol('skoSM')))), Integer(0)), StrictLessThan(Add(Mul(Rational(51539605505, 8589934592), Symbol('pi'), Symbol('skoS2')), Mul(Rational(51539605505, 17179869184), Symbol('pi')), Rational(10307921101, 34359738368)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_51(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (8388607*pi*skoS2/4194304 + 8388607*pi/8388608 - 25165823/83886080 < -51539605505*pi*skoS2/8589934592 - 51539605505*pi/17179869184 - 10307921101/34359738368)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Rational(8388607, 4194304), Symbol('pi'), Symbol('skoS2')), Mul(Rational(8388607, 8388608), Symbol('pi')), Rational(-25165823, 83886080)), Add(Mul(Integer(-1), Rational(51539605505, 8589934592), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(51539605505, 17179869184), Symbol('pi')), Rational(-10307921101, 34359738368))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_52(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoX*(34359736321 - 17179869184*skoSM)/17179869184 > 0) & (103079213057*pi*skoS2/17179869184 + 103079213057*pi/34359738368 + 103079213057/343597383680 < -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Mul(Rational(1, 17179869184), Symbol('skoX'), Add(Integer(34359736321), Mul(Integer(-1), Integer(17179869184), Symbol('skoSM')))), Integer(0)), StrictLessThan(Add(Mul(Rational(103079213057, 17179869184), Symbol('pi'), Symbol('skoS2')), Mul(Rational(103079213057, 34359738368), Symbol('pi')), Rational(103079213057, 343597383680)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_53(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (16777215*pi*skoS2/8388608 + 16777215*pi/16777216 - 50331647/167772160 < -103079213057*pi*skoS2/17179869184 - 103079213057*pi/34359738368 - 103079213057/343597383680)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Rational(16777215, 8388608), Symbol('pi'), Symbol('skoS2')), Mul(Rational(16777215, 16777216), Symbol('pi')), Rational(-50331647, 167772160)), Add(Mul(Integer(-1), Rational(103079213057, 17179869184), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(103079213057, 34359738368), Symbol('pi')), Rational(-103079213057, 343597383680))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_54(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoX*(68719474689 - 34359738368*skoSM)/34359738368 > 0) & (206158428161*pi*skoS2/34359738368 + 206158428161*pi/68719476736 + 206158428161/687194767360 < -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Mul(Rational(1, 34359738368), Symbol('skoX'), Add(Integer(68719474689), Mul(Integer(-1), Integer(34359738368), Symbol('skoSM')))), Integer(0)), StrictLessThan(Add(Mul(Rational(206158428161, 34359738368), Symbol('pi'), Symbol('skoS2')), Mul(Rational(206158428161, 68719476736), Symbol('pi')), Rational(206158428161, 687194767360)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_55(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (33554431*pi*skoS2/16777216 + 33554431*pi/33554432 - 20132659/67108864 < -206158428161*pi*skoS2/34359738368 - 206158428161*pi/68719476736 - 206158428161/687194767360)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Rational(33554431, 16777216), Symbol('pi'), Symbol('skoS2')), Mul(Rational(33554431, 33554432), Symbol('pi')), Rational(-20132659, 67108864)), Add(Mul(Integer(-1), Rational(206158428161, 34359738368), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(206158428161, 68719476736), Symbol('pi')), Rational(-206158428161, 687194767360))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_56(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoX*(137438951425 - 68719476736*skoSM)/68719476736 > 0) & (412316858369*pi*skoS2/68719476736 + 412316858369*pi/137438953472 + 412316858369/1374389534720 < -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Mul(Rational(1, 68719476736), Symbol('skoX'), Add(Integer(137438951425), Mul(Integer(-1), Integer(68719476736), Symbol('skoSM')))), Integer(0)), StrictLessThan(Add(Mul(Rational(412316858369, 68719476736), Symbol('pi'), Symbol('skoS2')), Mul(Rational(412316858369, 137438953472), Symbol('pi')), Rational(412316858369, 1374389534720)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_57(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (67108863*pi*skoS2/33554432 + 67108863*pi/67108864 - 201326591/671088640 < -412316858369*pi*skoS2/68719476736 - 412316858369*pi/137438953472 - 412316858369/1374389534720)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Rational(67108863, 33554432), Symbol('pi'), Symbol('skoS2')), Mul(Rational(67108863, 67108864), Symbol('pi')), Rational(-201326591, 671088640)), Add(Mul(Integer(-1), Rational(412316858369, 68719476736), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(412316858369, 137438953472), Symbol('pi')), Rational(-412316858369, 1374389534720))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_58(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoX*(274877904897 - 137438953472*skoSM)/137438953472 > 0) & (824633718785*pi*skoS2/137438953472 + 824633718785*pi/274877906944 + 164926743757/549755813888 < -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Mul(Rational(1, 137438953472), Symbol('skoX'), Add(Integer(274877904897), Mul(Integer(-1), Integer(137438953472), Symbol('skoSM')))), Integer(0)), StrictLessThan(Add(Mul(Rational(824633718785, 137438953472), Symbol('pi'), Symbol('skoS2')), Mul(Rational(824633718785, 274877906944), Symbol('pi')), Rational(164926743757, 549755813888)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_59(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (134217727*pi*skoS2/67108864 + 134217727*pi/134217728 - 402653183/1342177280 < -824633718785*pi*skoS2/137438953472 - 824633718785*pi/274877906944 - 164926743757/549755813888)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Rational(134217727, 67108864), Symbol('pi'), Symbol('skoS2')), Mul(Rational(134217727, 134217728), Symbol('pi')), Rational(-402653183, 1342177280)), Add(Mul(Integer(-1), Rational(824633718785, 137438953472), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(824633718785, 274877906944), Symbol('pi')), Rational(-164926743757, 549755813888))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_60(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoX*(549755811841 - 274877906944*skoSM)/274877906944 > 0) & (1649267439617*pi*skoS2/274877906944 + 1649267439617*pi/549755813888 + 1649267439617/5497558138880 < -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Mul(Rational(1, 274877906944), Symbol('skoX'), Add(Integer(549755811841), Mul(Integer(-1), Integer(274877906944), Symbol('skoSM')))), Integer(0)), StrictLessThan(Add(Mul(Rational(1649267439617, 274877906944), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1649267439617, 549755813888), Symbol('pi')), Rational(1649267439617, 5497558138880)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_61(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (268435455*pi*skoS2/134217728 + 268435455*pi/268435456 - 805306367/2684354560 < -1649267439617*pi*skoS2/274877906944 - 1649267439617*pi/549755813888 - 1649267439617/5497558138880)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Rational(268435455, 134217728), Symbol('pi'), Symbol('skoS2')), Mul(Rational(268435455, 268435456), Symbol('pi')), Rational(-805306367, 2684354560)), Add(Mul(Integer(-1), Rational(1649267439617, 274877906944), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(1649267439617, 549755813888), Symbol('pi')), Rational(-1649267439617, 5497558138880))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_62(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoX*(1099511625729 - 549755813888*skoSM)/549755813888 > 0) & (3298534881281*pi*skoS2/549755813888 + 3298534881281*pi/1099511627776 + 3298534881281/10995116277760 < -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Mul(Rational(1, 549755813888), Symbol('skoX'), Add(Integer(1099511625729), Mul(Integer(-1), Integer(549755813888), Symbol('skoSM')))), Integer(0)), StrictLessThan(Add(Mul(Rational(3298534881281, 549755813888), Symbol('pi'), Symbol('skoS2')), Mul(Rational(3298534881281, 1099511627776), Symbol('pi')), Rational(3298534881281, 10995116277760)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_63(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (536870911*pi*skoS2/268435456 + 536870911*pi/536870912 - 322122547/1073741824 < -3298534881281*pi*skoS2/549755813888 - 3298534881281*pi/1099511627776 - 3298534881281/10995116277760)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Rational(536870911, 268435456), Symbol('pi'), Symbol('skoS2')), Mul(Rational(536870911, 536870912), Symbol('pi')), Rational(-322122547, 1073741824)), Add(Mul(Integer(-1), Rational(3298534881281, 549755813888), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(3298534881281, 1099511627776), Symbol('pi')), Rational(-3298534881281, 10995116277760))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_64(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoX*(2199023253505 - 1099511627776*skoSM)/1099511627776 > 0) & (6597069764609*pi*skoS2/1099511627776 + 6597069764609*pi/2199023255552 + 6597069764609/21990232555520 < -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Mul(Rational(1, 1099511627776), Symbol('skoX'), Add(Integer(2199023253505), Mul(Integer(-1), Integer(1099511627776), Symbol('skoSM')))), Integer(0)), StrictLessThan(Add(Mul(Rational(6597069764609, 1099511627776), Symbol('pi'), Symbol('skoS2')), Mul(Rational(6597069764609, 2199023255552), Symbol('pi')), Rational(6597069764609, 21990232555520)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_65(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (1073741823*pi*skoS2/536870912 + 1073741823*pi/1073741824 - 3221225471/10737418240 < -6597069764609*pi*skoS2/1099511627776 - 6597069764609*pi/2199023255552 - 6597069764609/21990232555520)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Rational(1073741823, 536870912), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1073741823, 1073741824), Symbol('pi')), Rational(-3221225471, 10737418240)), Add(Mul(Integer(-1), Rational(6597069764609, 1099511627776), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(6597069764609, 2199023255552), Symbol('pi')), Rational(-6597069764609, 21990232555520))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_66(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoX*(4398046509057 - 2199023255552*skoSM)/2199023255552 > 0) & (13194139531265*pi*skoS2/2199023255552 + 13194139531265*pi/4398046511104 + 2638827906253/8796093022208 < -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Mul(Rational(1, 2199023255552), Symbol('skoX'), Add(Integer(4398046509057), Mul(Integer(-1), Integer(2199023255552), Symbol('skoSM')))), Integer(0)), StrictLessThan(Add(Mul(Rational(13194139531265, 2199023255552), Symbol('pi'), Symbol('skoS2')), Mul(Rational(13194139531265, 4398046511104), Symbol('pi')), Rational(2638827906253, 8796093022208)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_67(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (2147483647*pi*skoS2/1073741824 + 2147483647*pi/2147483648 - 6442450943/21474836480 < -13194139531265*pi*skoS2/2199023255552 - 13194139531265*pi/4398046511104 - 2638827906253/8796093022208)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Rational(2147483647, 1073741824), Symbol('pi'), Symbol('skoS2')), Mul(Rational(2147483647, 2147483648), Symbol('pi')), Rational(-6442450943, 21474836480)), Add(Mul(Integer(-1), Rational(13194139531265, 2199023255552), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(13194139531265, 4398046511104), Symbol('pi')), Rational(-2638827906253, 8796093022208))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_68(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoX*(8796093020161 - 4398046511104*skoSM)/4398046511104 > 0) & (26388279064577*pi*skoS2/4398046511104 + 26388279064577*pi/8796093022208 + 26388279064577/87960930222080 < -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Mul(Rational(1, 4398046511104), Symbol('skoX'), Add(Integer(8796093020161), Mul(Integer(-1), Integer(4398046511104), Symbol('skoSM')))), Integer(0)), StrictLessThan(Add(Mul(Rational(26388279064577, 4398046511104), Symbol('pi'), Symbol('skoS2')), Mul(Rational(26388279064577, 8796093022208), Symbol('pi')), Rational(26388279064577, 87960930222080)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_69(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (4294967295*pi*skoS2/2147483648 + 4294967295*pi/4294967296 - 12884901887/42949672960 < -26388279064577*pi*skoS2/4398046511104 - 26388279064577*pi/8796093022208 - 26388279064577/87960930222080)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Rational(4294967295, 2147483648), Symbol('pi'), Symbol('skoS2')), Mul(Rational(4294967295, 4294967296), Symbol('pi')), Rational(-12884901887, 42949672960)), Add(Mul(Integer(-1), Rational(26388279064577, 4398046511104), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(26388279064577, 8796093022208), Symbol('pi')), Rational(-26388279064577, 87960930222080))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_70(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoX*(17592186042369 - 8796093022208*skoSM)/8796093022208 > 0) & (52776558131201*pi*skoS2/8796093022208 + 52776558131201*pi/17592186044416 + 52776558131201/175921860444160 < -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Mul(Rational(1, 8796093022208), Symbol('skoX'), Add(Integer(17592186042369), Mul(Integer(-1), Integer(8796093022208), Symbol('skoSM')))), Integer(0)), StrictLessThan(Add(Mul(Rational(52776558131201, 8796093022208), Symbol('pi'), Symbol('skoS2')), Mul(Rational(52776558131201, 17592186044416), Symbol('pi')), Rational(52776558131201, 175921860444160)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_71(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (8589934591*pi*skoS2/4294967296 + 8589934591*pi/8589934592 - 5153960755/17179869184 < -52776558131201*pi*skoS2/8796093022208 - 52776558131201*pi/17592186044416 - 52776558131201/175921860444160)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Rational(8589934591, 4294967296), Symbol('pi'), Symbol('skoS2')), Mul(Rational(8589934591, 8589934592), Symbol('pi')), Rational(-5153960755, 17179869184)), Add(Mul(Integer(-1), Rational(52776558131201, 8796093022208), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(52776558131201, 17592186044416), Symbol('pi')), Rational(-52776558131201, 175921860444160))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_72(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoX*(35184372086785 - 17592186044416*skoSM)/17592186044416 > 0) & (105553116264449*pi*skoS2/17592186044416 + 105553116264449*pi/35184372088832 + 105553116264449/351843720888320 < -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Mul(Rational(1, 17592186044416), Symbol('skoX'), Add(Integer(35184372086785), Mul(Integer(-1), Integer(17592186044416), Symbol('skoSM')))), Integer(0)), StrictLessThan(Add(Mul(Rational(105553116264449, 17592186044416), Symbol('pi'), Symbol('skoS2')), Mul(Rational(105553116264449, 35184372088832), Symbol('pi')), Rational(105553116264449, 351843720888320)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_73(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (17179869183*pi*skoS2/8589934592 + 17179869183*pi/17179869184 - 51539607551/171798691840 < -105553116264449*pi*skoS2/17592186044416 - 105553116264449*pi/35184372088832 - 105553116264449/351843720888320)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Rational(17179869183, 8589934592), Symbol('pi'), Symbol('skoS2')), Mul(Rational(17179869183, 17179869184), Symbol('pi')), Rational(-51539607551, 171798691840)), Add(Mul(Integer(-1), Rational(105553116264449, 17592186044416), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(105553116264449, 35184372088832), Symbol('pi')), Rational(-105553116264449, 351843720888320))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_74(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoX*(70368744175617 - 35184372088832*skoSM)/35184372088832 > 0) & (211106232530945*pi*skoS2/35184372088832 + 211106232530945*pi/70368744177664 + 42221246506189/140737488355328 < -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Mul(Rational(1, 35184372088832), Symbol('skoX'), Add(Integer(70368744175617), Mul(Integer(-1), Integer(35184372088832), Symbol('skoSM')))), Integer(0)), StrictLessThan(Add(Mul(Rational(211106232530945, 35184372088832), Symbol('pi'), Symbol('skoS2')), Mul(Rational(211106232530945, 70368744177664), Symbol('pi')), Rational(42221246506189, 140737488355328)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_75(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (34359738367*pi*skoS2/17179869184 + 34359738367*pi/34359738368 - 103079215103/343597383680 < -211106232530945*pi*skoS2/35184372088832 - 211106232530945*pi/70368744177664 - 42221246506189/140737488355328)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Rational(34359738367, 17179869184), Symbol('pi'), Symbol('skoS2')), Mul(Rational(34359738367, 34359738368), Symbol('pi')), Rational(-103079215103, 343597383680)), Add(Mul(Integer(-1), Rational(211106232530945, 35184372088832), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(211106232530945, 70368744177664), Symbol('pi')), Rational(-42221246506189, 140737488355328))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_76(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoX*(140737488353281 - 70368744177664*skoSM)/70368744177664 > 0) & (422212465063937*pi*skoS2/70368744177664 + 422212465063937*pi/140737488355328 + 422212465063937/1407374883553280 < -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Mul(Rational(1, 70368744177664), Symbol('skoX'), Add(Integer(140737488353281), Mul(Integer(-1), Integer(70368744177664), Symbol('skoSM')))), Integer(0)), StrictLessThan(Add(Mul(Rational(422212465063937, 70368744177664), Symbol('pi'), Symbol('skoS2')), Mul(Rational(422212465063937, 140737488355328), Symbol('pi')), Rational(422212465063937, 1407374883553280)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_77(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (68719476735*pi*skoS2/34359738368 + 68719476735*pi/68719476736 - 206158430207/687194767360 < -422212465063937*pi*skoS2/70368744177664 - 422212465063937*pi/140737488355328 - 422212465063937/1407374883553280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Rational(68719476735, 34359738368), Symbol('pi'), Symbol('skoS2')), Mul(Rational(68719476735, 68719476736), Symbol('pi')), Rational(-206158430207, 687194767360)), Add(Mul(Integer(-1), Rational(422212465063937, 70368744177664), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(422212465063937, 140737488355328), Symbol('pi')), Rational(-422212465063937, 1407374883553280))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_78(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoX*(281474976708609 - 140737488355328*skoSM)/140737488355328 > 0) & (844424930129921*pi*skoS2/140737488355328 + 844424930129921*pi/281474976710656 + 844424930129921/2814749767106560 < -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Mul(Rational(1, 140737488355328), Symbol('skoX'), Add(Integer(281474976708609), Mul(Integer(-1), Integer(140737488355328), Symbol('skoSM')))), Integer(0)), StrictLessThan(Add(Mul(Rational(844424930129921, 140737488355328), Symbol('pi'), Symbol('skoS2')), Mul(Rational(844424930129921, 281474976710656), Symbol('pi')), Rational(844424930129921, 2814749767106560)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_79(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (137438953471*pi*skoS2/68719476736 + 137438953471*pi/137438953472 - 82463372083/274877906944 < -844424930129921*pi*skoS2/140737488355328 - 844424930129921*pi/281474976710656 - 844424930129921/2814749767106560)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Rational(137438953471, 68719476736), Symbol('pi'), Symbol('skoS2')), Mul(Rational(137438953471, 137438953472), Symbol('pi')), Rational(-82463372083, 274877906944)), Add(Mul(Integer(-1), Rational(844424930129921, 140737488355328), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(844424930129921, 281474976710656), Symbol('pi')), Rational(-844424930129921, 2814749767106560))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_80(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoX*(281474976709633 - 140737488355328*skoSM)/140737488355328 > 0) & (844424930130945*pi*skoS2/140737488355328 + 844424930130945*pi/281474976710656 + 168884986026189/562949953421312 < -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Mul(Rational(1, 140737488355328), Symbol('skoX'), Add(Integer(281474976709633), Mul(Integer(-1), Integer(140737488355328), Symbol('skoSM')))), Integer(0)), StrictLessThan(Add(Mul(Rational(844424930130945, 140737488355328), Symbol('pi'), Symbol('skoS2')), Mul(Rational(844424930130945, 281474976710656), Symbol('pi')), Rational(168884986026189, 562949953421312)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_81(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (274877906943*pi*skoS2/137438953472 + 274877906943*pi/274877906944 - 824633720831/2748779069440 < -844424930130945*pi*skoS2/140737488355328 - 844424930130945*pi/281474976710656 - 168884986026189/562949953421312)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Rational(274877906943, 137438953472), Symbol('pi'), Symbol('skoS2')), Mul(Rational(274877906943, 274877906944), Symbol('pi')), Rational(-824633720831, 2748779069440)), Add(Mul(Integer(-1), Rational(844424930130945, 140737488355328), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(844424930130945, 281474976710656), Symbol('pi')), Rational(-168884986026189, 562949953421312))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_82(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoX*(281474976710145 - 140737488355328*skoSM)/140737488355328 > 0) & (844424930131457*pi*skoS2/140737488355328 + 844424930131457*pi/281474976710656 + 844424930131457/2814749767106560 < -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Mul(Rational(1, 140737488355328), Symbol('skoX'), Add(Integer(281474976710145), Mul(Integer(-1), Integer(140737488355328), Symbol('skoSM')))), Integer(0)), StrictLessThan(Add(Mul(Rational(844424930131457, 140737488355328), Symbol('pi'), Symbol('skoS2')), Mul(Rational(844424930131457, 281474976710656), Symbol('pi')), Rational(844424930131457, 2814749767106560)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_83(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (549755813887*pi*skoS2/274877906944 + 549755813887*pi/549755813888 - 1649267441663/5497558138880 < -844424930131457*pi*skoS2/140737488355328 - 844424930131457*pi/281474976710656 - 844424930131457/2814749767106560)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Rational(549755813887, 274877906944), Symbol('pi'), Symbol('skoS2')), Mul(Rational(549755813887, 549755813888), Symbol('pi')), Rational(-1649267441663, 5497558138880)), Add(Mul(Integer(-1), Rational(844424930131457, 140737488355328), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(844424930131457, 281474976710656), Symbol('pi')), Rational(-844424930131457, 2814749767106560))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_84(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoX*(281474976710401 - 140737488355328*skoSM)/140737488355328 > 0) & (844424930131713*pi*skoS2/140737488355328 + 844424930131713*pi/281474976710656 + 844424930131713/2814749767106560 < -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Mul(Rational(1, 140737488355328), Symbol('skoX'), Add(Integer(281474976710401), Mul(Integer(-1), Integer(140737488355328), Symbol('skoSM')))), Integer(0)), StrictLessThan(Add(Mul(Rational(844424930131713, 140737488355328), Symbol('pi'), Symbol('skoS2')), Mul(Rational(844424930131713, 281474976710656), Symbol('pi')), Rational(844424930131713, 2814749767106560)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_85(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (1099511627775*pi*skoS2/549755813888 + 1099511627775*pi/1099511627776 - 3298534883327/10995116277760 < -844424930131713*pi*skoS2/140737488355328 - 844424930131713*pi/281474976710656 - 844424930131713/2814749767106560)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Rational(1099511627775, 549755813888), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1099511627775, 1099511627776), Symbol('pi')), Rational(-3298534883327, 10995116277760)), Add(Mul(Integer(-1), Rational(844424930131713, 140737488355328), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(844424930131713, 281474976710656), Symbol('pi')), Rational(-844424930131713, 2814749767106560))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_86(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoX*(562949953421057 - 281474976710656*skoSM)/281474976710656 > 0) & (1688849860263681*pi*skoS2/281474976710656 + 1688849860263681*pi/562949953421312 + 1688849860263681/5629499534213120 < -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Mul(Rational(1, 281474976710656), Symbol('skoX'), Add(Integer(562949953421057), Mul(Integer(-1), Integer(281474976710656), Symbol('skoSM')))), Integer(0)), StrictLessThan(Add(Mul(Rational(1688849860263681, 281474976710656), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1688849860263681, 562949953421312), Symbol('pi')), Rational(1688849860263681, 5629499534213120)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_87(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (2199023255551*pi*skoS2/1099511627776 + 2199023255551*pi/2199023255552 - 1319413953331/4398046511104 < -1688849860263681*pi*skoS2/281474976710656 - 1688849860263681*pi/562949953421312 - 1688849860263681/5629499534213120)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Rational(2199023255551, 1099511627776), Symbol('pi'), Symbol('skoS2')), Mul(Rational(2199023255551, 2199023255552), Symbol('pi')), Rational(-1319413953331, 4398046511104)), Add(Mul(Integer(-1), Rational(1688849860263681, 281474976710656), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(1688849860263681, 562949953421312), Symbol('pi')), Rational(-1688849860263681, 5629499534213120))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_88(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoX*(562949953421185 - 281474976710656*skoSM)/281474976710656 > 0) & (1688849860263809*pi*skoS2/281474976710656 + 1688849860263809*pi/562949953421312 + 1688849860263809/5629499534213120 < -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Mul(Rational(1, 281474976710656), Symbol('skoX'), Add(Integer(562949953421185), Mul(Integer(-1), Integer(281474976710656), Symbol('skoSM')))), Integer(0)), StrictLessThan(Add(Mul(Rational(1688849860263809, 281474976710656), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1688849860263809, 562949953421312), Symbol('pi')), Rational(1688849860263809, 5629499534213120)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_89(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (4398046511103*pi*skoS2/2199023255552 + 4398046511103*pi/4398046511104 - 13194139533311/43980465111040 < -1688849860263809*pi*skoS2/281474976710656 - 1688849860263809*pi/562949953421312 - 1688849860263809/5629499534213120)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Rational(4398046511103, 2199023255552), Symbol('pi'), Symbol('skoS2')), Mul(Rational(4398046511103, 4398046511104), Symbol('pi')), Rational(-13194139533311, 43980465111040)), Add(Mul(Integer(-1), Rational(1688849860263809, 281474976710656), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(1688849860263809, 562949953421312), Symbol('pi')), Rational(-1688849860263809, 5629499534213120))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_90(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoX*(4*skoSM + 11)/4 < 0) & (5*pi*skoS2/4 + 5*pi/8 + 1/16 < -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Mul(Rational(1, 4), Symbol('skoX'), Add(Mul(Integer(4), Symbol('skoSM')), Integer(11))), Integer(0)), StrictLessThan(Add(Mul(Rational(5, 4), Symbol('pi'), Symbol('skoS2')), Mul(Rational(5, 8), Symbol('pi')), Rational(1, 16)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_91(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (5*pi*skoS2/4 + 5*pi/8 + 1/16 < 3*pi*skoS2 + 3*pi/2 + 1/20)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Rational(5, 4), Symbol('pi'), Symbol('skoS2')), Mul(Rational(5, 8), Symbol('pi')), Rational(1, 16)), Add(Mul(Integer(3), Symbol('pi'), Symbol('skoS2')), Mul(Rational(3, 2), Symbol('pi')), Rational(1, 20))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_92(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoX*(32*skoSM + 127)/32 < 0) & (pi*skoS2/32 + pi/64 + 1/640 < -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Mul(Rational(1, 32), Symbol('skoX'), Add(Mul(Integer(32), Symbol('skoSM')), Integer(127))), Integer(0)), StrictLessThan(Add(Mul(Rational(1, 32), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 64), Symbol('pi')), Rational(1, 640)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_93(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (2*pi*(2*skoS2 + 1) > pi*skoS2/32 + pi/64 + 1/640)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Mul(Integer(2), Symbol('pi'), Add(Mul(Integer(2), Symbol('skoS2')), Integer(1))), Add(Mul(Rational(1, 32), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 64), Symbol('pi')), Rational(1, 640))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_94(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoX*(128*skoSM + 383)/128 < 0) & (129*pi*skoS2/128 + 129*pi/256 + 129/2560 < -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Mul(Rational(1, 128), Symbol('skoX'), Add(Mul(Integer(128), Symbol('skoSM')), Integer(383))), Integer(0)), StrictLessThan(Add(Mul(Rational(129, 128), Symbol('pi'), Symbol('skoS2')), Mul(Rational(129, 256), Symbol('pi')), Rational(129, 2560)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_95(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (129*pi*skoS2/128 + 129*pi/256 + 129/2560 < 3*pi*skoS2 + 3*pi/2 + 1/20)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Rational(129, 128), Symbol('pi'), Symbol('skoS2')), Mul(Rational(129, 256), Symbol('pi')), Rational(129, 2560)), Add(Mul(Integer(3), Symbol('pi'), Symbol('skoS2')), Mul(Rational(3, 2), Symbol('pi')), Rational(1, 20))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_96(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoX*(256*skoSM + 735)/256 < 0) & (289*pi*skoS2/256 + 289*pi/512 + 289/5120 < -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Mul(Rational(1, 256), Symbol('skoX'), Add(Mul(Integer(256), Symbol('skoSM')), Integer(735))), Integer(0)), StrictLessThan(Add(Mul(Rational(289, 256), Symbol('pi'), Symbol('skoS2')), Mul(Rational(289, 512), Symbol('pi')), Rational(289, 5120)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_97(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (289*pi*skoS2/256 + 289*pi/512 + 289/5120 < 23*pi*skoS2/8 + 23*pi/16 + 9/160)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Rational(289, 256), Symbol('pi'), Symbol('skoS2')), Mul(Rational(289, 512), Symbol('pi')), Rational(289, 5120)), Add(Mul(Rational(23, 8), Symbol('pi'), Symbol('skoS2')), Mul(Rational(23, 16), Symbol('pi')), Rational(9, 160))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_98(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoX*(1024*skoSM + 2879)/1024 < 0) & (1217*pi*skoS2/1024 + 1217*pi/2048 + 1217/20480 < -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Mul(Rational(1, 1024), Symbol('skoX'), Add(Mul(Integer(1024), Symbol('skoSM')), Integer(2879))), Integer(0)), StrictLessThan(Add(Mul(Rational(1217, 1024), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1217, 2048), Symbol('pi')), Rational(1217, 20480)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_99(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (1217*pi*skoS2/1024 + 1217*pi/2048 + 1217/20480 < 45*pi*skoS2/16 + 45*pi/32 + 19/320)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Rational(1217, 1024), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1217, 2048), Symbol('pi')), Rational(1217, 20480)), Add(Mul(Rational(45, 16), Symbol('pi'), Symbol('skoS2')), Mul(Rational(45, 32), Symbol('pi')), Rational(19, 320))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_100(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoX*(2048*skoSM + 5759)/2048 < 0) & (2433*pi*skoS2/2048 + 2433*pi/4096 + 2433/40960 < -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Mul(Rational(1, 2048), Symbol('skoX'), Add(Mul(Integer(2048), Symbol('skoSM')), Integer(5759))), Integer(0)), StrictLessThan(Add(Mul(Rational(2433, 2048), Symbol('pi'), Symbol('skoS2')), Mul(Rational(2433, 4096), Symbol('pi')), Rational(2433, 40960)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_101(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (2433*pi*skoS2/2048 + 2433*pi/4096 + 2433/40960 < 45*pi*skoS2/16 + 45*pi/32 + 19/320)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Rational(2433, 2048), Symbol('pi'), Symbol('skoS2')), Mul(Rational(2433, 4096), Symbol('pi')), Rational(2433, 40960)), Add(Mul(Rational(45, 16), Symbol('pi'), Symbol('skoS2')), Mul(Rational(45, 32), Symbol('pi')), Rational(19, 320))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_102(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoX*(4096*skoSM + 11517)/4096 < 0) & (4867*pi*skoS2/4096 + 4867*pi/8192 + 4867/81920 < -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Mul(Rational(1, 4096), Symbol('skoX'), Add(Mul(Integer(4096), Symbol('skoSM')), Integer(11517))), Integer(0)), StrictLessThan(Add(Mul(Rational(4867, 4096), Symbol('pi'), Symbol('skoS2')), Mul(Rational(4867, 8192), Symbol('pi')), Rational(4867, 81920)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_103(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (4867*pi*skoS2/4096 + 4867*pi/8192 + 4867/81920 < 23035*pi*skoS2/8192 + 23035*pi/16384 + 9733/163840)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Rational(4867, 4096), Symbol('pi'), Symbol('skoS2')), Mul(Rational(4867, 8192), Symbol('pi')), Rational(4867, 81920)), Add(Mul(Rational(23035, 8192), Symbol('pi'), Symbol('skoS2')), Mul(Rational(23035, 16384), Symbol('pi')), Rational(9733, 163840))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_104(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoX*(16384*skoSM + 46065)/16384 < 0) & (19471*pi*skoS2/16384 + 19471*pi/32768 + 19471/327680 < -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Mul(Rational(1, 16384), Symbol('skoX'), Add(Mul(Integer(16384), Symbol('skoSM')), Integer(46065))), Integer(0)), StrictLessThan(Add(Mul(Rational(19471, 16384), Symbol('pi'), Symbol('skoS2')), Mul(Rational(19471, 32768), Symbol('pi')), Rational(19471, 327680)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_105(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (19471*pi*skoS2/16384 + 19471*pi/32768 + 19471/327680 < 23033*pi*skoS2/8192 + 23033*pi/16384 + 1947/32768)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Rational(19471, 16384), Symbol('pi'), Symbol('skoS2')), Mul(Rational(19471, 32768), Symbol('pi')), Rational(19471, 327680)), Add(Mul(Rational(23033, 8192), Symbol('pi'), Symbol('skoS2')), Mul(Rational(23033, 16384), Symbol('pi')), Rational(1947, 32768))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_106(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoX*(32768*skoSM + 92129)/32768 < 0) & (38943*pi*skoS2/32768 + 38943*pi/65536 + 38943/655360 < -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Mul(Rational(1, 32768), Symbol('skoX'), Add(Mul(Integer(32768), Symbol('skoSM')), Integer(92129))), Integer(0)), StrictLessThan(Add(Mul(Rational(38943, 32768), Symbol('pi'), Symbol('skoS2')), Mul(Rational(38943, 65536), Symbol('pi')), Rational(38943, 655360)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_107(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (38943*pi*skoS2/32768 + 38943*pi/65536 + 38943/655360 < 184259*pi*skoS2/65536 + 184259*pi/131072 + 15577/262144)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Rational(38943, 32768), Symbol('pi'), Symbol('skoS2')), Mul(Rational(38943, 65536), Symbol('pi')), Rational(38943, 655360)), Add(Mul(Rational(184259, 65536), Symbol('pi'), Symbol('skoS2')), Mul(Rational(184259, 131072), Symbol('pi')), Rational(15577, 262144))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_108(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoX*(131072*skoSM + 368517)/131072 < 0) & (155771*pi*skoS2/131072 + 155771*pi/262144 + 155771/2621440 < -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Mul(Rational(1, 131072), Symbol('skoX'), Add(Mul(Integer(131072), Symbol('skoSM')), Integer(368517))), Integer(0)), StrictLessThan(Add(Mul(Rational(155771, 131072), Symbol('pi'), Symbol('skoS2')), Mul(Rational(155771, 262144), Symbol('pi')), Rational(155771, 2621440)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_109(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (155771*pi*skoS2/131072 + 155771*pi/262144 + 155771/2621440 < 184259*pi*skoS2/65536 + 184259*pi/131072 + 15577/262144)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Rational(155771, 131072), Symbol('pi'), Symbol('skoS2')), Mul(Rational(155771, 262144), Symbol('pi')), Rational(155771, 2621440)), Add(Mul(Rational(184259, 65536), Symbol('pi'), Symbol('skoS2')), Mul(Rational(184259, 131072), Symbol('pi')), Rational(15577, 262144))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_110(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoX*(524288*skoSM + 1474065)/524288 < 0) & (623087*pi*skoS2/524288 + 623087*pi/1048576 + 623087/10485760 < -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Mul(Rational(1, 524288), Symbol('skoX'), Add(Mul(Integer(524288), Symbol('skoSM')), Integer(1474065))), Integer(0)), StrictLessThan(Add(Mul(Rational(623087, 524288), Symbol('pi'), Symbol('skoS2')), Mul(Rational(623087, 1048576), Symbol('pi')), Rational(623087, 10485760)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_111(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (623087*pi*skoS2/524288 + 623087*pi/1048576 + 623087/10485760 < 737033*pi*skoS2/262144 + 737033*pi/524288 + 311543/5242880)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Rational(623087, 524288), Symbol('pi'), Symbol('skoS2')), Mul(Rational(623087, 1048576), Symbol('pi')), Rational(623087, 10485760)), Add(Mul(Rational(737033, 262144), Symbol('pi'), Symbol('skoS2')), Mul(Rational(737033, 524288), Symbol('pi')), Rational(311543, 5242880))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_112(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoX*(1048576*skoSM + 2948131)/1048576 < 0) & (1246173*pi*skoS2/1048576 + 1246173*pi/2097152 + 1246173/20971520 < -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Mul(Rational(1, 1048576), Symbol('skoX'), Add(Mul(Integer(1048576), Symbol('skoSM')), Integer(2948131))), Integer(0)), StrictLessThan(Add(Mul(Rational(1246173, 1048576), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1246173, 2097152), Symbol('pi')), Rational(1246173, 20971520)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_113(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (1246173*pi*skoS2/1048576 + 1246173*pi/2097152 + 1246173/20971520 < 737033*pi*skoS2/262144 + 737033*pi/524288 + 311543/5242880)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Rational(1246173, 1048576), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1246173, 2097152), Symbol('pi')), Rational(1246173, 20971520)), Add(Mul(Rational(737033, 262144), Symbol('pi'), Symbol('skoS2')), Mul(Rational(737033, 524288), Symbol('pi')), Rational(311543, 5242880))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_114(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoX*(2097152*skoSM + 5896261)/2097152 < 0) & (2492347*pi*skoS2/2097152 + 2492347*pi/4194304 + 2492347/41943040 < -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Mul(Rational(1, 2097152), Symbol('skoX'), Add(Mul(Integer(2097152), Symbol('skoSM')), Integer(5896261))), Integer(0)), StrictLessThan(Add(Mul(Rational(2492347, 2097152), Symbol('pi'), Symbol('skoS2')), Mul(Rational(2492347, 4194304), Symbol('pi')), Rational(2492347, 41943040)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_115(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (2492347*pi*skoS2/2097152 + 2492347*pi/4194304 + 2492347/41943040 < 11792523*pi*skoS2/4194304 + 11792523*pi/8388608 + 4984693/83886080)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Rational(2492347, 2097152), Symbol('pi'), Symbol('skoS2')), Mul(Rational(2492347, 4194304), Symbol('pi')), Rational(2492347, 41943040)), Add(Mul(Rational(11792523, 4194304), Symbol('pi'), Symbol('skoS2')), Mul(Rational(11792523, 8388608), Symbol('pi')), Rational(4984693, 83886080))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_116(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoX*(8388608*skoSM + 23585045)/8388608 < 0) & (9969387*pi*skoS2/8388608 + 9969387*pi/16777216 + 9969387/167772160 < -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Mul(Rational(1, 8388608), Symbol('skoX'), Add(Mul(Integer(8388608), Symbol('skoSM')), Integer(23585045))), Integer(0)), StrictLessThan(Add(Mul(Rational(9969387, 8388608), Symbol('pi'), Symbol('skoS2')), Mul(Rational(9969387, 16777216), Symbol('pi')), Rational(9969387, 167772160)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_117(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (9969387*pi*skoS2/8388608 + 9969387*pi/16777216 + 9969387/167772160 < 11792523*pi*skoS2/4194304 + 11792523*pi/8388608 + 4984693/83886080)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Rational(9969387, 8388608), Symbol('pi'), Symbol('skoS2')), Mul(Rational(9969387, 16777216), Symbol('pi')), Rational(9969387, 167772160)), Add(Mul(Rational(11792523, 4194304), Symbol('pi'), Symbol('skoS2')), Mul(Rational(11792523, 8388608), Symbol('pi')), Rational(4984693, 83886080))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_118(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoX*(16777216*skoSM + 47170089)/16777216 < 0) & (19938775*pi*skoS2/16777216 + 19938775*pi/33554432 + 3987755/67108864 < -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Mul(Rational(1, 16777216), Symbol('skoX'), Add(Mul(Integer(16777216), Symbol('skoSM')), Integer(47170089))), Integer(0)), StrictLessThan(Add(Mul(Rational(19938775, 16777216), Symbol('pi'), Symbol('skoS2')), Mul(Rational(19938775, 33554432), Symbol('pi')), Rational(3987755, 67108864)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_119(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (19938775*pi*skoS2/16777216 + 19938775*pi/33554432 + 3987755/67108864 < 94340179*pi*skoS2/33554432 + 94340179*pi/67108864 + 39877549/671088640)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Rational(19938775, 16777216), Symbol('pi'), Symbol('skoS2')), Mul(Rational(19938775, 33554432), Symbol('pi')), Rational(3987755, 67108864)), Add(Mul(Rational(94340179, 33554432), Symbol('pi'), Symbol('skoS2')), Mul(Rational(94340179, 67108864), Symbol('pi')), Rational(39877549, 671088640))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_120(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoX*(67108864*skoSM + 188680353)/67108864 < 0) & (79755103*pi*skoS2/67108864 + 79755103*pi/134217728 + 79755103/1342177280 < -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Mul(Rational(1, 67108864), Symbol('skoX'), Add(Mul(Integer(67108864), Symbol('skoSM')), Integer(188680353))), Integer(0)), StrictLessThan(Add(Mul(Rational(79755103, 67108864), Symbol('pi'), Symbol('skoS2')), Mul(Rational(79755103, 134217728), Symbol('pi')), Rational(79755103, 1342177280)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_121(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (79755103*pi*skoS2/67108864 + 79755103*pi/134217728 + 79755103/1342177280 < 94340177*pi*skoS2/33554432 + 94340177*pi/67108864 + 39877551/671088640)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Rational(79755103, 67108864), Symbol('pi'), Symbol('skoS2')), Mul(Rational(79755103, 134217728), Symbol('pi')), Rational(79755103, 1342177280)), Add(Mul(Rational(94340177, 33554432), Symbol('pi'), Symbol('skoS2')), Mul(Rational(94340177, 67108864), Symbol('pi')), Rational(39877551, 671088640))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_122(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoX*(134217728*skoSM + 377360705)/134217728 < 0) & (159510207*pi*skoS2/134217728 + 159510207*pi/268435456 + 159510207/2684354560 < -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Mul(Rational(1, 134217728), Symbol('skoX'), Add(Mul(Integer(134217728), Symbol('skoSM')), Integer(377360705))), Integer(0)), StrictLessThan(Add(Mul(Rational(159510207, 134217728), Symbol('pi'), Symbol('skoS2')), Mul(Rational(159510207, 268435456), Symbol('pi')), Rational(159510207, 2684354560)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_123(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (159510207*pi*skoS2/134217728 + 159510207*pi/268435456 + 159510207/2684354560 < 754721411*pi*skoS2/268435456 + 754721411*pi/536870912 + 319020413/5368709120)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Rational(159510207, 134217728), Symbol('pi'), Symbol('skoS2')), Mul(Rational(159510207, 268435456), Symbol('pi')), Rational(159510207, 2684354560)), Add(Mul(Rational(754721411, 268435456), Symbol('pi'), Symbol('skoS2')), Mul(Rational(754721411, 536870912), Symbol('pi')), Rational(319020413, 5368709120))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_124(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoX*(536870912*skoSM + 1509442821)/536870912 < 0) & (638040827*pi*skoS2/536870912 + 638040827*pi/1073741824 + 638040827/10737418240 < -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Mul(Rational(1, 536870912), Symbol('skoX'), Add(Mul(Integer(536870912), Symbol('skoSM')), Integer(1509442821))), Integer(0)), StrictLessThan(Add(Mul(Rational(638040827, 536870912), Symbol('pi'), Symbol('skoS2')), Mul(Rational(638040827, 1073741824), Symbol('pi')), Rational(638040827, 10737418240)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_125(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (638040827*pi*skoS2/536870912 + 638040827*pi/1073741824 + 638040827/10737418240 < 754721411*pi*skoS2/268435456 + 754721411*pi/536870912 + 319020413/5368709120)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Rational(638040827, 536870912), Symbol('pi'), Symbol('skoS2')), Mul(Rational(638040827, 1073741824), Symbol('pi')), Rational(638040827, 10737418240)), Add(Mul(Rational(754721411, 268435456), Symbol('pi'), Symbol('skoS2')), Mul(Rational(754721411, 536870912), Symbol('pi')), Rational(319020413, 5368709120))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_126(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoX*(1073741824*skoSM + 3018885641)/1073741824 < 0) & (1276081655*pi*skoS2/1073741824 + 1276081655*pi/2147483648 + 255216331/4294967296 < -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Mul(Rational(1, 1073741824), Symbol('skoX'), Add(Mul(Integer(1073741824), Symbol('skoSM')), Integer(3018885641))), Integer(0)), StrictLessThan(Add(Mul(Rational(1276081655, 1073741824), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1276081655, 2147483648), Symbol('pi')), Rational(255216331, 4294967296)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_127(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (1276081655*pi*skoS2/1073741824 + 1276081655*pi/2147483648 + 255216331/4294967296 < 6037771283*pi*skoS2/2147483648 + 6037771283*pi/4294967296 + 2552163309/42949672960)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Rational(1276081655, 1073741824), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1276081655, 2147483648), Symbol('pi')), Rational(255216331, 4294967296)), Add(Mul(Rational(6037771283, 2147483648), Symbol('pi'), Symbol('skoS2')), Mul(Rational(6037771283, 4294967296), Symbol('pi')), Rational(2552163309, 42949672960))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_128(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoX*(4294967296*skoSM + 12075542561)/4294967296 < 0) & (5104326623*pi*skoS2/4294967296 + 5104326623*pi/8589934592 + 5104326623/85899345920 < -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Mul(Rational(1, 4294967296), Symbol('skoX'), Add(Mul(Integer(4294967296), Symbol('skoSM')), Integer(12075542561))), Integer(0)), StrictLessThan(Add(Mul(Rational(5104326623, 4294967296), Symbol('pi'), Symbol('skoS2')), Mul(Rational(5104326623, 8589934592), Symbol('pi')), Rational(5104326623, 85899345920)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_129(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (5104326623*pi*skoS2/4294967296 + 5104326623*pi/8589934592 + 5104326623/85899345920 < 6037771281*pi*skoS2/2147483648 + 6037771281*pi/4294967296 + 2552163311/42949672960)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Rational(5104326623, 4294967296), Symbol('pi'), Symbol('skoS2')), Mul(Rational(5104326623, 8589934592), Symbol('pi')), Rational(5104326623, 85899345920)), Add(Mul(Rational(6037771281, 2147483648), Symbol('pi'), Symbol('skoS2')), Mul(Rational(6037771281, 4294967296), Symbol('pi')), Rational(2552163311, 42949672960))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_130(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoX*(8589934592*skoSM + 24151085121)/8589934592 < 0) & (10208653247*pi*skoS2/8589934592 + 10208653247*pi/17179869184 + 10208653247/171798691840 < -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Mul(Rational(1, 8589934592), Symbol('skoX'), Add(Mul(Integer(8589934592), Symbol('skoSM')), Integer(24151085121))), Integer(0)), StrictLessThan(Add(Mul(Rational(10208653247, 8589934592), Symbol('pi'), Symbol('skoS2')), Mul(Rational(10208653247, 17179869184), Symbol('pi')), Rational(10208653247, 171798691840)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_131(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (10208653247*pi*skoS2/8589934592 + 10208653247*pi/17179869184 + 10208653247/171798691840 < 48302170243*pi*skoS2/17179869184 + 48302170243*pi/34359738368 + 20417306493/343597383680)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Rational(10208653247, 8589934592), Symbol('pi'), Symbol('skoS2')), Mul(Rational(10208653247, 17179869184), Symbol('pi')), Rational(10208653247, 171798691840)), Add(Mul(Rational(48302170243, 17179869184), Symbol('pi'), Symbol('skoS2')), Mul(Rational(48302170243, 34359738368), Symbol('pi')), Rational(20417306493, 343597383680))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_132(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoX*(34359738368*skoSM + 96604340485)/34359738368 < 0) & (40834612987*pi*skoS2/34359738368 + 40834612987*pi/68719476736 + 40834612987/687194767360 < -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Mul(Rational(1, 34359738368), Symbol('skoX'), Add(Mul(Integer(34359738368), Symbol('skoSM')), Integer(96604340485))), Integer(0)), StrictLessThan(Add(Mul(Rational(40834612987, 34359738368), Symbol('pi'), Symbol('skoS2')), Mul(Rational(40834612987, 68719476736), Symbol('pi')), Rational(40834612987, 687194767360)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_133(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (40834612987*pi*skoS2/34359738368 + 40834612987*pi/68719476736 + 40834612987/687194767360 < 48302170243*pi*skoS2/17179869184 + 48302170243*pi/34359738368 + 20417306493/343597383680)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Rational(40834612987, 34359738368), Symbol('pi'), Symbol('skoS2')), Mul(Rational(40834612987, 68719476736), Symbol('pi')), Rational(40834612987, 687194767360)), Add(Mul(Rational(48302170243, 17179869184), Symbol('pi'), Symbol('skoS2')), Mul(Rational(48302170243, 34359738368), Symbol('pi')), Rational(20417306493, 343597383680))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_134(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoX*(68719476736*skoSM + 193208680969)/68719476736 < 0) & (81669225975*pi*skoS2/68719476736 + 81669225975*pi/137438953472 + 16333845195/274877906944 < -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Mul(Rational(1, 68719476736), Symbol('skoX'), Add(Mul(Integer(68719476736), Symbol('skoSM')), Integer(193208680969))), Integer(0)), StrictLessThan(Add(Mul(Rational(81669225975, 68719476736), Symbol('pi'), Symbol('skoS2')), Mul(Rational(81669225975, 137438953472), Symbol('pi')), Rational(16333845195, 274877906944)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_135(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (81669225975*pi*skoS2/68719476736 + 81669225975*pi/137438953472 + 16333845195/274877906944 < 386417361939*pi*skoS2/137438953472 + 386417361939*pi/274877906944 + 163338451949/2748779069440)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Rational(81669225975, 68719476736), Symbol('pi'), Symbol('skoS2')), Mul(Rational(81669225975, 137438953472), Symbol('pi')), Rational(16333845195, 274877906944)), Add(Mul(Rational(386417361939, 137438953472), Symbol('pi'), Symbol('skoS2')), Mul(Rational(386417361939, 274877906944), Symbol('pi')), Rational(163338451949, 2748779069440))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_136(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoX*(274877906944*skoSM + 772834723873)/274877906944 < 0) & (326676903903*pi*skoS2/274877906944 + 326676903903*pi/549755813888 + 326676903903/5497558138880 < -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Mul(Rational(1, 274877906944), Symbol('skoX'), Add(Mul(Integer(274877906944), Symbol('skoSM')), Integer(772834723873))), Integer(0)), StrictLessThan(Add(Mul(Rational(326676903903, 274877906944), Symbol('pi'), Symbol('skoS2')), Mul(Rational(326676903903, 549755813888), Symbol('pi')), Rational(326676903903, 5497558138880)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_137(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (326676903903*pi*skoS2/274877906944 + 326676903903*pi/549755813888 + 326676903903/5497558138880 < 386417361937*pi*skoS2/137438953472 + 386417361937*pi/274877906944 + 163338451951/2748779069440)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Rational(326676903903, 274877906944), Symbol('pi'), Symbol('skoS2')), Mul(Rational(326676903903, 549755813888), Symbol('pi')), Rational(326676903903, 5497558138880)), Add(Mul(Rational(386417361937, 137438953472), Symbol('pi'), Symbol('skoS2')), Mul(Rational(386417361937, 274877906944), Symbol('pi')), Rational(163338451951, 2748779069440))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_138(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoX*(549755813888*skoSM + 1545669447745)/549755813888 < 0) & (653353807807*pi*skoS2/549755813888 + 653353807807*pi/1099511627776 + 653353807807/10995116277760 < -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Mul(Rational(1, 549755813888), Symbol('skoX'), Add(Mul(Integer(549755813888), Symbol('skoSM')), Integer(1545669447745))), Integer(0)), StrictLessThan(Add(Mul(Rational(653353807807, 549755813888), Symbol('pi'), Symbol('skoS2')), Mul(Rational(653353807807, 1099511627776), Symbol('pi')), Rational(653353807807, 10995116277760)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_139(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (653353807807*pi*skoS2/549755813888 + 653353807807*pi/1099511627776 + 653353807807/10995116277760 < 3091338895491*pi*skoS2/1099511627776 + 3091338895491*pi/2199023255552 + 1306707615613/21990232555520)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Rational(653353807807, 549755813888), Symbol('pi'), Symbol('skoS2')), Mul(Rational(653353807807, 1099511627776), Symbol('pi')), Rational(653353807807, 10995116277760)), Add(Mul(Rational(3091338895491, 1099511627776), Symbol('pi'), Symbol('skoS2')), Mul(Rational(3091338895491, 2199023255552), Symbol('pi')), Rational(1306707615613, 21990232555520))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_140(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoX*(2199023255552*skoSM + 6182677790981)/2199023255552 < 0) & (2613415231227*pi*skoS2/2199023255552 + 2613415231227*pi/4398046511104 + 2613415231227/43980465111040 < -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Mul(Rational(1, 2199023255552), Symbol('skoX'), Add(Mul(Integer(2199023255552), Symbol('skoSM')), Integer(6182677790981))), Integer(0)), StrictLessThan(Add(Mul(Rational(2613415231227, 2199023255552), Symbol('pi'), Symbol('skoS2')), Mul(Rational(2613415231227, 4398046511104), Symbol('pi')), Rational(2613415231227, 43980465111040)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_141(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (2613415231227*pi*skoS2/2199023255552 + 2613415231227*pi/4398046511104 + 2613415231227/43980465111040 < 3091338895491*pi*skoS2/1099511627776 + 3091338895491*pi/2199023255552 + 1306707615613/21990232555520)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Rational(2613415231227, 2199023255552), Symbol('pi'), Symbol('skoS2')), Mul(Rational(2613415231227, 4398046511104), Symbol('pi')), Rational(2613415231227, 43980465111040)), Add(Mul(Rational(3091338895491, 1099511627776), Symbol('pi'), Symbol('skoS2')), Mul(Rational(3091338895491, 2199023255552), Symbol('pi')), Rational(1306707615613, 21990232555520))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_142(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoX*(4398046511104*skoSM + 12365355581961)/4398046511104 < 0) & (5226830462455*pi*skoS2/4398046511104 + 5226830462455*pi/8796093022208 + 1045366092491/17592186044416 < -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Mul(Rational(1, 4398046511104), Symbol('skoX'), Add(Mul(Integer(4398046511104), Symbol('skoSM')), Integer(12365355581961))), Integer(0)), StrictLessThan(Add(Mul(Rational(5226830462455, 4398046511104), Symbol('pi'), Symbol('skoS2')), Mul(Rational(5226830462455, 8796093022208), Symbol('pi')), Rational(1045366092491, 17592186044416)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_143(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (5226830462455*pi*skoS2/4398046511104 + 5226830462455*pi/8796093022208 + 1045366092491/17592186044416 < 24730711163923*pi*skoS2/8796093022208 + 24730711163923*pi/17592186044416 + 10453660924909/175921860444160)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Rational(5226830462455, 4398046511104), Symbol('pi'), Symbol('skoS2')), Mul(Rational(5226830462455, 8796093022208), Symbol('pi')), Rational(1045366092491, 17592186044416)), Add(Mul(Rational(24730711163923, 8796093022208), Symbol('pi'), Symbol('skoS2')), Mul(Rational(24730711163923, 17592186044416), Symbol('pi')), Rational(10453660924909, 175921860444160))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_144(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoX*(8796093022208*skoSM + 24730711163921)/8796093022208 < 0) & (10453660924911*pi*skoS2/8796093022208 + 10453660924911*pi/17592186044416 + 10453660924911/175921860444160 < -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Mul(Rational(1, 8796093022208), Symbol('skoX'), Add(Mul(Integer(8796093022208), Symbol('skoSM')), Integer(24730711163921))), Integer(0)), StrictLessThan(Add(Mul(Rational(10453660924911, 8796093022208), Symbol('pi'), Symbol('skoS2')), Mul(Rational(10453660924911, 17592186044416), Symbol('pi')), Rational(10453660924911, 175921860444160)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_145(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (10453660924911*pi*skoS2/8796093022208 + 10453660924911*pi/17592186044416 + 10453660924911/175921860444160 < 49461422327843*pi*skoS2/17592186044416 + 49461422327843*pi/35184372088832 + 20907321849821/351843720888320)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Rational(10453660924911, 8796093022208), Symbol('pi'), Symbol('skoS2')), Mul(Rational(10453660924911, 17592186044416), Symbol('pi')), Rational(10453660924911, 175921860444160)), Add(Mul(Rational(49461422327843, 17592186044416), Symbol('pi'), Symbol('skoS2')), Mul(Rational(49461422327843, 35184372088832), Symbol('pi')), Rational(20907321849821, 351843720888320))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_146(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoX*(17592186044416*skoSM + 49461422327841)/17592186044416 < 0) & (20907321849823*pi*skoS2/17592186044416 + 20907321849823*pi/35184372088832 + 20907321849823/351843720888320 < -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Mul(Rational(1, 17592186044416), Symbol('skoX'), Add(Mul(Integer(17592186044416), Symbol('skoSM')), Integer(49461422327841))), Integer(0)), StrictLessThan(Add(Mul(Rational(20907321849823, 17592186044416), Symbol('pi'), Symbol('skoS2')), Mul(Rational(20907321849823, 35184372088832), Symbol('pi')), Rational(20907321849823, 351843720888320)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_147(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (20907321849823*pi*skoS2/17592186044416 + 20907321849823*pi/35184372088832 + 20907321849823/351843720888320 < 98922844655683*pi*skoS2/35184372088832 + 98922844655683*pi/70368744177664 + 8362928739929/140737488355328)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Rational(20907321849823, 17592186044416), Symbol('pi'), Symbol('skoS2')), Mul(Rational(20907321849823, 35184372088832), Symbol('pi')), Rational(20907321849823, 351843720888320)), Add(Mul(Rational(98922844655683, 35184372088832), Symbol('pi'), Symbol('skoS2')), Mul(Rational(98922844655683, 70368744177664), Symbol('pi')), Rational(8362928739929, 140737488355328))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_148(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoX*(70368744177664*skoSM + 197845689311365)/70368744177664 < 0) & (83629287399291*pi*skoS2/70368744177664 + 83629287399291*pi/140737488355328 + 83629287399291/1407374883553280 < -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Mul(Rational(1, 70368744177664), Symbol('skoX'), Add(Mul(Integer(70368744177664), Symbol('skoSM')), Integer(197845689311365))), Integer(0)), StrictLessThan(Add(Mul(Rational(83629287399291, 70368744177664), Symbol('pi'), Symbol('skoS2')), Mul(Rational(83629287399291, 140737488355328), Symbol('pi')), Rational(83629287399291, 1407374883553280)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_149(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (83629287399291*pi*skoS2/70368744177664 + 83629287399291*pi/140737488355328 + 83629287399291/1407374883553280 < 98922844655683*pi*skoS2/35184372088832 + 98922844655683*pi/70368744177664 + 8362928739929/140737488355328)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Rational(83629287399291, 70368744177664), Symbol('pi'), Symbol('skoS2')), Mul(Rational(83629287399291, 140737488355328), Symbol('pi')), Rational(83629287399291, 1407374883553280)), Add(Mul(Rational(98922844655683, 35184372088832), Symbol('pi'), Symbol('skoS2')), Mul(Rational(98922844655683, 70368744177664), Symbol('pi')), Rational(8362928739929, 140737488355328))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_150(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoX*(140737488355328*skoSM + 395691378622729)/140737488355328 < 0) & (167258574798583*pi*skoS2/140737488355328 + 167258574798583*pi/281474976710656 + 167258574798583/2814749767106560 < -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Mul(Rational(1, 140737488355328), Symbol('skoX'), Add(Mul(Integer(140737488355328), Symbol('skoSM')), Integer(395691378622729))), Integer(0)), StrictLessThan(Add(Mul(Rational(167258574798583, 140737488355328), Symbol('pi'), Symbol('skoS2')), Mul(Rational(167258574798583, 281474976710656), Symbol('pi')), Rational(167258574798583, 2814749767106560)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_151(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (167258574798583*pi*skoS2/140737488355328 + 167258574798583*pi/281474976710656 + 167258574798583/2814749767106560 < 791382757245459*pi*skoS2/281474976710656 + 791382757245459*pi/562949953421312 + 66903429919433/1125899906842624)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Rational(167258574798583, 140737488355328), Symbol('pi'), Symbol('skoS2')), Mul(Rational(167258574798583, 281474976710656), Symbol('pi')), Rational(167258574798583, 2814749767106560)), Add(Mul(Rational(791382757245459, 281474976710656), Symbol('pi'), Symbol('skoS2')), Mul(Rational(791382757245459, 562949953421312), Symbol('pi')), Rational(66903429919433, 1125899906842624))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_152(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoX*(281474976710656*skoSM + 791382757245457)/281474976710656 < 0) & (334517149597167*pi*skoS2/281474976710656 + 334517149597167*pi/562949953421312 + 334517149597167/5629499534213120 < -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Mul(Rational(1, 281474976710656), Symbol('skoX'), Add(Mul(Integer(281474976710656), Symbol('skoSM')), Integer(791382757245457))), Integer(0)), StrictLessThan(Add(Mul(Rational(334517149597167, 281474976710656), Symbol('pi'), Symbol('skoS2')), Mul(Rational(334517149597167, 562949953421312), Symbol('pi')), Rational(334517149597167, 5629499534213120)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_153(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (334517149597167*pi*skoS2/281474976710656 + 334517149597167*pi/562949953421312 + 334517149597167/5629499534213120 < 1582765514490915*pi*skoS2/562949953421312 + 1582765514490915*pi/1125899906842624 + 669034299194333/11258999068426240)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Rational(334517149597167, 281474976710656), Symbol('pi'), Symbol('skoS2')), Mul(Rational(334517149597167, 562949953421312), Symbol('pi')), Rational(334517149597167, 5629499534213120)), Add(Mul(Rational(1582765514490915, 562949953421312), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1582765514490915, 1125899906842624), Symbol('pi')), Rational(669034299194333, 11258999068426240))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(delta:sympy.Rational, skoX:sympy.Rational, skoS2:sympy.Rational, pi:sympy.Rational, skoSP:sympy.Rational, skoSM:sympy.Rational):
	# (0 <= delta) & (1 > skoX) & (31415927/10000000 > pi) & (pi > 15707963/5000000) & (skoX > 0) & (skoX*(-skoSM - skoSP - 4) > 0) & (skoSP*(pi*skoS2 + pi/2 + 1/20) > skoSM*(pi*skoS2 + pi/2 - 1/20) - 1/5)

	post_cond =  And(LessThan(Integer(0), Symbol('delta')), StrictGreaterThan(Integer(1), Symbol('skoX')), StrictGreaterThan(Rational(31415927, 10000000), Symbol('pi')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictGreaterThan(Mul(Symbol('skoX'), Add(Mul(Integer(-1), Symbol('skoSM')), Mul(Integer(-1), Symbol('skoSP')), Integer(-4))), Integer(0)), StrictGreaterThan(Mul(Symbol('skoSP'), Add(Mul(Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 2), Symbol('pi')), Rational(1, 20))), Add(Mul(Symbol('skoSM'), Add(Mul(Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 2), Symbol('pi')), Rational(-1, 20))), Rational(-1, 5))))

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
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = -6')
		print('skoSP = 1/8')
		print('skoS2 = 1')
		exit(0)
	
	
	if pre_condition_1(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_1 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = -6')
		print('skoSP = 1/8')
		print('skoS2 = 1')
		exit(0)
	
	
	if pre_condition_2(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_2 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 1/16')
		print('skoSP = -6')
		print('skoS2 = -50331648/26353589')
		exit(0)
	
	
	if pre_condition_3(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_3 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 1/16')
		print('skoSP = -6')
		print('skoS2 = -50331648/26353589')
		exit(0)
	
	
	if pre_condition_4(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_4 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 1/2')
		print('skoSP = -5')
		print('skoS2 = -13238272/26353589')
		exit(0)
	
	
	if pre_condition_5(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_5 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 1/2')
		print('skoSP = -5')
		print('skoS2 = -13238272/26353589')
		exit(0)
	
	
	if pre_condition_6(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_6 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 1')
		print('skoSP = -21/4')
		print('skoS2 = -13205504/26353589')
		exit(0)
	
	
	if pre_condition_7(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_7 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 1')
		print('skoSP = -21/4')
		print('skoS2 = -13205504/26353589')
		exit(0)
	
	
	if pre_condition_8(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_8 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 3/2')
		print('skoSP = -45/8')
		print('skoS2 = -13189120/26353589')
		exit(0)
	
	
	if pre_condition_9(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_9 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 3/2')
		print('skoSP = -45/8')
		print('skoS2 = -13189120/26353589')
		exit(0)
	
	
	if pre_condition_10(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_10 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 7/4')
		print('skoSP = -93/16')
		print('skoS2 = -13180928/26353589')
		exit(0)
	
	
	if pre_condition_11(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_11 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 7/4')
		print('skoSP = -93/16')
		print('skoS2 = -13180928/26353589')
		exit(0)
	
	
	if pre_condition_12(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_12 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 15/8')
		print('skoSP = -12033/2048')
		print('skoS2 = -13176832/26353589')
		exit(0)
	
	
	if pre_condition_13(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_13 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 15/8')
		print('skoSP = -12033/2048')
		print('skoS2 = -13176832/26353589')
		exit(0)
	
	
	if pre_condition_14(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_14 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 31/16')
		print('skoSP = -97281/16384')
		print('skoS2 = -13176800/26353589')
		exit(0)
	
	
	if pre_condition_15(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_15 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 31/16')
		print('skoSP = -97281/16384')
		print('skoS2 = -13176800/26353589')
		exit(0)
	
	
	if pre_condition_16(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_16 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 63/32')
		print('skoSP = -391169/65536')
		print('skoS2 = -13176796/26353589')
		exit(0)
	
	
	if pre_condition_17(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_17 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 63/32')
		print('skoSP = -391169/65536')
		print('skoS2 = -13176796/26353589')
		exit(0)
	
	
	if pre_condition_18(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_18 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 127/64')
		print('skoSP = -784385/131072')
		print('skoS2 = -13176795/26353589')
		exit(0)
	
	
	if pre_condition_19(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_19 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 127/64')
		print('skoSP = -784385/131072')
		print('skoS2 = -13176795/26353589')
		exit(0)
	
	
	if pre_condition_20(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_20 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 255/128')
		print('skoSP = -1570817/262144')
		print('skoS2 = -52707179/105414356')
		exit(0)
	
	
	if pre_condition_21(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_21 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 255/128')
		print('skoSP = -1570817/262144')
		print('skoS2 = -52707179/105414356')
		exit(0)
	
	
	if pre_condition_22(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_22 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 511/256')
		print('skoSP = -3143681/524288')
		print('skoS2 = -105414357/210828712')
		exit(0)
	
	
	if pre_condition_23(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_23 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 511/256')
		print('skoSP = -3143681/524288')
		print('skoS2 = -105414357/210828712')
		exit(0)
	
	
	if pre_condition_24(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_24 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 1023/512')
		print('skoSP = -6289409/1048576')
		print('skoS2 = -210828713/421657424')
		exit(0)
	
	
	if pre_condition_25(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_25 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 1023/512')
		print('skoSP = -6289409/1048576')
		print('skoS2 = -210828713/421657424')
		exit(0)
	
	
	if pre_condition_26(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_26 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 2047/1024')
		print('skoSP = -12580865/2097152')
		print('skoS2 = -421657425/843314848')
		exit(0)
	
	
	if pre_condition_27(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_27 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 2047/1024')
		print('skoSP = -12580865/2097152')
		print('skoS2 = -421657425/843314848')
		exit(0)
	
	
	if pre_condition_28(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_28 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 4095/2048')
		print('skoSP = -25163777/4194304')
		print('skoS2 = -843314849/1686629696')
		exit(0)
	
	
	if pre_condition_29(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_29 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 4095/2048')
		print('skoSP = -25163777/4194304')
		print('skoS2 = -843314849/1686629696')
		exit(0)
	
	
	if pre_condition_30(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_30 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 8191/4096')
		print('skoSP = -50329601/8388608')
		print('skoS2 = -1686629697/3373259392')
		exit(0)
	
	
	if pre_condition_31(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_31 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 8191/4096')
		print('skoSP = -50329601/8388608')
		print('skoS2 = -1686629697/3373259392')
		exit(0)
	
	
	if pre_condition_32(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_32 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 16383/8192')
		print('skoSP = -100661249/16777216')
		print('skoS2 = -3373259393/6746518784')
		exit(0)
	
	
	if pre_condition_33(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_33 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 16383/8192')
		print('skoSP = -100661249/16777216')
		print('skoS2 = -3373259393/6746518784')
		exit(0)
	
	
	if pre_condition_34(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_34 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 32767/16384')
		print('skoSP = -201324545/33554432')
		print('skoS2 = -6746518785/13493037568')
		exit(0)
	
	
	if pre_condition_35(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_35 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 32767/16384')
		print('skoSP = -201324545/33554432')
		print('skoS2 = -6746518785/13493037568')
		exit(0)
	
	
	if pre_condition_36(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_36 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 65535/32768')
		print('skoSP = -402651137/67108864')
		print('skoS2 = -13493037569/26986075136')
		exit(0)
	
	
	if pre_condition_37(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_37 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 65535/32768')
		print('skoSP = -402651137/67108864')
		print('skoS2 = -13493037569/26986075136')
		exit(0)
	
	
	if pre_condition_38(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_38 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 131071/65536')
		print('skoSP = -805304321/134217728')
		print('skoS2 = -26986075137/53972150272')
		exit(0)
	
	
	if pre_condition_39(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_39 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 131071/65536')
		print('skoSP = -805304321/134217728')
		print('skoS2 = -26986075137/53972150272')
		exit(0)
	
	
	if pre_condition_40(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_40 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 262143/131072')
		print('skoSP = -1610610689/268435456')
		print('skoS2 = -53972150273/107944300544')
		exit(0)
	
	
	if pre_condition_41(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_41 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 262143/131072')
		print('skoSP = -1610610689/268435456')
		print('skoS2 = -53972150273/107944300544')
		exit(0)
	
	
	if pre_condition_42(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_42 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 524287/262144')
		print('skoSP = -3221223425/536870912')
		print('skoS2 = -107944300545/215888601088')
		exit(0)
	
	
	if pre_condition_43(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_43 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 524287/262144')
		print('skoSP = -3221223425/536870912')
		print('skoS2 = -107944300545/215888601088')
		exit(0)
	
	
	if pre_condition_44(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_44 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 1048575/524288')
		print('skoSP = -6442448897/1073741824')
		print('skoS2 = -215888601089/431777202176')
		exit(0)
	
	
	if pre_condition_45(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_45 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 1048575/524288')
		print('skoSP = -6442448897/1073741824')
		print('skoS2 = -215888601089/431777202176')
		exit(0)
	
	
	if pre_condition_46(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_46 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 2097151/1048576')
		print('skoSP = -12884899841/2147483648')
		print('skoS2 = -431777202177/863554404352')
		exit(0)
	
	
	if pre_condition_47(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_47 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 2097151/1048576')
		print('skoSP = -12884899841/2147483648')
		print('skoS2 = -431777202177/863554404352')
		exit(0)
	
	
	if pre_condition_48(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_48 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 4194303/2097152')
		print('skoSP = -25769801729/4294967296')
		print('skoS2 = -863554404353/1727108808704')
		exit(0)
	
	
	if pre_condition_49(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_49 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 4194303/2097152')
		print('skoSP = -25769801729/4294967296')
		print('skoS2 = -863554404353/1727108808704')
		exit(0)
	
	
	if pre_condition_50(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_50 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 8388607/4194304')
		print('skoSP = -51539605505/8589934592')
		print('skoS2 = -1727108808705/3454217617408')
		exit(0)
	
	
	if pre_condition_51(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_51 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 8388607/4194304')
		print('skoSP = -51539605505/8589934592')
		print('skoS2 = -1727108808705/3454217617408')
		exit(0)
	
	
	if pre_condition_52(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_52 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 16777215/8388608')
		print('skoSP = -103079213057/17179869184')
		print('skoS2 = -3454217617409/6908435234816')
		exit(0)
	
	
	if pre_condition_53(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_53 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 16777215/8388608')
		print('skoSP = -103079213057/17179869184')
		print('skoS2 = -3454217617409/6908435234816')
		exit(0)
	
	
	if pre_condition_54(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_54 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 33554431/16777216')
		print('skoSP = -206158428161/34359738368')
		print('skoS2 = -6908435234817/13816870469632')
		exit(0)
	
	
	if pre_condition_55(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_55 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 33554431/16777216')
		print('skoSP = -206158428161/34359738368')
		print('skoS2 = -6908435234817/13816870469632')
		exit(0)
	
	
	if pre_condition_56(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_56 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 67108863/33554432')
		print('skoSP = -412316858369/68719476736')
		print('skoS2 = -13816870469633/27633740939264')
		exit(0)
	
	
	if pre_condition_57(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_57 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 67108863/33554432')
		print('skoSP = -412316858369/68719476736')
		print('skoS2 = -13816870469633/27633740939264')
		exit(0)
	
	
	if pre_condition_58(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_58 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 134217727/67108864')
		print('skoSP = -824633718785/137438953472')
		print('skoS2 = -27633740939265/55267481878528')
		exit(0)
	
	
	if pre_condition_59(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_59 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 134217727/67108864')
		print('skoSP = -824633718785/137438953472')
		print('skoS2 = -27633740939265/55267481878528')
		exit(0)
	
	
	if pre_condition_60(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_60 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 268435455/134217728')
		print('skoSP = -1649267439617/274877906944')
		print('skoS2 = -55267481878529/110534963757056')
		exit(0)
	
	
	if pre_condition_61(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_61 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 268435455/134217728')
		print('skoSP = -1649267439617/274877906944')
		print('skoS2 = -55267481878529/110534963757056')
		exit(0)
	
	
	if pre_condition_62(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_62 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 536870911/268435456')
		print('skoSP = -3298534881281/549755813888')
		print('skoS2 = -110534963757057/221069927514112')
		exit(0)
	
	
	if pre_condition_63(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_63 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 536870911/268435456')
		print('skoSP = -3298534881281/549755813888')
		print('skoS2 = -110534963757057/221069927514112')
		exit(0)
	
	
	if pre_condition_64(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_64 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 1073741823/536870912')
		print('skoSP = -6597069764609/1099511627776')
		print('skoS2 = -221069927514113/442139855028224')
		exit(0)
	
	
	if pre_condition_65(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_65 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 1073741823/536870912')
		print('skoSP = -6597069764609/1099511627776')
		print('skoS2 = -221069927514113/442139855028224')
		exit(0)
	
	
	if pre_condition_66(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_66 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 2147483647/1073741824')
		print('skoSP = -13194139531265/2199023255552')
		print('skoS2 = -442139855028225/884279710056448')
		exit(0)
	
	
	if pre_condition_67(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_67 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 2147483647/1073741824')
		print('skoSP = -13194139531265/2199023255552')
		print('skoS2 = -442139855028225/884279710056448')
		exit(0)
	
	
	if pre_condition_68(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_68 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 4294967295/2147483648')
		print('skoSP = -26388279064577/4398046511104')
		print('skoS2 = -884279710056449/1768559420112896')
		exit(0)
	
	
	if pre_condition_69(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_69 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 4294967295/2147483648')
		print('skoSP = -26388279064577/4398046511104')
		print('skoS2 = -884279710056449/1768559420112896')
		exit(0)
	
	
	if pre_condition_70(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_70 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 8589934591/4294967296')
		print('skoSP = -52776558131201/8796093022208')
		print('skoS2 = -1768559420112897/3537118840225792')
		exit(0)
	
	
	if pre_condition_71(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_71 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 8589934591/4294967296')
		print('skoSP = -52776558131201/8796093022208')
		print('skoS2 = -1768559420112897/3537118840225792')
		exit(0)
	
	
	if pre_condition_72(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_72 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 17179869183/8589934592')
		print('skoSP = -105553116264449/17592186044416')
		print('skoS2 = -3537118840225793/7074237680451584')
		exit(0)
	
	
	if pre_condition_73(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_73 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 17179869183/8589934592')
		print('skoSP = -105553116264449/17592186044416')
		print('skoS2 = -3537118840225793/7074237680451584')
		exit(0)
	
	
	if pre_condition_74(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_74 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 34359738367/17179869184')
		print('skoSP = -211106232530945/35184372088832')
		print('skoS2 = -7074237680451585/14148475360903168')
		exit(0)
	
	
	if pre_condition_75(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_75 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 34359738367/17179869184')
		print('skoSP = -211106232530945/35184372088832')
		print('skoS2 = -7074237680451585/14148475360903168')
		exit(0)
	
	
	if pre_condition_76(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_76 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 68719476735/34359738368')
		print('skoSP = -422212465063937/70368744177664')
		print('skoS2 = -14148475360903169/28296950721806336')
		exit(0)
	
	
	if pre_condition_77(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_77 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 68719476735/34359738368')
		print('skoSP = -422212465063937/70368744177664')
		print('skoS2 = -14148475360903169/28296950721806336')
		exit(0)
	
	
	if pre_condition_78(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_78 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 137438953471/68719476736')
		print('skoSP = -844424930129921/140737488355328')
		print('skoS2 = -28296950721806337/56593901443612672')
		exit(0)
	
	
	if pre_condition_79(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_79 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 137438953471/68719476736')
		print('skoSP = -844424930129921/140737488355328')
		print('skoS2 = -28296950721806337/56593901443612672')
		exit(0)
	
	
	if pre_condition_80(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_80 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 274877906943/137438953472')
		print('skoSP = -844424930130945/140737488355328')
		print('skoS2 = -28296950721806337/56593901443612672')
		exit(0)
	
	
	if pre_condition_81(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_81 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 274877906943/137438953472')
		print('skoSP = -844424930130945/140737488355328')
		print('skoS2 = -28296950721806337/56593901443612672')
		exit(0)
	
	
	if pre_condition_82(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_82 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 549755813887/274877906944')
		print('skoSP = -844424930131457/140737488355328')
		print('skoS2 = -28296950721806337/56593901443612672')
		exit(0)
	
	
	if pre_condition_83(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_83 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 549755813887/274877906944')
		print('skoSP = -844424930131457/140737488355328')
		print('skoS2 = -28296950721806337/56593901443612672')
		exit(0)
	
	
	if pre_condition_84(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_84 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 1099511627775/549755813888')
		print('skoSP = -844424930131713/140737488355328')
		print('skoS2 = -28296950721806337/56593901443612672')
		exit(0)
	
	
	if pre_condition_85(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_85 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 1099511627775/549755813888')
		print('skoSP = -844424930131713/140737488355328')
		print('skoS2 = -28296950721806337/56593901443612672')
		exit(0)
	
	
	if pre_condition_86(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_86 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 2199023255551/1099511627776')
		print('skoSP = -1688849860263681/281474976710656')
		print('skoS2 = -56593901443612673/113187802887225344')
		exit(0)
	
	
	if pre_condition_87(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_87 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 2199023255551/1099511627776')
		print('skoSP = -1688849860263681/281474976710656')
		print('skoS2 = -56593901443612673/113187802887225344')
		exit(0)
	
	
	if pre_condition_88(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_88 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 4398046511103/2199023255552')
		print('skoSP = -1688849860263809/281474976710656')
		print('skoS2 = -56593901443612673/113187802887225344')
		exit(0)
	
	
	if pre_condition_89(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_89 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 4398046511103/2199023255552')
		print('skoSP = -1688849860263809/281474976710656')
		print('skoS2 = -56593901443612673/113187802887225344')
		exit(0)
	
	
	if pre_condition_90(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_90 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = -3')
		print('skoSP = -5/4')
		print('skoS2 = -13107200/26353589')
		exit(0)
	
	
	if pre_condition_91(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_91 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = -3')
		print('skoSP = -5/4')
		print('skoS2 = -13107200/26353589')
		exit(0)
	
	
	if pre_condition_92(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_92 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = -4')
		print('skoSP = -1/32')
		print('skoS2 = -13172736/26353589')
		exit(0)
	
	
	if pre_condition_93(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_93 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = -4')
		print('skoSP = -1/32')
		print('skoS2 = -13172736/26353589')
		exit(0)
	
	
	if pre_condition_94(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_94 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = -3')
		print('skoSP = -129/128')
		print('skoS2 = -13174784/26353589')
		exit(0)
	
	
	if pre_condition_95(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_95 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = -3')
		print('skoSP = -129/128')
		print('skoS2 = -13174784/26353589')
		exit(0)
	
	
	if pre_condition_96(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_96 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = -23/8')
		print('skoSP = -289/256')
		print('skoS2 = -13175808/26353589')
		exit(0)
	
	
	if pre_condition_97(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_97 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = -23/8')
		print('skoSP = -289/256')
		print('skoS2 = -13175808/26353589')
		exit(0)
	
	
	if pre_condition_98(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_98 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = -45/16')
		print('skoSP = -1217/1024')
		print('skoS2 = -13176320/26353589')
		exit(0)
	
	
	if pre_condition_99(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_99 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = -45/16')
		print('skoSP = -1217/1024')
		print('skoS2 = -13176320/26353589')
		exit(0)
	
	
	if pre_condition_100(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_100 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = -45/16')
		print('skoSP = -2433/2048')
		print('skoS2 = -693504/1387031')
		exit(0)
	
	
	if pre_condition_101(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_101 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = -45/16')
		print('skoSP = -2433/2048')
		print('skoS2 = -693504/1387031')
		exit(0)
	
	
	if pre_condition_102(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_102 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = -23035/8192')
		print('skoSP = -4867/4096')
		print('skoS2 = -13176704/26353589')
		exit(0)
	
	
	if pre_condition_103(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_103 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = -23035/8192')
		print('skoSP = -4867/4096')
		print('skoS2 = -13176704/26353589')
		exit(0)
	
	
	if pre_condition_104(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_104 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = -23033/8192')
		print('skoSP = -19471/16384')
		print('skoS2 = -13176768/26353589')
		exit(0)
	
	
	if pre_condition_105(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_105 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = -23033/8192')
		print('skoSP = -19471/16384')
		print('skoS2 = -13176768/26353589')
		exit(0)
	
	
	if pre_condition_106(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_106 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = -184259/65536')
		print('skoSP = -38943/32768')
		print('skoS2 = -13176784/26353589')
		exit(0)
	
	
	if pre_condition_107(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_107 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = -184259/65536')
		print('skoSP = -38943/32768')
		print('skoS2 = -13176784/26353589')
		exit(0)
	
	
	if pre_condition_108(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_108 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = -184259/65536')
		print('skoSP = -155771/131072')
		print('skoS2 = -13176792/26353589')
		exit(0)
	
	
	if pre_condition_109(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_109 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = -184259/65536')
		print('skoSP = -155771/131072')
		print('skoS2 = -13176792/26353589')
		exit(0)
	
	
	if pre_condition_110(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_110 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = -737033/262144')
		print('skoSP = -623087/524288')
		print('skoS2 = -13176794/26353589')
		exit(0)
	
	
	if pre_condition_111(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_111 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = -737033/262144')
		print('skoSP = -623087/524288')
		print('skoS2 = -13176794/26353589')
		exit(0)
	
	
	if pre_condition_112(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_112 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = -737033/262144')
		print('skoSP = -1246173/1048576')
		print('skoS2 = -52707177/105414356')
		exit(0)
	
	
	if pre_condition_113(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_113 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = -737033/262144')
		print('skoSP = -1246173/1048576')
		print('skoS2 = -52707177/105414356')
		exit(0)
	
	
	if pre_condition_114(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_114 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = -11792523/4194304')
		print('skoSP = -2492347/2097152')
		print('skoS2 = -105414355/210828712')
		exit(0)
	
	
	if pre_condition_115(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_115 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = -11792523/4194304')
		print('skoSP = -2492347/2097152')
		print('skoS2 = -105414355/210828712')
		exit(0)
	
	
	if pre_condition_116(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_116 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = -11792523/4194304')
		print('skoSP = -9969387/8388608')
		print('skoS2 = -421657423/843314848')
		exit(0)
	
	
	if pre_condition_117(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_117 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = -11792523/4194304')
		print('skoSP = -9969387/8388608')
		print('skoS2 = -421657423/843314848')
		exit(0)
	
	
	if pre_condition_118(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_118 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = -94340179/33554432')
		print('skoSP = -19938775/16777216')
		print('skoS2 = -843314847/1686629696')
		exit(0)
	
	
	if pre_condition_119(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_119 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = -94340179/33554432')
		print('skoSP = -19938775/16777216')
		print('skoS2 = -843314847/1686629696')
		exit(0)
	
	
	if pre_condition_120(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_120 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = -94340177/33554432')
		print('skoSP = -79755103/67108864')
		print('skoS2 = -3373259391/6746518784')
		exit(0)
	
	
	if pre_condition_121(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_121 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = -94340177/33554432')
		print('skoSP = -79755103/67108864')
		print('skoS2 = -3373259391/6746518784')
		exit(0)
	
	
	if pre_condition_122(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_122 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = -754721411/268435456')
		print('skoSP = -159510207/134217728')
		print('skoS2 = -6746518783/13493037568')
		exit(0)
	
	
	if pre_condition_123(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_123 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = -754721411/268435456')
		print('skoSP = -159510207/134217728')
		print('skoS2 = -6746518783/13493037568')
		exit(0)
	
	
	if pre_condition_124(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_124 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = -754721411/268435456')
		print('skoSP = -638040827/536870912')
		print('skoS2 = -26986075135/53972150272')
		exit(0)
	
	
	if pre_condition_125(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_125 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = -754721411/268435456')
		print('skoSP = -638040827/536870912')
		print('skoS2 = -26986075135/53972150272')
		exit(0)
	
	
	if pre_condition_126(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_126 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = -6037771283/2147483648')
		print('skoSP = -1276081655/1073741824')
		print('skoS2 = -53972150271/107944300544')
		exit(0)
	
	
	if pre_condition_127(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_127 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = -6037771283/2147483648')
		print('skoSP = -1276081655/1073741824')
		print('skoS2 = -53972150271/107944300544')
		exit(0)
	
	
	if pre_condition_128(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_128 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = -6037771281/2147483648')
		print('skoSP = -5104326623/4294967296')
		print('skoS2 = -215888601087/431777202176')
		exit(0)
	
	
	if pre_condition_129(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_129 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = -6037771281/2147483648')
		print('skoSP = -5104326623/4294967296')
		print('skoS2 = -215888601087/431777202176')
		exit(0)
	
	
	if pre_condition_130(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_130 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = -48302170243/17179869184')
		print('skoSP = -10208653247/8589934592')
		print('skoS2 = -431777202175/863554404352')
		exit(0)
	
	
	if pre_condition_131(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_131 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = -48302170243/17179869184')
		print('skoSP = -10208653247/8589934592')
		print('skoS2 = -431777202175/863554404352')
		exit(0)
	
	
	if pre_condition_132(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_132 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = -48302170243/17179869184')
		print('skoSP = -40834612987/34359738368')
		print('skoS2 = -1727108808703/3454217617408')
		exit(0)
	
	
	if pre_condition_133(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_133 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = -48302170243/17179869184')
		print('skoSP = -40834612987/34359738368')
		print('skoS2 = -1727108808703/3454217617408')
		exit(0)
	
	
	if pre_condition_134(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_134 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = -386417361939/137438953472')
		print('skoSP = -81669225975/68719476736')
		print('skoS2 = -3454217617407/6908435234816')
		exit(0)
	
	
	if pre_condition_135(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_135 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = -386417361939/137438953472')
		print('skoSP = -81669225975/68719476736')
		print('skoS2 = -3454217617407/6908435234816')
		exit(0)
	
	
	if pre_condition_136(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_136 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = -386417361937/137438953472')
		print('skoSP = -326676903903/274877906944')
		print('skoS2 = -13816870469631/27633740939264')
		exit(0)
	
	
	if pre_condition_137(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_137 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = -386417361937/137438953472')
		print('skoSP = -326676903903/274877906944')
		print('skoS2 = -13816870469631/27633740939264')
		exit(0)
	
	
	if pre_condition_138(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_138 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = -3091338895491/1099511627776')
		print('skoSP = -653353807807/549755813888')
		print('skoS2 = -27633740939263/55267481878528')
		exit(0)
	
	
	if pre_condition_139(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_139 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = -3091338895491/1099511627776')
		print('skoSP = -653353807807/549755813888')
		print('skoS2 = -27633740939263/55267481878528')
		exit(0)
	
	
	if pre_condition_140(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_140 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = -3091338895491/1099511627776')
		print('skoSP = -2613415231227/2199023255552')
		print('skoS2 = -110534963757055/221069927514112')
		exit(0)
	
	
	if pre_condition_141(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_141 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = -3091338895491/1099511627776')
		print('skoSP = -2613415231227/2199023255552')
		print('skoS2 = -110534963757055/221069927514112')
		exit(0)
	
	
	if pre_condition_142(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_142 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = -24730711163923/8796093022208')
		print('skoSP = -5226830462455/4398046511104')
		print('skoS2 = -221069927514111/442139855028224')
		exit(0)
	
	
	if pre_condition_143(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_143 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = -24730711163923/8796093022208')
		print('skoSP = -5226830462455/4398046511104')
		print('skoS2 = -221069927514111/442139855028224')
		exit(0)
	
	
	if pre_condition_144(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_144 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = -49461422327843/17592186044416')
		print('skoSP = -10453660924911/8796093022208')
		print('skoS2 = -442139855028223/884279710056448')
		exit(0)
	
	
	if pre_condition_145(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_145 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = -49461422327843/17592186044416')
		print('skoSP = -10453660924911/8796093022208')
		print('skoS2 = -442139855028223/884279710056448')
		exit(0)
	
	
	if pre_condition_146(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_146 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = -98922844655683/35184372088832')
		print('skoSP = -20907321849823/17592186044416')
		print('skoS2 = -884279710056447/1768559420112896')
		exit(0)
	
	
	if pre_condition_147(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_147 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = -98922844655683/35184372088832')
		print('skoSP = -20907321849823/17592186044416')
		print('skoS2 = -884279710056447/1768559420112896')
		exit(0)
	
	
	if pre_condition_148(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_148 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = -98922844655683/35184372088832')
		print('skoSP = -83629287399291/70368744177664')
		print('skoS2 = -3537118840225791/7074237680451584')
		exit(0)
	
	
	if pre_condition_149(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_149 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = -98922844655683/35184372088832')
		print('skoSP = -83629287399291/70368744177664')
		print('skoS2 = -3537118840225791/7074237680451584')
		exit(0)
	
	
	if pre_condition_150(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_150 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = -791382757245459/281474976710656')
		print('skoSP = -167258574798583/140737488355328')
		print('skoS2 = -7074237680451583/14148475360903168')
		exit(0)
	
	
	if pre_condition_151(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_151 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = -791382757245459/281474976710656')
		print('skoSP = -167258574798583/140737488355328')
		print('skoS2 = -7074237680451583/14148475360903168')
		exit(0)
	
	
	if pre_condition_152(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_152 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = -1582765514490915/562949953421312')
		print('skoSP = -334517149597167/281474976710656')
		print('skoS2 = -14148475360903167/28296950721806336')
		exit(0)
	
	
	if pre_condition_153(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_153 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = -1582765514490915/562949953421312')
		print('skoSP = -334517149597167/281474976710656')
		print('skoS2 = -14148475360903167/28296950721806336')
		exit(0)


	print("Weakest pre-condition UNSAT")
	exit(0)
