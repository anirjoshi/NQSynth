import sympy
from sympy import *
from NQS.helper_program_cav import get_lambda_val

def pre_condition_0(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi - 2*skoS > 0) & (skoS**3 + 3*skoS**2 <= 1)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Add(Symbol('pi'), Mul(Integer(-1), Integer(2), Symbol('skoS'))), Integer(0)), LessThan(Add(Pow(Symbol('skoS'), Integer(3)), Mul(Integer(3), Pow(Symbol('skoS'), Integer(2)))), Integer(1)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#((delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi - 2*skoS > 0) & (4*skoS**3 + 16*skoS**2 - skoS <= 55/8)) | ((delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi - 2*skoS > 0) & (skoS**3 + 4*skoS**2 - 2*skoS >= 13/4) & (8*skoS**6 + 32*skoS**5 - 96*skoS**4 - 460*skoS**3 - 233*skoS**2 + 222*skoS >= -279/2))

	pre_cond = Or(And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Add(Symbol('pi'), Mul(Integer(-1), Integer(2), Symbol('skoS'))), Integer(0)), LessThan(Add(Mul(Integer(4), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(16), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Symbol('skoS'))), Rational(55, 8))), And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Add(Symbol('pi'), Mul(Integer(-1), Integer(2), Symbol('skoS'))), Integer(0)), GreaterThan(Add(Pow(Symbol('skoS'), Integer(3)), Mul(Integer(4), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(2), Symbol('skoS'))), Rational(13, 4)), GreaterThan(Add(Mul(Integer(8), Pow(Symbol('skoS'), Integer(6))), Mul(Integer(32), Pow(Symbol('skoS'), Integer(5))), Mul(Integer(-1), Integer(96), Pow(Symbol('skoS'), Integer(4))), Mul(Integer(-1), Integer(460), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(-1), Integer(233), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(222), Symbol('skoS'))), Rational(-279, 2))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 11/16) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi - 2*skoS > 0) & (688*skoS**3 + 1888*skoS**2 - 583*skoS <= 919)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(11, 16)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Add(Symbol('pi'), Mul(Integer(-1), Integer(2), Symbol('skoS'))), Integer(0)), LessThan(Add(Mul(Integer(688), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(1888), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(583), Symbol('skoS'))), Integer(919)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#((delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi - 2*skoS > 0) & (512*skoS**3 + 2048*skoS**2 - 509*skoS <= 1047551/1024)) | ((delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi - 2*skoS > 0) & (skoS**3 + 4*skoS**2 - 2*skoS >= 1537/512) & (131072*skoS**6 + 524288*skoS**5 - 1572864*skoS**4 - 7081472*skoS**3 - 2630657*skoS**2 + 4190206*skoS >= -4457471/2))

	pre_cond = Or(And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Add(Symbol('pi'), Mul(Integer(-1), Integer(2), Symbol('skoS'))), Integer(0)), LessThan(Add(Mul(Integer(512), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(2048), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(509), Symbol('skoS'))), Rational(1047551, 1024))), And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Add(Symbol('pi'), Mul(Integer(-1), Integer(2), Symbol('skoS'))), Integer(0)), GreaterThan(Add(Pow(Symbol('skoS'), Integer(3)), Mul(Integer(4), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(2), Symbol('skoS'))), Rational(1537, 512)), GreaterThan(Add(Mul(Integer(131072), Pow(Symbol('skoS'), Integer(6))), Mul(Integer(524288), Pow(Symbol('skoS'), Integer(5))), Mul(Integer(-1), Integer(1572864), Pow(Symbol('skoS'), Integer(4))), Mul(Integer(-1), Integer(7081472), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(-1), Integer(2630657), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(4190206), Symbol('skoS'))), Rational(-4457471, 2))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_4(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 97/128) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi - 2*skoS > 0) & (45184*skoS**3 + 123136*skoS**2 - 40255*skoS <= 60607)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(97, 128)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Add(Symbol('pi'), Mul(Integer(-1), Integer(2), Symbol('skoS'))), Integer(0)), LessThan(Add(Mul(Integer(45184), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(123136), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(40255), Symbol('skoS'))), Integer(60607)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_5(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#((delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi - 2*skoS > 0) & (2048*skoS**3 + 8192*skoS**2 - 2045*skoS <= 16773119/4096)) | ((delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi - 2*skoS > 0) & (skoS**3 + 4*skoS**2 - 2*skoS >= 6145/2048) & (2097152*skoS**6 + 8388608*skoS**5 - 25165824*skoS**4 - 113260544*skoS**3 - 41979905*skoS**2 + 67092478*skoS >= -71307263/2))

	pre_cond = Or(And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Add(Symbol('pi'), Mul(Integer(-1), Integer(2), Symbol('skoS'))), Integer(0)), LessThan(Add(Mul(Integer(2048), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(8192), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(2045), Symbol('skoS'))), Rational(16773119, 4096))), And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Add(Symbol('pi'), Mul(Integer(-1), Integer(2), Symbol('skoS'))), Integer(0)), GreaterThan(Add(Pow(Symbol('skoS'), Integer(3)), Mul(Integer(4), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(2), Symbol('skoS'))), Rational(6145, 2048)), GreaterThan(Add(Mul(Integer(2097152), Pow(Symbol('skoS'), Integer(6))), Mul(Integer(8388608), Pow(Symbol('skoS'), Integer(5))), Mul(Integer(-1), Integer(25165824), Pow(Symbol('skoS'), Integer(4))), Mul(Integer(-1), Integer(113260544), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(-1), Integer(41979905), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(67092478), Symbol('skoS'))), Rational(-71307263, 2))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_6(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 1559/2048) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi - 2*skoS > 0) & (11581440*skoS**3 + 31551488*skoS**2 - 10340847*skoS <= 15536623)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(1559, 2048)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Add(Symbol('pi'), Mul(Integer(-1), Integer(2), Symbol('skoS'))), Integer(0)), LessThan(Add(Mul(Integer(11581440), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(31551488), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(10340847), Symbol('skoS'))), Integer(15536623)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_7(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#((delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi - 2*skoS > 0) & (16384*skoS**3 + 65536*skoS**2 - 16381*skoS <= 1073709055/32768)) | ((delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi - 2*skoS > 0) & (skoS**3 + 4*skoS**2 - 2*skoS >= 49153/16384) & (134217728*skoS**6 + 536870912*skoS**5 - 1610612736*skoS**4 - 7247872000*skoS**3 - 2684649473*skoS**2 + 4294836222*skoS >= -4563435519/2))

	pre_cond = Or(And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Add(Symbol('pi'), Mul(Integer(-1), Integer(2), Symbol('skoS'))), Integer(0)), LessThan(Add(Mul(Integer(16384), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(65536), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(16381), Symbol('skoS'))), Rational(1073709055, 32768))), And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Add(Symbol('pi'), Mul(Integer(-1), Integer(2), Symbol('skoS'))), Integer(0)), GreaterThan(Add(Pow(Symbol('skoS'), Integer(3)), Mul(Integer(4), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(2), Symbol('skoS'))), Rational(49153, 16384)), GreaterThan(Add(Mul(Integer(134217728), Pow(Symbol('skoS'), Integer(6))), Mul(Integer(536870912), Pow(Symbol('skoS'), Integer(5))), Mul(Integer(-1), Integer(1610612736), Pow(Symbol('skoS'), Integer(4))), Mul(Integer(-1), Integer(7247872000), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(-1), Integer(2684649473), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(4294836222), Symbol('skoS'))), Rational(-4563435519, 2))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_8(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 3119/4096) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi - 2*skoS > 0) & (46329856*skoS**3 + 126214144*skoS**2 - 41373535*skoS <= 62152543)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(3119, 4096)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Add(Symbol('pi'), Mul(Integer(-1), Integer(2), Symbol('skoS'))), Integer(0)), LessThan(Add(Mul(Integer(46329856), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(126214144), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(41373535), Symbol('skoS'))), Integer(62152543)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_9(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#((delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi - 2*skoS > 0) & (65536*skoS**3 + 262144*skoS**2 - 65533*skoS <= 17179738111/131072)) | ((delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi - 2*skoS > 0) & (skoS**3 + 4*skoS**2 - 2*skoS >= 196609/65536) & (2147483648*skoS**6 + 8589934592*skoS**5 - 25769803776*skoS**4 - 115964575744*skoS**3 - 42950852609*skoS**2 + 68718952446*skoS >= -73014575103/2))

	pre_cond = Or(And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Add(Symbol('pi'), Mul(Integer(-1), Integer(2), Symbol('skoS'))), Integer(0)), LessThan(Add(Mul(Integer(65536), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(262144), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(65533), Symbol('skoS'))), Rational(17179738111, 131072))), And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Add(Symbol('pi'), Mul(Integer(-1), Integer(2), Symbol('skoS'))), Integer(0)), GreaterThan(Add(Pow(Symbol('skoS'), Integer(3)), Mul(Integer(4), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(2), Symbol('skoS'))), Rational(196609, 65536)), GreaterThan(Add(Mul(Integer(2147483648), Pow(Symbol('skoS'), Integer(6))), Mul(Integer(8589934592), Pow(Symbol('skoS'), Integer(5))), Mul(Integer(-1), Integer(25769803776), Pow(Symbol('skoS'), Integer(4))), Mul(Integer(-1), Integer(115964575744), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(-1), Integer(42950852609), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(68718952446), Symbol('skoS'))), Rational(-73014575103, 2))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_10(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 12477/16384) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi - 2*skoS > 0) & (741294080*skoS**3 + 2019459072*skoS**2 - 662017143*skoS <= 994464887)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(12477, 16384)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Add(Symbol('pi'), Mul(Integer(-1), Integer(2), Symbol('skoS'))), Integer(0)), LessThan(Add(Mul(Integer(741294080), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(2019459072), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(662017143), Symbol('skoS'))), Integer(994464887)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_11(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#((delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi - 2*skoS > 0) & (131072*skoS**3 + 524288*skoS**2 - 131069*skoS <= 68719214591/262144)) | ((delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi - 2*skoS > 0) & (skoS**3 + 4*skoS**2 - 2*skoS >= 393217/131072) & (8589934592*skoS**6 + 34359738368*skoS**5 - 103079215104*skoS**4 - 463857385472*skoS**3 - 171801051137*skoS**2 + 274876858366*skoS >= -292058038271/2))

	pre_cond = Or(And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Add(Symbol('pi'), Mul(Integer(-1), Integer(2), Symbol('skoS'))), Integer(0)), LessThan(Add(Mul(Integer(131072), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(524288), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(131069), Symbol('skoS'))), Rational(68719214591, 262144))), And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Add(Symbol('pi'), Mul(Integer(-1), Integer(2), Symbol('skoS'))), Integer(0)), GreaterThan(Add(Pow(Symbol('skoS'), Integer(3)), Mul(Integer(4), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(2), Symbol('skoS'))), Rational(393217, 131072)), GreaterThan(Add(Mul(Integer(8589934592), Pow(Symbol('skoS'), Integer(6))), Mul(Integer(34359738368), Pow(Symbol('skoS'), Integer(5))), Mul(Integer(-1), Integer(103079215104), Pow(Symbol('skoS'), Integer(4))), Mul(Integer(-1), Integer(463857385472), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(-1), Integer(171801051137), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(274876858366), Symbol('skoS'))), Rational(-292058038271, 2))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_12(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 49909/65536) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi - 2*skoS > 0) & (11860770816*skoS**3 + 32311476224*skoS**2 - 10592436615*skoS <= 15911534983)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(49909, 65536)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Add(Symbol('pi'), Mul(Integer(-1), Integer(2), Symbol('skoS'))), Integer(0)), LessThan(Add(Mul(Integer(11860770816), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(32311476224), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(10592436615), Symbol('skoS'))), Integer(15911534983)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_13(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#((delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi - 2*skoS > 0) & (262144*skoS**3 + 1048576*skoS**2 - 262141*skoS <= 274877382655/524288)) | ((delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi - 2*skoS > 0) & (skoS**3 + 4*skoS**2 - 2*skoS >= 786433/262144) & (34359738368*skoS**6 + 137438953472*skoS**5 - 412316860416*skoS**4 - 1855427706880*skoS**3 - 687199485953*skoS**2 + 1099509530622*skoS >= -1168231628799/2))

	pre_cond = Or(And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Add(Symbol('pi'), Mul(Integer(-1), Integer(2), Symbol('skoS'))), Integer(0)), LessThan(Add(Mul(Integer(262144), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(1048576), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(262141), Symbol('skoS'))), Rational(274877382655, 524288))), And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Add(Symbol('pi'), Mul(Integer(-1), Integer(2), Symbol('skoS'))), Integer(0)), GreaterThan(Add(Pow(Symbol('skoS'), Integer(3)), Mul(Integer(4), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(2), Symbol('skoS'))), Rational(786433, 262144)), GreaterThan(Add(Mul(Integer(34359738368), Pow(Symbol('skoS'), Integer(6))), Mul(Integer(137438953472), Pow(Symbol('skoS'), Integer(5))), Mul(Integer(-1), Integer(412316860416), Pow(Symbol('skoS'), Integer(4))), Mul(Integer(-1), Integer(1855427706880), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(-1), Integer(687199485953), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(1099509530622), Symbol('skoS'))), Rational(-1168231628799, 2))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_14(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 199637/262144) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi - 2*skoS > 0) & (189772595200*skoS**3 + 516984143872*skoS**2 - 169479635143*skoS <= 254584946887)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(199637, 262144)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Add(Symbol('pi'), Mul(Integer(-1), Integer(2), Symbol('skoS'))), Integer(0)), LessThan(Add(Mul(Integer(189772595200), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(516984143872), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(169479635143), Symbol('skoS'))), Integer(254584946887)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_15(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#((delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi - 2*skoS > 0) & (2097152*skoS**3 + 8388608*skoS**2 - 2097149*skoS <= 17592181850111/4194304)) | ((delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi - 2*skoS > 0) & (skoS**3 + 4*skoS**2 - 2*skoS >= 6291457/2097152) & (2199023255552*skoS**6 + 8796093022208*skoS**5 - 26388279066624*skoS**4 - 118747270479872*skoS**3 - 43980502859777*skoS**2 + 70368727400446*skoS >= -74766794883071/2))

	pre_cond = Or(And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Add(Symbol('pi'), Mul(Integer(-1), Integer(2), Symbol('skoS'))), Integer(0)), LessThan(Add(Mul(Integer(2097152), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(8388608), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(2097149), Symbol('skoS'))), Rational(17592181850111, 4194304))), And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Add(Symbol('pi'), Mul(Integer(-1), Integer(2), Symbol('skoS'))), Integer(0)), GreaterThan(Add(Pow(Symbol('skoS'), Integer(3)), Mul(Integer(4), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(2), Symbol('skoS'))), Rational(6291457, 2097152)), GreaterThan(Add(Mul(Integer(2199023255552), Pow(Symbol('skoS'), Integer(6))), Mul(Integer(8796093022208), Pow(Symbol('skoS'), Integer(5))), Mul(Integer(-1), Integer(26388279066624), Pow(Symbol('skoS'), Integer(4))), Mul(Integer(-1), Integer(118747270479872), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(-1), Integer(43980502859777), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(70368727400446), Symbol('skoS'))), Rational(-74766794883071, 2))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_16(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 399275/524288) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi - 2*skoS > 0) & (759090905088*skoS**3 + 2067937624064*skoS**2 - 677919839175*skoS <= 1018340561863)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(399275, 524288)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Add(Symbol('pi'), Mul(Integer(-1), Integer(2), Symbol('skoS'))), Integer(0)), LessThan(Add(Mul(Integer(759090905088), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(2067937624064), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(677919839175), Symbol('skoS'))), Integer(1018340561863)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_17(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#((delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi - 2*skoS > 0) & (67108864*skoS**3 + 268435456*skoS**2 - 67108861*skoS <= 18014398375264255/134217728)) | ((delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi - 2*skoS > 0) & (skoS**3 + 4*skoS**2 - 2*skoS >= 201326593/67108864) & (2251799813685248*skoS**6 + 9007199254740992*skoS**5 - 27021597764222976*skoS**4 - 121597190408765440*skoS**3 - 45035997481664513*skoS**2 + 72057593501057022*skoS >= -76561193799516159/2))

	pre_cond = Or(And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Add(Symbol('pi'), Mul(Integer(-1), Integer(2), Symbol('skoS'))), Integer(0)), LessThan(Add(Mul(Integer(67108864), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(268435456), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(67108861), Symbol('skoS'))), Rational(18014398375264255, 134217728))), And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Add(Symbol('pi'), Mul(Integer(-1), Integer(2), Symbol('skoS'))), Integer(0)), GreaterThan(Add(Pow(Symbol('skoS'), Integer(3)), Mul(Integer(4), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(2), Symbol('skoS'))), Rational(201326593, 67108864)), GreaterThan(Add(Mul(Integer(2251799813685248), Pow(Symbol('skoS'), Integer(6))), Mul(Integer(9007199254740992), Pow(Symbol('skoS'), Integer(5))), Mul(Integer(-1), Integer(27021597764222976), Pow(Symbol('skoS'), Integer(4))), Mul(Integer(-1), Integer(121597190408765440), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(-1), Integer(45035997481664513), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(72057593501057022), Symbol('skoS'))), Rational(-76561193799516159, 2))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_18(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 12776809/16777216) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi - 2*skoS > 0) & (777309237805056*skoS**3 + 2117568429031424*skoS**2 - 694190289312495*skoS <= 1042780958350063)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(12776809, 16777216)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Add(Symbol('pi'), Mul(Integer(-1), Integer(2), Symbol('skoS'))), Integer(0)), LessThan(Add(Mul(Integer(777309237805056), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(2117568429031424), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(694190289312495), Symbol('skoS'))), Integer(1042780958350063)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_19(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#((delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi - 2*skoS > 0) & (268435456*skoS**3 + 1073741824*skoS**2 - 268435453*skoS <= 288230375614840831/536870912)) | ((delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi - 2*skoS > 0) & (skoS**3 + 4*skoS**2 - 2*skoS >= 805306369/268435456) & (36028797018963968*skoS**6 + 144115188075855872*skoS**5 - 432345564227567616*skoS**4 - 1945555040903102464*skoS**3 - 720575945211117569*skoS**2 + 1152921502459363326*skoS >= -1224979099181645823/2))

	pre_cond = Or(And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Add(Symbol('pi'), Mul(Integer(-1), Integer(2), Symbol('skoS'))), Integer(0)), LessThan(Add(Mul(Integer(268435456), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(1073741824), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(268435453), Symbol('skoS'))), Rational(288230375614840831, 536870912))), And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Add(Symbol('pi'), Mul(Integer(-1), Integer(2), Symbol('skoS'))), Integer(0)), GreaterThan(Add(Pow(Symbol('skoS'), Integer(3)), Mul(Integer(4), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(2), Symbol('skoS'))), Rational(805306369, 268435456)), GreaterThan(Add(Mul(Integer(36028797018963968), Pow(Symbol('skoS'), Integer(6))), Mul(Integer(144115188075855872), Pow(Symbol('skoS'), Integer(5))), Mul(Integer(-1), Integer(432345564227567616), Pow(Symbol('skoS'), Integer(4))), Mul(Integer(-1), Integer(1945555040903102464), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(-1), Integer(720575945211117569), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(1152921502459363326), Symbol('skoS'))), Rational(-1224979099181645823, 2))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_20(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 51107237/67108864) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi - 2*skoS > 0) & (12436947871989760*skoS**3 + 33881094998720512*skoS**2 - 11107044795220903*skoS <= 16684495432713127)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(51107237, 67108864)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Add(Symbol('pi'), Mul(Integer(-1), Integer(2), Symbol('skoS'))), Integer(0)), LessThan(Add(Mul(Integer(12436947871989760), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(33881094998720512), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(11107044795220903), Symbol('skoS'))), Integer(16684495432713127)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_21(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#((delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi - 2*skoS > 0) & (1073741824*skoS**3 + 4294967296*skoS**2 - 1073741821*skoS <= 4611686016279904255/2147483648)) | ((delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi - 2*skoS > 0) & (skoS**3 + 4*skoS**2 - 2*skoS >= 3221225473/1073741824) & (576460752303423488*skoS**6 + 2305843009213693952*skoS**5 - 6917529027641081856*skoS**4 - 31128880631901061120*skoS**3 - 11529215065395822593*skoS**2 + 18446744065119617022*skoS >= -19599665580463882239/2))

	pre_cond = Or(And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Add(Symbol('pi'), Mul(Integer(-1), Integer(2), Symbol('skoS'))), Integer(0)), LessThan(Add(Mul(Integer(1073741824), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(4294967296), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(1073741821), Symbol('skoS'))), Rational(4611686016279904255, 2147483648))), And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Add(Symbol('pi'), Mul(Integer(-1), Integer(2), Symbol('skoS'))), Integer(0)), GreaterThan(Add(Pow(Symbol('skoS'), Integer(3)), Mul(Integer(4), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(2), Symbol('skoS'))), Rational(3221225473, 1073741824)), GreaterThan(Add(Mul(Integer(576460752303423488), Pow(Symbol('skoS'), Integer(6))), Mul(Integer(2305843009213693952), Pow(Symbol('skoS'), Integer(5))), Mul(Integer(-1), Integer(6917529027641081856), Pow(Symbol('skoS'), Integer(4))), Mul(Integer(-1), Integer(31128880631901061120), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(-1), Integer(11529215065395822593), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(18446744065119617022), Symbol('skoS'))), Rational(-19599665580463882239, 2))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_22(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 418670488319/549755813888) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi - 2*skoS > 0) & (834629444864012829327360*skoS**3 + 2273721799535340246007808*skoS**2 - 745381162437523052451327*skoS <= 1119677537188139397830143)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(418670488319, 549755813888)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Add(Symbol('pi'), Mul(Integer(-1), Integer(2), Symbol('skoS'))), Integer(0)), LessThan(Add(Mul(Integer(834629444864012829327360), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(2273721799535340246007808), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(745381162437523052451327), Symbol('skoS'))), Integer(1119677537188139397830143)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_23(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#((delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi - 2*skoS > 0) & (4398046511104*skoS**3 + 17592186044416*skoS**2 - 4398046511101*skoS <= 77371252455327471088173055/8796093022208)) | ((delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi - 2*skoS > 0) & (skoS**3 + 4*skoS**2 - 2*skoS >= 13194139533313/4398046511104) & (9671406556917033397649408*skoS**6 + 38685626227668133590597632*skoS**5 - 116056878683004400771792896*skoS**4 - 522255954073550589798645760*skoS**3 - 193428131138419832790188033*skoS**2 + 309485009821309884352692222*skoS >= -328827822935187931613102079/2))

	pre_cond = Or(And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Add(Symbol('pi'), Mul(Integer(-1), Integer(2), Symbol('skoS'))), Integer(0)), LessThan(Add(Mul(Integer(4398046511104), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(17592186044416), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(4398046511101), Symbol('skoS'))), Rational(77371252455327471088173055, 8796093022208))), And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Add(Symbol('pi'), Mul(Integer(-1), Integer(2), Symbol('skoS'))), Integer(0)), GreaterThan(Add(Pow(Symbol('skoS'), Integer(3)), Mul(Integer(4), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(2), Symbol('skoS'))), Rational(13194139533313, 4398046511104)), GreaterThan(Add(Mul(Integer(9671406556917033397649408), Pow(Symbol('skoS'), Integer(6))), Mul(Integer(38685626227668133590597632), Pow(Symbol('skoS'), Integer(5))), Mul(Integer(-1), Integer(116056878683004400771792896), Pow(Symbol('skoS'), Integer(4))), Mul(Integer(-1), Integer(522255954073550589798645760), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(-1), Integer(193428131138419832790188033), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(309485009821309884352692222), Symbol('skoS'))), Rational(-328827822935187931613102079, 2))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_24(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 1635431595/2147483648) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi - 2*skoS > 0) & (12735434644539834368*skoS**3 + 34694241325934444544*skoS**2 - 11373613928815990215*skoS <= 17084923357985707463)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(1635431595, 2147483648)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Add(Symbol('pi'), Mul(Integer(-1), Integer(2), Symbol('skoS'))), Integer(0)), LessThan(Add(Mul(Integer(12735434644539834368), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(34694241325934444544), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(11373613928815990215), Symbol('skoS'))), Integer(17084923357985707463)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_25(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#((delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi - 2*skoS > 0) & (17592186044416*skoS**3 + 70368744177664*skoS**2 - 17592186044413*skoS <= 1237940039285345090527035391/35184372088832)) | ((delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi - 2*skoS > 0) & (skoS**3 + 4*skoS**2 - 2*skoS >= 52776558133249/17592186044416) & (154742504910672534362390528*skoS**6 + 618970019642690137449562112*skoS**5 - 1856910058928070412348686336*skoS**4 - 8356095265176440000871399424*skoS**3 - 3094850098213767346596610049*skoS**2 + 4951760157141380362108141566*skoS >= -5261245166962901352693366783/2))

	pre_cond = Or(And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Add(Symbol('pi'), Mul(Integer(-1), Integer(2), Symbol('skoS'))), Integer(0)), LessThan(Add(Mul(Integer(17592186044416), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(70368744177664), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(17592186044413), Symbol('skoS'))), Rational(1237940039285345090527035391, 35184372088832))), And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Add(Symbol('pi'), Mul(Integer(-1), Integer(2), Symbol('skoS'))), Integer(0)), GreaterThan(Add(Pow(Symbol('skoS'), Integer(3)), Mul(Integer(4), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(2), Symbol('skoS'))), Rational(52776558133249, 17592186044416)), GreaterThan(Add(Mul(Integer(154742504910672534362390528), Pow(Symbol('skoS'), Integer(6))), Mul(Integer(618970019642690137449562112), Pow(Symbol('skoS'), Integer(5))), Mul(Integer(-1), Integer(1856910058928070412348686336), Pow(Symbol('skoS'), Integer(4))), Mul(Integer(-1), Integer(8356095265176440000871399424), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(-1), Integer(3094850098213767346596610049), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(4951760157141380362108141566), Symbol('skoS'))), Rational(-5261245166962901352693366783, 2))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_26(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 6698727813123/8796093022208) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi - 2*skoS > 0) & (213665137885354410075226112*skoS**3 + 582072780681381354512842752*skoS**2 - 190817577584419852840329207*skoS <= 286637449520410511489884151)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(6698727813123, 8796093022208)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Add(Symbol('pi'), Mul(Integer(-1), Integer(2), Symbol('skoS'))), Integer(0)), LessThan(Add(Mul(Integer(213665137885354410075226112), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(582072780681381354512842752), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(190817577584419852840329207), Symbol('skoS'))), Integer(286637449520410511489884151)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_27(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#((delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi - 2*skoS > 0) & (281474976710656*skoS**3 + 1125899906842624*skoS**2 - 281474976710653*skoS <= 316912650057056787424222380031/562949953421312)) | ((delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi - 2*skoS > 0) & (skoS**3 + 4*skoS**2 - 2*skoS >= 844424930131969/281474976710656) & (39614081257132168796771975168*skoS**6 + 158456325028528675187087900672*skoS**5 - 475368975085586025561263702016*skoS**4 - 2139160387885139085350523633664*skoS**3 - 792281625142648442485020295169*skoS**2 + 1267650600228227149696889520126*skoS >= -1346878762742494302040200577023/2))

	pre_cond = Or(And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Add(Symbol('pi'), Mul(Integer(-1), Integer(2), Symbol('skoS'))), Integer(0)), LessThan(Add(Mul(Integer(281474976710656), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(1125899906842624), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(281474976710653), Symbol('skoS'))), Rational(316912650057056787424222380031, 562949953421312))), And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Add(Symbol('pi'), Mul(Integer(-1), Integer(2), Symbol('skoS'))), Integer(0)), GreaterThan(Add(Pow(Symbol('skoS'), Integer(3)), Mul(Integer(4), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(2), Symbol('skoS'))), Rational(844424930131969, 281474976710656)), GreaterThan(Add(Mul(Integer(39614081257132168796771975168), Pow(Symbol('skoS'), Integer(6))), Mul(Integer(158456325028528675187087900672), Pow(Symbol('skoS'), Integer(5))), Mul(Integer(-1), Integer(475368975085586025561263702016), Pow(Symbol('skoS'), Integer(4))), Mul(Integer(-1), Integer(2139160387885139085350523633664), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(-1), Integer(792281625142648442485020295169), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(1267650600228227149696889520126), Symbol('skoS'))), Rational(-1346878762742494302040200577023, 2))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_28(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 214359290019963/281474976710656) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi - 2*skoS > 0) & (218793101194610515741402726400*skoS**3 + 596042527417749706669893353472*skoS**2 - 195397199446464753204320781543*skoS <= 293516748308911587837093856487)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(214359290019963, 281474976710656)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Add(Symbol('pi'), Mul(Integer(-1), Integer(2), Symbol('skoS'))), Integer(0)), LessThan(Add(Mul(Integer(218793101194610515741402726400), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(596042527417749706669893353472), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(195397199446464753204320781543), Symbol('skoS'))), Integer(293516748308911587837093856487)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_29(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#((delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi - 2*skoS > 0) & (2251799813685248*skoS**3 + 9007199254740992*skoS**2 - 2251799813685245*skoS <= 20282409603651665920347623915519/4503599627370496)) | ((delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi - 2*skoS > 0) & (skoS**3 + 4*skoS**2 - 2*skoS >= 6755399441055745/2251799813685248) & (2535301200456458802993406410752*skoS**6 + 10141204801825835211973625643008*skoS**5 - 30423614405477505635920876929024*skoS**4 - 136906264824648791124242641977344*skoS**3 - 50706024009129216592264774549505*skoS**2 + 81129638414606663681390495662078*skoS >= -86200240815519603805375445336063/2))

	pre_cond = Or(And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Add(Symbol('pi'), Mul(Integer(-1), Integer(2), Symbol('skoS'))), Integer(0)), LessThan(Add(Mul(Integer(2251799813685248), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(9007199254740992), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(2251799813685245), Symbol('skoS'))), Rational(20282409603651665920347623915519, 4503599627370496))), And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Add(Symbol('pi'), Mul(Integer(-1), Integer(2), Symbol('skoS'))), Integer(0)), GreaterThan(Add(Pow(Symbol('skoS'), Integer(3)), Mul(Integer(4), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(2), Symbol('skoS'))), Rational(6755399441055745, 2251799813685248)), GreaterThan(Add(Mul(Integer(2535301200456458802993406410752), Pow(Symbol('skoS'), Integer(6))), Mul(Integer(10141204801825835211973625643008), Pow(Symbol('skoS'), Integer(5))), Mul(Integer(-1), Integer(30423614405477505635920876929024), Pow(Symbol('skoS'), Integer(4))), Mul(Integer(-1), Integer(136906264824648791124242641977344), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(-1), Integer(50706024009129216592264774549505), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(81129638414606663681390495662078), Symbol('skoS'))), Rational(-86200240815519603805375445336063, 2))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_30(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 53589822504991/70368744177664) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi - 2*skoS > 0) & (13674568824663174826023714816*skoS**3 + 37252657963609391851240423424*skoS**2 - 12212324965404090649102974015*skoS <= 18344796769307000221465246783)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(53589822504991, 70368744177664)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Add(Symbol('pi'), Mul(Integer(-1), Integer(2), Symbol('skoS'))), Integer(0)), LessThan(Add(Mul(Integer(13674568824663174826023714816), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(37252657963609391851240423424), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(12212324965404090649102974015), Symbol('skoS'))), Integer(18344796769307000221465246783)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_31(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#((delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi - 2*skoS > 0) & (36028797018963968*skoS**3 + 144115188075855872*skoS**2 - 36028797018963965*skoS <= 5192296858534827556472902291292159/72057594037927936)) | ((delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi - 2*skoS > 0) & (skoS**3 + 4*skoS**2 - 2*skoS >= 108086391056891905/36028797018963968) & (649037107316853453566312041152512*skoS**6 + 2596148429267413814265248164610048*skoS**5 - 7788445287802241442795744493830144*skoS**4 - 35048003795110086744782429354983424*skoS**3 - 12980742146337069719844587164401665*skoS**2 + 20769187434139310225891609165168638*skoS >= -22067261648773017493312203437113343/2))

	pre_cond = Or(And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Add(Symbol('pi'), Mul(Integer(-1), Integer(2), Symbol('skoS'))), Integer(0)), LessThan(Add(Mul(Integer(36028797018963968), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(144115188075855872), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(36028797018963965), Symbol('skoS'))), Rational(5192296858534827556472902291292159, 72057594037927936))), And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Add(Symbol('pi'), Mul(Integer(-1), Integer(2), Symbol('skoS'))), Integer(0)), GreaterThan(Add(Pow(Symbol('skoS'), Integer(3)), Mul(Integer(4), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(2), Symbol('skoS'))), Rational(108086391056891905, 36028797018963968)), GreaterThan(Add(Mul(Integer(649037107316853453566312041152512), Pow(Symbol('skoS'), Integer(6))), Mul(Integer(2596148429267413814265248164610048), Pow(Symbol('skoS'), Integer(5))), Mul(Integer(-1), Integer(7788445287802241442795744493830144), Pow(Symbol('skoS'), Integer(4))), Mul(Integer(-1), Integer(35048003795110086744782429354983424), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(-1), Integer(12980742146337069719844587164401665), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(20769187434139310225891609165168638), Symbol('skoS'))), Rational(-22067261648773017493312203437113343, 2))))

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
	
	
	if pre_condition_21(delta=delta,skoS=skoS,pi=pi)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoS'] = skoS
		all_vals['pi'] = pi
		all_vals['skoCOSS'] = Rational(1, 2147483648)
		all_vals['skoSINS'] = Add(Symbol('lambda_var_0'), Rational(51107237, 67108864))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_21 SAT")

			print("skoCOSS=", all_vals["skoCOSS"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSINS=", all_vals["skoSINS"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_22(delta=delta,skoS=skoS,pi=pi)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoS'] = skoS
		all_vals['pi'] = pi
		all_vals['skoCOSS'] = Add(Symbol('lambda_var_0'), Rational(1, 8796093022208))
		all_vals['skoSINS'] = Rational(418670488319, 549755813888)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_22 SAT")

			print("skoCOSS=", all_vals["skoCOSS"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSINS=", all_vals["skoSINS"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_23(delta=delta,skoS=skoS,pi=pi)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoS'] = skoS
		all_vals['pi'] = pi
		all_vals['skoCOSS'] = Rational(1, 8796093022208)
		all_vals['skoSINS'] = Add(Symbol('lambda_var_0'), Rational(418670488319, 549755813888))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_23 SAT")

			print("skoCOSS=", all_vals["skoCOSS"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSINS=", all_vals["skoSINS"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_24(delta=delta,skoS=skoS,pi=pi)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoS'] = skoS
		all_vals['pi'] = pi
		all_vals['skoCOSS'] = Add(Symbol('lambda_var_0'), Rational(1, 35184372088832))
		all_vals['skoSINS'] = Rational(1635431595, 2147483648)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_24 SAT")

			print("skoCOSS=", all_vals["skoCOSS"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSINS=", all_vals["skoSINS"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_25(delta=delta,skoS=skoS,pi=pi)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoS'] = skoS
		all_vals['pi'] = pi
		all_vals['skoCOSS'] = Rational(1, 35184372088832)
		all_vals['skoSINS'] = Add(Symbol('lambda_var_0'), Rational(1635431595, 2147483648))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_25 SAT")

			print("skoCOSS=", all_vals["skoCOSS"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSINS=", all_vals["skoSINS"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_26(delta=delta,skoS=skoS,pi=pi)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoS'] = skoS
		all_vals['pi'] = pi
		all_vals['skoCOSS'] = Add(Symbol('lambda_var_0'), Rational(1, 562949953421312))
		all_vals['skoSINS'] = Rational(6698727813123, 8796093022208)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_26 SAT")

			print("skoCOSS=", all_vals["skoCOSS"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSINS=", all_vals["skoSINS"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_27(delta=delta,skoS=skoS,pi=pi)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoS'] = skoS
		all_vals['pi'] = pi
		all_vals['skoCOSS'] = Rational(1, 562949953421312)
		all_vals['skoSINS'] = Add(Symbol('lambda_var_0'), Rational(6698727813123, 8796093022208))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_27 SAT")

			print("skoCOSS=", all_vals["skoCOSS"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSINS=", all_vals["skoSINS"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_28(delta=delta,skoS=skoS,pi=pi)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoS'] = skoS
		all_vals['pi'] = pi
		all_vals['skoCOSS'] = Add(Symbol('lambda_var_0'), Rational(1, 4503599627370496))
		all_vals['skoSINS'] = Rational(214359290019963, 281474976710656)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_28 SAT")

			print("skoCOSS=", all_vals["skoCOSS"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSINS=", all_vals["skoSINS"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_29(delta=delta,skoS=skoS,pi=pi)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoS'] = skoS
		all_vals['pi'] = pi
		all_vals['skoCOSS'] = Rational(1, 4503599627370496)
		all_vals['skoSINS'] = Add(Symbol('lambda_var_0'), Rational(214359290019963, 281474976710656))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_29 SAT")

			print("skoCOSS=", all_vals["skoCOSS"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSINS=", all_vals["skoSINS"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_30(delta=delta,skoS=skoS,pi=pi)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoS'] = skoS
		all_vals['pi'] = pi
		all_vals['skoCOSS'] = Add(Symbol('lambda_var_0'), Rational(1, 72057594037927936))
		all_vals['skoSINS'] = Rational(53589822504991, 70368744177664)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_30 SAT")

			print("skoCOSS=", all_vals["skoCOSS"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSINS=", all_vals["skoSINS"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_31(delta=delta,skoS=skoS,pi=pi)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoS'] = skoS
		all_vals['pi'] = pi
		all_vals['skoCOSS'] = Rational(1, 72057594037927936)
		all_vals['skoSINS'] = Add(Symbol('lambda_var_0'), Rational(53589822504991, 70368744177664))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_31 SAT")

			print("skoCOSS=", all_vals["skoCOSS"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSINS=", all_vals["skoSINS"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass


	print("Weakest pre-condition UNSAT")
