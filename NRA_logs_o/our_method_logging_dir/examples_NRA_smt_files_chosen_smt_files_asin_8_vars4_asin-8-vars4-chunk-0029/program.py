import sympy
from sympy import *
from NQS.helper_program_cav import get_lambda_val

def pre_condition_0(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(skoS2 > 0) & (skoX > 0) & (skoX - 1 < 0) & (delta + skoS2**2 - 2 >= 0) & (-delta + skoS2**2 - 2 <= 0) & (-15876*delta*skoS2**2 - 16380*delta*skoS2 - 4225*delta + 15876*skoS2**2*skoX + 16380*skoS2*skoX + 3024*skoS2 + 4225*skoX + 1416 <= 0)

	pre_cond = And(StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Add(Symbol('skoX'), Integer(-1)), Integer(0)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), LessThan(Add(Mul(Integer(-1), Integer(15876), Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Mul(Integer(-1), Integer(16380), Symbol('delta'), Symbol('skoS2')), Mul(Integer(-1), Integer(4225), Symbol('delta')), Mul(Integer(15876), Pow(Symbol('skoS2'), Integer(2)), Symbol('skoX')), Mul(Integer(16380), Symbol('skoS2'), Symbol('skoX')), Mul(Integer(3024), Symbol('skoS2')), Mul(Integer(4225), Symbol('skoX')), Integer(1416)), Integer(0)))

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
	#(delta > 0) & (skoS2 > 0) & (skoX > 0) & (skoX - 1 < 0) & (delta + skoS2**2 - 2 >= 0) & (-1024*delta + 1024*skoX + 65 <= 0) & (-delta + skoS2**2 - 2 <= 0) & (-16257024*delta*skoS2**2 - 16773120*delta*skoS2 - 4326400*delta + 16257024*skoS2**2*skoX - 1031940*skoS2**2 + 16773120*skoS2*skoX + 2161908*skoS2 + 4326400*skoX + 1239351 <= 0)

	pre_cond = And(StrictGreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Add(Symbol('skoX'), Integer(-1)), Integer(0)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), LessThan(Add(Mul(Integer(-1), Integer(1024), Symbol('delta')), Mul(Integer(1024), Symbol('skoX')), Integer(65)), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), LessThan(Add(Mul(Integer(-1), Integer(16257024), Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Mul(Integer(-1), Integer(16773120), Symbol('delta'), Symbol('skoS2')), Mul(Integer(-1), Integer(4326400), Symbol('delta')), Mul(Integer(16257024), Pow(Symbol('skoS2'), Integer(2)), Symbol('skoX')), Mul(Integer(-1), Integer(1031940), Pow(Symbol('skoS2'), Integer(2))), Mul(Integer(16773120), Symbol('skoS2'), Symbol('skoX')), Mul(Integer(2161908), Symbol('skoS2')), Mul(Integer(4326400), Symbol('skoX')), Integer(1239351)), Integer(0)))

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
	#(delta > 0) & (skoS2 > 0) & (skoX > 0) & (skoX - 1 < 0) & (delta + skoS2**2 - 2 >= 0) & (-1048576*delta + 1048576*skoX + 68673 <= 0) & (-delta + skoS2**2 - 2 <= 0)

	pre_cond = And(StrictGreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Add(Symbol('skoX'), Integer(-1)), Integer(0)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), LessThan(Add(Mul(Integer(-1), Integer(1048576), Symbol('delta')), Mul(Integer(1048576), Symbol('skoX')), Integer(68673)), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_5(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta > 0) & (skoS2 > 0) & (skoX > 0) & (skoX - 1 < 0) & (delta + skoS2**2 - 2 >= 0) & (-262144*delta + 262144*skoX + 17119 <= 0) & (-delta + skoS2**2 - 2 <= 0)

	pre_cond = And(StrictGreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Add(Symbol('skoX'), Integer(-1)), Integer(0)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), LessThan(Add(Mul(Integer(-1), Integer(262144), Symbol('delta')), Mul(Integer(262144), Symbol('skoX')), Integer(17119)), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_6(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta > 0) & (skoS2 > 0) & (skoX > 0) & (skoX - 1 < 0) & (delta + skoS2**2 - 2 >= 0) & (-4194304*delta + 4194304*skoX + 270465 <= 0) & (-delta + skoS2**2 - 2 <= 0) & (-66588770304*delta*skoS2**2 - 68702699520*delta*skoS2 - 17720934400*delta + 66588770304*skoS2**2*skoX - 4293902340*skoS2**2 + 68702699520*skoS2*skoX + 8794357236*skoS2 + 17720934400*skoX + 5062659319 <= 0)

	pre_cond = And(StrictGreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Add(Symbol('skoX'), Integer(-1)), Integer(0)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), LessThan(Add(Mul(Integer(-1), Integer(4194304), Symbol('delta')), Mul(Integer(4194304), Symbol('skoX')), Integer(270465)), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), LessThan(Add(Mul(Integer(-1), Integer(66588770304), Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Mul(Integer(-1), Integer(68702699520), Symbol('delta'), Symbol('skoS2')), Mul(Integer(-1), Integer(17720934400), Symbol('delta')), Mul(Integer(66588770304), Pow(Symbol('skoS2'), Integer(2)), Symbol('skoX')), Mul(Integer(-1), Integer(4293902340), Pow(Symbol('skoS2'), Integer(2))), Mul(Integer(68702699520), Symbol('skoS2'), Symbol('skoX')), Mul(Integer(8794357236), Symbol('skoS2')), Mul(Integer(17720934400), Symbol('skoX')), Integer(5062659319)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_7(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta > 0) & (skoS2 > 0) & (skoX > 0) & (skoX - 1 < 0) & (delta + skoS2**2 - 2 >= 0) & (-268435456*delta + 268435456*skoX + 17498175 <= 0) & (-delta + skoS2**2 - 2 <= 0)

	pre_cond = And(StrictGreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Add(Symbol('skoX'), Integer(-1)), Integer(0)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), LessThan(Add(Mul(Integer(-1), Integer(268435456), Symbol('delta')), Mul(Integer(268435456), Symbol('skoX')), Integer(17498175)), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_8(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta > 0) & (skoS2 > 0) & (skoX > 0) & (skoX - 1 < 0) & (delta + skoS2**2 - 2 >= 0) & (-16777216*delta + 16777216*skoX + 1090313 <= 0) & (-delta + skoS2**2 - 2 <= 0)

	pre_cond = And(StrictGreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Add(Symbol('skoX'), Integer(-1)), Integer(0)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), LessThan(Add(Mul(Integer(-1), Integer(16777216), Symbol('delta')), Mul(Integer(16777216), Symbol('skoX')), Integer(1090313)), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_9(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta > 0) & (skoS2 > 0) & (skoX > 0) & (skoX - 1 < 0) & (delta + skoS2**2 - 2 >= 0) & (-16777216*delta + 16777216*skoX + 1087695 <= 0) & (-delta + skoS2**2 - 2 <= 0) & (-266355081216*delta*skoS2**2 - 257899364352*delta*skoS2 - 62428020736*delta + 266355081216*skoS2**2*skoX - 17268245820*skoS2**2 + 257899364352*skoS2*skoX + 31803089724*skoS2 + 62428020736*skoX + 21807173553 <= 0)

	pre_cond = And(StrictGreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Add(Symbol('skoX'), Integer(-1)), Integer(0)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), LessThan(Add(Mul(Integer(-1), Integer(16777216), Symbol('delta')), Mul(Integer(16777216), Symbol('skoX')), Integer(1087695)), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), LessThan(Add(Mul(Integer(-1), Integer(266355081216), Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Mul(Integer(-1), Integer(257899364352), Symbol('delta'), Symbol('skoS2')), Mul(Integer(-1), Integer(62428020736), Symbol('delta')), Mul(Integer(266355081216), Pow(Symbol('skoS2'), Integer(2)), Symbol('skoX')), Mul(Integer(-1), Integer(17268245820), Pow(Symbol('skoS2'), Integer(2))), Mul(Integer(257899364352), Symbol('skoS2'), Symbol('skoX')), Mul(Integer(31803089724), Symbol('skoS2')), Mul(Integer(62428020736), Symbol('skoX')), Integer(21807173553)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_10(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta > 0) & (skoS2 > 0) & (skoX > 0) & (skoX - 1 < 0) & (delta + skoS2**2 - 2 >= 0) & (-1073741824*delta + 1073741824*skoX + 69577145 <= 0) & (-delta + skoS2**2 - 2 <= 0) & (-17046725197824*delta*skoS2**2 - 17587891077120*delta*skoS2 - 4536559206400*delta + 17046725197824*skoS2**2*skoX - 1104606754020*skoS2**2 + 17587891077120*skoS2*skoX + 2246488403796*skoS2 + 4536559206400*skoX + 1294942604799 <= 0)

	pre_cond = And(StrictGreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Add(Symbol('skoX'), Integer(-1)), Integer(0)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), LessThan(Add(Mul(Integer(-1), Integer(1073741824), Symbol('delta')), Mul(Integer(1073741824), Symbol('skoX')), Integer(69577145)), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), LessThan(Add(Mul(Integer(-1), Integer(17046725197824), Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Mul(Integer(-1), Integer(17587891077120), Symbol('delta'), Symbol('skoS2')), Mul(Integer(-1), Integer(4536559206400), Symbol('delta')), Mul(Integer(17046725197824), Pow(Symbol('skoS2'), Integer(2)), Symbol('skoX')), Mul(Integer(-1), Integer(1104606754020), Pow(Symbol('skoS2'), Integer(2))), Mul(Integer(17587891077120), Symbol('skoS2'), Symbol('skoX')), Mul(Integer(2246488403796), Symbol('skoS2')), Mul(Integer(4536559206400), Symbol('skoX')), Integer(1294942604799)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_11(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta > 0) & (skoS2 > 0) & (skoX > 0) & (skoX - 1 < 0) & (delta + skoS2**2 - 2 >= 0) & (-4294967296*delta + 4294967296*skoX + 278323167 <= 0) & (-delta + skoS2**2 - 2 <= 0) & (-68186900791296*delta*skoS2**2 - 66022237274112*delta*skoS2 - 15981573308416*delta + 68186900791296*skoS2**2*skoX - 4418658599292*skoS2**2 + 66022237274112*skoS2*skoX + 8143799304060*skoS2 + 15981573308416*skoX + 5583240118433 <= 0)

	pre_cond = And(StrictGreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Add(Symbol('skoX'), Integer(-1)), Integer(0)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), LessThan(Add(Mul(Integer(-1), Integer(4294967296), Symbol('delta')), Mul(Integer(4294967296), Symbol('skoX')), Integer(278323167)), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), LessThan(Add(Mul(Integer(-1), Integer(68186900791296), Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Mul(Integer(-1), Integer(66022237274112), Symbol('delta'), Symbol('skoS2')), Mul(Integer(-1), Integer(15981573308416), Symbol('delta')), Mul(Integer(68186900791296), Pow(Symbol('skoS2'), Integer(2)), Symbol('skoX')), Mul(Integer(-1), Integer(4418658599292), Pow(Symbol('skoS2'), Integer(2))), Mul(Integer(66022237274112), Symbol('skoS2'), Symbol('skoX')), Mul(Integer(8143799304060), Symbol('skoS2')), Mul(Integer(15981573308416), Symbol('skoX')), Integer(5583240118433)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_12(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta > 0) & (skoS2 > 0) & (skoX > 0) & (skoX - 1 < 0) & (delta + skoS2**2 - 2 >= 0) & (-4294967296*delta + 4294967296*skoX + 278443833 <= 0) & (-delta + skoS2**2 - 2 <= 0) & (-68186900791296*delta*skoS2**2 - 70351564308480*delta*skoS2 - 18146236825600*delta + 68186900791296*skoS2**2*skoX - 4420574292708*skoS2**2 + 70351564308480*skoS2*skoX + 8984006626644*skoS2 + 18146236825600*skoX + 5179331105919 <= 0)

	pre_cond = And(StrictGreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Add(Symbol('skoX'), Integer(-1)), Integer(0)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), LessThan(Add(Mul(Integer(-1), Integer(4294967296), Symbol('delta')), Mul(Integer(4294967296), Symbol('skoX')), Integer(278443833)), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), LessThan(Add(Mul(Integer(-1), Integer(68186900791296), Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Mul(Integer(-1), Integer(70351564308480), Symbol('delta'), Symbol('skoS2')), Mul(Integer(-1), Integer(18146236825600), Symbol('delta')), Mul(Integer(68186900791296), Pow(Symbol('skoS2'), Integer(2)), Symbol('skoX')), Mul(Integer(-1), Integer(4420574292708), Pow(Symbol('skoS2'), Integer(2))), Mul(Integer(70351564308480), Symbol('skoS2'), Symbol('skoX')), Mul(Integer(8984006626644), Symbol('skoS2')), Mul(Integer(18146236825600), Symbol('skoX')), Integer(5179331105919)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_13(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta > 0) & (skoS2 > 0) & (skoX > 0) & (skoX - 1 < 0) & (delta + skoS2**2 - 2 >= 0) & (-17179869184*delta + 17179869184*skoX + 1113546175 <= 0) & (-delta + skoS2**2 - 2 <= 0) & (-272747603165184*delta*skoS2**2 - 264088949096448*delta*skoS2 - 63926293233664*delta + 272747603165184*skoS2**2*skoX - 17678659074300*skoS2**2 + 264088949096448*skoS2*skoX + 32570780530428*skoS2 + 63926293233664*skoX + 22331753091777 <= 0)

	pre_cond = And(StrictGreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Add(Symbol('skoX'), Integer(-1)), Integer(0)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), LessThan(Add(Mul(Integer(-1), Integer(17179869184), Symbol('delta')), Mul(Integer(17179869184), Symbol('skoX')), Integer(1113546175)), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), LessThan(Add(Mul(Integer(-1), Integer(272747603165184), Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Mul(Integer(-1), Integer(264088949096448), Symbol('delta'), Symbol('skoS2')), Mul(Integer(-1), Integer(63926293233664), Symbol('delta')), Mul(Integer(272747603165184), Pow(Symbol('skoS2'), Integer(2)), Symbol('skoX')), Mul(Integer(-1), Integer(17678659074300), Pow(Symbol('skoS2'), Integer(2))), Mul(Integer(264088949096448), Symbol('skoS2'), Symbol('skoX')), Mul(Integer(32570780530428), Symbol('skoS2')), Mul(Integer(63926293233664), Symbol('skoX')), Integer(22331753091777)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_14(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta > 0) & (skoS2 > 0) & (skoX > 0) & (skoX - 1 < 0) & (delta + skoS2**2 - 2 >= 0) & (-4398046511104*delta + 4398046511104*skoX + 285130813121 <= 0) & (-delta + skoS2**2 - 2 <= 0) & (-69823386410287104*delta*skoS2**2 - 72040001851883520*delta*skoS2 - 18581746509414400*delta + 69823386410287104*skoS2**2*skoX - 4526736789108996*skoS2**2 + 72040001851883520*skoS2*skoX + 9199560481542900*skoS2 + 18581746509414400*skoX + 5303620994313399 <= 0)

	pre_cond = And(StrictGreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Add(Symbol('skoX'), Integer(-1)), Integer(0)), GreaterThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), LessThan(Add(Mul(Integer(-1), Integer(4398046511104), Symbol('delta')), Mul(Integer(4398046511104), Symbol('skoX')), Integer(285130813121)), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), LessThan(Add(Mul(Integer(-1), Integer(69823386410287104), Symbol('delta'), Pow(Symbol('skoS2'), Integer(2))), Mul(Integer(-1), Integer(72040001851883520), Symbol('delta'), Symbol('skoS2')), Mul(Integer(-1), Integer(18581746509414400), Symbol('delta')), Mul(Integer(69823386410287104), Pow(Symbol('skoS2'), Integer(2)), Symbol('skoX')), Mul(Integer(-1), Integer(4526736789108996), Pow(Symbol('skoS2'), Integer(2))), Mul(Integer(72040001851883520), Symbol('skoS2'), Symbol('skoX')), Mul(Integer(9199560481542900), Symbol('skoS2')), Mul(Integer(18581746509414400), Symbol('skoX')), Integer(5303620994313399)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(delta:sympy.Rational, skoX:sympy.Rational, skoS2:sympy.Rational, skoSP:sympy.Rational, skoSM:sympy.Rational):
	# (0 <= delta) & (1 > skoX) & (skoS2 > 0) & (skoSM > 0) & (skoSP > 0) & (skoX > 0) & (skoS2**2 - 2 <= delta) & (skoSM**2 + skoX - 1 <= delta) & (2 - skoS2**2 <= delta) & (-skoSP**2 + skoX + 1 <= delta) & (skoSP**2 - skoX - 1 <= delta) & (-skoSM**2 - skoX + 1 <= delta) & (skoSP*(63*skoS2/20 + 13/8) <= skoSM*(63*skoS2/20 + 61/40) - 1/5)

	post_cond =  And(LessThan(Integer(0), Symbol('delta')), StrictGreaterThan(Integer(1), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoSP'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), LessThan(Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Symbol('delta')), LessThan(Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1)), Symbol('delta')), LessThan(Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Symbol('delta')), LessThan(Add(Mul(Integer(-1), Pow(Symbol('skoSP'), Integer(2))), Symbol('skoX'), Integer(1)), Symbol('delta')), LessThan(Add(Pow(Symbol('skoSP'), Integer(2)), Mul(Integer(-1), Symbol('skoX')), Integer(-1)), Symbol('delta')), LessThan(Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)), Symbol('delta')), LessThan(Mul(Symbol('skoSP'), Add(Mul(Rational(63, 20), Symbol('skoS2')), Rational(13, 8))), Add(Mul(Symbol('skoSM'), Add(Mul(Rational(63, 20), Symbol('skoS2')), Rational(61, 40))), Rational(-1, 5))))

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


	post_cond =  And(LessThan(Integer(0), Symbol('delta')), StrictGreaterThan(Integer(1), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoSP'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), LessThan(Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Symbol('delta')), LessThan(Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1)), Symbol('delta')), LessThan(Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Symbol('delta')), LessThan(Add(Mul(Integer(-1), Pow(Symbol('skoSP'), Integer(2))), Symbol('skoX'), Integer(1)), Symbol('delta')), LessThan(Add(Pow(Symbol('skoSP'), Integer(2)), Mul(Integer(-1), Symbol('skoX')), Integer(-1)), Symbol('delta')), LessThan(Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)), Symbol('delta')), LessThan(Mul(Symbol('skoSP'), Add(Mul(Rational(63, 20), Symbol('skoS2')), Rational(13, 8))), Add(Mul(Symbol('skoSM'), Add(Mul(Rational(63, 20), Symbol('skoS2')), Rational(61, 40))), Rational(-1, 5))))

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
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(495, 512))
		all_vals['skoSM'] = Rational(1057, 1024)
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
		all_vals['skoSP'] = Rational(495, 512)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(1057, 1024))
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
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(15841, 16384))
		all_vals['skoSM'] = Rational(2113, 2048)
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
		all_vals['skoSP'] = Rational(15841, 16384)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(2113, 2048))
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
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(3961, 4096))
		all_vals['skoSM'] = Rational(4227, 4096)
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
		all_vals['skoSP'] = Rational(3961, 4096)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(4227, 4096))
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
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(63377, 65536))
		all_vals['skoSM'] = Rational(33813, 32768)
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
		all_vals['skoSP'] = Rational(63377, 65536)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(33813, 32768))
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
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(126753, 131072))
		all_vals['skoSM'] = Rational(67627, 65536)
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
		all_vals['skoSP'] = Rational(126753, 131072)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(67627, 65536))
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
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(4056065, 4194304))
		all_vals['skoSM'] = Rational(2164065, 2097152)
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
