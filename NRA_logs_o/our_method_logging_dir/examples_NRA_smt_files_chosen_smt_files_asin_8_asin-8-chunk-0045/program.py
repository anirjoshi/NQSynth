import sympy
from sympy import *
from NQS.helper_program_cav import get_lambda_val

def pre_condition_0(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(skoS2 >= 0) & (skoX > 0) & (skoX - 1 < 0) & (-delta + skoX <= 0) & (5000000*pi - 15707963 > 0) & (10000000*pi - 31415927 < 0) & (delta + skoS2**2 - 2 >= 0) & (-delta + skoS2**2 - 2 <= 0)

	pre_cond = And(GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Add(Symbol('skoX'), Integer(-1)), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Symbol('skoX')), Integer(0)), StrictGreaterThan(Add(Mul(Integer(5000000), Symbol('pi')), Integer(-15707963)), Integer(0)), StrictLessThan(Add(Mul(Integer(10000000), Symbol('pi')), Integer(-31415927)), Integer(0)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(skoS2 >= 0) & (skoX > 0) & (skoX - 1 < 0) & (-delta + skoX <= 0) & (5000000*pi - 15707963 > 0) & (10000000*pi - 31415927 < 0) & (delta + skoS2**2 - 2 >= 0) & (-delta + skoS2**2 - 2 <= 0)

	pre_cond = And(GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Add(Symbol('skoX'), Integer(-1)), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Symbol('skoX')), Integer(0)), StrictGreaterThan(Add(Mul(Integer(5000000), Symbol('pi')), Integer(-15707963)), Integer(0)), StrictLessThan(Add(Mul(Integer(10000000), Symbol('pi')), Integer(-31415927)), Integer(0)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoX > 0) & (skoX - 1 < 0) & (5000000*pi - 15707963 > 0) & (10000000*pi - 31415927 < 0) & (delta + skoS2**2 - 2 >= 0) & (4*delta + 4*skoX - 3 >= 0) & (-4*delta + 4*skoX - 3 <= 0) & (-delta + skoS2**2 - 2 <= 0)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Add(Symbol('skoX'), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(5000000), Symbol('pi')), Integer(-15707963)), Integer(0)), StrictLessThan(Add(Mul(Integer(10000000), Symbol('pi')), Integer(-31415927)), Integer(0)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), GreaterThan(Add(Mul(Integer(4), Symbol('delta')), Mul(Integer(4), Symbol('skoX')), Integer(-3)), Integer(0)), LessThan(Add(Mul(Integer(-1), Integer(4), Symbol('delta')), Mul(Integer(4), Symbol('skoX')), Integer(-3)), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(skoS2 >= 0) & (delta > 0) & (skoX > 0) & (skoX - 1 < 0) & (5000000*pi - 15707963 > 0) & (10000000*pi - 31415927 < 0) & (delta + skoS2**2 - 2 >= 0) & (4*delta + 4*skoX - 5 >= 0) & (-delta + skoS2**2 - 2 <= 0)

	pre_cond = And(GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Add(Symbol('skoX'), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(5000000), Symbol('pi')), Integer(-15707963)), Integer(0)), StrictLessThan(Add(Mul(Integer(10000000), Symbol('pi')), Integer(-31415927)), Integer(0)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), GreaterThan(Add(Mul(Integer(4), Symbol('delta')), Mul(Integer(4), Symbol('skoX')), Integer(-5)), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_4(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoX > 0) & (skoX - 1 < 0) & (5000000*pi - 15707963 > 0) & (10000000*pi - 31415927 < 0) & (delta + skoS2**2 - 2 >= 0) & (16*delta + 16*skoX - 7 >= 0) & (-16*delta + 16*skoX - 7 <= 0) & (-delta + skoS2**2 - 2 <= 0)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Add(Symbol('skoX'), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(5000000), Symbol('pi')), Integer(-15707963)), Integer(0)), StrictLessThan(Add(Mul(Integer(10000000), Symbol('pi')), Integer(-31415927)), Integer(0)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), GreaterThan(Add(Mul(Integer(16), Symbol('delta')), Mul(Integer(16), Symbol('skoX')), Integer(-7)), Integer(0)), LessThan(Add(Mul(Integer(-1), Integer(16), Symbol('delta')), Mul(Integer(16), Symbol('skoX')), Integer(-7)), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_5(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoX > 0) & (skoX - 1 < 0) & (5000000*pi - 15707963 > 0) & (10000000*pi - 31415927 < 0) & (delta + skoS2**2 - 2 >= 0) & (16*delta + 16*skoX - 9 >= 0) & (-16*delta + 16*skoX - 9 <= 0) & (-delta + skoS2**2 - 2 <= 0)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Add(Symbol('skoX'), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(5000000), Symbol('pi')), Integer(-15707963)), Integer(0)), StrictLessThan(Add(Mul(Integer(10000000), Symbol('pi')), Integer(-31415927)), Integer(0)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), GreaterThan(Add(Mul(Integer(16), Symbol('delta')), Mul(Integer(16), Symbol('skoX')), Integer(-9)), Integer(0)), LessThan(Add(Mul(Integer(-1), Integer(16), Symbol('delta')), Mul(Integer(16), Symbol('skoX')), Integer(-9)), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_6(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoX > 0) & (skoX - 1 < 0) & (5000000*pi - 15707963 > 0) & (10000000*pi - 31415927 < 0) & (delta + skoS2**2 - 2 >= 0) & (256*delta + 256*skoX - 135 >= 0) & (-256*delta + 256*skoX - 135 <= 0) & (-delta + skoS2**2 - 2 <= 0)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Add(Symbol('skoX'), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(5000000), Symbol('pi')), Integer(-15707963)), Integer(0)), StrictLessThan(Add(Mul(Integer(10000000), Symbol('pi')), Integer(-31415927)), Integer(0)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), GreaterThan(Add(Mul(Integer(256), Symbol('delta')), Mul(Integer(256), Symbol('skoX')), Integer(-135)), Integer(0)), LessThan(Add(Mul(Integer(-1), Integer(256), Symbol('delta')), Mul(Integer(256), Symbol('skoX')), Integer(-135)), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_7(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoX > 0) & (skoX - 1 < 0) & (5000000*pi - 15707963 > 0) & (10000000*pi - 31415927 < 0) & (delta + skoS2**2 - 2 >= 0) & (1024*delta + 1024*skoX - 497 >= 0) & (-1024*delta + 1024*skoX - 497 <= 0) & (-delta + skoS2**2 - 2 <= 0)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Add(Symbol('skoX'), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(5000000), Symbol('pi')), Integer(-15707963)), Integer(0)), StrictLessThan(Add(Mul(Integer(10000000), Symbol('pi')), Integer(-31415927)), Integer(0)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), GreaterThan(Add(Mul(Integer(1024), Symbol('delta')), Mul(Integer(1024), Symbol('skoX')), Integer(-497)), Integer(0)), LessThan(Add(Mul(Integer(-1), Integer(1024), Symbol('delta')), Mul(Integer(1024), Symbol('skoX')), Integer(-497)), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_8(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoX > 0) & (skoX - 1 < 0) & (5000000*pi - 15707963 > 0) & (10000000*pi - 31415927 < 0) & (delta + skoS2**2 - 2 >= 0) & (4096*delta + 4096*skoX - 2247 >= 0) & (-4096*delta + 4096*skoX - 2247 <= 0) & (-delta + skoS2**2 - 2 <= 0)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Add(Symbol('skoX'), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(5000000), Symbol('pi')), Integer(-15707963)), Integer(0)), StrictLessThan(Add(Mul(Integer(10000000), Symbol('pi')), Integer(-31415927)), Integer(0)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), GreaterThan(Add(Mul(Integer(4096), Symbol('delta')), Mul(Integer(4096), Symbol('skoX')), Integer(-2247)), Integer(0)), LessThan(Add(Mul(Integer(-1), Integer(4096), Symbol('delta')), Mul(Integer(4096), Symbol('skoX')), Integer(-2247)), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_9(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoX > 0) & (skoX - 1 < 0) & (5000000*pi - 15707963 > 0) & (10000000*pi - 31415927 < 0) & (delta + skoS2**2 - 2 >= 0) & (16384*delta + 16384*skoX - 8897 >= 0) & (-16384*delta + 16384*skoX - 8897 <= 0) & (-delta + skoS2**2 - 2 <= 0)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Add(Symbol('skoX'), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(5000000), Symbol('pi')), Integer(-15707963)), Integer(0)), StrictLessThan(Add(Mul(Integer(10000000), Symbol('pi')), Integer(-31415927)), Integer(0)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), GreaterThan(Add(Mul(Integer(16384), Symbol('delta')), Mul(Integer(16384), Symbol('skoX')), Integer(-8897)), Integer(0)), LessThan(Add(Mul(Integer(-1), Integer(16384), Symbol('delta')), Mul(Integer(16384), Symbol('skoX')), Integer(-8897)), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_10(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoX > 0) & (skoX - 1 < 0) & (5000000*pi - 15707963 > 0) & (10000000*pi - 31415927 < 0) & (delta + skoS2**2 - 2 >= 0) & (16384*delta + 16384*skoX - 9159 >= 0) & (-16384*delta + 16384*skoX - 9159 <= 0) & (-delta + skoS2**2 - 2 <= 0)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Add(Symbol('skoX'), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(5000000), Symbol('pi')), Integer(-15707963)), Integer(0)), StrictLessThan(Add(Mul(Integer(10000000), Symbol('pi')), Integer(-31415927)), Integer(0)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), GreaterThan(Add(Mul(Integer(16384), Symbol('delta')), Mul(Integer(16384), Symbol('skoX')), Integer(-9159)), Integer(0)), LessThan(Add(Mul(Integer(-1), Integer(16384), Symbol('delta')), Mul(Integer(16384), Symbol('skoX')), Integer(-9159)), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_11(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoX > 0) & (skoX - 1 < 0) & (5000000*pi - 15707963 > 0) & (10000000*pi - 31415927 < 0) & (delta + skoS2**2 - 2 >= 0) & (65536*delta + 65536*skoX - 36225 >= 0) & (-65536*delta + 65536*skoX - 36225 <= 0) & (-delta + skoS2**2 - 2 <= 0)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Add(Symbol('skoX'), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(5000000), Symbol('pi')), Integer(-15707963)), Integer(0)), StrictLessThan(Add(Mul(Integer(10000000), Symbol('pi')), Integer(-31415927)), Integer(0)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), GreaterThan(Add(Mul(Integer(65536), Symbol('delta')), Mul(Integer(65536), Symbol('skoX')), Integer(-36225)), Integer(0)), LessThan(Add(Mul(Integer(-1), Integer(65536), Symbol('delta')), Mul(Integer(65536), Symbol('skoX')), Integer(-36225)), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_12(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoX > 0) & (skoX - 1 < 0) & (5000000*pi - 15707963 > 0) & (10000000*pi - 31415927 < 0) & (delta + skoS2**2 - 2 >= 0) & (262144*delta + 262144*skoX - 147223 >= 0) & (-262144*delta + 262144*skoX - 147223 <= 0) & (-delta + skoS2**2 - 2 <= 0)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Add(Symbol('skoX'), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(5000000), Symbol('pi')), Integer(-15707963)), Integer(0)), StrictLessThan(Add(Mul(Integer(10000000), Symbol('pi')), Integer(-31415927)), Integer(0)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), GreaterThan(Add(Mul(Integer(262144), Symbol('delta')), Mul(Integer(262144), Symbol('skoX')), Integer(-147223)), Integer(0)), LessThan(Add(Mul(Integer(-1), Integer(262144), Symbol('delta')), Mul(Integer(262144), Symbol('skoX')), Integer(-147223)), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_13(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoX > 0) & (skoX - 1 < 0) & (5000000*pi - 15707963 > 0) & (10000000*pi - 31415927 < 0) & (delta + skoS2**2 - 2 >= 0) & (1048576*delta + 1048576*skoX - 587265 >= 0) & (-1048576*delta + 1048576*skoX - 587265 <= 0) & (-delta + skoS2**2 - 2 <= 0)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Add(Symbol('skoX'), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(5000000), Symbol('pi')), Integer(-15707963)), Integer(0)), StrictLessThan(Add(Mul(Integer(10000000), Symbol('pi')), Integer(-31415927)), Integer(0)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), GreaterThan(Add(Mul(Integer(1048576), Symbol('delta')), Mul(Integer(1048576), Symbol('skoX')), Integer(-587265)), Integer(0)), LessThan(Add(Mul(Integer(-1), Integer(1048576), Symbol('delta')), Mul(Integer(1048576), Symbol('skoX')), Integer(-587265)), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_14(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoX > 0) & (skoX - 1 < 0) & (5000000*pi - 15707963 > 0) & (10000000*pi - 31415927 < 0) & (delta + skoS2**2 - 2 >= 0) & (4194304*delta + 4194304*skoX - 2358279 >= 0) & (-4194304*delta + 4194304*skoX - 2358279 <= 0) & (-delta + skoS2**2 - 2 <= 0)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Add(Symbol('skoX'), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(5000000), Symbol('pi')), Integer(-15707963)), Integer(0)), StrictLessThan(Add(Mul(Integer(10000000), Symbol('pi')), Integer(-31415927)), Integer(0)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), GreaterThan(Add(Mul(Integer(4194304), Symbol('delta')), Mul(Integer(4194304), Symbol('skoX')), Integer(-2358279)), Integer(0)), LessThan(Add(Mul(Integer(-1), Integer(4194304), Symbol('delta')), Mul(Integer(4194304), Symbol('skoX')), Integer(-2358279)), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_15(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoX > 0) & (skoX - 1 < 0) & (5000000*pi - 15707963 > 0) & (10000000*pi - 31415927 < 0) & (delta + skoS2**2 - 2 >= 0) & (16777216*delta + 16777216*skoX - 9426945 >= 0) & (-16777216*delta + 16777216*skoX - 9426945 <= 0) & (-delta + skoS2**2 - 2 <= 0)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Add(Symbol('skoX'), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(5000000), Symbol('pi')), Integer(-15707963)), Integer(0)), StrictLessThan(Add(Mul(Integer(10000000), Symbol('pi')), Integer(-31415927)), Integer(0)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), GreaterThan(Add(Mul(Integer(16777216), Symbol('delta')), Mul(Integer(16777216), Symbol('skoX')), Integer(-9426945)), Integer(0)), LessThan(Add(Mul(Integer(-1), Integer(16777216), Symbol('delta')), Mul(Integer(16777216), Symbol('skoX')), Integer(-9426945)), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_16(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoX > 0) & (skoX - 1 < 0) & (5000000*pi - 15707963 > 0) & (10000000*pi - 31415927 < 0) & (delta + skoS2**2 - 2 >= 0) & (67108864*delta + 67108864*skoX - 37743303 >= 0) & (-67108864*delta + 67108864*skoX - 37743303 <= 0) & (-delta + skoS2**2 - 2 <= 0)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Add(Symbol('skoX'), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(5000000), Symbol('pi')), Integer(-15707963)), Integer(0)), StrictLessThan(Add(Mul(Integer(10000000), Symbol('pi')), Integer(-31415927)), Integer(0)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), GreaterThan(Add(Mul(Integer(67108864), Symbol('delta')), Mul(Integer(67108864), Symbol('skoX')), Integer(-37743303)), Integer(0)), LessThan(Add(Mul(Integer(-1), Integer(67108864), Symbol('delta')), Mul(Integer(67108864), Symbol('skoX')), Integer(-37743303)), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_17(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS2 >= 0) & (skoX > 0) & (skoX - 1 < 0) & (5000000*pi - 15707963 > 0) & (10000000*pi - 31415927 < 0) & (delta + skoS2**2 - 2 >= 0) & (268435456*delta + 268435456*skoX - 150953985 >= 0) & (-268435456*delta + 268435456*skoX - 150953985 <= 0) & (-delta + skoS2**2 - 2 <= 0)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Add(Symbol('skoX'), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(5000000), Symbol('pi')), Integer(-15707963)), Integer(0)), StrictLessThan(Add(Mul(Integer(10000000), Symbol('pi')), Integer(-31415927)), Integer(0)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), GreaterThan(Add(Mul(Integer(268435456), Symbol('delta')), Mul(Integer(268435456), Symbol('skoX')), Integer(-150953985)), Integer(0)), LessThan(Add(Mul(Integer(-1), Integer(268435456), Symbol('delta')), Mul(Integer(268435456), Symbol('skoX')), Integer(-150953985)), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(delta:sympy.Rational, skoX:sympy.Rational, skoS2:sympy.Rational, pi:sympy.Rational, skoSP:sympy.Rational, skoSM:sympy.Rational):
	# (0 <= delta) & (0 <= skoS2) & (0 <= skoSM) & (0 <= skoSP) & (1 > skoX) & (31415927/10000000 > pi) & (pi > 15707963/5000000) & (skoX > 0) & (skoS2**2 - 2 <= delta) & (skoSM**2 + skoX - 1 <= delta) & (2 - skoS2**2 <= delta) & (-skoSP**2 + skoX + 1 <= delta) & (skoSP**2 - skoX - 1 <= delta) & (skoX*(-skoSM - skoSP - 4) <= 0) & (-skoSM**2 - skoX + 1 <= delta)

	post_cond =  And(LessThan(Integer(0), Symbol('delta')), LessThan(Integer(0), Symbol('skoS2')), LessThan(Integer(0), Symbol('skoSM')), LessThan(Integer(0), Symbol('skoSP')), StrictGreaterThan(Integer(1), Symbol('skoX')), StrictGreaterThan(Rational(31415927, 10000000), Symbol('pi')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), LessThan(Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Symbol('delta')), LessThan(Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1)), Symbol('delta')), LessThan(Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Symbol('delta')), LessThan(Add(Mul(Integer(-1), Pow(Symbol('skoSP'), Integer(2))), Symbol('skoX'), Integer(1)), Symbol('delta')), LessThan(Add(Pow(Symbol('skoSP'), Integer(2)), Mul(Integer(-1), Symbol('skoX')), Integer(-1)), Symbol('delta')), LessThan(Mul(Symbol('skoX'), Add(Mul(Integer(-1), Symbol('skoSM')), Mul(Integer(-1), Symbol('skoSP')), Integer(-4))), Integer(0)), LessThan(Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)), Symbol('delta')))

	eval = post_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi, 'skoSP':skoSP, 'skoSM':skoSM })

	return eval == sympy.logic.boolalg.BooleanTrue



#return post-condition single variable
def return_post_condition_single_var(post_condition, delta:sympy.Rational=None, skoX:sympy.Rational=None, skoS2:sympy.Rational=None, pi:sympy.Rational=None, skoSP:sympy.Rational=None, skoSM:sympy.Rational=None):
	assert delta!=None
	assert skoX!=None
	assert skoS2!=None
	assert pi!=None


	if skoSP==None:
		assert skoSM!=None
		return lambda skoSP: post_condition(delta=delta, skoX=skoX, skoS2=skoS2, pi=pi, skoSP=skoSP, skoSM=skoSM)

	if skoSM==None:
		assert skoSP!=None
		return lambda skoSM: post_condition(delta=delta, skoX=skoX, skoS2=skoS2, pi=pi, skoSP=skoSP, skoSM=skoSM)


	return post_condition(delta=delta, skoX=skoX, skoS2=skoS2, pi=pi, skoSP=skoSP, skoSM=skoSM)


def get_univariate_poly( delta:sympy.Rational, skoX:sympy.Rational, skoS2:sympy.Rational, pi:sympy.Rational, skoSP:sympy.Rational, skoSM:sympy.Rational ):


	post_cond =  And(LessThan(Integer(0), Symbol('delta')), LessThan(Integer(0), Symbol('skoS2')), LessThan(Integer(0), Symbol('skoSM')), LessThan(Integer(0), Symbol('skoSP')), StrictGreaterThan(Integer(1), Symbol('skoX')), StrictGreaterThan(Rational(31415927, 10000000), Symbol('pi')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), LessThan(Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Symbol('delta')), LessThan(Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1)), Symbol('delta')), LessThan(Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Symbol('delta')), LessThan(Add(Mul(Integer(-1), Pow(Symbol('skoSP'), Integer(2))), Symbol('skoX'), Integer(1)), Symbol('delta')), LessThan(Add(Pow(Symbol('skoSP'), Integer(2)), Mul(Integer(-1), Symbol('skoX')), Integer(-1)), Symbol('delta')), LessThan(Mul(Symbol('skoX'), Add(Mul(Integer(-1), Symbol('skoSM')), Mul(Integer(-1), Symbol('skoSP')), Integer(-4))), Integer(0)), LessThan(Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)), Symbol('delta')))

	eval = post_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi, 'skoSP':skoSP, 'skoSM':skoSM })
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
	
	
	ip_0=int(input("enter numerator of pi:\n"))
	ip_1=int(input("enter denominator of pi:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	pi=sympy.Rational(ip_0,ip_1)
	
	
	lambda_var_0 = sympy.symbols('lambda_var_0')
	
	
	if pre_condition_0(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['pi'] = pi
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
	
	
	if pre_condition_1(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['pi'] = pi
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
	
	
	if pre_condition_2(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['pi'] = pi
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
	
	
	if pre_condition_3(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['pi'] = pi
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
	
	
	if pre_condition_4(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['pi'] = pi
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
	
	
	if pre_condition_5(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['pi'] = pi
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
	
	
	if pre_condition_6(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['pi'] = pi
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(39, 32))
		all_vals['skoSM'] = Rational(11, 16)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_6 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_7(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['pi'] = pi
		all_vals['skoSP'] = Rational(39, 32)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(11, 16))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_7 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_8(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['pi'] = pi
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(159, 128))
		all_vals['skoSM'] = Rational(43, 64)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_8 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_9(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['pi'] = pi
		all_vals['skoSP'] = Rational(159, 128)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(43, 64))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_9 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_10(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['pi'] = pi
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(319, 256))
		all_vals['skoSM'] = Rational(85, 128)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_10 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_11(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['pi'] = pi
		all_vals['skoSP'] = Rational(319, 256)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(85, 128))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_11 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_12(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['pi'] = pi
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(1279, 1024))
		all_vals['skoSM'] = Rational(339, 512)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_12 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_13(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['pi'] = pi
		all_vals['skoSP'] = Rational(1279, 1024)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(339, 512))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_13 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_14(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['pi'] = pi
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(5119, 4096))
		all_vals['skoSM'] = Rational(1355, 2048)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_14 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_15(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['pi'] = pi
		all_vals['skoSP'] = Rational(5119, 4096)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(1355, 2048))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_15 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_16(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['pi'] = pi
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(20479, 16384))
		all_vals['skoSM'] = Rational(5419, 8192)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_16 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_17(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['pi'] = pi
		all_vals['skoSP'] = Rational(20479, 16384)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(5419, 8192))
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
