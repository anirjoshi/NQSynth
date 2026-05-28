import sympy
from sympy import *

def pre_condition_0(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (2*skoS*(skoS*(skoS - 3) - 6) + 2 > -skoSINS*(skoS*(skoS*(skoS + 2) - 4) + skoSINS*(skoS + 1) + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), StrictGreaterThan(Add(Mul(Integer(2), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(-3))), Integer(-6))), Integer(2)), Mul(Integer(-1), Symbol('skoSINS'), Add(Mul(Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(2))), Integer(-4))), Mul(Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (-2*skoS**3 + 4*skoS**2 + 11*skoS < 11/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), StrictLessThan(Add(Mul(Integer(-1), Integer(2), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(4), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(11), Symbol('skoS'))), Rational(11, 5)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (2*skoS*(skoS*(skoS + 6) + 6) + 2 > -skoSINS*(skoS*(skoS*(skoS + 2) - 4) + skoSINS*(skoS + 1) - 5))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), StrictGreaterThan(Add(Mul(Integer(2), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(6))), Integer(6))), Integer(2)), Mul(Integer(-1), Symbol('skoSINS'), Add(Mul(Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(2))), Integer(-4))), Mul(Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(-5)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (skoS**3 + 10*skoS**2 + 17*skoS > -8)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), StrictGreaterThan(Add(Pow(Symbol('skoS'), Integer(3)), Mul(Integer(10), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(17), Symbol('skoS'))), Integer(-8)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_4(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (2*skoS*(skoS*(skoS + 9) + 14) + 10 > -skoSINS*(skoS*(skoS*(skoS + 2) - 4) + skoSINS*(skoS + 1) - 7))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), StrictGreaterThan(Add(Mul(Integer(2), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(9))), Integer(14))), Integer(10)), Mul(Integer(-1), Symbol('skoSINS'), Add(Mul(Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(2))), Integer(-4))), Mul(Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(-7)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_5(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (skoS**3 + 16*skoS**2 + 33*skoS > -18)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), StrictGreaterThan(Add(Pow(Symbol('skoS'), Integer(3)), Mul(Integer(16), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(33), Symbol('skoS'))), Integer(-18)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_6(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (2*skoS*(skoS*(skoS + 12) + 24) + 22 > -skoSINS*(skoS*(skoS*(skoS + 2) - 4) + skoSINS*(skoS + 1) - 9))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), StrictGreaterThan(Add(Mul(Integer(2), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(12))), Integer(24))), Integer(22)), Mul(Integer(-1), Symbol('skoSINS'), Add(Mul(Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(2))), Integer(-4))), Mul(Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(-9)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_7(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (skoS**3 + 22*skoS**2 + 53*skoS > -32)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), StrictGreaterThan(Add(Pow(Symbol('skoS'), Integer(3)), Mul(Integer(22), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(53), Symbol('skoS'))), Integer(-32)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_8(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (2*skoS*(skoS*(skoS + 15) + 36) + 38 > -skoSINS*(skoS*(skoS*(skoS + 2) - 4) + skoSINS*(skoS + 1) - 11))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), StrictGreaterThan(Add(Mul(Integer(2), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(15))), Integer(36))), Integer(38)), Mul(Integer(-1), Symbol('skoSINS'), Add(Mul(Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(2))), Integer(-4))), Mul(Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(-11)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_9(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (skoS**3 + 28*skoS**2 + 77*skoS > -50)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), StrictGreaterThan(Add(Pow(Symbol('skoS'), Integer(3)), Mul(Integer(28), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(77), Symbol('skoS'))), Integer(-50)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_10(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (2*skoS*(skoS*(skoS + 18) + 50) + 58 > -skoSINS*(skoS*(skoS*(skoS + 2) - 4) + skoSINS*(skoS + 1) - 13))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), StrictGreaterThan(Add(Mul(Integer(2), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(18))), Integer(50))), Integer(58)), Mul(Integer(-1), Symbol('skoSINS'), Add(Mul(Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(2))), Integer(-4))), Mul(Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(-13)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_11(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (skoS**3 + 34*skoS**2 + 105*skoS > -72)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), StrictGreaterThan(Add(Pow(Symbol('skoS'), Integer(3)), Mul(Integer(34), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(105), Symbol('skoS'))), Integer(-72)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_12(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (2*skoS*(skoS*(skoS + 30) + 126) + 178 > -skoSINS*(skoS*(skoS*(skoS + 2) - 4) + skoSINS*(skoS + 1) - 21))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), StrictGreaterThan(Add(Mul(Integer(2), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(30))), Integer(126))), Integer(178)), Mul(Integer(-1), Symbol('skoSINS'), Add(Mul(Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(2))), Integer(-4))), Mul(Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(-21)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_13(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (923*skoS**3 + 1790*skoS**2 - 859577*skoS < 875228)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), StrictLessThan(Add(Mul(Integer(923), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(1790), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(859577), Symbol('skoS'))), Integer(875228)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_14(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (2*skoS*(skoS*(skoS + 45) + 266) + 418 > -skoSINS*(skoS*(skoS*(skoS + 2) - 4) + skoSINS*(skoS + 1) - 31))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), StrictGreaterThan(Add(Mul(Integer(2), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(45))), Integer(266))), Integer(418)), Mul(Integer(-1), Symbol('skoSINS'), Add(Mul(Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(2))), Integer(-4))), Mul(Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(-31)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_15(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (909*skoS**3 + 1732*skoS**2 - 834097*skoS < 858580)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), StrictLessThan(Add(Mul(Integer(909), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(1732), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(834097), Symbol('skoS'))), Integer(858580)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_16(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (2*skoS*(skoS*(skoS + 57) + 414) + 682 > -skoSINS*(skoS*(skoS*(skoS + 2) - 4) + skoSINS*(skoS + 1) - 39))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), StrictGreaterThan(Add(Mul(Integer(2), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(57))), Integer(414))), Integer(682)), Mul(Integer(-1), Symbol('skoSINS'), Add(Mul(Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(2))), Integer(-4))), Mul(Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(-39)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_17(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (453*skoS**3 + 851*skoS**2 - 414462*skoS < 430279)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), StrictLessThan(Add(Mul(Integer(453), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(851), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(414462), Symbol('skoS'))), Integer(430279)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_18(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (2*skoS*(skoS*(skoS + 297) + 10094) + 19402 > -skoSINS*(skoS*(skoS*(skoS + 2) - 4) + skoSINS*(skoS + 1) - 199))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), StrictGreaterThan(Add(Mul(Integer(2), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(297))), Integer(10094))), Integer(19402)), Mul(Integer(-1), Symbol('skoSINS'), Add(Mul(Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(2))), Integer(-4))), Mul(Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(-199)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_19(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (181*skoS**3 + 244*skoS**2 - 169293*skoS < 1022544/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), StrictLessThan(Add(Mul(Integer(181), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(244), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(169293), Symbol('skoS'))), Rational(1022544, 5)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_20(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (2*skoS*(skoS*(skoS + 75) + 696) + 1198 > -skoSINS*(skoS*(skoS*(skoS + 2) - 4) + skoSINS*(skoS + 1) - 51))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), StrictGreaterThan(Add(Mul(Integer(2), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(75))), Integer(696))), Integer(1198)), Mul(Integer(-1), Symbol('skoSINS'), Add(Mul(Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(2))), Integer(-4))), Mul(Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(-51)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_21(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (905*skoS**3 + 1664*skoS**2 - 827669*skoS < 870104)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), StrictLessThan(Add(Mul(Integer(905), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(1664), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(827669), Symbol('skoS'))), Integer(870104)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_22(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (2*skoS*(skoS*(skoS + 78) + 750) + 1298 > -skoSINS*(skoS*(skoS*(skoS + 2) - 4) + skoSINS*(skoS + 1) - 53))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), StrictGreaterThan(Add(Mul(Integer(2), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(78))), Integer(750))), Integer(1298)), Mul(Integer(-1), Symbol('skoSINS'), Add(Mul(Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(2))), Integer(-4))), Mul(Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(-53)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_23(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (905*skoS**3 + 1658*skoS**2 - 827777*skoS < 872018)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), StrictLessThan(Add(Mul(Integer(905), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(1658), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(827777), Symbol('skoS'))), Integer(872018)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(delta:sympy.Rational, skoS:sympy.Rational, pi:sympy.Rational, skoCOSS:sympy.Rational, skoSINS:sympy.Rational):
	# (0 <= delta) & (31415927/10000000 > pi) & (pi > 15707963/5000000) & (pi/2 > skoS) & (skoSINS*(-2*skoCOSS + skoS*(skoS*(skoS + 2) - 4) + skoSINS*(skoS + 1) - 3) > skoCOSS*(-2*skoCOSS - 2) + skoS*(skoCOSS*(-2*skoCOSS - 10) + skoS*(-6*skoCOSS - 2*skoS - 6)) + 2)

	post_cond =  And(LessThan(Integer(0), Symbol('delta')), StrictGreaterThan(Rational(31415927, 10000000), Symbol('pi')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Mul(Rational(1, 2), Symbol('pi')), Symbol('skoS')), StrictGreaterThan(Mul(Symbol('skoSINS'), Add(Mul(Integer(-1), Integer(2), Symbol('skoCOSS')), Mul(Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(2))), Integer(-4))), Mul(Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(-3))), Add(Mul(Symbol('skoCOSS'), Add(Mul(Integer(-1), Integer(2), Symbol('skoCOSS')), Integer(-2))), Mul(Symbol('skoS'), Add(Mul(Symbol('skoCOSS'), Add(Mul(Integer(-1), Integer(2), Symbol('skoCOSS')), Integer(-10))), Mul(Symbol('skoS'), Add(Mul(Integer(-1), Integer(6), Symbol('skoCOSS')), Mul(Integer(-1), Integer(2), Symbol('skoS')), Integer(-6))))), Integer(2))))

	eval = post_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi, 'skoCOSS':skoCOSS, 'skoSINS':skoSINS })

	return eval == sympy.logic.boolalg.BooleanTrue





if __name__=="__main__":
	
	ip_0=int(input("enter integer numerator of delta:\n"))
	ip_1=int(input("enter integer denominator of delta:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	delta=sympy.Rational(ip_0,ip_1)
	
	
	ip_0=int(input("enter integer numerator of skoS:\n"))
	ip_1=int(input("enter integer denominator of skoS:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	skoS=sympy.Rational(ip_0,ip_1)
	
	
	ip_0=int(input("enter integer numerator of pi:\n"))
	ip_1=int(input("enter integer denominator of pi:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	pi=sympy.Rational(ip_0,ip_1)
	
	
	
	
	if pre_condition_0(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_0 SAT")
		print('delta = 0')
		print('pi = 26353589/8388608')
		print('skoS = 1/8')
		print('skoSINS = 1/2')
		print('skoCOSS = -2')
		exit(0)
	
	
	if pre_condition_1(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_1 SAT")
		print('delta = 0')
		print('pi = 26353589/8388608')
		print('skoS = 1/8')
		print('skoSINS = 1/2')
		print('skoCOSS = -2')
		exit(0)
	
	
	if pre_condition_2(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_2 SAT")
		print('delta = 0')
		print('pi = 26353589/8388608')
		print('skoS = -2')
		print('skoSINS = -1')
		print('skoCOSS = 1')
		exit(0)
	
	
	if pre_condition_3(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_3 SAT")
		print('delta = 0')
		print('pi = 26353589/8388608')
		print('skoS = -2')
		print('skoSINS = -1')
		print('skoCOSS = 1')
		exit(0)
	
	
	if pre_condition_4(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_4 SAT")
		print('delta = 0')
		print('pi = 26353589/8388608')
		print('skoS = -9')
		print('skoSINS = -1')
		print('skoCOSS = 2')
		exit(0)
	
	
	if pre_condition_5(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_5 SAT")
		print('delta = 0')
		print('pi = 26353589/8388608')
		print('skoS = -9')
		print('skoSINS = -1')
		print('skoCOSS = 2')
		exit(0)
	
	
	if pre_condition_6(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_6 SAT")
		print('delta = 0')
		print('pi = 26353589/8388608')
		print('skoS = -14')
		print('skoSINS = -1')
		print('skoCOSS = 3')
		exit(0)
	
	
	if pre_condition_7(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_7 SAT")
		print('delta = 0')
		print('pi = 26353589/8388608')
		print('skoS = -14')
		print('skoSINS = -1')
		print('skoCOSS = 3')
		exit(0)
	
	
	if pre_condition_8(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_8 SAT")
		print('delta = 0')
		print('pi = 26353589/8388608')
		print('skoS = -20')
		print('skoSINS = -1')
		print('skoCOSS = 4')
		exit(0)
	
	
	if pre_condition_9(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_9 SAT")
		print('delta = 0')
		print('pi = 26353589/8388608')
		print('skoS = -20')
		print('skoSINS = -1')
		print('skoCOSS = 4')
		exit(0)
	
	
	if pre_condition_10(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_10 SAT")
		print('delta = 0')
		print('pi = 26353589/8388608')
		print('skoS = -26')
		print('skoSINS = -1')
		print('skoCOSS = 5')
		exit(0)
	
	
	if pre_condition_11(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_11 SAT")
		print('delta = 0')
		print('pi = 26353589/8388608')
		print('skoS = -26')
		print('skoSINS = -1')
		print('skoCOSS = 5')
		exit(0)
	
	
	if pre_condition_12(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_12 SAT")
		print('delta = 0')
		print('pi = 26353589/8388608')
		print('skoS = -31')
		print('skoSINS = -925')
		print('skoCOSS = 9')
		exit(0)
	
	
	if pre_condition_13(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_13 SAT")
		print('delta = 0')
		print('pi = 26353589/8388608')
		print('skoS = -31')
		print('skoSINS = -925')
		print('skoCOSS = 9')
		exit(0)
	
	
	if pre_condition_14(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_14 SAT")
		print('delta = 0')
		print('pi = 26353589/8388608')
		print('skoS = -123/4')
		print('skoSINS = -911')
		print('skoCOSS = 14')
		exit(0)
	
	
	if pre_condition_15(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_15 SAT")
		print('delta = 0')
		print('pi = 26353589/8388608')
		print('skoS = -123/4')
		print('skoSINS = -911')
		print('skoCOSS = 14')
		exit(0)
	
	
	if pre_condition_16(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_16 SAT")
		print('delta = 0')
		print('pi = 26353589/8388608')
		print('skoS = -491/16')
		print('skoSINS = -908')
		print('skoCOSS = 18')
		exit(0)
	
	
	if pre_condition_17(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_17 SAT")
		print('delta = 0')
		print('pi = 26353589/8388608')
		print('skoS = -491/16')
		print('skoSINS = -908')
		print('skoCOSS = 18')
		exit(0)
	
	
	if pre_condition_18(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_18 SAT")
		print('delta = 0')
		print('pi = 26353589/8388608')
		print('skoS = -981/32')
		print('skoSINS = -907')
		print('skoCOSS = 98')
		exit(0)
	
	
	if pre_condition_19(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_19 SAT")
		print('delta = 0')
		print('pi = 26353589/8388608')
		print('skoS = -981/32')
		print('skoSINS = -907')
		print('skoCOSS = 98')
		exit(0)
	
	
	if pre_condition_20(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_20 SAT")
		print('delta = 0')
		print('pi = 26353589/8388608')
		print('skoS = -7847/256')
		print('skoSINS = -907')
		print('skoCOSS = 24')
		exit(0)
	
	
	if pre_condition_21(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_21 SAT")
		print('delta = 0')
		print('pi = 26353589/8388608')
		print('skoS = -7847/256')
		print('skoSINS = -907')
		print('skoCOSS = 24')
		exit(0)
	
	
	if pre_condition_22(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_22 SAT")
		print('delta = 0')
		print('pi = 26353589/8388608')
		print('skoS = -31387/1024')
		print('skoSINS = -907')
		print('skoCOSS = 25')
		exit(0)
	
	
	if pre_condition_23(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_23 SAT")
		print('delta = 0')
		print('pi = 26353589/8388608')
		print('skoS = -31387/1024')
		print('skoSINS = -907')
		print('skoCOSS = 25')
		exit(0)


	print("Weakest pre-condition UNSAT")
	exit(0)
