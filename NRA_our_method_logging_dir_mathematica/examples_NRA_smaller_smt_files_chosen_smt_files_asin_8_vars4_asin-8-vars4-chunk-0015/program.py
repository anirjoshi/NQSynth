import sympy
from sympy import *
from NQS.helper_program_cav import get_lambda_val

def pre_condition_0(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta > 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoS2**2 >= 2) & (delta - skoX >= 0) & (delta - skoS2**2 >= -2)

	pre_cond = And(StrictGreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(0)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta > 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoS2**2 >= 2) & (delta - skoX >= 0) & (delta - skoS2**2 >= -2)

	pre_cond = And(StrictGreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(0)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 3/4) & (delta + skoS2**2 >= 2) & (delta - skoX >= -3/4) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(3, 4)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-3, 4)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 5/4) & (delta + skoS2**2 >= 2) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(5, 4)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_4(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 15/16) & (delta + skoS2**2 >= 2) & (delta - skoX >= -15/16) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(15, 16)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-15, 16)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_5(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 57/64) & (delta + skoS2**2 >= 2) & (delta - skoX >= -57/64) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(57, 64)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-57, 64)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_6(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 231/256) & (delta + skoS2**2 >= 2) & (delta - skoX >= -231/256) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(231, 256)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-231, 256)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_7(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 3825/4096) & (delta + skoS2**2 >= 2) & (delta - skoX >= -3825/4096) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(3825, 4096)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-3825, 4096)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_8(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 7/16) & (delta + skoS2**2 >= 2) & (delta - skoX >= -7/16) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(7, 16)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-7, 16)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_9(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 9/16) & (delta + skoS2**2 >= 2) & (delta - skoX >= -9/16) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(9, 16)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-9, 16)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_10(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 63/64) & (delta + skoS2**2 >= 2) & (delta - skoX >= -63/64) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(63, 64)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-63, 64)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_11(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 1001/1024) & (delta + skoS2**2 >= 2) & (delta - skoX >= -1001/1024) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(1001, 1024)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-1001, 1024)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_12(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 4015/4096) & (delta + skoS2**2 >= 2) & (delta - skoX >= -4015/4096) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(4015, 4096)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-4015, 4096)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_13(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 257697/262144) & (delta + skoS2**2 >= 2) & (delta - skoX >= -257697/262144) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(257697, 262144)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-257697, 262144)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_14(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 255/256) & (delta + skoS2**2 >= 2) & (delta - skoX >= -255/256) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(255, 256)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-255, 256)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_15(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 16377/16384) & (delta + skoS2**2 >= 2) & (delta - skoX >= -16377/16384) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(16377, 16384)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-16377, 16384)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_16(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 247/256) & (delta + skoS2**2 >= 2) & (delta - skoX >= -247/256) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(247, 256)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-247, 256)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_17(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 15657/16384) & (delta + skoS2**2 >= 2) & (delta - skoX >= -15657/16384) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(15657, 16384)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-15657, 16384)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_18(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 3927/4096) & (delta + skoS2**2 >= 2) & (delta - skoX >= -3927/4096) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(3927, 4096)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-3927, 4096)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_19(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 251945/262144) & (delta + skoS2**2 >= 2) & (delta - skoX >= -251945/262144) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(251945, 262144)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-251945, 262144)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_20(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 16095/16384) & (delta + skoS2**2 >= 2) & (delta - skoX >= -16095/16384) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(16095, 16384)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-16095, 16384)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_21(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 1027905/1048576) & (delta + skoS2**2 >= 2) & (delta - skoX >= -1027905/1048576) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(1027905, 1048576)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-1027905, 1048576)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_22(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 64447/65536) & (delta + skoS2**2 >= 2) & (delta - skoX >= -64447/65536) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(64447, 65536)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-64447, 65536)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_23(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 257697/262144) & (delta + skoS2**2 >= 2) & (delta - skoX >= -257697/262144) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(257697, 262144)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-257697, 262144)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_24(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 1015/1024) & (delta + skoS2**2 >= 2) & (delta - skoX >= -1015/1024) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(1015, 1024)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-1015, 1024)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_25(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 64785/65536) & (delta + skoS2**2 >= 2) & (delta - skoX >= -64785/65536) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(64785, 65536)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-64785, 65536)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_26(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 1023/1024) & (delta + skoS2**2 >= 2) & (delta - skoX >= -1023/1024) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(1023, 1024)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-1023, 1024)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_27(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 1045233/1048576) & (delta + skoS2**2 >= 2) & (delta - skoX >= -1045233/1048576) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(1045233, 1048576)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-1045233, 1048576)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_28(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 4095/4096) & (delta + skoS2**2 >= 2) & (delta - skoX >= -4095/4096) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(4095, 4096)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-4095, 4096)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_29(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 16781633/16777216) & (delta + skoS2**2 >= 2) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(16781633, 16777216)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_30(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 975/1024) & (delta + skoS2**2 >= 2) & (delta - skoX >= -975/1024) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(975, 1024)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-975, 1024)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_31(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 61913/65536) & (delta + skoS2**2 >= 2) & (delta - skoX >= -61913/65536) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(61913, 65536)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-61913, 65536)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_32(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 3871/4096) & (delta + skoS2**2 >= 2) & (delta - skoX >= -3871/4096) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(3871, 4096)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-3871, 4096)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_33(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 249081/262144) & (delta + skoS2**2 >= 2) & (delta - skoX >= -249081/262144) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(249081, 262144)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-249081, 262144)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_34(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 62935/65536) & (delta + skoS2**2 >= 2) & (delta - skoX >= -62935/65536) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(62935, 65536)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-62935, 65536)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_35(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 4025385/4194304) & (delta + skoS2**2 >= 2) & (delta - skoX >= -4025385/4194304) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(4025385, 4194304)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-4025385, 4194304)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_36(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 15759/16384) & (delta + skoS2**2 >= 2) & (delta - skoX >= -15759/16384) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(15759, 16384)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-15759, 16384)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_37(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 251945/262144) & (delta + skoS2**2 >= 2) & (delta - skoX >= -251945/262144) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(251945, 262144)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-251945, 262144)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_38(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 64311/65536) & (delta + skoS2**2 >= 2) & (delta - skoX >= -64311/65536) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(64311, 65536)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-64311, 65536)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_39(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 1027905/1048576) & (delta + skoS2**2 >= 2) & (delta - skoX >= -1027905/1048576) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(1027905, 1048576)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-1027905, 1048576)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_40(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 257655/262144) & (delta + skoS2**2 >= 2) & (delta - skoX >= -257655/262144) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(257655, 262144)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-257655, 262144)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_41(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 65947361/67108864) & (delta + skoS2**2 >= 2) & (delta - skoX >= -65947361/67108864) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(65947361, 67108864)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-65947361, 67108864)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_42(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 1030887/1048576) & (delta + skoS2**2 >= 2) & (delta - skoX >= -1030887/1048576) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(1030887, 1048576)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-1030887, 1048576)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_43(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 257697/262144) & (delta + skoS2**2 >= 2) & (delta - skoX >= -257697/262144) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(257697, 262144)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-257697, 262144)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_44(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 257919/262144) & (delta + skoS2**2 >= 2) & (delta - skoX >= -257919/262144) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(257919, 262144)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-257919, 262144)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_45(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 16504145/16777216) & (delta + skoS2**2 >= 2) & (delta - skoX >= -16504145/16777216) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(16504145, 16777216)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-16504145, 16777216)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_46(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 16215/16384) & (delta + skoS2**2 >= 2) & (delta - skoX >= -16215/16384) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(16215, 16384)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-16215, 16384)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_47(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 4152017/4194304) & (delta + skoS2**2 >= 2) & (delta - skoX >= -4152017/4194304) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(4152017, 4194304)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-4152017, 4194304)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_48(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 4071/4096) & (delta + skoS2**2 >= 2) & (delta - skoX >= -4071/4096) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(4071, 4096)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-4071, 4096)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_49(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 260585/262144) & (delta + skoS2**2 >= 2) & (delta - skoX >= -260585/262144) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(260585, 262144)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-260585, 262144)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_50(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 4087/4096) & (delta + skoS2**2 >= 2) & (delta - skoX >= -4087/4096) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(4087, 4096)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-4087, 4096)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_51(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 1045233/1048576) & (delta + skoS2**2 >= 2) & (delta - skoX >= -1045233/1048576) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(1045233, 1048576)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-1045233, 1048576)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_52(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 16375/16384) & (delta + skoS2**2 >= 2) & (delta - skoX >= -16375/16384) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(16375, 16384)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-16375, 16384)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_53(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 67057025/67108864) & (delta + skoS2**2 >= 2) & (delta - skoX >= -67057025/67108864) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(67057025, 67108864)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-67057025, 67108864)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_54(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 65511/65536) & (delta + skoS2**2 >= 2) & (delta - skoX >= -65511/65536) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(65511, 65536)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-65511, 65536)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_55(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 268367105/268435456) & (delta + skoS2**2 >= 2) & (delta - skoX >= -268367105/268435456) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(268367105, 268435456)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-268367105, 268435456)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_56(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 16383/16384) & (delta + skoS2**2 >= 2) & (delta - skoX >= -16383/16384) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(16383, 16384)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-16383, 16384)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_57(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 67103361/67108864) & (delta + skoS2**2 >= 2) & (delta - skoX >= -67103361/67108864) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(67103361, 67108864)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-67103361, 67108864)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_58(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 15423/16384) & (delta + skoS2**2 >= 2) & (delta - skoX >= -15423/16384) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(15423, 16384)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-15423, 16384)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_59(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 246225/262144) & (delta + skoS2**2 >= 2) & (delta - skoX >= -246225/262144) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(246225, 262144)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-246225, 262144)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_60(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 61815/65536) & (delta + skoS2**2 >= 2) & (delta - skoX >= -61815/65536) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(61815, 65536)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-61815, 65536)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_61(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 987753/1048576) & (delta + skoS2**2 >= 2) & (delta - skoX >= -987753/1048576) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(987753, 1048576)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-987753, 1048576)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_62(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 247503/262144) & (delta + skoS2**2 >= 2) & (delta - skoX >= -247503/262144) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(247503, 262144)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-247503, 262144)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_63(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 3956721/4194304) & (delta + skoS2**2 >= 2) & (delta - skoX >= -3956721/4194304) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(3956721, 4194304)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-3956721, 4194304)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_64(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 990495/1048576) & (delta + skoS2**2 >= 2) & (delta - skoX >= -990495/1048576) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(990495, 1048576)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-990495, 1048576)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_65(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 63376065/67108864) & (delta + skoS2**2 >= 2) & (delta - skoX >= -63376065/67108864) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(63376065, 67108864)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-63376065, 67108864)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_66(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 63395535/67108864) & (delta + skoS2**2 >= 2) & (delta - skoX >= -63395535/67108864) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(63395535, 67108864)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-63395535, 67108864)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_67(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 1014291201/1073741824) & (delta + skoS2**2 >= 2) & (delta - skoX >= -1014291201/1073741824) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(1014291201, 1073741824)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-1014291201, 1073741824)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_68(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 253589847/268435456) & (delta + skoS2**2 >= 2) & (delta - skoX >= -253589847/268435456) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(253589847, 268435456)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-253589847, 268435456)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_69(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 4057347585/4294967296) & (delta + skoS2**2 >= 2) & (delta - skoX >= -4057347585/4294967296) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(4057347585, 4294967296)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-4057347585, 4294967296)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_70(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 253589847/268435456) & (delta + skoS2**2 >= 2) & (delta - skoX >= -253589847/268435456) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(253589847, 268435456)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-253589847, 268435456)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_71(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 16229755905/17179869184) & (delta + skoS2**2 >= 2) & (delta - skoX >= -16229755905/17179869184) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(16229755905, 17179869184)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-16229755905, 17179869184)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_72(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 1014374799/1073741824) & (delta + skoS2**2 >= 2) & (delta - skoX >= -1014374799/1073741824) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(1014374799, 1073741824)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-1014374799, 1073741824)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_73(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 16229755905/17179869184) & (delta + skoS2**2 >= 2) & (delta - skoX >= -16229755905/17179869184) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(16229755905, 17179869184)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-16229755905, 17179869184)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_74(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 1014374799/1073741824) & (delta + skoS2**2 >= 2) & (delta - skoX >= -1014374799/1073741824) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(1014374799, 1073741824)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-1014374799, 1073741824)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_75(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 259680481281/274877906944) & (delta + skoS2**2 >= 2) & (delta - skoX >= -259680481281/274877906944) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(259680481281, 274877906944)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-259680481281, 274877906944)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_76(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 4057530015/4294967296) & (delta + skoS2**2 >= 2) & (delta - skoX >= -4057530015/4294967296) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(4057530015, 4294967296)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-4057530015, 4294967296)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_77(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 1038724849665/1099511627776) & (delta + skoS2**2 >= 2) & (delta - skoX >= -1038724849665/1099511627776) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(1038724849665, 1099511627776)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-1038724849665, 1099511627776)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_78(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 66478575710463/70368744177664) & (delta + skoS2**2 >= 2) & (delta - skoX >= -66478575710463/70368744177664) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(66478575710463, 70368744177664)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-66478575710463, 70368744177664)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_79(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 4254628775985153/4503599627370496) & (delta + skoS2**2 >= 2) & (delta - skoX >= -4254628775985153/4503599627370496) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(4254628775985153, 4503599627370496)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-4254628775985153, 4503599627370496)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_80(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 66478575710463/70368744177664) & (delta + skoS2**2 >= 2) & (delta - skoX >= -66478575710463/70368744177664) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(66478575710463, 70368744177664)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-66478575710463, 70368744177664)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_81(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 17018515478282241/18014398509481984) & (delta + skoS2**2 >= 2) & (delta - skoX >= -17018515478282241/18014398509481984) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(17018515478282241, 18014398509481984)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-17018515478282241, 18014398509481984)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_82(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 1063657227146215/1125899906842624) & (delta + skoS2**2 >= 2) & (delta - skoX >= -1063657227146215/1125899906842624) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(1063657227146215, 1125899906842624)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-1063657227146215, 1125899906842624)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_83(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 17018515478282241/18014398509481984) & (delta + skoS2**2 >= 2) & (delta - skoX >= -17018515478282241/18014398509481984) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(17018515478282241, 18014398509481984)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-17018515478282241, 18014398509481984)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_84(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 4254628940142471/4503599627370496) & (delta + skoS2**2 >= 2) & (delta - skoX >= -4254628940142471/4503599627370496) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(4254628940142471, 4503599627370496)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-4254628940142471, 4503599627370496)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_85(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 68074062661812225/72057594037927936) & (delta + skoS2**2 >= 2) & (delta - skoX >= -68074062661812225/72057594037927936) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(68074062661812225, 72057594037927936)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-68074062661812225, 72057594037927936)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_86(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 17018515823685103/18014398509481984) & (delta + skoS2**2 >= 2) & (delta - skoX >= -17018515823685103/18014398509481984) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(17018515823685103, 18014398509481984)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-17018515823685103, 18014398509481984)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_87(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 1089185011573194753/1152921504606846976) & (delta + skoS2**2 >= 2) & (delta - skoX >= -1089185011573194753/1152921504606846976) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(1089185011573194753, 1152921504606846976)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-1089185011573194753, 1152921504606846976)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_88(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 272296253431422519/288230376151711744) & (delta + skoS2**2 >= 2) & (delta - skoX >= -272296253431422519/288230376151711744) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(272296253431422519, 288230376151711744)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-272296253431422519, 288230376151711744)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_89(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 4356740052282245121/4611686018427387904) & (delta + skoS2**2 >= 2) & (delta - skoX >= -4356740052282245121/4611686018427387904) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(4356740052282245121, 4611686018427387904)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-4356740052282245121, 4611686018427387904)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_90(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 272296253431422519/288230376151711744) & (delta + skoS2**2 >= 2) & (delta - skoX >= -272296253431422519/288230376151711744) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(272296253431422519, 288230376151711744)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-272296253431422519, 288230376151711744)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_91(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 17426960221107912705/18446744073709551616) & (delta + skoS2**2 >= 2) & (delta - skoX >= -17426960221107912705/18446744073709551616) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(17426960221107912705, 18446744073709551616)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-17426960221107912705, 18446744073709551616)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_92(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 1089185014230611815/1152921504606846976) & (delta + skoS2**2 >= 2) & (delta - skoX >= -1089185014230611815/1152921504606846976) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(1089185014230611815, 1152921504606846976)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-1089185014230611815, 1152921504606846976)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_93(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 69707840908389515265/73786976294838206464) & (delta + skoS2**2 >= 2) & (delta - skoX >= -69707840908389515265/73786976294838206464) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(69707840908389515265, 73786976294838206464)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-69707840908389515265, 73786976294838206464)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_94(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 1089185014230611815/1152921504606846976) & (delta + skoS2**2 >= 2) & (delta - skoX >= -1089185014230611815/1152921504606846976) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(1089185014230611815, 1152921504606846976)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-1089185014230611815, 1152921504606846976)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_95(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 278831363681473789953/295147905179352825856) & (delta + skoS2**2 >= 2) & (delta - skoX >= -278831363681473789953/295147905179352825856) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(278831363681473789953, 295147905179352825856)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-278831363681473789953, 295147905179352825856)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_96(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 4356740057932290735/4611686018427387904) & (delta + skoS2**2 >= 2) & (delta - skoX >= -4356740057932290735/4611686018427387904) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(4356740057932290735, 4611686018427387904)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-4356740057932290735, 4611686018427387904)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_97(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 1115325454821726617601/1180591620717411303424) & (delta + skoS2**2 >= 2) & (delta - skoX >= -1115325454821726617601/1180591620717411303424) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(1115325454821726617601, 1180591620717411303424)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-1115325454821726617601, 1180591620717411303424)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_98(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 4356740057932290735/4611686018427387904) & (delta + skoS2**2 >= 2) & (delta - skoX >= -4356740057932290735/4611686018427387904) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(4356740057932290735, 4611686018427387904)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-4356740057932290735, 4611686018427387904)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_99(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 4461301819478569385985/4722366482869645213696) & (delta + skoS2**2 >= 2) & (delta - skoX >= -4461301819478569385985/4722366482869645213696) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(4461301819478569385985, 4722366482869645213696)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-4461301819478569385985, 4722366482869645213696)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_100(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 69707840930956025655/73786976294838206464) & (delta + skoS2**2 >= 2) & (delta - skoX >= -69707840930956025655/73786976294838206464) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(69707840930956025655, 73786976294838206464)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-69707840930956025655, 73786976294838206464)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_101(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 17845207278297603375105/18889465931478580854784) & (delta + skoS2**2 >= 2) & (delta - skoX >= -17845207278297603375105/18889465931478580854784) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(17845207278297603375105, 18889465931478580854784)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-17845207278297603375105, 18889465931478580854784)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_102(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 69707840930956025655/73786976294838206464) & (delta + skoS2**2 >= 2) & (delta - skoX >= -69707840930956025655/73786976294838206464) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(69707840930956025655, 73786976294838206464)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-69707840930956025655, 73786976294838206464)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_103(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 71380829113957065162753/75557863725914323419136) & (delta + skoS2**2 >= 2) & (delta - skoX >= -71380829113957065162753/75557863725914323419136) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(71380829113957065162753, 75557863725914323419136)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-71380829113957065162753, 75557863725914323419136)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_104(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 1115325454911453906055/1180591620717411303424) & (delta + skoS2**2 >= 2) & (delta - skoX >= -1115325454911453906055/1180591620717411303424) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(1115325454911453906055, 1180591620717411303424)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-1115325454911453906055, 1180591620717411303424)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_105(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 285523316457361563975681/302231454903657293676544) & (delta + skoS2**2 >= 2) & (delta - skoX >= -285523316457361563975681/302231454903657293676544) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(285523316457361563975681, 302231454903657293676544)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-285523316457361563975681, 302231454903657293676544)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_106(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 17845207278647892479175/18889465931478580854784) & (delta + skoS2**2 >= 2) & (delta - skoX >= -17845207278647892479175/18889465931478580854784) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(17845207278647892479175, 18889465931478580854784)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-17845207278647892479175, 18889465931478580854784)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_107(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 285523316457361563975681/302231454903657293676544) & (delta + skoS2**2 >= 2) & (delta - skoX >= -285523316457361563975681/302231454903657293676544) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(285523316457361563975681, 302231454903657293676544)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-285523316457361563975681, 302231454903657293676544)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_108(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 71380829114720829881287/75557863725914323419136) & (delta + skoS2**2 >= 2) & (delta - skoX >= -71380829114720829881287/75557863725914323419136) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(71380829114720829881287, 75557863725914323419136)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-71380829114720829881287, 75557863725914323419136)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_109(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 4568373063336184663506945/4835703278458516698824704) & (delta + skoS2**2 >= 2) & (delta - skoX >= -4568373063336184663506945/4835703278458516698824704) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(4568373063336184663506945, 4835703278458516698824704)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-4568373063336184663506945, 4835703278458516698824704)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_110(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 292375876053904791831485055/309485009821345068724781056) & (delta + skoS2**2 >= 2) & (delta - skoX >= -292375876053904791831485055/309485009821345068724781056) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(292375876053904791831485055, 309485009821345068724781056)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-292375876053904791831485055, 309485009821345068724781056)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_111(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 18712056067449741497744752641/19807040628566084398385987584) & (delta + skoS2**2 >= 2) & (delta - skoX >= -18712056067449741497744752641/19807040628566084398385987584) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(18712056067449741497744752641, 19807040628566084398385987584)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-18712056067449741497744752641, 19807040628566084398385987584)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_112(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 4678014016862509759854694887/4951760157141521099596496896) & (delta + skoS2**2 >= 2) & (delta - skoX >= -4678014016862509759854694887/4951760157141521099596496896) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(4678014016862509759854694887, 4951760157141521099596496896)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-4678014016862509759854694887, 4951760157141521099596496896)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_113(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 74848224269799751042281242625/79228162514264337593543950336) & (delta + skoS2**2 >= 2) & (delta - skoX >= -74848224269799751042281242625/79228162514264337593543950336) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(74848224269799751042281242625, 79228162514264337593543950336)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-74848224269799751042281242625, 79228162514264337593543950336)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_114(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 4678014016862509759854694887/4951760157141521099596496896) & (delta + skoS2**2 >= 2) & (delta - skoX >= -4678014016862509759854694887/4951760157141521099596496896) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(4678014016862509759854694887, 4951760157141521099596496896)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-4678014016862509759854694887, 4951760157141521099596496896)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_115(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 1197571588316805437292126666753/1267650600228229401496703205376) & (delta + skoS2**2 >= 2) & (delta - skoX >= -1197571588316805437292126666753/1267650600228229401496703205376) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(1197571588316805437292126666753, 1267650600228229401496703205376)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-1197571588316805437292126666753, 1267650600228229401496703205376)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_116(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 18712056067450105220520647559/19807040628566084398385987584) & (delta + skoS2**2 >= 2) & (delta - skoX >= -18712056067450105220520647559/19807040628566084398385987584) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(18712056067450105220520647559, 19807040628566084398385987584)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-18712056067450105220520647559, 19807040628566084398385987584)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_117(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 4790286353267228029578924523521/5070602400912917605986812821504) & (delta + skoS2**2 >= 2) & (delta - skoX >= -4790286353267228029578924523521/5070602400912917605986812821504) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(4790286353267228029578924523521, 5070602400912917605986812821504)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-4790286353267228029578924523521, 5070602400912917605986812821504)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_118(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 299392897079201948252737832983/316912650057057350374175801344) & (delta + skoS2**2 >= 2) & (delta - skoX >= -299392897079201948252737832983/316912650057057350374175801344) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(299392897079201948252737832983, 316912650057057350374175801344)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-299392897079201948252737832983, 316912650057057350374175801344)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_119(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 19161145413068924679136533807105/20282409603651670423947251286016) & (delta + skoS2**2 >= 2) & (delta - skoX >= -19161145413068924679136533807105/20282409603651670423947251286016) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(19161145413068924679136533807105, 20282409603651670423947251286016)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-19161145413068924679136533807105, 20282409603651670423947251286016)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_120(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 299392897079201948252737832983/316912650057057350374175801344) & (delta + skoS2**2 >= 2) & (delta - skoX >= -299392897079201948252737832983/316912650057057350374175801344) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(299392897079201948252737832983, 316912650057057350374175801344)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-299392897079201948252737832983, 316912650057057350374175801344)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_121(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 19161145413068924679136533807105/20282409603651670423947251286016) & (delta + skoS2**2 >= 2) & (delta - skoX >= -19161145413068924679136533807105/20282409603651670423947251286016) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(19161145413068924679136533807105, 20282409603651670423947251286016)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-19161145413068924679136533807105, 20282409603651670423947251286016)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_122(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 299392897079201948252737832983/316912650057057350374175801344) & (delta + skoS2**2 >= 2) & (delta - skoX >= -299392897079201948252737832983/316912650057057350374175801344) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(299392897079201948252737832983, 316912650057057350374175801344)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-299392897079201948252737832983, 316912650057057350374175801344)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_123(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 19161145413068924679136533807105/20282409603651670423947251286016) & (delta + skoS2**2 >= 2) & (delta - skoX >= -19161145413068924679136533807105/20282409603651670423947251286016) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(19161145413068924679136533807105, 20282409603651670423947251286016)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-19161145413068924679136533807105, 20282409603651670423947251286016)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_124(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 299392897079201948252737832983/316912650057057350374175801344) & (delta + skoS2**2 >= 2) & (delta - skoX >= -299392897079201948252737832983/316912650057057350374175801344) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(299392897079201948252737832983, 316912650057057350374175801344)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-299392897079201948252737832983, 316912650057057350374175801344)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_125(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 19161145413068924679136533807105/20282409603651670423947251286016) & (delta + skoS2**2 >= 2) & (delta - skoX >= -19161145413068924679136533807105/20282409603651670423947251286016) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(19161145413068924679136533807105, 20282409603651670423947251286016)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-19161145413068924679136533807105, 20282409603651670423947251286016)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_126(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 299392897079201948252737832983/316912650057057350374175801344) & (delta + skoS2**2 >= 2) & (delta - skoX >= -299392897079201948252737832983/316912650057057350374175801344) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(299392897079201948252737832983, 316912650057057350374175801344)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-299392897079201948252737832983, 316912650057057350374175801344)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_127(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 19161145413068924679136533807105/20282409603651670423947251286016) & (delta + skoS2**2 >= 2) & (delta - skoX >= -19161145413068924679136533807105/20282409603651670423947251286016) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(19161145413068924679136533807105, 20282409603651670423947251286016)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-19161145413068924679136533807105, 20282409603651670423947251286016)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_128(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 299392897079201948252737832983/316912650057057350374175801344) & (delta + skoS2**2 >= 2) & (delta - skoX >= -299392897079201948252737832983/316912650057057350374175801344) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(299392897079201948252737832983, 316912650057057350374175801344)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-299392897079201948252737832983, 316912650057057350374175801344)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_129(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 19161145413068924679136533807105/20282409603651670423947251286016) & (delta + skoS2**2 >= 2) & (delta - skoX >= -19161145413068924679136533807105/20282409603651670423947251286016) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(19161145413068924679136533807105, 20282409603651670423947251286016)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-19161145413068924679136533807105, 20282409603651670423947251286016)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_130(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 299392897079201948252737832983/316912650057057350374175801344) & (delta + skoS2**2 >= 2) & (delta - skoX >= -299392897079201948252737832983/316912650057057350374175801344) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(299392897079201948252737832983, 316912650057057350374175801344)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-299392897079201948252737832983, 316912650057057350374175801344)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_131(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 19161145413068924679136533807105/20282409603651670423947251286016) & (delta + skoS2**2 >= 2) & (delta - skoX >= -19161145413068924679136533807105/20282409603651670423947251286016) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(19161145413068924679136533807105, 20282409603651670423947251286016)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-19161145413068924679136533807105, 20282409603651670423947251286016)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_132(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 299392897079201948252737832983/316912650057057350374175801344) & (delta + skoS2**2 >= 2) & (delta - skoX >= -299392897079201948252737832983/316912650057057350374175801344) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(299392897079201948252737832983, 316912650057057350374175801344)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-299392897079201948252737832983, 316912650057057350374175801344)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_133(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 19161145413068924679136533807105/20282409603651670423947251286016) & (delta + skoS2**2 >= 2) & (delta - skoX >= -19161145413068924679136533807105/20282409603651670423947251286016) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(19161145413068924679136533807105, 20282409603651670423947251286016)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-19161145413068924679136533807105, 20282409603651670423947251286016)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_134(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 299392897079201948252737832983/316912650057057350374175801344) & (delta + skoS2**2 >= 2) & (delta - skoX >= -299392897079201948252737832983/316912650057057350374175801344) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(299392897079201948252737832983, 316912650057057350374175801344)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-299392897079201948252737832983, 316912650057057350374175801344)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_135(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 19161145413068924679136533807105/20282409603651670423947251286016) & (delta + skoS2**2 >= 2) & (delta - skoX >= -19161145413068924679136533807105/20282409603651670423947251286016) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(19161145413068924679136533807105, 20282409603651670423947251286016)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-19161145413068924679136533807105, 20282409603651670423947251286016)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_136(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 299392897079201948252737832983/316912650057057350374175801344) & (delta + skoS2**2 >= 2) & (delta - skoX >= -299392897079201948252737832983/316912650057057350374175801344) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(299392897079201948252737832983, 316912650057057350374175801344)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-299392897079201948252737832983, 316912650057057350374175801344)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_137(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 19161145413068924679136533807105/20282409603651670423947251286016) & (delta + skoS2**2 >= 2) & (delta - skoX >= -19161145413068924679136533807105/20282409603651670423947251286016) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(19161145413068924679136533807105, 20282409603651670423947251286016)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-19161145413068924679136533807105, 20282409603651670423947251286016)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_138(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 299392897079201948252737832983/316912650057057350374175801344) & (delta + skoS2**2 >= 2) & (delta - skoX >= -299392897079201948252737832983/316912650057057350374175801344) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(299392897079201948252737832983, 316912650057057350374175801344)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-299392897079201948252737832983, 316912650057057350374175801344)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_139(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 19161145413068924679136533807105/20282409603651670423947251286016) & (delta + skoS2**2 >= 2) & (delta - skoX >= -19161145413068924679136533807105/20282409603651670423947251286016) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(19161145413068924679136533807105, 20282409603651670423947251286016)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-19161145413068924679136533807105, 20282409603651670423947251286016)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_140(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 299392897079201948252737832983/316912650057057350374175801344) & (delta + skoS2**2 >= 2) & (delta - skoX >= -299392897079201948252737832983/316912650057057350374175801344) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(299392897079201948252737832983, 316912650057057350374175801344)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-299392897079201948252737832983, 316912650057057350374175801344)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_141(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 19161145413068924679136533807105/20282409603651670423947251286016) & (delta + skoS2**2 >= 2) & (delta - skoX >= -19161145413068924679136533807105/20282409603651670423947251286016) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(19161145413068924679136533807105, 20282409603651670423947251286016)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-19161145413068924679136533807105, 20282409603651670423947251286016)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_142(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 299392897079201948252737832983/316912650057057350374175801344) & (delta + skoS2**2 >= 2) & (delta - skoX >= -299392897079201948252737832983/316912650057057350374175801344) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(299392897079201948252737832983, 316912650057057350374175801344)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-299392897079201948252737832983, 316912650057057350374175801344)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_143(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 19161145413068924679136533807105/20282409603651670423947251286016) & (delta + skoS2**2 >= 2) & (delta - skoX >= -19161145413068924679136533807105/20282409603651670423947251286016) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(19161145413068924679136533807105, 20282409603651670423947251286016)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-19161145413068924679136533807105, 20282409603651670423947251286016)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_144(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 299392897079201948252737832983/316912650057057350374175801344) & (delta + skoS2**2 >= 2) & (delta - skoX >= -299392897079201948252737832983/316912650057057350374175801344) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(299392897079201948252737832983, 316912650057057350374175801344)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-299392897079201948252737832983, 316912650057057350374175801344)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_145(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 19161145413068924679136533807105/20282409603651670423947251286016) & (delta + skoS2**2 >= 2) & (delta - skoX >= -19161145413068924679136533807105/20282409603651670423947251286016) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(19161145413068924679136533807105, 20282409603651670423947251286016)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-19161145413068924679136533807105, 20282409603651670423947251286016)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_146(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 299392897079201948252737832983/316912650057057350374175801344) & (delta + skoS2**2 >= 2) & (delta - skoX >= -299392897079201948252737832983/316912650057057350374175801344) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(299392897079201948252737832983, 316912650057057350374175801344)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-299392897079201948252737832983, 316912650057057350374175801344)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_147(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 19161145413068924679136533807105/20282409603651670423947251286016) & (delta + skoS2**2 >= 2) & (delta - skoX >= -19161145413068924679136533807105/20282409603651670423947251286016) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(19161145413068924679136533807105, 20282409603651670423947251286016)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-19161145413068924679136533807105, 20282409603651670423947251286016)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_148(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 299392897079201948252737832983/316912650057057350374175801344) & (delta + skoS2**2 >= 2) & (delta - skoX >= -299392897079201948252737832983/316912650057057350374175801344) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(299392897079201948252737832983, 316912650057057350374175801344)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-299392897079201948252737832983, 316912650057057350374175801344)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_149(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 19161145413068924679136533807105/20282409603651670423947251286016) & (delta + skoS2**2 >= 2) & (delta - skoX >= -19161145413068924679136533807105/20282409603651670423947251286016) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(19161145413068924679136533807105, 20282409603651670423947251286016)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-19161145413068924679136533807105, 20282409603651670423947251286016)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_150(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 299392897079201948252737832983/316912650057057350374175801344) & (delta + skoS2**2 >= 2) & (delta - skoX >= -299392897079201948252737832983/316912650057057350374175801344) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(299392897079201948252737832983, 316912650057057350374175801344)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-299392897079201948252737832983, 316912650057057350374175801344)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_151(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 19161145413068924679136533807105/20282409603651670423947251286016) & (delta + skoS2**2 >= 2) & (delta - skoX >= -19161145413068924679136533807105/20282409603651670423947251286016) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(19161145413068924679136533807105, 20282409603651670423947251286016)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-19161145413068924679136533807105, 20282409603651670423947251286016)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_152(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 299392897079201948252737832983/316912650057057350374175801344) & (delta + skoS2**2 >= 2) & (delta - skoX >= -299392897079201948252737832983/316912650057057350374175801344) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(299392897079201948252737832983, 316912650057057350374175801344)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-299392897079201948252737832983, 316912650057057350374175801344)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_153(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 19161145413068924679136533807105/20282409603651670423947251286016) & (delta + skoS2**2 >= 2) & (delta - skoX >= -19161145413068924679136533807105/20282409603651670423947251286016) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(19161145413068924679136533807105, 20282409603651670423947251286016)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-19161145413068924679136533807105, 20282409603651670423947251286016)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_154(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 299392897079201948252737832983/316912650057057350374175801344) & (delta + skoS2**2 >= 2) & (delta - skoX >= -299392897079201948252737832983/316912650057057350374175801344) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(299392897079201948252737832983, 316912650057057350374175801344)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-299392897079201948252737832983, 316912650057057350374175801344)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_155(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 19161145413068924679136533807105/20282409603651670423947251286016) & (delta + skoS2**2 >= 2) & (delta - skoX >= -19161145413068924679136533807105/20282409603651670423947251286016) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(19161145413068924679136533807105, 20282409603651670423947251286016)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-19161145413068924679136533807105, 20282409603651670423947251286016)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_156(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 299392897079201948252737832983/316912650057057350374175801344) & (delta + skoS2**2 >= 2) & (delta - skoX >= -299392897079201948252737832983/316912650057057350374175801344) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(299392897079201948252737832983, 316912650057057350374175801344)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-299392897079201948252737832983, 316912650057057350374175801344)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_157(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 19161145413068924679136533807105/20282409603651670423947251286016) & (delta + skoS2**2 >= 2) & (delta - skoX >= -19161145413068924679136533807105/20282409603651670423947251286016) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(19161145413068924679136533807105, 20282409603651670423947251286016)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-19161145413068924679136533807105, 20282409603651670423947251286016)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_158(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 299392897079201948252737832983/316912650057057350374175801344) & (delta + skoS2**2 >= 2) & (delta - skoX >= -299392897079201948252737832983/316912650057057350374175801344) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(299392897079201948252737832983, 316912650057057350374175801344)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-299392897079201948252737832983, 316912650057057350374175801344)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_159(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 19161145413068924679136533807105/20282409603651670423947251286016) & (delta + skoS2**2 >= 2) & (delta - skoX >= -19161145413068924679136533807105/20282409603651670423947251286016) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(19161145413068924679136533807105, 20282409603651670423947251286016)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-19161145413068924679136533807105, 20282409603651670423947251286016)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_160(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 299392897079201948252737832983/316912650057057350374175801344) & (delta + skoS2**2 >= 2) & (delta - skoX >= -299392897079201948252737832983/316912650057057350374175801344) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(299392897079201948252737832983, 316912650057057350374175801344)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-299392897079201948252737832983, 316912650057057350374175801344)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_161(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 19161145413068924679136533807105/20282409603651670423947251286016) & (delta + skoS2**2 >= 2) & (delta - skoX >= -19161145413068924679136533807105/20282409603651670423947251286016) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(19161145413068924679136533807105, 20282409603651670423947251286016)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-19161145413068924679136533807105, 20282409603651670423947251286016)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_162(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 299392897079201948252737832983/316912650057057350374175801344) & (delta + skoS2**2 >= 2) & (delta - skoX >= -299392897079201948252737832983/316912650057057350374175801344) & (delta - skoS2**2 >= -2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(299392897079201948252737832983, 316912650057057350374175801344)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-299392897079201948252737832983, 316912650057057350374175801344)), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(delta:sympy.Rational, skoX:sympy.Rational, skoS2:sympy.Rational, skoSP:sympy.Rational, skoSM:sympy.Rational):
	# (0 <= delta) & (1 > skoX) & (skoS2 > 0) & (skoSM > 0) & (skoSP > 0) & (skoX > 0) & (skoS2**2 - 2 <= delta) & (skoSM**2 + skoX - 1 <= delta) & (2 - skoS2**2 <= delta) & (-skoSP**2 + skoX + 1 <= delta) & (skoSP**2 - skoX - 1 <= delta) & (-skoSM**2 - skoX + 1 <= delta)

	post_cond =  And(LessThan(Integer(0), Symbol('delta')), StrictGreaterThan(Integer(1), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoSP'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), LessThan(Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Symbol('delta')), LessThan(Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1)), Symbol('delta')), LessThan(Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Symbol('delta')), LessThan(Add(Mul(Integer(-1), Pow(Symbol('skoSP'), Integer(2))), Symbol('skoX'), Integer(1)), Symbol('delta')), LessThan(Add(Pow(Symbol('skoSP'), Integer(2)), Mul(Integer(-1), Symbol('skoX')), Integer(-1)), Symbol('delta')), LessThan(Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)), Symbol('delta')))

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


	post_cond =  And(LessThan(Integer(0), Symbol('delta')), StrictGreaterThan(Integer(1), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoSP'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), LessThan(Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Symbol('delta')), LessThan(Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1)), Symbol('delta')), LessThan(Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Symbol('delta')), LessThan(Add(Mul(Integer(-1), Pow(Symbol('skoSP'), Integer(2))), Symbol('skoX'), Integer(1)), Symbol('delta')), LessThan(Add(Pow(Symbol('skoSP'), Integer(2)), Mul(Integer(-1), Symbol('skoX')), Integer(-1)), Symbol('delta')), LessThan(Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)), Symbol('delta')))

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
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Integer(1))
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
		all_vals['skoSP'] = Integer(1)
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
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(11, 8))
		all_vals['skoSM'] = Rational(1, 4)
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
		all_vals['skoSP'] = Rational(11, 8)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(1, 4))
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
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(89, 64))
		all_vals['skoSM'] = Rational(5, 16)
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
		all_vals['skoSP'] = Rational(89, 64)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(5, 16))
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
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(5, 4))
		all_vals['skoSM'] = Rational(3, 4)
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
		all_vals['skoSP'] = Rational(5, 4)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(3, 4))
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
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(45, 32))
		all_vals['skoSM'] = Rational(1, 8)
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
		all_vals['skoSP'] = Rational(45, 32)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(1, 8))
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
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(721, 512))
		all_vals['skoSM'] = Rational(9, 64)
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
		all_vals['skoSP'] = Rational(721, 512)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(9, 64))
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
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(181, 128))
		all_vals['skoSM'] = Rational(1, 16)
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
		all_vals['skoSP'] = Rational(181, 128)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(1, 16))
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
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(179, 128))
		all_vals['skoSM'] = Rational(3, 16)
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
		all_vals['skoSP'] = Rational(179, 128)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(3, 16))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_17 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_18(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(717, 512))
		all_vals['skoSM'] = Rational(13, 64)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_18 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_19(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Rational(717, 512)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(13, 64))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_19 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_20(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(1441, 1024))
		all_vals['skoSM'] = Rational(17, 128)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_20 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_21(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Rational(1441, 1024)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(17, 128))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_21 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_22(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(721, 512))
		all_vals['skoSM'] = Rational(33, 256)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_22 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_23(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Rational(721, 512)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(33, 256))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_23 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_24(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(361, 256))
		all_vals['skoSM'] = Rational(3, 32)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_24 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_25(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Rational(361, 256)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(3, 32))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_25 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_26(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(1447, 1024))
		all_vals['skoSM'] = Rational(1, 32)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_26 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_27(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Rational(1447, 1024)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(1, 32))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_27 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_28(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(5793, 4096))
		all_vals['skoSM'] = Rational(1, 64)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_28 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_29(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Rational(5793, 4096)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(1, 64))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_29 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_30(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(357, 256))
		all_vals['skoSM'] = Rational(7, 32)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_30 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_31(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Rational(357, 256)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(7, 32))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_31 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_32(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(715, 512))
		all_vals['skoSM'] = Rational(15, 64)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_32 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_33(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Rational(715, 512)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(15, 64))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_33 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_34(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(2867, 2048))
		all_vals['skoSM'] = Rational(51, 256)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_34 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_35(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Rational(2867, 2048)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(51, 256))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_35 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_36(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(717, 512))
		all_vals['skoSM'] = Rational(25, 128)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_36 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_37(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Rational(717, 512)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(25, 128))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_37 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_38(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(1441, 1024))
		all_vals['skoSM'] = Rational(35, 256)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_38 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_39(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Rational(1441, 1024)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(35, 256))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_39 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_40(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(11535, 8192))
		all_vals['skoSM'] = Rational(67, 512)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_40 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_41(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Rational(11535, 8192)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(67, 512))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_41 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_42(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(721, 512))
		all_vals['skoSM'] = Rational(133, 1024)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_42 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_43(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Rational(721, 512)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(133, 1024))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_43 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_44(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(5769, 4096))
		all_vals['skoSM'] = Rational(65, 512)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_44 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_45(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Rational(5769, 4096)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(65, 512))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_45 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_46(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(2889, 2048))
		all_vals['skoSM'] = Rational(13, 128)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_46 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_47(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Rational(2889, 2048)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(13, 128))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_47 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_48(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(723, 512))
		all_vals['skoSM'] = Rational(5, 64)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_48 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_49(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Rational(723, 512)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(5, 64))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_49 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_50(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(1447, 1024))
		all_vals['skoSM'] = Rational(3, 64)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_50 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_51(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Rational(1447, 1024)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(3, 64))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_51 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_52(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(11583, 8192))
		all_vals['skoSM'] = Rational(3, 128)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_52 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_53(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Rational(11583, 8192)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(3, 128))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_53 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_54(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(23169, 16384))
		all_vals['skoSM'] = Rational(5, 256)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_54 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_55(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Rational(23169, 16384)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(5, 256))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_55 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_56(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(11585, 8192))
		all_vals['skoSM'] = Rational(1, 128)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_56 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_57(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Rational(11585, 8192)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(1, 128))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_57 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_58(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(713, 512))
		all_vals['skoSM'] = Rational(31, 128)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_58 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_59(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Rational(713, 512)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(31, 128))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_59 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_60(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(1427, 1024))
		all_vals['skoSM'] = Rational(61, 256)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_60 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_61(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Rational(1427, 1024)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(61, 256))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_61 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_62(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(2855, 2048))
		all_vals['skoSM'] = Rational(121, 512)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_62 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_63(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Rational(2855, 2048)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(121, 512))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_63 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_64(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(11423, 8192))
		all_vals['skoSM'] = Rational(241, 1024)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_64 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_65(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Rational(11423, 8192)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(241, 1024))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_65 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_66(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(45695, 32768))
		all_vals['skoSM'] = Rational(1927, 8192)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_66 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_67(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Rational(45695, 32768)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(1927, 8192))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_67 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_68(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(91391, 65536))
		all_vals['skoSM'] = Rational(3853, 16384)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_68 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_69(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Rational(91391, 65536)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(3853, 16384))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_69 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_70(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(182783, 131072))
		all_vals['skoSM'] = Rational(3853, 16384)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_70 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_71(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Rational(182783, 131072)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(3853, 16384))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_71 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_72(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(182783, 131072))
		all_vals['skoSM'] = Rational(7705, 32768)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_72 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_73(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Rational(182783, 131072)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(7705, 32768))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_73 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_74(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(731135, 524288))
		all_vals['skoSM'] = Rational(7705, 32768)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_74 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_75(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Rational(731135, 524288)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(7705, 32768))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_75 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_76(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(1462271, 1048576))
		all_vals['skoSM'] = Rational(15409, 65536)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_76 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_77(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Rational(1462271, 1048576)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(15409, 65536))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_77 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_78(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(93585407, 67108864))
		all_vals['skoSM'] = Rational(1972351, 8388608)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_78 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_79(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Rational(93585407, 67108864)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(1972351, 8388608))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_79 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_80(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(187170815, 134217728))
		all_vals['skoSM'] = Rational(1972351, 8388608)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_80 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_81(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Rational(187170815, 134217728)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(1972351, 8388608))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_81 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_82(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(187170815, 134217728))
		all_vals['skoSM'] = Rational(7889403, 33554432)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_82 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_83(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Rational(187170815, 134217728)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(7889403, 33554432))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_83 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_84(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(374341631, 268435456))
		all_vals['skoSM'] = Rational(15778805, 67108864)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_84 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_85(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Rational(374341631, 268435456)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(15778805, 67108864))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_85 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_86(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(1497366527, 1073741824))
		all_vals['skoSM'] = Rational(31557609, 134217728)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_86 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_87(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Rational(1497366527, 1073741824)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(31557609, 134217728))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_87 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_88(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(2994733055, 2147483648))
		all_vals['skoSM'] = Rational(126230435, 536870912)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_88 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_89(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Rational(2994733055, 2147483648)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(126230435, 536870912))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_89 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_90(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(5989466111, 4294967296))
		all_vals['skoSM'] = Rational(126230435, 536870912)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_90 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_91(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Rational(5989466111, 4294967296)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(126230435, 536870912))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_91 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_92(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(11978932223, 8589934592))
		all_vals['skoSM'] = Rational(252460869, 1073741824)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_92 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_93(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Rational(11978932223, 8589934592)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(252460869, 1073741824))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_93 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_94(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(23957864447, 17179869184))
		all_vals['skoSM'] = Rational(252460869, 1073741824)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_94 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_95(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Rational(23957864447, 17179869184)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(252460869, 1073741824))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_95 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_96(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(47915728895, 34359738368))
		all_vals['skoSM'] = Rational(504921737, 2147483648)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_96 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_97(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Rational(47915728895, 34359738368)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(504921737, 2147483648))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_97 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_98(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(95831457791, 68719476736))
		all_vals['skoSM'] = Rational(504921737, 2147483648)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_98 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_99(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Rational(95831457791, 68719476736)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(504921737, 2147483648))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_99 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_100(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(191662915583, 137438953472))
		all_vals['skoSM'] = Rational(2019686947, 8589934592)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_100 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_101(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Rational(191662915583, 137438953472)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(2019686947, 8589934592))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_101 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_102(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(383325831167, 274877906944))
		all_vals['skoSM'] = Rational(2019686947, 8589934592)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_102 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_103(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Rational(383325831167, 274877906944)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(2019686947, 8589934592))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_103 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_104(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(766651662335, 549755813888))
		all_vals['skoSM'] = Rational(8078747787, 34359738368)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_104 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_105(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Rational(766651662335, 549755813888)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(8078747787, 34359738368))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_105 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_106(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(766651662335, 549755813888))
		all_vals['skoSM'] = Rational(32314991147, 137438953472)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_106 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_107(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Rational(766651662335, 549755813888)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(32314991147, 137438953472))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_107 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_108(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(3066606649343, 2199023255552))
		all_vals['skoSM'] = Rational(64629982293, 274877906944)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_108 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_109(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Rational(3066606649343, 2199023255552)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(64629982293, 274877906944))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_109 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_110(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(196262825558015, 140737488355328))
		all_vals['skoSM'] = Rational(4136318866751, 17592186044416)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_110 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_111(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Rational(196262825558015, 140737488355328)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(4136318866751, 17592186044416))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_111 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_112(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(392525651116031, 281474976710656))
		all_vals['skoSM'] = Rational(16545275467003, 70368744177664)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_112 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_113(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Rational(392525651116031, 281474976710656)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(16545275467003, 70368744177664))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_113 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_114(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(1570102604464127, 1125899906842624))
		all_vals['skoSM'] = Rational(16545275467003, 70368744177664)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_114 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_115(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Rational(1570102604464127, 1125899906842624)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(16545275467003, 70368744177664))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_115 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_116(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(3140205208928255, 2251799813685248))
		all_vals['skoSM'] = Rational(33090550934005, 140737488355328)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_116 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_117(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Rational(3140205208928255, 2251799813685248)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(33090550934005, 140737488355328))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_117 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_118(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(6280410417856511, 4503599627370496))
		all_vals['skoSM'] = Rational(132362203736019, 562949953421312)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_118 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_119(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Rational(6280410417856511, 4503599627370496)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(132362203736019, 562949953421312))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_119 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_120(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(6280410417856511, 4503599627370496))
		all_vals['skoSM'] = Rational(132362203736019, 562949953421312)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_120 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_121(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Rational(6280410417856511, 4503599627370496)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(132362203736019, 562949953421312))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_121 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_122(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(6280410417856511, 4503599627370496))
		all_vals['skoSM'] = Rational(132362203736019, 562949953421312)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_122 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_123(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Rational(6280410417856511, 4503599627370496)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(132362203736019, 562949953421312))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_123 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_124(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(6280410417856511, 4503599627370496))
		all_vals['skoSM'] = Rational(132362203736019, 562949953421312)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_124 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_125(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Rational(6280410417856511, 4503599627370496)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(132362203736019, 562949953421312))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_125 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_126(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(6280410417856511, 4503599627370496))
		all_vals['skoSM'] = Rational(132362203736019, 562949953421312)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_126 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_127(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Rational(6280410417856511, 4503599627370496)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(132362203736019, 562949953421312))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_127 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_128(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(6280410417856511, 4503599627370496))
		all_vals['skoSM'] = Rational(132362203736019, 562949953421312)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_128 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_129(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Rational(6280410417856511, 4503599627370496)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(132362203736019, 562949953421312))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_129 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_130(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(6280410417856511, 4503599627370496))
		all_vals['skoSM'] = Rational(132362203736019, 562949953421312)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_130 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_131(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Rational(6280410417856511, 4503599627370496)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(132362203736019, 562949953421312))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_131 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_132(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(6280410417856511, 4503599627370496))
		all_vals['skoSM'] = Rational(132362203736019, 562949953421312)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_132 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_133(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Rational(6280410417856511, 4503599627370496)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(132362203736019, 562949953421312))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_133 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_134(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(6280410417856511, 4503599627370496))
		all_vals['skoSM'] = Rational(132362203736019, 562949953421312)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_134 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_135(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Rational(6280410417856511, 4503599627370496)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(132362203736019, 562949953421312))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_135 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_136(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(6280410417856511, 4503599627370496))
		all_vals['skoSM'] = Rational(132362203736019, 562949953421312)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_136 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_137(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Rational(6280410417856511, 4503599627370496)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(132362203736019, 562949953421312))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_137 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_138(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(6280410417856511, 4503599627370496))
		all_vals['skoSM'] = Rational(132362203736019, 562949953421312)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_138 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_139(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Rational(6280410417856511, 4503599627370496)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(132362203736019, 562949953421312))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_139 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_140(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(6280410417856511, 4503599627370496))
		all_vals['skoSM'] = Rational(132362203736019, 562949953421312)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_140 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_141(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Rational(6280410417856511, 4503599627370496)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(132362203736019, 562949953421312))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_141 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_142(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(6280410417856511, 4503599627370496))
		all_vals['skoSM'] = Rational(132362203736019, 562949953421312)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_142 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_143(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Rational(6280410417856511, 4503599627370496)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(132362203736019, 562949953421312))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_143 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_144(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(6280410417856511, 4503599627370496))
		all_vals['skoSM'] = Rational(132362203736019, 562949953421312)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_144 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_145(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Rational(6280410417856511, 4503599627370496)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(132362203736019, 562949953421312))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_145 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_146(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(6280410417856511, 4503599627370496))
		all_vals['skoSM'] = Rational(132362203736019, 562949953421312)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_146 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_147(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Rational(6280410417856511, 4503599627370496)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(132362203736019, 562949953421312))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_147 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_148(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(6280410417856511, 4503599627370496))
		all_vals['skoSM'] = Rational(132362203736019, 562949953421312)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_148 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_149(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Rational(6280410417856511, 4503599627370496)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(132362203736019, 562949953421312))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_149 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_150(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(6280410417856511, 4503599627370496))
		all_vals['skoSM'] = Rational(132362203736019, 562949953421312)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_150 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_151(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Rational(6280410417856511, 4503599627370496)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(132362203736019, 562949953421312))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_151 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_152(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(6280410417856511, 4503599627370496))
		all_vals['skoSM'] = Rational(132362203736019, 562949953421312)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_152 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_153(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Rational(6280410417856511, 4503599627370496)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(132362203736019, 562949953421312))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_153 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_154(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(6280410417856511, 4503599627370496))
		all_vals['skoSM'] = Rational(132362203736019, 562949953421312)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_154 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_155(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Rational(6280410417856511, 4503599627370496)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(132362203736019, 562949953421312))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_155 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_156(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(6280410417856511, 4503599627370496))
		all_vals['skoSM'] = Rational(132362203736019, 562949953421312)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_156 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_157(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Rational(6280410417856511, 4503599627370496)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(132362203736019, 562949953421312))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_157 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_158(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(6280410417856511, 4503599627370496))
		all_vals['skoSM'] = Rational(132362203736019, 562949953421312)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_158 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_159(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Rational(6280410417856511, 4503599627370496)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(132362203736019, 562949953421312))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_159 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_160(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(6280410417856511, 4503599627370496))
		all_vals['skoSM'] = Rational(132362203736019, 562949953421312)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_160 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_161(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Rational(6280410417856511, 4503599627370496)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(132362203736019, 562949953421312))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_161 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_162(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(6280410417856511, 4503599627370496))
		all_vals['skoSM'] = Rational(132362203736019, 562949953421312)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_162 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass


	print("UNKNOWN")
