import sympy
from sympy import *
from NQS.helper_program_cav import get_lambda_val

def pre_condition_0(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (5000000*pi - 15707963 > 0) & (10000000*pi - 31415927 < 0) & (skoS**3 + 3*skoS**2 - 1 <= 0)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Add(Mul(Integer(5000000), Symbol('pi')), Integer(-15707963)), Integer(0)), StrictLessThan(Add(Mul(Integer(10000000), Symbol('pi')), Integer(-31415927)), Integer(0)), LessThan(Add(Pow(Symbol('skoS'), Integer(3)), Mul(Integer(3), Pow(Symbol('skoS'), Integer(2))), Integer(-1)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (5000000*pi - 15707963 > 0) & (10000000*pi - 31415927 < 0) & (32*skoS**3 + 128*skoS**2 - 8*skoS - 55 <= 0)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Add(Mul(Integer(5000000), Symbol('pi')), Integer(-15707963)), Integer(0)), StrictLessThan(Add(Mul(Integer(10000000), Symbol('pi')), Integer(-31415927)), Integer(0)), LessThan(Add(Mul(Integer(32), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(128), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(8), Symbol('skoS')), Integer(-55)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (16*skoS - 11 >= 0) & (5000000*pi - 15707963 > 0) & (10000000*pi - 31415927 < 0) & (688*skoS**3 + 1888*skoS**2 - 583*skoS - 919 <= 0)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Add(Mul(Integer(16), Symbol('skoS')), Integer(-11)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(5000000), Symbol('pi')), Integer(-15707963)), Integer(0)), StrictLessThan(Add(Mul(Integer(10000000), Symbol('pi')), Integer(-31415927)), Integer(0)), LessThan(Add(Mul(Integer(688), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(1888), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(583), Symbol('skoS')), Integer(-919)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (5000000*pi - 15707963 > 0) & (10000000*pi - 31415927 < 0) & (524288*skoS**3 + 2097152*skoS**2 - 521216*skoS - 1047551 <= 0)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Add(Mul(Integer(5000000), Symbol('pi')), Integer(-15707963)), Integer(0)), StrictLessThan(Add(Mul(Integer(10000000), Symbol('pi')), Integer(-31415927)), Integer(0)), LessThan(Add(Mul(Integer(524288), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(2097152), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(521216), Symbol('skoS')), Integer(-1047551)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_4(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (128*skoS - 97 >= 0) & (5000000*pi - 15707963 > 0) & (10000000*pi - 31415927 < 0) & (45184*skoS**3 + 123136*skoS**2 - 40255*skoS - 60607 <= 0)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Add(Mul(Integer(128), Symbol('skoS')), Integer(-97)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(5000000), Symbol('pi')), Integer(-15707963)), Integer(0)), StrictLessThan(Add(Mul(Integer(10000000), Symbol('pi')), Integer(-31415927)), Integer(0)), LessThan(Add(Mul(Integer(45184), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(123136), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(40255), Symbol('skoS')), Integer(-60607)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_5(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (5000000*pi - 15707963 > 0) & (10000000*pi - 31415927 < 0) & (8388608*skoS**3 + 33554432*skoS**2 - 8376320*skoS - 16773119 <= 0)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Add(Mul(Integer(5000000), Symbol('pi')), Integer(-15707963)), Integer(0)), StrictLessThan(Add(Mul(Integer(10000000), Symbol('pi')), Integer(-31415927)), Integer(0)), LessThan(Add(Mul(Integer(8388608), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(33554432), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(8376320), Symbol('skoS')), Integer(-16773119)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_6(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (2048*skoS - 1559 >= 0) & (5000000*pi - 15707963 > 0) & (10000000*pi - 31415927 < 0) & (11581440*skoS**3 + 31551488*skoS**2 - 10340847*skoS - 15536623 <= 0)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Add(Mul(Integer(2048), Symbol('skoS')), Integer(-1559)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(5000000), Symbol('pi')), Integer(-15707963)), Integer(0)), StrictLessThan(Add(Mul(Integer(10000000), Symbol('pi')), Integer(-31415927)), Integer(0)), LessThan(Add(Mul(Integer(11581440), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(31551488), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(10340847), Symbol('skoS')), Integer(-15536623)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_7(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (5000000*pi - 15707963 > 0) & (10000000*pi - 31415927 < 0) & (536870912*skoS**3 + 2147483648*skoS**2 - 536772608*skoS - 1073709055 <= 0)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Add(Mul(Integer(5000000), Symbol('pi')), Integer(-15707963)), Integer(0)), StrictLessThan(Add(Mul(Integer(10000000), Symbol('pi')), Integer(-31415927)), Integer(0)), LessThan(Add(Mul(Integer(536870912), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(2147483648), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(536772608), Symbol('skoS')), Integer(-1073709055)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_8(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (4096*skoS - 3119 >= 0) & (5000000*pi - 15707963 > 0) & (10000000*pi - 31415927 < 0) & (46329856*skoS**3 + 126214144*skoS**2 - 41373535*skoS - 62152543 <= 0)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Add(Mul(Integer(4096), Symbol('skoS')), Integer(-3119)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(5000000), Symbol('pi')), Integer(-15707963)), Integer(0)), StrictLessThan(Add(Mul(Integer(10000000), Symbol('pi')), Integer(-31415927)), Integer(0)), LessThan(Add(Mul(Integer(46329856), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(126214144), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(41373535), Symbol('skoS')), Integer(-62152543)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_9(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (5000000*pi - 15707963 > 0) & (10000000*pi - 31415927 < 0) & (8589934592*skoS**3 + 34359738368*skoS**2 - 8589541376*skoS - 17179738111 <= 0)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Add(Mul(Integer(5000000), Symbol('pi')), Integer(-15707963)), Integer(0)), StrictLessThan(Add(Mul(Integer(10000000), Symbol('pi')), Integer(-31415927)), Integer(0)), LessThan(Add(Mul(Integer(8589934592), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(34359738368), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(8589541376), Symbol('skoS')), Integer(-17179738111)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_10(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (16384*skoS - 12477 >= 0) & (5000000*pi - 15707963 > 0) & (10000000*pi - 31415927 < 0) & (741294080*skoS**3 + 2019459072*skoS**2 - 662017143*skoS - 994464887 <= 0)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Add(Mul(Integer(16384), Symbol('skoS')), Integer(-12477)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(5000000), Symbol('pi')), Integer(-15707963)), Integer(0)), StrictLessThan(Add(Mul(Integer(10000000), Symbol('pi')), Integer(-31415927)), Integer(0)), LessThan(Add(Mul(Integer(741294080), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(2019459072), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(662017143), Symbol('skoS')), Integer(-994464887)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_11(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (5000000*pi - 15707963 > 0) & (10000000*pi - 31415927 < 0) & (34359738368*skoS**3 + 137438953472*skoS**2 - 34358951936*skoS - 68719214591 <= 0)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Add(Mul(Integer(5000000), Symbol('pi')), Integer(-15707963)), Integer(0)), StrictLessThan(Add(Mul(Integer(10000000), Symbol('pi')), Integer(-31415927)), Integer(0)), LessThan(Add(Mul(Integer(34359738368), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(137438953472), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(34358951936), Symbol('skoS')), Integer(-68719214591)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_12(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (65536*skoS - 49909 >= 0) & (5000000*pi - 15707963 > 0) & (10000000*pi - 31415927 < 0) & (11860770816*skoS**3 + 32311476224*skoS**2 - 10592436615*skoS - 15911534983 <= 0)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Add(Mul(Integer(65536), Symbol('skoS')), Integer(-49909)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(5000000), Symbol('pi')), Integer(-15707963)), Integer(0)), StrictLessThan(Add(Mul(Integer(10000000), Symbol('pi')), Integer(-31415927)), Integer(0)), LessThan(Add(Mul(Integer(11860770816), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(32311476224), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(10592436615), Symbol('skoS')), Integer(-15911534983)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_13(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (5000000*pi - 15707963 > 0) & (10000000*pi - 31415927 < 0) & (137438953472*skoS**3 + 549755813888*skoS**2 - 137437380608*skoS - 274877382655 <= 0)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Add(Mul(Integer(5000000), Symbol('pi')), Integer(-15707963)), Integer(0)), StrictLessThan(Add(Mul(Integer(10000000), Symbol('pi')), Integer(-31415927)), Integer(0)), LessThan(Add(Mul(Integer(137438953472), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(549755813888), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(137437380608), Symbol('skoS')), Integer(-274877382655)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_14(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (262144*skoS - 199637 >= 0) & (5000000*pi - 15707963 > 0) & (10000000*pi - 31415927 < 0) & (189772595200*skoS**3 + 516984143872*skoS**2 - 169479635143*skoS - 254584946887 <= 0)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Add(Mul(Integer(262144), Symbol('skoS')), Integer(-199637)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(5000000), Symbol('pi')), Integer(-15707963)), Integer(0)), StrictLessThan(Add(Mul(Integer(10000000), Symbol('pi')), Integer(-31415927)), Integer(0)), LessThan(Add(Mul(Integer(189772595200), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(516984143872), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(169479635143), Symbol('skoS')), Integer(-254584946887)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_15(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (5000000*pi - 15707963 > 0) & (10000000*pi - 31415927 < 0) & (8796093022208*skoS**3 + 35184372088832*skoS**2 - 8796080439296*skoS - 17592181850111 <= 0)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Add(Mul(Integer(5000000), Symbol('pi')), Integer(-15707963)), Integer(0)), StrictLessThan(Add(Mul(Integer(10000000), Symbol('pi')), Integer(-31415927)), Integer(0)), LessThan(Add(Mul(Integer(8796093022208), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(35184372088832), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(8796080439296), Symbol('skoS')), Integer(-17592181850111)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_16(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (524288*skoS - 399275 >= 0) & (5000000*pi - 15707963 > 0) & (10000000*pi - 31415927 < 0) & (759090905088*skoS**3 + 2067937624064*skoS**2 - 677919839175*skoS - 1018340561863 <= 0)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Add(Mul(Integer(524288), Symbol('skoS')), Integer(-399275)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(5000000), Symbol('pi')), Integer(-15707963)), Integer(0)), StrictLessThan(Add(Mul(Integer(10000000), Symbol('pi')), Integer(-31415927)), Integer(0)), LessThan(Add(Mul(Integer(759090905088), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(2067937624064), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(677919839175), Symbol('skoS')), Integer(-1018340561863)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_17(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (5000000*pi - 15707963 > 0) & (10000000*pi - 31415927 < 0) & (9007199254740992*skoS**3 + 36028797018963968*skoS**2 - 9007198852087808*skoS - 18014398375264255 <= 0)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Add(Mul(Integer(5000000), Symbol('pi')), Integer(-15707963)), Integer(0)), StrictLessThan(Add(Mul(Integer(10000000), Symbol('pi')), Integer(-31415927)), Integer(0)), LessThan(Add(Mul(Integer(9007199254740992), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(36028797018963968), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(9007198852087808), Symbol('skoS')), Integer(-18014398375264255)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_18(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (16777216*skoS - 12776809 >= 0) & (5000000*pi - 15707963 > 0) & (10000000*pi - 31415927 < 0) & (777309237805056*skoS**3 + 2117568429031424*skoS**2 - 694190289312495*skoS - 1042780958350063 <= 0)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Add(Mul(Integer(16777216), Symbol('skoS')), Integer(-12776809)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(5000000), Symbol('pi')), Integer(-15707963)), Integer(0)), StrictLessThan(Add(Mul(Integer(10000000), Symbol('pi')), Integer(-31415927)), Integer(0)), LessThan(Add(Mul(Integer(777309237805056), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(2117568429031424), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(694190289312495), Symbol('skoS')), Integer(-1042780958350063)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_19(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (5000000*pi - 15707963 > 0) & (10000000*pi - 31415927 < 0) & (144115188075855872*skoS**3 + 576460752303423488*skoS**2 - 144115186465243136*skoS - 288230375614840831 <= 0)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Add(Mul(Integer(5000000), Symbol('pi')), Integer(-15707963)), Integer(0)), StrictLessThan(Add(Mul(Integer(10000000), Symbol('pi')), Integer(-31415927)), Integer(0)), LessThan(Add(Mul(Integer(144115188075855872), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(576460752303423488), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(144115186465243136), Symbol('skoS')), Integer(-288230375614840831)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_20(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (67108864*skoS - 51107237 >= 0) & (5000000*pi - 15707963 > 0) & (10000000*pi - 31415927 < 0) & (12436947871989760*skoS**3 + 33881094998720512*skoS**2 - 11107044795220903*skoS - 16684495432713127 <= 0)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Add(Mul(Integer(67108864), Symbol('skoS')), Integer(-51107237)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(5000000), Symbol('pi')), Integer(-15707963)), Integer(0)), StrictLessThan(Add(Mul(Integer(10000000), Symbol('pi')), Integer(-31415927)), Integer(0)), LessThan(Add(Mul(Integer(12436947871989760), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(33881094998720512), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(11107044795220903), Symbol('skoS')), Integer(-16684495432713127)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(delta:sympy.Rational, skoS:sympy.Rational, pi:sympy.Rational, skoCOSS:sympy.Rational, skoSINS:sympy.Rational):
	# (0 <= delta) & (0 <= skoCOSS) & (0 <= skoS) & (skoSINS <= skoS) & (31415927/10000000 > pi) & (pi > 15707963/5000000) & (pi/2 > skoS) & (skoSINS*(-2*skoCOSS + skoS*(skoS*(skoS + 2) - 4) + skoSINS*(skoS + 1) - 3) <= skoCOSS*(-2*skoCOSS - 2) + skoS*(skoCOSS*(-2*skoCOSS - 10) + skoS*(-6*skoCOSS - 2*skoS - 6)) + 2)

	post_cond =  And(LessThan(Integer(0), Symbol('delta')), LessThan(Integer(0), Symbol('skoCOSS')), LessThan(Integer(0), Symbol('skoS')), LessThan(Symbol('skoSINS'), Symbol('skoS')), StrictGreaterThan(Rational(31415927, 10000000), Symbol('pi')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Mul(Rational(1, 2), Symbol('pi')), Symbol('skoS')), LessThan(Mul(Symbol('skoSINS'), Add(Mul(Integer(-1), Integer(2), Symbol('skoCOSS')), Mul(Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(2))), Integer(-4))), Mul(Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(-3))), Add(Mul(Symbol('skoCOSS'), Add(Mul(Integer(-1), Integer(2), Symbol('skoCOSS')), Integer(-2))), Mul(Symbol('skoS'), Add(Mul(Symbol('skoCOSS'), Add(Mul(Integer(-1), Integer(2), Symbol('skoCOSS')), Integer(-10))), Mul(Symbol('skoS'), Add(Mul(Integer(-1), Integer(6), Symbol('skoCOSS')), Mul(Integer(-1), Integer(2), Symbol('skoS')), Integer(-6))))), Integer(2))))

	eval = post_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi, 'skoCOSS':skoCOSS, 'skoSINS':skoSINS })

	return eval == sympy.logic.boolalg.BooleanTrue



#return post-condition single variable
def return_post_condition_single_var(post_condition, delta:sympy.Rational=None, skoS:sympy.Rational=None, pi:sympy.Rational=None, skoCOSS:sympy.Rational=None, skoSINS:sympy.Rational=None):
	assert delta!=None
	assert skoS!=None
	assert pi!=None


	if skoCOSS==None:
		assert skoSINS!=None
		return lambda skoCOSS: post_condition(delta=delta, skoS=skoS, pi=pi, skoCOSS=skoCOSS, skoSINS=skoSINS)

	if skoSINS==None:
		assert skoCOSS!=None
		return lambda skoSINS: post_condition(delta=delta, skoS=skoS, pi=pi, skoCOSS=skoCOSS, skoSINS=skoSINS)


	return post_condition(delta=delta, skoS=skoS, pi=pi, skoCOSS=skoCOSS, skoSINS=skoSINS)


def get_univariate_poly( delta:sympy.Rational, skoS:sympy.Rational, pi:sympy.Rational, skoCOSS:sympy.Rational, skoSINS:sympy.Rational ):


	post_cond =  And(LessThan(Integer(0), Symbol('delta')), LessThan(Integer(0), Symbol('skoCOSS')), LessThan(Integer(0), Symbol('skoS')), LessThan(Symbol('skoSINS'), Symbol('skoS')), StrictGreaterThan(Rational(31415927, 10000000), Symbol('pi')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Mul(Rational(1, 2), Symbol('pi')), Symbol('skoS')), LessThan(Mul(Symbol('skoSINS'), Add(Mul(Integer(-1), Integer(2), Symbol('skoCOSS')), Mul(Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(2))), Integer(-4))), Mul(Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(-3))), Add(Mul(Symbol('skoCOSS'), Add(Mul(Integer(-1), Integer(2), Symbol('skoCOSS')), Integer(-2))), Mul(Symbol('skoS'), Add(Mul(Symbol('skoCOSS'), Add(Mul(Integer(-1), Integer(2), Symbol('skoCOSS')), Integer(-10))), Mul(Symbol('skoS'), Add(Mul(Integer(-1), Integer(6), Symbol('skoCOSS')), Mul(Integer(-1), Integer(2), Symbol('skoS')), Integer(-6))))), Integer(2))))

	eval = post_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi, 'skoCOSS':skoCOSS, 'skoSINS':skoSINS })
	return eval



if __name__=="__main__":
	
	ip_0=int(input("enter numerator of delta:\n"))
	ip_1=int(input("enter denominator of delta:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	delta=sympy.Rational(ip_0,ip_1)
	
	
	ip_0=int(input("enter numerator of skoS:\n"))
	ip_1=int(input("enter denominator of skoS:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	skoS=sympy.Rational(ip_0,ip_1)
	
	
	ip_0=int(input("enter numerator of pi:\n"))
	ip_1=int(input("enter denominator of pi:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	pi=sympy.Rational(ip_0,ip_1)
	
	
	lambda_var_0 = sympy.symbols('lambda_var_0')
	
	
	if pre_condition_0(delta=delta,skoS=skoS,pi=pi)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoS'] = skoS
		all_vals['pi'] = pi
		all_vals['skoCOSS'] = Add(Symbol('lambda_var_0'), Rational(1, 8))
		all_vals['skoSINS'] = Integer(0)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_0 SAT")

			print("skoCOSS=", all_vals["skoCOSS"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSINS=", all_vals["skoSINS"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_1(delta=delta,skoS=skoS,pi=pi)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoS'] = skoS
		all_vals['pi'] = pi
		all_vals['skoCOSS'] = Rational(1, 8)
		all_vals['skoSINS'] = Symbol('lambda_var_0')
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_1 SAT")

			print("skoCOSS=", all_vals["skoCOSS"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSINS=", all_vals["skoSINS"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_2(delta=delta,skoS=skoS,pi=pi)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoS'] = skoS
		all_vals['pi'] = pi
		all_vals['skoCOSS'] = Add(Symbol('lambda_var_0'), Rational(1, 1024))
		all_vals['skoSINS'] = Rational(11, 16)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_2 SAT")

			print("skoCOSS=", all_vals["skoCOSS"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSINS=", all_vals["skoSINS"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_3(delta=delta,skoS=skoS,pi=pi)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoS'] = skoS
		all_vals['pi'] = pi
		all_vals['skoCOSS'] = Rational(1, 1024)
		all_vals['skoSINS'] = Add(Symbol('lambda_var_0'), Rational(11, 16))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_3 SAT")

			print("skoCOSS=", all_vals["skoCOSS"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSINS=", all_vals["skoSINS"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_4(delta=delta,skoS=skoS,pi=pi)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoS'] = skoS
		all_vals['pi'] = pi
		all_vals['skoCOSS'] = Add(Symbol('lambda_var_0'), Rational(1, 4096))
		all_vals['skoSINS'] = Rational(97, 128)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_4 SAT")

			print("skoCOSS=", all_vals["skoCOSS"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSINS=", all_vals["skoSINS"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_5(delta=delta,skoS=skoS,pi=pi)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoS'] = skoS
		all_vals['pi'] = pi
		all_vals['skoCOSS'] = Rational(1, 4096)
		all_vals['skoSINS'] = Add(Symbol('lambda_var_0'), Rational(97, 128))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_5 SAT")

			print("skoCOSS=", all_vals["skoCOSS"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSINS=", all_vals["skoSINS"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_6(delta=delta,skoS=skoS,pi=pi)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoS'] = skoS
		all_vals['pi'] = pi
		all_vals['skoCOSS'] = Add(Symbol('lambda_var_0'), Rational(1, 32768))
		all_vals['skoSINS'] = Rational(1559, 2048)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_6 SAT")

			print("skoCOSS=", all_vals["skoCOSS"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSINS=", all_vals["skoSINS"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_7(delta=delta,skoS=skoS,pi=pi)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoS'] = skoS
		all_vals['pi'] = pi
		all_vals['skoCOSS'] = Rational(1, 32768)
		all_vals['skoSINS'] = Add(Symbol('lambda_var_0'), Rational(1559, 2048))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_7 SAT")

			print("skoCOSS=", all_vals["skoCOSS"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSINS=", all_vals["skoSINS"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_8(delta=delta,skoS=skoS,pi=pi)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoS'] = skoS
		all_vals['pi'] = pi
		all_vals['skoCOSS'] = Add(Symbol('lambda_var_0'), Rational(1, 131072))
		all_vals['skoSINS'] = Rational(3119, 4096)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_8 SAT")

			print("skoCOSS=", all_vals["skoCOSS"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSINS=", all_vals["skoSINS"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_9(delta=delta,skoS=skoS,pi=pi)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoS'] = skoS
		all_vals['pi'] = pi
		all_vals['skoCOSS'] = Rational(1, 131072)
		all_vals['skoSINS'] = Add(Symbol('lambda_var_0'), Rational(3119, 4096))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_9 SAT")

			print("skoCOSS=", all_vals["skoCOSS"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSINS=", all_vals["skoSINS"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_10(delta=delta,skoS=skoS,pi=pi)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoS'] = skoS
		all_vals['pi'] = pi
		all_vals['skoCOSS'] = Add(Symbol('lambda_var_0'), Rational(1, 262144))
		all_vals['skoSINS'] = Rational(12477, 16384)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_10 SAT")

			print("skoCOSS=", all_vals["skoCOSS"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSINS=", all_vals["skoSINS"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_11(delta=delta,skoS=skoS,pi=pi)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoS'] = skoS
		all_vals['pi'] = pi
		all_vals['skoCOSS'] = Rational(1, 262144)
		all_vals['skoSINS'] = Add(Symbol('lambda_var_0'), Rational(12477, 16384))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_11 SAT")

			print("skoCOSS=", all_vals["skoCOSS"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSINS=", all_vals["skoSINS"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_12(delta=delta,skoS=skoS,pi=pi)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoS'] = skoS
		all_vals['pi'] = pi
		all_vals['skoCOSS'] = Add(Symbol('lambda_var_0'), Rational(1, 524288))
		all_vals['skoSINS'] = Rational(49909, 65536)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_12 SAT")

			print("skoCOSS=", all_vals["skoCOSS"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSINS=", all_vals["skoSINS"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_13(delta=delta,skoS=skoS,pi=pi)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoS'] = skoS
		all_vals['pi'] = pi
		all_vals['skoCOSS'] = Rational(1, 524288)
		all_vals['skoSINS'] = Add(Symbol('lambda_var_0'), Rational(49909, 65536))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_13 SAT")

			print("skoCOSS=", all_vals["skoCOSS"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSINS=", all_vals["skoSINS"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_14(delta=delta,skoS=skoS,pi=pi)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoS'] = skoS
		all_vals['pi'] = pi
		all_vals['skoCOSS'] = Add(Symbol('lambda_var_0'), Rational(1, 4194304))
		all_vals['skoSINS'] = Rational(199637, 262144)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_14 SAT")

			print("skoCOSS=", all_vals["skoCOSS"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSINS=", all_vals["skoSINS"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_15(delta=delta,skoS=skoS,pi=pi)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoS'] = skoS
		all_vals['pi'] = pi
		all_vals['skoCOSS'] = Rational(1, 4194304)
		all_vals['skoSINS'] = Add(Symbol('lambda_var_0'), Rational(199637, 262144))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_15 SAT")

			print("skoCOSS=", all_vals["skoCOSS"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSINS=", all_vals["skoSINS"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_16(delta=delta,skoS=skoS,pi=pi)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoS'] = skoS
		all_vals['pi'] = pi
		all_vals['skoCOSS'] = Add(Symbol('lambda_var_0'), Rational(1, 134217728))
		all_vals['skoSINS'] = Rational(399275, 524288)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_16 SAT")

			print("skoCOSS=", all_vals["skoCOSS"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSINS=", all_vals["skoSINS"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_17(delta=delta,skoS=skoS,pi=pi)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoS'] = skoS
		all_vals['pi'] = pi
		all_vals['skoCOSS'] = Rational(1, 134217728)
		all_vals['skoSINS'] = Add(Symbol('lambda_var_0'), Rational(399275, 524288))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_17 SAT")

			print("skoCOSS=", all_vals["skoCOSS"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSINS=", all_vals["skoSINS"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_18(delta=delta,skoS=skoS,pi=pi)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoS'] = skoS
		all_vals['pi'] = pi
		all_vals['skoCOSS'] = Add(Symbol('lambda_var_0'), Rational(1, 536870912))
		all_vals['skoSINS'] = Rational(12776809, 16777216)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_18 SAT")

			print("skoCOSS=", all_vals["skoCOSS"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSINS=", all_vals["skoSINS"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_19(delta=delta,skoS=skoS,pi=pi)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoS'] = skoS
		all_vals['pi'] = pi
		all_vals['skoCOSS'] = Rational(1, 536870912)
		all_vals['skoSINS'] = Add(Symbol('lambda_var_0'), Rational(12776809, 16777216))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_19 SAT")

			print("skoCOSS=", all_vals["skoCOSS"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSINS=", all_vals["skoSINS"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_20(delta=delta,skoS=skoS,pi=pi)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoS'] = skoS
		all_vals['pi'] = pi
		all_vals['skoCOSS'] = Add(Symbol('lambda_var_0'), Rational(1, 2147483648))
		all_vals['skoSINS'] = Rational(51107237, 67108864)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_20 SAT")

			print("skoCOSS=", all_vals["skoCOSS"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSINS=", all_vals["skoSINS"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass


	print("UNKNOWN")
