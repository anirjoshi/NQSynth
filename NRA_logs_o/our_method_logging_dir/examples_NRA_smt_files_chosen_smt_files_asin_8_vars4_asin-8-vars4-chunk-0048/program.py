import sympy
from sympy import *
from NQS.helper_program_cav import get_lambda_val

def pre_condition_0(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(skoS2 > 0) & (skoX > 0) & (skoX - 1 < 0) & (delta + skoS2**2 - 2 >= 0) & (-delta + skoS2**2 - 2 <= 0) & (-15876*delta*skoS2**2 - 16380*delta*skoS2 - 4225*delta + 15876*skoS2**2*skoX + 16380*skoS2*skoX + 3024*skoS2 + 4225*skoX + 1416 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Add(Symbol('skoX'), Integer(-1)), Integer(0)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Integer(15876), Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Mul(Integer(-1), Integer(16380), Symbol('delta'), Symbol('skoS2')), Mul(Integer(-1), Integer(4225), Symbol('delta')), Mul(Integer(15876), Pow(Symbol('skoS2'), Integer(2)), Symbol('skoX')), Mul(Integer(16380), Symbol('skoS2'), Symbol('skoX')), Mul(Integer(3024), Symbol('skoS2')), Mul(Integer(4225), Symbol('skoX')), Integer(1416)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta > 0) & (skoS2 > 0) & (skoX > 0) & (skoX - 1 < 0) & (delta + skoS2**2 - 2 >= 0) & (-4*delta + 4*skoX + 3 <= 0) & (-delta + skoS2**2 - 2 <= 0)

	pre_cond = And(StrictGreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Add(Symbol('skoX'), Integer(-1)), Integer(0)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), LessThan(Add(Mul(Integer(-1), Integer(4), Symbol('delta')), Mul(Integer(4), Symbol('skoX')), Integer(3)), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta > 0) & (skoS2 > 0) & (skoX > 0) & (skoX - 1 < 0) & (delta + skoS2**2 - 2 >= 0) & (-1024*delta + 1024*skoX + 65 <= 0) & (-delta + skoS2**2 - 2 <= 0) & (-16257024*delta*skoS2**2 - 16773120*delta*skoS2 - 4326400*delta + 16257024*skoS2**2*skoX - 1031940*skoS2**2 + 16773120*skoS2*skoX + 2161908*skoS2 + 4326400*skoX + 1239351 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Add(Symbol('skoX'), Integer(-1)), Integer(0)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), LessThan(Add(Mul(Integer(-1), Integer(1024), Symbol('delta')), Mul(Integer(1024), Symbol('skoX')), Integer(65)), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Integer(16257024), Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Mul(Integer(-1), Integer(16773120), Symbol('delta'), Symbol('skoS2')), Mul(Integer(-1), Integer(4326400), Symbol('delta')), Mul(Integer(16257024), Pow(Symbol('skoS2'), Integer(2)), Symbol('skoX')), Mul(Integer(-1), Integer(1031940), Pow(Symbol('skoS2'), Integer(2))), Mul(Integer(16773120), Symbol('skoS2'), Symbol('skoX')), Mul(Integer(2161908), Symbol('skoS2')), Mul(Integer(4326400), Symbol('skoX')), Integer(1239351)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta > 0) & (skoS2 > 0) & (skoX > 0) & (skoX - 1 < 0) & (delta + skoS2**2 - 2 >= 0) & (-256*delta + 256*skoX + 31 <= 0) & (-delta + skoS2**2 - 2 <= 0)

	pre_cond = And(StrictGreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Add(Symbol('skoX'), Integer(-1)), Integer(0)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), LessThan(Add(Mul(Integer(-1), Integer(256), Symbol('delta')), Mul(Integer(256), Symbol('skoX')), Integer(31)), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_4(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta > 0) & (skoS2 > 0) & (skoX > 0) & (skoX - 1 < 0) & (delta + skoS2**2 - 2 >= 0) & (-4294967296*delta + 4294967296*skoX + 272494593 <= 0) & (-delta + skoS2**2 - 2 <= 0) & (-68186900791296*delta*skoS2**2 - 70351564308480*delta*skoS2 - 18146236825600*delta + 68186900791296*skoS2**2*skoX - 4326124158468*skoS2**2 + 70351564308480*skoS2*skoX + 9069645038580*skoS2 + 18146236825600*skoX + 5198653849975 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Add(Symbol('skoX'), Integer(-1)), Integer(0)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), LessThan(Add(Mul(Integer(-1), Integer(4294967296), Symbol('delta')), Mul(Integer(4294967296), Symbol('skoX')), Integer(272494593)), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Integer(68186900791296), Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Mul(Integer(-1), Integer(70351564308480), Symbol('delta'), Symbol('skoS2')), Mul(Integer(-1), Integer(18146236825600), Symbol('delta')), Mul(Integer(68186900791296), Pow(Symbol('skoS2'), Integer(2)), Symbol('skoX')), Mul(Integer(-1), Integer(4326124158468), Pow(Symbol('skoS2'), Integer(2))), Mul(Integer(70351564308480), Symbol('skoS2'), Symbol('skoX')), Mul(Integer(9069645038580), Symbol('skoS2')), Mul(Integer(18146236825600), Symbol('skoX')), Integer(5198653849975)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_5(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta > 0) & (skoS2 > 0) & (skoX > 0) & (skoX - 1 < 0) & (delta + skoS2**2 - 2 >= 0) & (-1073741824*delta + 1073741824*skoX + 68154303 <= 0) & (-delta + skoS2**2 - 2 <= 0) & (-17046725197824*delta*skoS2**2 - 16505559318528*delta*skoS2 - 3995393327104*delta + 17046725197824*skoS2**2*skoX - 1082017714428*skoS2**2 + 16505559318528*skoS2*skoX + 2060802068220*skoS2 + 3995393327104*skoX + 1402603715777 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Add(Symbol('skoX'), Integer(-1)), Integer(0)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), LessThan(Add(Mul(Integer(-1), Integer(1073741824), Symbol('delta')), Mul(Integer(1073741824), Symbol('skoX')), Integer(68154303)), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Integer(17046725197824), Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Mul(Integer(-1), Integer(16505559318528), Symbol('delta'), Symbol('skoS2')), Mul(Integer(-1), Integer(3995393327104), Symbol('delta')), Mul(Integer(17046725197824), Pow(Symbol('skoS2'), Integer(2)), Symbol('skoX')), Mul(Integer(-1), Integer(1082017714428), Pow(Symbol('skoS2'), Integer(2))), Mul(Integer(16505559318528), Symbol('skoS2'), Symbol('skoX')), Mul(Integer(2060802068220), Symbol('skoS2')), Mul(Integer(3995393327104), Symbol('skoX')), Integer(1402603715777)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_6(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta > 0) & (skoS2 > 0) & (skoX > 0) & (skoX - 1 < 0) & (delta + skoS2**2 - 2 >= 0) & (-16384*delta + 16384*skoX + 777 <= 0) & (-delta + skoS2**2 - 2 <= 0) & (-260112384*delta*skoS2**2 - 268369920*delta*skoS2 - 69222400*delta + 260112384*skoS2**2*skoX - 12335652*skoS2**2 + 268369920*skoS2*skoX + 38375316*skoS2 + 69222400*skoX + 20683311 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Add(Symbol('skoX'), Integer(-1)), Integer(0)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), LessThan(Add(Mul(Integer(-1), Integer(16384), Symbol('delta')), Mul(Integer(16384), Symbol('skoX')), Integer(777)), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Integer(260112384), Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Mul(Integer(-1), Integer(268369920), Symbol('delta'), Symbol('skoS2')), Mul(Integer(-1), Integer(69222400), Symbol('delta')), Mul(Integer(260112384), Pow(Symbol('skoS2'), Integer(2)), Symbol('skoX')), Mul(Integer(-1), Integer(12335652), Pow(Symbol('skoS2'), Integer(2))), Mul(Integer(268369920), Symbol('skoS2'), Symbol('skoX')), Mul(Integer(38375316), Symbol('skoS2')), Mul(Integer(69222400), Symbol('skoX')), Integer(20683311)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_7(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta > 0) & (skoS2 > 0) & (skoX > 0) & (skoX - 1 < 0) & (delta + skoS2**2 - 2 >= 0) & (-1024*delta + 1024*skoX + 63 <= 0) & (-delta + skoS2**2 - 2 <= 0) & (-16257024*delta*skoS2**2 - 15740928*delta*skoS2 - 3810304*delta + 16257024*skoS2**2*skoX - 1000188*skoS2**2 + 15740928*skoS2*skoX + 2000124*skoS2 + 3810304*skoX + 1347137 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Add(Symbol('skoX'), Integer(-1)), Integer(0)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), LessThan(Add(Mul(Integer(-1), Integer(1024), Symbol('delta')), Mul(Integer(1024), Symbol('skoX')), Integer(63)), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Integer(16257024), Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Mul(Integer(-1), Integer(15740928), Symbol('delta'), Symbol('skoS2')), Mul(Integer(-1), Integer(3810304), Symbol('delta')), Mul(Integer(16257024), Pow(Symbol('skoS2'), Integer(2)), Symbol('skoX')), Mul(Integer(-1), Integer(1000188), Pow(Symbol('skoS2'), Integer(2))), Mul(Integer(15740928), Symbol('skoS2'), Symbol('skoX')), Mul(Integer(2000124), Symbol('skoS2')), Mul(Integer(3810304), Symbol('skoX')), Integer(1347137)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_8(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta > 0) & (skoS2 > 0) & (skoX > 0) & (skoX - 1 < 0) & (delta + skoS2**2 - 2 >= 0) & (-262144*delta + 262144*skoX + 11385 <= 0) & (-delta + skoS2**2 - 2 <= 0) & (-4161798144*delta*skoS2**2 - 4293918720*delta*skoS2 - 1107558400*delta + 4161798144*skoS2**2*skoX - 180748260*skoS2**2 + 4293918720*skoS2*skoX + 629067348*skoS2 + 1107558400*skoX + 334329151 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Add(Symbol('skoX'), Integer(-1)), Integer(0)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), LessThan(Add(Mul(Integer(-1), Integer(262144), Symbol('delta')), Mul(Integer(262144), Symbol('skoX')), Integer(11385)), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Integer(4161798144), Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Mul(Integer(-1), Integer(4293918720), Symbol('delta'), Symbol('skoS2')), Mul(Integer(-1), Integer(1107558400), Symbol('delta')), Mul(Integer(4161798144), Pow(Symbol('skoS2'), Integer(2)), Symbol('skoX')), Mul(Integer(-1), Integer(180748260), Pow(Symbol('skoS2'), Integer(2))), Mul(Integer(4293918720), Symbol('skoS2'), Symbol('skoX')), Mul(Integer(629067348), Symbol('skoS2')), Mul(Integer(1107558400), Symbol('skoX')), Integer(334329151)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_9(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta > 0) & (skoS2 > 0) & (skoX > 0) & (skoX - 1 < 0) & (delta + skoS2**2 - 2 >= 0) & (-16384*delta + 16384*skoX + 759 <= 0) & (-delta + skoS2**2 - 2 <= 0) & (-260112384*delta*skoS2**2 - 251854848*delta*skoS2 - 60964864*delta + 260112384*skoS2**2*skoX - 12049884*skoS2**2 + 251854848*skoS2*skoX + 36338652*skoS2 + 60964864*skoX + 22739337 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Add(Symbol('skoX'), Integer(-1)), Integer(0)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), LessThan(Add(Mul(Integer(-1), Integer(16384), Symbol('delta')), Mul(Integer(16384), Symbol('skoX')), Integer(759)), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Integer(260112384), Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Mul(Integer(-1), Integer(251854848), Symbol('delta'), Symbol('skoS2')), Mul(Integer(-1), Integer(60964864), Symbol('delta')), Mul(Integer(260112384), Pow(Symbol('skoS2'), Integer(2)), Symbol('skoX')), Mul(Integer(-1), Integer(12049884), Pow(Symbol('skoS2'), Integer(2))), Mul(Integer(251854848), Symbol('skoS2'), Symbol('skoX')), Mul(Integer(36338652), Symbol('skoS2')), Mul(Integer(60964864), Symbol('skoX')), Integer(22739337)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_10(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta > 0) & (skoS2 > 0) & (skoX > 0) & (skoX - 1 < 0) & (delta + skoS2**2 - 2 >= 0) & (-1073741824*delta + 1073741824*skoX + 46566017 <= 0) & (-delta + skoS2**2 - 2 <= 0) & (-17046725197824*delta*skoS2**2 - 17587891077120*delta*skoS2 - 4536559206400*delta + 17046725197824*skoS2**2*skoX - 739282085892*skoS2**2 + 17587891077120*skoS2*skoX + 2577622844916*skoS2 + 4536559206400*skoX + 1369629315831 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Add(Symbol('skoX'), Integer(-1)), Integer(0)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), LessThan(Add(Mul(Integer(-1), Integer(1073741824), Symbol('delta')), Mul(Integer(1073741824), Symbol('skoX')), Integer(46566017)), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Integer(17046725197824), Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Mul(Integer(-1), Integer(17587891077120), Symbol('delta'), Symbol('skoS2')), Mul(Integer(-1), Integer(4536559206400), Symbol('delta')), Mul(Integer(17046725197824), Pow(Symbol('skoS2'), Integer(2)), Symbol('skoX')), Mul(Integer(-1), Integer(739282085892), Pow(Symbol('skoS2'), Integer(2))), Mul(Integer(17587891077120), Symbol('skoS2'), Symbol('skoX')), Mul(Integer(2577622844916), Symbol('skoS2')), Mul(Integer(4536559206400), Symbol('skoX')), Integer(1369629315831)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_11(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta > 0) & (skoS2 > 0) & (skoX > 0) & (skoX - 1 < 0) & (delta + skoS2**2 - 2 >= 0) & (-262144*delta + 262144*skoX + 11143 <= 0) & (-delta + skoS2**2 - 2 <= 0) & (-4161798144*delta*skoS2**2 - 4029677568*delta*skoS2 - 975437824*delta + 4161798144*skoS2**2*skoX - 176906268*skoS2**2 + 4029677568*skoS2*skoX + 598847004*skoS2 + 975437824*skoX + 368591097 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Add(Symbol('skoX'), Integer(-1)), Integer(0)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), LessThan(Add(Mul(Integer(-1), Integer(262144), Symbol('delta')), Mul(Integer(262144), Symbol('skoX')), Integer(11143)), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Integer(4161798144), Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Mul(Integer(-1), Integer(4029677568), Symbol('delta'), Symbol('skoS2')), Mul(Integer(-1), Integer(975437824), Symbol('delta')), Mul(Integer(4161798144), Pow(Symbol('skoS2'), Integer(2)), Symbol('skoX')), Mul(Integer(-1), Integer(176906268), Pow(Symbol('skoS2'), Integer(2))), Mul(Integer(4029677568), Symbol('skoS2'), Symbol('skoX')), Mul(Integer(598847004), Symbol('skoS2')), Mul(Integer(975437824), Symbol('skoX')), Integer(368591097)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_12(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta > 0) & (skoS2 > 0) & (skoX > 0) & (skoX - 1 < 0) & (delta + skoS2**2 - 2 >= 0) & (-1073741824*delta + 1073741824*skoX + 45629025 <= 0) & (-delta + skoS2**2 - 2 <= 0) & (-17046725197824*delta*skoS2**2 - 17587891077120*delta*skoS2 - 4536559206400*delta + 17046725197824*skoS2**2*skoX - 724406400900*skoS2**2 + 17587891077120*skoS2*skoX + 2591101441908*skoS2 + 4536559206400*skoX + 1372668121111 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Add(Symbol('skoX'), Integer(-1)), Integer(0)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), LessThan(Add(Mul(Integer(-1), Integer(1073741824), Symbol('delta')), Mul(Integer(1073741824), Symbol('skoX')), Integer(45629025)), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Integer(17046725197824), Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Mul(Integer(-1), Integer(17587891077120), Symbol('delta'), Symbol('skoS2')), Mul(Integer(-1), Integer(4536559206400), Symbol('delta')), Mul(Integer(17046725197824), Pow(Symbol('skoS2'), Integer(2)), Symbol('skoX')), Mul(Integer(-1), Integer(724406400900), Pow(Symbol('skoS2'), Integer(2))), Mul(Integer(17587891077120), Symbol('skoS2'), Symbol('skoX')), Mul(Integer(2591101441908), Symbol('skoS2')), Mul(Integer(4536559206400), Symbol('skoX')), Integer(1372668121111)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_13(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta > 0) & (skoS2 > 0) & (skoX > 0) & (skoX - 1 < 0) & (delta + skoS2**2 - 2 >= 0) & (-1073741824*delta + 1073741824*skoX + 45577599 <= 0) & (-delta + skoS2**2 - 2 <= 0) & (-17046725197824*delta*skoS2**2 - 16505559318528*delta*skoS2 - 3995393327104*delta + 17046725197824*skoS2**2*skoX - 723589961724*skoS2**2 + 16505559318528*skoS2*skoX + 2453993821692*skoS2 + 3995393327104*skoX + 1510054157057 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Add(Symbol('skoX'), Integer(-1)), Integer(0)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), LessThan(Add(Mul(Integer(-1), Integer(1073741824), Symbol('delta')), Mul(Integer(1073741824), Symbol('skoX')), Integer(45577599)), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Integer(17046725197824), Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Mul(Integer(-1), Integer(16505559318528), Symbol('delta'), Symbol('skoS2')), Mul(Integer(-1), Integer(3995393327104), Symbol('delta')), Mul(Integer(17046725197824), Pow(Symbol('skoS2'), Integer(2)), Symbol('skoX')), Mul(Integer(-1), Integer(723589961724), Pow(Symbol('skoS2'), Integer(2))), Mul(Integer(16505559318528), Symbol('skoS2'), Symbol('skoX')), Mul(Integer(2453993821692), Symbol('skoS2')), Mul(Integer(3995393327104), Symbol('skoX')), Integer(1510054157057)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_14(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta > 0) & (skoS2 > 0) & (skoX > 0) & (skoX - 1 < 0) & (delta + skoS2**2 - 2 >= 0) & (-68719476736*delta + 68719476736*skoX + 2916510465 <= 0) & (-delta + skoS2**2 - 2 <= 0) & (-1090990412660736*delta*skoS2**2 - 1125625028935680*delta*skoS2 - 290339789209600*delta + 1090990412660736*skoS2**2*skoX - 46302520142340*skoS2**2 + 1125625028935680*skoS2*skoX + 165884393865204*skoS2 + 290339789209600*skoX + 87862911872631 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Add(Symbol('skoX'), Integer(-1)), Integer(0)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), LessThan(Add(Mul(Integer(-1), Integer(68719476736), Symbol('delta')), Mul(Integer(68719476736), Symbol('skoX')), Integer(2916510465)), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Integer(1090990412660736), Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Mul(Integer(-1), Integer(1125625028935680), Symbol('delta'), Symbol('skoS2')), Mul(Integer(-1), Integer(290339789209600), Symbol('delta')), Mul(Integer(1090990412660736), Pow(Symbol('skoS2'), Integer(2)), Symbol('skoX')), Mul(Integer(-1), Integer(46302520142340), Pow(Symbol('skoS2'), Integer(2))), Mul(Integer(1125625028935680), Symbol('skoS2'), Symbol('skoX')), Mul(Integer(165884393865204), Symbol('skoS2')), Mul(Integer(290339789209600), Symbol('skoX')), Integer(87862911872631)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(delta:sympy.Rational, skoX:sympy.Rational, skoS2:sympy.Rational, skoSP:sympy.Rational, skoSM:sympy.Rational):
	# (0 <= delta) & (1 > skoX) & (skoS2 > 0) & (skoSM > 0) & (skoSP > 0) & (skoX > 0) & (skoS2**2 - 2 <= delta) & (skoSM**2 + skoX - 1 <= delta) & (2 - skoS2**2 <= delta) & (-skoSP**2 + skoX + 1 <= delta) & (skoSP**2 - skoX - 1 <= delta) & (-skoSM**2 - skoX + 1 <= delta) & (skoSP*(-63*skoS2/20 - 13/8) > skoSM*(-63*skoS2/20 - 61/40) + 1/5)

	post_cond =  And(LessThan(Integer(0), Symbol('delta')), StrictGreaterThan(Integer(1), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoSP'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), LessThan(Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Symbol('delta')), LessThan(Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1)), Symbol('delta')), LessThan(Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Symbol('delta')), LessThan(Add(Mul(Integer(-1), Pow(Symbol('skoSP'), Integer(2))), Symbol('skoX'), Integer(1)), Symbol('delta')), LessThan(Add(Pow(Symbol('skoSP'), Integer(2)), Mul(Integer(-1), Symbol('skoX')), Integer(-1)), Symbol('delta')), LessThan(Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)), Symbol('delta')), StrictGreaterThan(Mul(Symbol('skoSP'), Add(Mul(Integer(-1), Rational(63, 20), Symbol('skoS2')), Rational(-13, 8))), Add(Mul(Symbol('skoSM'), Add(Mul(Integer(-1), Rational(63, 20), Symbol('skoS2')), Rational(-61, 40))), Rational(1, 5))))

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


	post_cond =  And(LessThan(Integer(0), Symbol('delta')), StrictGreaterThan(Integer(1), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoSP'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), LessThan(Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Symbol('delta')), LessThan(Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1)), Symbol('delta')), LessThan(Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Symbol('delta')), LessThan(Add(Mul(Integer(-1), Pow(Symbol('skoSP'), Integer(2))), Symbol('skoX'), Integer(1)), Symbol('delta')), LessThan(Add(Pow(Symbol('skoSP'), Integer(2)), Mul(Integer(-1), Symbol('skoX')), Integer(-1)), Symbol('delta')), LessThan(Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)), Symbol('delta')), StrictGreaterThan(Mul(Symbol('skoSP'), Add(Mul(Integer(-1), Rational(63, 20), Symbol('skoS2')), Rational(-13, 8))), Add(Mul(Symbol('skoSM'), Add(Mul(Integer(-1), Rational(63, 20), Symbol('skoS2')), Rational(-61, 40))), Rational(1, 5))))

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
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(1, 2))
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
		all_vals['skoSP'] = Rational(1, 2)
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
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(15, 16))
		all_vals['skoSM'] = Rational(33, 32)
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
		all_vals['skoSP'] = Rational(15, 16)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(33, 32))
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
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(31711, 32768))
		all_vals['skoSM'] = Rational(67583, 65536)
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
		all_vals['skoSP'] = Rational(31711, 32768)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(67583, 65536))
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
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(31, 32))
		all_vals['skoSM'] = Rational(131, 128)
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
		all_vals['skoSP'] = Rational(31, 32)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(131, 128))
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
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(125, 128))
		all_vals['skoSM'] = Rational(523, 512)
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
		all_vals['skoSP'] = Rational(125, 128)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(523, 512))
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
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(501, 512))
		all_vals['skoSM'] = Rational(33471, 32768)
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
		all_vals['skoSP'] = Rational(501, 512)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(33471, 32768))
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
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(32065, 32768))
		all_vals['skoSM'] = Rational(33457, 32768)
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
		all_vals['skoSP'] = Rational(32065, 32768)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(33457, 32768))
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
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(64131, 65536))
		all_vals['skoSM'] = Rational(267649, 262144)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_14 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass


	print("UNKNOWN")
