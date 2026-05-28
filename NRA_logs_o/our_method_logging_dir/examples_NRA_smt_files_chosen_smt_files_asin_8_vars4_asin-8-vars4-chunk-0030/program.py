import sympy
from sympy import *
from NQS.helper_program_cav import get_lambda_val

def pre_condition_0(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(skoS2 > 0) & (skoX > 0) & (skoX - 1 < 0) & (-delta + skoX <= 0) & (delta + skoS2**2 - 2 >= 0) & (-delta + skoS2**2 - 2 <= 0)

	pre_cond = And(StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Add(Symbol('skoX'), Integer(-1)), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Symbol('skoX')), Integer(0)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(skoS2 > 0) & (skoX > 0) & (delta - 2 > 0) & (skoX - 1 < 0) & (delta + skoX - 3 >= 0) & (-delta + skoS2**2 - 2 <= 0)

	pre_cond = And(StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictGreaterThan(Add(Symbol('delta'), Integer(-2)), Integer(0)), StrictLessThan(Add(Symbol('skoX'), Integer(-1)), Integer(0)), GreaterThan(Add(Symbol('delta'), Symbol('skoX'), Integer(-3)), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX - 1 < 0) & (delta + skoS2**2 - 2 >= 0) & (4*delta + 4*skoX - 3 >= 0) & (-4*delta + 4*skoX - 3 <= 0) & (-delta + skoS2**2 - 2 <= 0)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Add(Symbol('skoX'), Integer(-1)), Integer(0)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), GreaterThan(Add(Mul(Integer(4), Symbol('delta')), Mul(Integer(4), Symbol('skoX')), Integer(-3)), Integer(0)), LessThan(Add(Mul(Integer(-1), Integer(4), Symbol('delta')), Mul(Integer(4), Symbol('skoX')), Integer(-3)), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta > 0) & (skoS2 > 0) & (skoX > 0) & (skoX - 1 < 0) & (delta + skoS2**2 - 2 >= 0) & (4*delta + 4*skoX - 5 >= 0) & (-delta + skoS2**2 - 2 <= 0)

	pre_cond = And(StrictGreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Add(Symbol('skoX'), Integer(-1)), Integer(0)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), GreaterThan(Add(Mul(Integer(4), Symbol('delta')), Mul(Integer(4), Symbol('skoX')), Integer(-5)), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_4(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX - 1 < 0) & (delta + skoS2**2 - 2 >= 0) & (16*delta + 16*skoX - 7 >= 0) & (-16*delta + 16*skoX - 7 <= 0) & (-delta + skoS2**2 - 2 <= 0)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Add(Symbol('skoX'), Integer(-1)), Integer(0)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), GreaterThan(Add(Mul(Integer(16), Symbol('delta')), Mul(Integer(16), Symbol('skoX')), Integer(-7)), Integer(0)), LessThan(Add(Mul(Integer(-1), Integer(16), Symbol('delta')), Mul(Integer(16), Symbol('skoX')), Integer(-7)), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_5(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX - 1 < 0) & (delta + skoS2**2 - 2 >= 0) & (16*delta + 16*skoX - 9 >= 0) & (-16*delta + 16*skoX - 9 <= 0) & (-delta + skoS2**2 - 2 <= 0)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Add(Symbol('skoX'), Integer(-1)), Integer(0)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), GreaterThan(Add(Mul(Integer(16), Symbol('delta')), Mul(Integer(16), Symbol('skoX')), Integer(-9)), Integer(0)), LessThan(Add(Mul(Integer(-1), Integer(16), Symbol('delta')), Mul(Integer(16), Symbol('skoX')), Integer(-9)), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_6(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX - 1 < 0) & (delta + skoS2**2 - 2 >= 0) & (16*delta + 16*skoX - 15 >= 0) & (-16*delta + 16*skoX - 15 <= 0) & (-delta + skoS2**2 - 2 <= 0)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Add(Symbol('skoX'), Integer(-1)), Integer(0)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), GreaterThan(Add(Mul(Integer(16), Symbol('delta')), Mul(Integer(16), Symbol('skoX')), Integer(-15)), Integer(0)), LessThan(Add(Mul(Integer(-1), Integer(16), Symbol('delta')), Mul(Integer(16), Symbol('skoX')), Integer(-15)), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_7(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX - 1 < 0) & (delta + skoS2**2 - 2 >= 0) & (64*delta + 64*skoX - 57 >= 0) & (-64*delta + 64*skoX - 57 <= 0) & (-delta + skoS2**2 - 2 <= 0)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Add(Symbol('skoX'), Integer(-1)), Integer(0)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), GreaterThan(Add(Mul(Integer(64), Symbol('delta')), Mul(Integer(64), Symbol('skoX')), Integer(-57)), Integer(0)), LessThan(Add(Mul(Integer(-1), Integer(64), Symbol('delta')), Mul(Integer(64), Symbol('skoX')), Integer(-57)), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_8(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX - 1 < 0) & (delta + skoS2**2 - 2 >= 0) & (64*delta + 64*skoX - 63 >= 0) & (-64*delta + 64*skoX - 63 <= 0) & (-delta + skoS2**2 - 2 <= 0)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Add(Symbol('skoX'), Integer(-1)), Integer(0)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), GreaterThan(Add(Mul(Integer(64), Symbol('delta')), Mul(Integer(64), Symbol('skoX')), Integer(-63)), Integer(0)), LessThan(Add(Mul(Integer(-1), Integer(64), Symbol('delta')), Mul(Integer(64), Symbol('skoX')), Integer(-63)), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_9(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX - 1 < 0) & (delta + skoS2**2 - 2 >= 0) & (1024*delta + 1024*skoX - 1001 >= 0) & (-1024*delta + 1024*skoX - 1001 <= 0) & (-delta + skoS2**2 - 2 <= 0)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Add(Symbol('skoX'), Integer(-1)), Integer(0)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), GreaterThan(Add(Mul(Integer(1024), Symbol('delta')), Mul(Integer(1024), Symbol('skoX')), Integer(-1001)), Integer(0)), LessThan(Add(Mul(Integer(-1), Integer(1024), Symbol('delta')), Mul(Integer(1024), Symbol('skoX')), Integer(-1001)), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_10(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX - 1 < 0) & (delta + skoS2**2 - 2 >= 0) & (256*delta + 256*skoX - 255 >= 0) & (-256*delta + 256*skoX - 255 <= 0) & (-delta + skoS2**2 - 2 <= 0)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Add(Symbol('skoX'), Integer(-1)), Integer(0)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), GreaterThan(Add(Mul(Integer(256), Symbol('delta')), Mul(Integer(256), Symbol('skoX')), Integer(-255)), Integer(0)), LessThan(Add(Mul(Integer(-1), Integer(256), Symbol('delta')), Mul(Integer(256), Symbol('skoX')), Integer(-255)), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_11(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX - 1 < 0) & (delta + skoS2**2 - 2 >= 0) & (16384*delta + 16384*skoX - 16377 >= 0) & (-16384*delta + 16384*skoX - 16377 <= 0) & (-delta + skoS2**2 - 2 <= 0)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Add(Symbol('skoX'), Integer(-1)), Integer(0)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), GreaterThan(Add(Mul(Integer(16384), Symbol('delta')), Mul(Integer(16384), Symbol('skoX')), Integer(-16377)), Integer(0)), LessThan(Add(Mul(Integer(-1), Integer(16384), Symbol('delta')), Mul(Integer(16384), Symbol('skoX')), Integer(-16377)), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_12(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX - 1 < 0) & (delta + skoS2**2 - 2 >= 0) & (4096*delta + 4096*skoX - 4095 >= 0) & (-4096*delta + 4096*skoX - 4095 <= 0) & (-delta + skoS2**2 - 2 <= 0)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Add(Symbol('skoX'), Integer(-1)), Integer(0)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), GreaterThan(Add(Mul(Integer(4096), Symbol('delta')), Mul(Integer(4096), Symbol('skoX')), Integer(-4095)), Integer(0)), LessThan(Add(Mul(Integer(-1), Integer(4096), Symbol('delta')), Mul(Integer(4096), Symbol('skoX')), Integer(-4095)), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_13(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta > 0) & (skoS2 > 0) & (skoX > 0) & (skoX - 1 < 0) & (delta + skoS2**2 - 2 >= 0) & (16777216*delta + 16777216*skoX - 16781633 >= 0) & (-delta + skoS2**2 - 2 <= 0)

	pre_cond = And(StrictGreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Add(Symbol('skoX'), Integer(-1)), Integer(0)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), GreaterThan(Add(Mul(Integer(16777216), Symbol('delta')), Mul(Integer(16777216), Symbol('skoX')), Integer(-16781633)), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_14(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX - 1 < 0) & (delta + skoS2**2 - 2 >= 0) & (16384*delta + 16384*skoX - 16383 >= 0) & (-16384*delta + 16384*skoX - 16383 <= 0) & (-delta + skoS2**2 - 2 <= 0)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Add(Symbol('skoX'), Integer(-1)), Integer(0)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), GreaterThan(Add(Mul(Integer(16384), Symbol('delta')), Mul(Integer(16384), Symbol('skoX')), Integer(-16383)), Integer(0)), LessThan(Add(Mul(Integer(-1), Integer(16384), Symbol('delta')), Mul(Integer(16384), Symbol('skoX')), Integer(-16383)), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_15(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX - 1 < 0) & (delta + skoS2**2 - 2 >= 0) & (67108864*delta + 67108864*skoX - 67103361 >= 0) & (-67108864*delta + 67108864*skoX - 67103361 <= 0) & (-delta + skoS2**2 - 2 <= 0)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Add(Symbol('skoX'), Integer(-1)), Integer(0)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), GreaterThan(Add(Mul(Integer(67108864), Symbol('delta')), Mul(Integer(67108864), Symbol('skoX')), Integer(-67103361)), Integer(0)), LessThan(Add(Mul(Integer(-1), Integer(67108864), Symbol('delta')), Mul(Integer(67108864), Symbol('skoX')), Integer(-67103361)), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_16(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX - 1 < 0) & (delta + skoS2**2 - 2 >= 0) & (65536*delta + 65536*skoX - 65535 >= 0) & (-65536*delta + 65536*skoX - 65535 <= 0) & (-delta + skoS2**2 - 2 <= 0)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Add(Symbol('skoX'), Integer(-1)), Integer(0)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), GreaterThan(Add(Mul(Integer(65536), Symbol('delta')), Mul(Integer(65536), Symbol('skoX')), Integer(-65535)), Integer(0)), LessThan(Add(Mul(Integer(-1), Integer(65536), Symbol('delta')), Mul(Integer(65536), Symbol('skoX')), Integer(-65535)), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_17(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta > 0) & (skoS2 > 0) & (skoX > 0) & (skoX - 1 < 0) & (delta + skoS2**2 - 2 >= 0) & (1073741824*delta + 1073741824*skoX - 1073746457 >= 0) & (-delta + skoS2**2 - 2 <= 0)

	pre_cond = And(StrictGreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Add(Symbol('skoX'), Integer(-1)), Integer(0)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), GreaterThan(Add(Mul(Integer(1073741824), Symbol('delta')), Mul(Integer(1073741824), Symbol('skoX')), Integer(-1073746457)), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(delta:sympy.Rational, skoX:sympy.Rational, skoS2:sympy.Rational, skoSP:sympy.Rational, skoSM:sympy.Rational):
	# (0 <= delta) & (1 > skoX) & (skoS2 > 0) & (skoSM > 0) & (skoSP > 0) & (skoX > 0) & (skoS2**2 - 2 <= delta) & (skoSM**2 + skoX - 1 <= delta) & (2 - skoS2**2 <= delta) & (-skoSP**2 + skoX + 1 <= delta) & (skoSP**2 - skoX - 1 <= delta) & (-skoSM**2 - skoX + 1 <= delta) & (skoSP*(-63*skoS2/20 - 13/8) <= skoSM*(-63*skoS2/20 - 61/40) + 1/5)

	post_cond =  And(LessThan(Integer(0), Symbol('delta')), StrictGreaterThan(Integer(1), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoSP'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), LessThan(Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Symbol('delta')), LessThan(Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1)), Symbol('delta')), LessThan(Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Symbol('delta')), LessThan(Add(Mul(Integer(-1), Pow(Symbol('skoSP'), Integer(2))), Symbol('skoX'), Integer(1)), Symbol('delta')), LessThan(Add(Pow(Symbol('skoSP'), Integer(2)), Mul(Integer(-1), Symbol('skoX')), Integer(-1)), Symbol('delta')), LessThan(Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)), Symbol('delta')), LessThan(Mul(Symbol('skoSP'), Add(Mul(Integer(-1), Rational(63, 20), Symbol('skoS2')), Rational(-13, 8))), Add(Mul(Symbol('skoSM'), Add(Mul(Integer(-1), Rational(63, 20), Symbol('skoS2')), Rational(-61, 40))), Rational(1, 5))))

	eval = post_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'skoSP':skoSP, 'skoSM':skoSM })

	return eval == sympy.logic.boolalg.BooleanTrue



#return post-condition single variable
def return_post_condition_single_var(post_condition, delta:sympy.Rational=None, skoX:sympy.Rational=None, skoS2:sympy.Rational=None, skoSP:sympy.Rational=None, skoSM:sympy.Rational=None):
	assert delta!=None
	assert skoX!=None
	assert skoS2!=None


	if skoSP==None:
		assert skoSM!=None
		return lambda skoSP: post_condition(delta=delta, skoX=skoX, skoS2=skoS2, skoSP=skoSP, skoSM=skoSM)

	if skoSM==None:
		assert skoSP!=None
		return lambda skoSM: post_condition(delta=delta, skoX=skoX, skoS2=skoS2, skoSP=skoSP, skoSM=skoSM)


	return post_condition(delta=delta, skoX=skoX, skoS2=skoS2, skoSP=skoSP, skoSM=skoSM)


def get_univariate_poly( delta:sympy.Rational, skoX:sympy.Rational, skoS2:sympy.Rational, skoSP:sympy.Rational, skoSM:sympy.Rational ):


	post_cond =  And(LessThan(Integer(0), Symbol('delta')), StrictGreaterThan(Integer(1), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoSP'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), LessThan(Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Symbol('delta')), LessThan(Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1)), Symbol('delta')), LessThan(Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Symbol('delta')), LessThan(Add(Mul(Integer(-1), Pow(Symbol('skoSP'), Integer(2))), Symbol('skoX'), Integer(1)), Symbol('delta')), LessThan(Add(Pow(Symbol('skoSP'), Integer(2)), Mul(Integer(-1), Symbol('skoX')), Integer(-1)), Symbol('delta')), LessThan(Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)), Symbol('delta')), LessThan(Mul(Symbol('skoSP'), Add(Mul(Integer(-1), Rational(63, 20), Symbol('skoS2')), Rational(-13, 8))), Add(Mul(Symbol('skoSM'), Add(Mul(Integer(-1), Rational(63, 20), Symbol('skoS2')), Rational(-61, 40))), Rational(1, 5))))

	eval = post_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'skoSP':skoSP, 'skoSM':skoSM })
	return eval



if __name__=="__main__":
	
	ip_0=int(input("enter numerator of delta:\n"))
	ip_1=int(input("enter denominator of delta:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	delta=sympy.Rational(ip_0,ip_1)
	
	
	ip_0=int(input("enter numerator of skoX:\n"))
	ip_1=int(input("enter denominator of skoX:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	skoX=sympy.Rational(ip_0,ip_1)
	
	
	ip_0=int(input("enter numerator of skoS2:\n"))
	ip_1=int(input("enter denominator of skoS2:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	skoS2=sympy.Rational(ip_0,ip_1)
	
	
	lambda_var_0 = sympy.symbols('lambda_var_0')
	
	
	if pre_condition_0(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Integer(2))
		all_vals['skoSM'] = Integer(1)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_0 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_1(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Integer(2)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Integer(1))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_1 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_2(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(3, 2))
		all_vals['skoSM'] = Rational(1, 2)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_2 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_3(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Rational(3, 2)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(1, 2))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_3 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_4(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(5, 4))
		all_vals['skoSM'] = Rational(3, 4)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_4 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_5(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Rational(5, 4)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(3, 4))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_5 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_6(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(11, 8))
		all_vals['skoSM'] = Rational(1, 4)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_6 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_7(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Rational(11, 8)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(1, 4))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_7 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_8(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(45, 32))
		all_vals['skoSM'] = Rational(1, 8)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_8 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_9(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Rational(45, 32)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(1, 8))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_9 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_10(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(181, 128))
		all_vals['skoSM'] = Rational(1, 16)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_10 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_11(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Rational(181, 128)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(1, 16))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_11 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_12(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(5793, 4096))
		all_vals['skoSM'] = Rational(1, 64)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_12 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_13(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Rational(5793, 4096)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(1, 64))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_13 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_14(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(11585, 8192))
		all_vals['skoSM'] = Rational(1, 128)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_14 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_15(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Rational(11585, 8192)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(1, 128))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_15 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_16(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(46341, 32768))
		all_vals['skoSM'] = Rational(1, 256)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_16 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_17(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Rational(46341, 32768)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(1, 256))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_17 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass


	print("UNKNOWN")
