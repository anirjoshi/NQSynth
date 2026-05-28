import sympy
from sympy import *

def pre_condition_0(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (skoM**2 > 0) & (delta >= skoSINS**2 + 483) & (delta >= -skoSINS**2 - 483) & (skoM**3*skoSINS*(skoM*skoS*(skoS*(skoS + 3) - 3) - 5*skoM + skoSINS*(skoS + 1) + 44) <= 2*skoM**3*(-skoM*(skoM - 66) - skoS*(skoM*skoS*(skoM*skoS + 3*skoM - 66) + 3*skoM*(skoM - 44) + 484) - 484))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), StrictGreaterThan(Pow(Symbol('skoM'), Integer(2)), Integer(0)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(483))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-483))), LessThan(Mul(Pow(Symbol('skoM'), Integer(3)), Symbol('skoSINS'), Add(Mul(Symbol('skoM'), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(3))), Integer(-3))), Mul(Integer(-1), Integer(5), Symbol('skoM')), Mul(Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(44))), Mul(Integer(2), Pow(Symbol('skoM'), Integer(3)), Add(Mul(Integer(-1), Symbol('skoM'), Add(Symbol('skoM'), Integer(-66))), Mul(Integer(-1), Symbol('skoS'), Add(Mul(Symbol('skoM'), Symbol('skoS'), Add(Mul(Symbol('skoM'), Symbol('skoS')), Mul(Integer(3), Symbol('skoM')), Integer(-66))), Mul(Integer(3), Symbol('skoM'), Add(Symbol('skoM'), Integer(-44))), Integer(484))), Integer(-484)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoM**2 > 0) & (delta >= skoSINS**2 + 483) & (delta >= -skoSINS**2 - 483) & (4*skoM**3*skoSINS*(10*skoM + skoSINS + 11) <= skoM**3*(-128*skoM**2 + 2112*skoM - 3872))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), StrictGreaterThan(Pow(Symbol('skoM'), Integer(2)), Integer(0)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(483))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-483))), LessThan(Mul(Integer(4), Pow(Symbol('skoM'), Integer(3)), Symbol('skoSINS'), Add(Mul(Integer(10), Symbol('skoM')), Symbol('skoSINS'), Integer(11))), Mul(Pow(Symbol('skoM'), Integer(3)), Add(Mul(Integer(-1), Integer(128), Pow(Symbol('skoM'), Integer(2))), Mul(Integer(2112), Symbol('skoM')), Integer(-3872)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (skoM**2 > 0) & (delta >= skoSINS**2 + 444888) & (delta >= -skoSINS**2 - 444888) & (skoM**3*skoSINS*(skoM*skoS*(skoS*(skoS + 3) - 3) - 5*skoM + skoSINS*(skoS + 1) + 1334) <= 2*skoM**3*(-skoM*(skoM - 2001) - skoS*(skoM*skoS*(skoM*skoS + 3*skoM - 2001) + 3*skoM*(skoM - 1334) + 444889) - 444889))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), StrictGreaterThan(Pow(Symbol('skoM'), Integer(2)), Integer(0)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(444888))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-444888))), LessThan(Mul(Pow(Symbol('skoM'), Integer(3)), Symbol('skoSINS'), Add(Mul(Symbol('skoM'), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(3))), Integer(-3))), Mul(Integer(-1), Integer(5), Symbol('skoM')), Mul(Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(1334))), Mul(Integer(2), Pow(Symbol('skoM'), Integer(3)), Add(Mul(Integer(-1), Symbol('skoM'), Add(Symbol('skoM'), Integer(-2001))), Mul(Integer(-1), Symbol('skoS'), Add(Mul(Symbol('skoM'), Symbol('skoS'), Add(Mul(Symbol('skoM'), Symbol('skoS')), Mul(Integer(3), Symbol('skoM')), Integer(-2001))), Mul(Integer(3), Symbol('skoM'), Add(Symbol('skoM'), Integer(-1334))), Integer(444889))), Integer(-444889)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoM**2 > 0) & (delta >= skoSINS**2 + 444888) & (delta >= -skoSINS**2 - 444888) & (skoM**3*skoSINS*(4811*skoM + 17*skoSINS + 1334) <= skoM**3*(-9826*skoM**2 + 1156578*skoM - 15126226))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), StrictGreaterThan(Pow(Symbol('skoM'), Integer(2)), Integer(0)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(444888))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-444888))), LessThan(Mul(Pow(Symbol('skoM'), Integer(3)), Symbol('skoSINS'), Add(Mul(Integer(4811), Symbol('skoM')), Mul(Integer(17), Symbol('skoSINS')), Integer(1334))), Mul(Pow(Symbol('skoM'), Integer(3)), Add(Mul(Integer(-1), Integer(9826), Pow(Symbol('skoM'), Integer(2))), Mul(Integer(1156578), Symbol('skoM')), Integer(-15126226)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_4(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (skoM**2 > 0) & (delta >= skoSINS**2 + 360) & (delta >= -skoSINS**2 - 360) & (skoM**3*skoSINS*(skoM*skoS*(skoS*(skoS + 3) - 3) - 5*skoM + skoSINS*(skoS + 1) + 38) <= 2*skoM**3*(-skoM*(skoM - 57) - skoS*(skoM*skoS*(skoM*skoS + 3*skoM - 57) + 3*skoM*(skoM - 38) + 361) - 361))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), StrictGreaterThan(Pow(Symbol('skoM'), Integer(2)), Integer(0)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(360))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-360))), LessThan(Mul(Pow(Symbol('skoM'), Integer(3)), Symbol('skoSINS'), Add(Mul(Symbol('skoM'), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(3))), Integer(-3))), Mul(Integer(-1), Integer(5), Symbol('skoM')), Mul(Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(38))), Mul(Integer(2), Pow(Symbol('skoM'), Integer(3)), Add(Mul(Integer(-1), Symbol('skoM'), Add(Symbol('skoM'), Integer(-57))), Mul(Integer(-1), Symbol('skoS'), Add(Mul(Symbol('skoM'), Symbol('skoS'), Add(Mul(Symbol('skoM'), Symbol('skoS')), Mul(Integer(3), Symbol('skoM')), Integer(-57))), Mul(Integer(3), Symbol('skoM'), Add(Symbol('skoM'), Integer(-38))), Integer(361))), Integer(-361)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_5(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoM**2 > 0) & (delta >= skoSINS**2 + 360) & (delta >= -skoSINS**2 - 360) & (skoM**3*(-128*skoM**2 + 1824*skoM - 2888) >= 2*skoM**3*skoSINS*(20*skoM + 2*skoSINS + 19))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), StrictGreaterThan(Pow(Symbol('skoM'), Integer(2)), Integer(0)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(360))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-360))), GreaterThan(Mul(Pow(Symbol('skoM'), Integer(3)), Add(Mul(Integer(-1), Integer(128), Pow(Symbol('skoM'), Integer(2))), Mul(Integer(1824), Symbol('skoM')), Integer(-2888))), Mul(Integer(2), Pow(Symbol('skoM'), Integer(3)), Symbol('skoSINS'), Add(Mul(Integer(20), Symbol('skoM')), Mul(Integer(2), Symbol('skoSINS')), Integer(19)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_6(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (skoM**2 > 0) & (delta >= skoSINS**2 + 323) & (delta >= -skoSINS**2 - 323) & (skoM**3*skoSINS*(skoM*skoS*(skoS*(skoS + 3) - 3) - 5*skoM + skoSINS*(skoS + 1) + 36) <= 2*skoM**3*(-skoM*(skoM - 54) - skoS*(skoM*skoS*(skoM*skoS + 3*skoM - 54) + 3*skoM*(skoM - 36) + 324) - 324))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), StrictGreaterThan(Pow(Symbol('skoM'), Integer(2)), Integer(0)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(323))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-323))), LessThan(Mul(Pow(Symbol('skoM'), Integer(3)), Symbol('skoSINS'), Add(Mul(Symbol('skoM'), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(3))), Integer(-3))), Mul(Integer(-1), Integer(5), Symbol('skoM')), Mul(Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(36))), Mul(Integer(2), Pow(Symbol('skoM'), Integer(3)), Add(Mul(Integer(-1), Symbol('skoM'), Add(Symbol('skoM'), Integer(-54))), Mul(Integer(-1), Symbol('skoS'), Add(Mul(Symbol('skoM'), Symbol('skoS'), Add(Mul(Symbol('skoM'), Symbol('skoS')), Mul(Integer(3), Symbol('skoM')), Integer(-54))), Mul(Integer(3), Symbol('skoM'), Add(Symbol('skoM'), Integer(-36))), Integer(324))), Integer(-324)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_7(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoM**2 > 0) & (delta >= skoSINS**2 + 323) & (delta >= -skoSINS**2 - 323) & (4*skoM**3*skoSINS*(10*skoM + skoSINS + 9) <= skoM**3*(-128*skoM**2 + 1728*skoM - 2592))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), StrictGreaterThan(Pow(Symbol('skoM'), Integer(2)), Integer(0)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(323))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-323))), LessThan(Mul(Integer(4), Pow(Symbol('skoM'), Integer(3)), Symbol('skoSINS'), Add(Mul(Integer(10), Symbol('skoM')), Symbol('skoSINS'), Integer(9))), Mul(Pow(Symbol('skoM'), Integer(3)), Add(Mul(Integer(-1), Integer(128), Pow(Symbol('skoM'), Integer(2))), Mul(Integer(1728), Symbol('skoM')), Integer(-2592)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_8(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (skoM**2 > 0) & (delta >= skoSINS**2 + 1221/4) & (delta >= -skoSINS**2 - 1221/4) & (skoM**3*skoSINS*(skoM*skoS*(skoS*(skoS + 3) - 3) - 5*skoM + skoSINS*(skoS + 1) + 35) <= skoM**3*(-2*skoM*(2*skoM - 105) - skoS*(2*skoM*skoS*(2*skoM*skoS + 6*skoM - 105) + 12*skoM*(skoM - 35) + 1225) - 1225)/2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), StrictGreaterThan(Pow(Symbol('skoM'), Integer(2)), Integer(0)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(1221, 4))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Rational(-1221, 4))), LessThan(Mul(Pow(Symbol('skoM'), Integer(3)), Symbol('skoSINS'), Add(Mul(Symbol('skoM'), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(3))), Integer(-3))), Mul(Integer(-1), Integer(5), Symbol('skoM')), Mul(Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(35))), Mul(Rational(1, 2), Pow(Symbol('skoM'), Integer(3)), Add(Mul(Integer(-1), Integer(2), Symbol('skoM'), Add(Mul(Integer(2), Symbol('skoM')), Integer(-105))), Mul(Integer(-1), Symbol('skoS'), Add(Mul(Integer(2), Symbol('skoM'), Symbol('skoS'), Add(Mul(Integer(2), Symbol('skoM'), Symbol('skoS')), Mul(Integer(6), Symbol('skoM')), Integer(-105))), Mul(Integer(12), Symbol('skoM'), Add(Symbol('skoM'), Integer(-35))), Integer(1225))), Integer(-1225)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_9(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoM**2 > 0) & (delta >= skoSINS**2 + 1221/4) & (delta >= -skoSINS**2 - 1221/4) & (skoM**3*skoSINS*(40*skoM + 4*skoSINS + 35) <= skoM**3*(-128*skoM**2 + 1680*skoM - 2450))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), StrictGreaterThan(Pow(Symbol('skoM'), Integer(2)), Integer(0)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(1221, 4))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Rational(-1221, 4))), LessThan(Mul(Pow(Symbol('skoM'), Integer(3)), Symbol('skoSINS'), Add(Mul(Integer(40), Symbol('skoM')), Mul(Integer(4), Symbol('skoSINS')), Integer(35))), Mul(Pow(Symbol('skoM'), Integer(3)), Add(Mul(Integer(-1), Integer(128), Pow(Symbol('skoM'), Integer(2))), Mul(Integer(1680), Symbol('skoM')), Integer(-2450)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_10(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (skoM**2 > 0) & (delta >= skoSINS**2 + 4745/16) & (delta >= -skoSINS**2 - 4745/16) & (skoM**3*skoSINS*(2*skoM*skoS*(skoS*(skoS + 3) - 3) - 10*skoM + 2*skoSINS*(skoS + 1) + 69)/2 <= skoM**3*(-4*skoM*(4*skoM - 207) - skoS*(4*skoM*skoS*(4*skoM*skoS + 12*skoM - 207) + 24*skoM*(2*skoM - 69) + 4761) - 4761)/8)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), StrictGreaterThan(Pow(Symbol('skoM'), Integer(2)), Integer(0)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(4745, 16))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Rational(-4745, 16))), LessThan(Mul(Rational(1, 2), Pow(Symbol('skoM'), Integer(3)), Symbol('skoSINS'), Add(Mul(Integer(2), Symbol('skoM'), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(3))), Integer(-3))), Mul(Integer(-1), Integer(10), Symbol('skoM')), Mul(Integer(2), Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(69))), Mul(Rational(1, 8), Pow(Symbol('skoM'), Integer(3)), Add(Mul(Integer(-1), Integer(4), Symbol('skoM'), Add(Mul(Integer(4), Symbol('skoM')), Integer(-207))), Mul(Integer(-1), Symbol('skoS'), Add(Mul(Integer(4), Symbol('skoM'), Symbol('skoS'), Add(Mul(Integer(4), Symbol('skoM'), Symbol('skoS')), Mul(Integer(12), Symbol('skoM')), Integer(-207))), Mul(Integer(24), Symbol('skoM'), Add(Mul(Integer(2), Symbol('skoM')), Integer(-69))), Integer(4761))), Integer(-4761)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_11(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoM**2 > 0) & (delta >= skoSINS**2 + 4745/16) & (delta >= -skoSINS**2 - 4745/16) & (skoM**3*skoSINS*(80*skoM + 8*skoSINS + 69)/2 <= skoM**3*(-256*skoM**2 + 3312*skoM - 4761)/2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), StrictGreaterThan(Pow(Symbol('skoM'), Integer(2)), Integer(0)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(4745, 16))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Rational(-4745, 16))), LessThan(Mul(Rational(1, 2), Pow(Symbol('skoM'), Integer(3)), Symbol('skoSINS'), Add(Mul(Integer(80), Symbol('skoM')), Mul(Integer(8), Symbol('skoSINS')), Integer(69))), Mul(Rational(1, 2), Pow(Symbol('skoM'), Integer(3)), Add(Mul(Integer(-1), Integer(256), Pow(Symbol('skoM'), Integer(2))), Mul(Integer(3312), Symbol('skoM')), Integer(-4761)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_12(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (skoM**2 > 0) & (delta >= skoSINS**2 + 18705/64) & (delta >= -skoSINS**2 - 18705/64) & (skoM**3*skoSINS*(4*skoM*skoS*(skoS*(skoS + 3) - 3) - 20*skoM + 4*skoSINS*(skoS + 1) + 137)/4 <= skoM**3*(-8*skoM*(8*skoM - 411) - skoS*(8*skoM*skoS*(8*skoM*skoS + 24*skoM - 411) + 48*skoM*(4*skoM - 137) + 18769) - 18769)/32)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), StrictGreaterThan(Pow(Symbol('skoM'), Integer(2)), Integer(0)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(18705, 64))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Rational(-18705, 64))), LessThan(Mul(Rational(1, 4), Pow(Symbol('skoM'), Integer(3)), Symbol('skoSINS'), Add(Mul(Integer(4), Symbol('skoM'), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(3))), Integer(-3))), Mul(Integer(-1), Integer(20), Symbol('skoM')), Mul(Integer(4), Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(137))), Mul(Rational(1, 32), Pow(Symbol('skoM'), Integer(3)), Add(Mul(Integer(-1), Integer(8), Symbol('skoM'), Add(Mul(Integer(8), Symbol('skoM')), Integer(-411))), Mul(Integer(-1), Symbol('skoS'), Add(Mul(Integer(8), Symbol('skoM'), Symbol('skoS'), Add(Mul(Integer(8), Symbol('skoM'), Symbol('skoS')), Mul(Integer(24), Symbol('skoM')), Integer(-411))), Mul(Integer(48), Symbol('skoM'), Add(Mul(Integer(4), Symbol('skoM')), Integer(-137))), Integer(18769))), Integer(-18769)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_13(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoM**2 > 0) & (delta >= skoSINS**2 + 18705/64) & (delta >= -skoSINS**2 - 18705/64) & (skoM**3*skoSINS*(160*skoM + 16*skoSINS + 137)/4 <= skoM**3*(-1024*skoM**2 + 13152*skoM - 18769)/8)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), StrictGreaterThan(Pow(Symbol('skoM'), Integer(2)), Integer(0)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(18705, 64))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Rational(-18705, 64))), LessThan(Mul(Rational(1, 4), Pow(Symbol('skoM'), Integer(3)), Symbol('skoSINS'), Add(Mul(Integer(160), Symbol('skoM')), Mul(Integer(16), Symbol('skoSINS')), Integer(137))), Mul(Rational(1, 8), Pow(Symbol('skoM'), Integer(3)), Add(Mul(Integer(-1), Integer(1024), Pow(Symbol('skoM'), Integer(2))), Mul(Integer(13152), Symbol('skoM')), Integer(-18769)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_14(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (skoM**2 > 0) & (delta >= skoSINS**2 + 74273/256) & (delta >= -skoSINS**2 - 74273/256) & (skoM**3*skoSINS*(8*skoM*skoS*(skoS*(skoS + 3) - 3) - 40*skoM + 8*skoSINS*(skoS + 1) + 273)/8 <= skoM**3*(-16*skoM*(16*skoM - 819) - skoS*(16*skoM*skoS*(16*skoM*skoS + 48*skoM - 819) + 96*skoM*(8*skoM - 273) + 74529) - 74529)/128)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), StrictGreaterThan(Pow(Symbol('skoM'), Integer(2)), Integer(0)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(74273, 256))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Rational(-74273, 256))), LessThan(Mul(Rational(1, 8), Pow(Symbol('skoM'), Integer(3)), Symbol('skoSINS'), Add(Mul(Integer(8), Symbol('skoM'), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(3))), Integer(-3))), Mul(Integer(-1), Integer(40), Symbol('skoM')), Mul(Integer(8), Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(273))), Mul(Rational(1, 128), Pow(Symbol('skoM'), Integer(3)), Add(Mul(Integer(-1), Integer(16), Symbol('skoM'), Add(Mul(Integer(16), Symbol('skoM')), Integer(-819))), Mul(Integer(-1), Symbol('skoS'), Add(Mul(Integer(16), Symbol('skoM'), Symbol('skoS'), Add(Mul(Integer(16), Symbol('skoM'), Symbol('skoS')), Mul(Integer(48), Symbol('skoM')), Integer(-819))), Mul(Integer(96), Symbol('skoM'), Add(Mul(Integer(8), Symbol('skoM')), Integer(-273))), Integer(74529))), Integer(-74529)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_15(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoM**2 > 0) & (delta >= skoSINS**2 + 74273/256) & (delta >= -skoSINS**2 - 74273/256) & (skoM**3*skoSINS*(320*skoM + 32*skoSINS + 273)/8 <= skoM**3*(-4096*skoM**2 + 52416*skoM - 74529)/32)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), StrictGreaterThan(Pow(Symbol('skoM'), Integer(2)), Integer(0)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(74273, 256))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Rational(-74273, 256))), LessThan(Mul(Rational(1, 8), Pow(Symbol('skoM'), Integer(3)), Symbol('skoSINS'), Add(Mul(Integer(320), Symbol('skoM')), Mul(Integer(32), Symbol('skoSINS')), Integer(273))), Mul(Rational(1, 32), Pow(Symbol('skoM'), Integer(3)), Add(Mul(Integer(-1), Integer(4096), Pow(Symbol('skoM'), Integer(2))), Mul(Integer(52416), Symbol('skoM')), Integer(-74529)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_16(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (skoM**2 > 0) & (delta >= skoSINS**2 + 1186185/4096) & (delta >= -skoSINS**2 - 1186185/4096) & (skoM**3*skoSINS*(32*skoM*skoS*(skoS*(skoS + 3) - 3) - 160*skoM + 32*skoSINS*(skoS + 1) + 1091)/32 <= skoM**3*(-64*skoM*(64*skoM - 3273) - skoS*(64*skoM*skoS*(64*skoM*skoS + 192*skoM - 3273) + 384*skoM*(32*skoM - 1091) + 1190281) - 1190281)/2048)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), StrictGreaterThan(Pow(Symbol('skoM'), Integer(2)), Integer(0)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(1186185, 4096))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Rational(-1186185, 4096))), LessThan(Mul(Rational(1, 32), Pow(Symbol('skoM'), Integer(3)), Symbol('skoSINS'), Add(Mul(Integer(32), Symbol('skoM'), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(3))), Integer(-3))), Mul(Integer(-1), Integer(160), Symbol('skoM')), Mul(Integer(32), Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(1091))), Mul(Rational(1, 2048), Pow(Symbol('skoM'), Integer(3)), Add(Mul(Integer(-1), Integer(64), Symbol('skoM'), Add(Mul(Integer(64), Symbol('skoM')), Integer(-3273))), Mul(Integer(-1), Symbol('skoS'), Add(Mul(Integer(64), Symbol('skoM'), Symbol('skoS'), Add(Mul(Integer(64), Symbol('skoM'), Symbol('skoS')), Mul(Integer(192), Symbol('skoM')), Integer(-3273))), Mul(Integer(384), Symbol('skoM'), Add(Mul(Integer(32), Symbol('skoM')), Integer(-1091))), Integer(1190281))), Integer(-1190281)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_17(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoM**2 > 0) & (delta >= skoSINS**2 + 1186185/4096) & (delta >= -skoSINS**2 - 1186185/4096) & (skoM**3*skoSINS*(1280*skoM + 128*skoSINS + 1091)/32 <= skoM**3*(-65536*skoM**2 + 837888*skoM - 1190281)/512)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), StrictGreaterThan(Pow(Symbol('skoM'), Integer(2)), Integer(0)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(1186185, 4096))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Rational(-1186185, 4096))), LessThan(Mul(Rational(1, 32), Pow(Symbol('skoM'), Integer(3)), Symbol('skoSINS'), Add(Mul(Integer(1280), Symbol('skoM')), Mul(Integer(128), Symbol('skoSINS')), Integer(1091))), Mul(Rational(1, 512), Pow(Symbol('skoM'), Integer(3)), Add(Mul(Integer(-1), Integer(65536), Pow(Symbol('skoM'), Integer(2))), Mul(Integer(837888), Symbol('skoM')), Integer(-1190281)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_18(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (skoM**2 > 0) & (delta >= skoSINS**2 + 4740377/16384) & (delta >= -skoSINS**2 - 4740377/16384) & (skoM**3*skoSINS*(64*skoM*skoS*(skoS*(skoS + 3) - 3) - 320*skoM + 64*skoSINS*(skoS + 1) + 2181)/64 <= skoM**3*(-128*skoM*(128*skoM - 6543) - skoS*(128*skoM*skoS*(128*skoM*skoS + 384*skoM - 6543) + 768*skoM*(64*skoM - 2181) + 4756761) - 4756761)/8192)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), StrictGreaterThan(Pow(Symbol('skoM'), Integer(2)), Integer(0)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(4740377, 16384))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Rational(-4740377, 16384))), LessThan(Mul(Rational(1, 64), Pow(Symbol('skoM'), Integer(3)), Symbol('skoSINS'), Add(Mul(Integer(64), Symbol('skoM'), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(3))), Integer(-3))), Mul(Integer(-1), Integer(320), Symbol('skoM')), Mul(Integer(64), Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(2181))), Mul(Rational(1, 8192), Pow(Symbol('skoM'), Integer(3)), Add(Mul(Integer(-1), Integer(128), Symbol('skoM'), Add(Mul(Integer(128), Symbol('skoM')), Integer(-6543))), Mul(Integer(-1), Symbol('skoS'), Add(Mul(Integer(128), Symbol('skoM'), Symbol('skoS'), Add(Mul(Integer(128), Symbol('skoM'), Symbol('skoS')), Mul(Integer(384), Symbol('skoM')), Integer(-6543))), Mul(Integer(768), Symbol('skoM'), Add(Mul(Integer(64), Symbol('skoM')), Integer(-2181))), Integer(4756761))), Integer(-4756761)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_19(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoM**2 > 0) & (delta >= skoSINS**2 + 4740377/16384) & (delta >= -skoSINS**2 - 4740377/16384) & (skoM**3*skoSINS*(2560*skoM + 256*skoSINS + 2181)/64 <= skoM**3*(-262144*skoM**2 + 3350016*skoM - 4756761)/2048)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), StrictGreaterThan(Pow(Symbol('skoM'), Integer(2)), Integer(0)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(4740377, 16384))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Rational(-4740377, 16384))), LessThan(Mul(Rational(1, 64), Pow(Symbol('skoM'), Integer(3)), Symbol('skoSINS'), Add(Mul(Integer(2560), Symbol('skoM')), Mul(Integer(256), Symbol('skoSINS')), Integer(2181))), Mul(Rational(1, 2048), Pow(Symbol('skoM'), Integer(3)), Add(Mul(Integer(-1), Integer(262144), Pow(Symbol('skoM'), Integer(2))), Mul(Integer(3350016), Symbol('skoM')), Integer(-4756761)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_20(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (skoM**2 > 0) & (delta >= skoSINS**2 + 18952785/65536) & (delta >= -skoSINS**2 - 18952785/65536) & (skoM**3*skoSINS*(128*skoM*skoS*(skoS*(skoS + 3) - 3) - 640*skoM + 128*skoSINS*(skoS + 1) + 4361)/128 <= skoM**3*(-256*skoM*(256*skoM - 13083) - skoS*(256*skoM*skoS*(256*skoM*skoS + 768*skoM - 13083) + 1536*skoM*(128*skoM - 4361) + 19018321) - 19018321)/32768)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), StrictGreaterThan(Pow(Symbol('skoM'), Integer(2)), Integer(0)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(18952785, 65536))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Rational(-18952785, 65536))), LessThan(Mul(Rational(1, 128), Pow(Symbol('skoM'), Integer(3)), Symbol('skoSINS'), Add(Mul(Integer(128), Symbol('skoM'), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(3))), Integer(-3))), Mul(Integer(-1), Integer(640), Symbol('skoM')), Mul(Integer(128), Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(4361))), Mul(Rational(1, 32768), Pow(Symbol('skoM'), Integer(3)), Add(Mul(Integer(-1), Integer(256), Symbol('skoM'), Add(Mul(Integer(256), Symbol('skoM')), Integer(-13083))), Mul(Integer(-1), Symbol('skoS'), Add(Mul(Integer(256), Symbol('skoM'), Symbol('skoS'), Add(Mul(Integer(256), Symbol('skoM'), Symbol('skoS')), Mul(Integer(768), Symbol('skoM')), Integer(-13083))), Mul(Integer(1536), Symbol('skoM'), Add(Mul(Integer(128), Symbol('skoM')), Integer(-4361))), Integer(19018321))), Integer(-19018321)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_21(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoM**2 > 0) & (delta >= skoSINS**2 + 18952785/65536) & (delta >= -skoSINS**2 - 18952785/65536) & (skoM**3*skoSINS*(5120*skoM + 512*skoSINS + 4361)/128 <= skoM**3*(-1048576*skoM**2 + 13396992*skoM - 19018321)/8192)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), StrictGreaterThan(Pow(Symbol('skoM'), Integer(2)), Integer(0)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(18952785, 65536))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Rational(-18952785, 65536))), LessThan(Mul(Rational(1, 128), Pow(Symbol('skoM'), Integer(3)), Symbol('skoSINS'), Add(Mul(Integer(5120), Symbol('skoM')), Mul(Integer(512), Symbol('skoSINS')), Integer(4361))), Mul(Rational(1, 8192), Pow(Symbol('skoM'), Integer(3)), Add(Mul(Integer(-1), Integer(1048576), Pow(Symbol('skoM'), Integer(2))), Mul(Integer(13396992), Symbol('skoM')), Integer(-19018321)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_22(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (skoM**2 > 0) & (delta >= skoSINS**2 + 75793697/262144) & (delta >= -skoSINS**2 - 75793697/262144) & (skoM**3*skoSINS*(256*skoM*skoS*(skoS*(skoS + 3) - 3) - 1280*skoM + 256*skoSINS*(skoS + 1) + 8721)/256 <= skoM**3*(-512*skoM*(512*skoM - 26163) - skoS*(512*skoM*skoS*(512*skoM*skoS + 1536*skoM - 26163) + 3072*skoM*(256*skoM - 8721) + 76055841) - 76055841)/131072)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), StrictGreaterThan(Pow(Symbol('skoM'), Integer(2)), Integer(0)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(75793697, 262144))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Rational(-75793697, 262144))), LessThan(Mul(Rational(1, 256), Pow(Symbol('skoM'), Integer(3)), Symbol('skoSINS'), Add(Mul(Integer(256), Symbol('skoM'), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(3))), Integer(-3))), Mul(Integer(-1), Integer(1280), Symbol('skoM')), Mul(Integer(256), Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(8721))), Mul(Rational(1, 131072), Pow(Symbol('skoM'), Integer(3)), Add(Mul(Integer(-1), Integer(512), Symbol('skoM'), Add(Mul(Integer(512), Symbol('skoM')), Integer(-26163))), Mul(Integer(-1), Symbol('skoS'), Add(Mul(Integer(512), Symbol('skoM'), Symbol('skoS'), Add(Mul(Integer(512), Symbol('skoM'), Symbol('skoS')), Mul(Integer(1536), Symbol('skoM')), Integer(-26163))), Mul(Integer(3072), Symbol('skoM'), Add(Mul(Integer(256), Symbol('skoM')), Integer(-8721))), Integer(76055841))), Integer(-76055841)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_23(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoM**2 > 0) & (delta >= skoSINS**2 + 75793697/262144) & (delta >= -skoSINS**2 - 75793697/262144) & (skoM**3*skoSINS*(10240*skoM + 1024*skoSINS + 8721)/256 <= skoM**3*(-4194304*skoM**2 + 53581824*skoM - 76055841)/32768)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), StrictGreaterThan(Pow(Symbol('skoM'), Integer(2)), Integer(0)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(75793697, 262144))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Rational(-75793697, 262144))), LessThan(Mul(Rational(1, 256), Pow(Symbol('skoM'), Integer(3)), Symbol('skoSINS'), Add(Mul(Integer(10240), Symbol('skoM')), Mul(Integer(1024), Symbol('skoSINS')), Integer(8721))), Mul(Rational(1, 32768), Pow(Symbol('skoM'), Integer(3)), Add(Mul(Integer(-1), Integer(4194304), Pow(Symbol('skoM'), Integer(2))), Mul(Integer(53581824), Symbol('skoM')), Integer(-76055841)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_24(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (skoM**2 > 0) & (delta >= skoSINS**2 + 1212629385/4194304) & (delta >= -skoSINS**2 - 1212629385/4194304) & (skoM**3*skoSINS*(1024*skoM*skoS*(skoS*(skoS + 3) - 3) - 5120*skoM + 1024*skoSINS*(skoS + 1) + 34883)/1024 <= skoM**3*(-2048*skoM*(2048*skoM - 104649) - skoS*(2048*skoM*skoS*(2048*skoM*skoS + 6144*skoM - 104649) + 12288*skoM*(1024*skoM - 34883) + 1216823689) - 1216823689)/2097152)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), StrictGreaterThan(Pow(Symbol('skoM'), Integer(2)), Integer(0)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(1212629385, 4194304))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Rational(-1212629385, 4194304))), LessThan(Mul(Rational(1, 1024), Pow(Symbol('skoM'), Integer(3)), Symbol('skoSINS'), Add(Mul(Integer(1024), Symbol('skoM'), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(3))), Integer(-3))), Mul(Integer(-1), Integer(5120), Symbol('skoM')), Mul(Integer(1024), Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(34883))), Mul(Rational(1, 2097152), Pow(Symbol('skoM'), Integer(3)), Add(Mul(Integer(-1), Integer(2048), Symbol('skoM'), Add(Mul(Integer(2048), Symbol('skoM')), Integer(-104649))), Mul(Integer(-1), Symbol('skoS'), Add(Mul(Integer(2048), Symbol('skoM'), Symbol('skoS'), Add(Mul(Integer(2048), Symbol('skoM'), Symbol('skoS')), Mul(Integer(6144), Symbol('skoM')), Integer(-104649))), Mul(Integer(12288), Symbol('skoM'), Add(Mul(Integer(1024), Symbol('skoM')), Integer(-34883))), Integer(1216823689))), Integer(-1216823689)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_25(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoM**2 > 0) & (delta >= skoSINS**2 + 1212629385/4194304) & (delta >= -skoSINS**2 - 1212629385/4194304) & (skoM**3*skoSINS*(40960*skoM + 4096*skoSINS + 34883)/1024 <= skoM**3*(-67108864*skoM**2 + 857284608*skoM - 1216823689)/524288)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), StrictGreaterThan(Pow(Symbol('skoM'), Integer(2)), Integer(0)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(1212629385, 4194304))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Rational(-1212629385, 4194304))), LessThan(Mul(Rational(1, 1024), Pow(Symbol('skoM'), Integer(3)), Symbol('skoSINS'), Add(Mul(Integer(40960), Symbol('skoM')), Mul(Integer(4096), Symbol('skoSINS')), Integer(34883))), Mul(Rational(1, 524288), Pow(Symbol('skoM'), Integer(3)), Add(Mul(Integer(-1), Integer(67108864), Pow(Symbol('skoM'), Integer(2))), Mul(Integer(857284608), Symbol('skoM')), Integer(-1216823689)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_26(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (skoM**2 > 0) & (delta >= skoSINS**2 + 4850378009/16777216) & (delta >= -skoSINS**2 - 4850378009/16777216) & (skoM**3*skoSINS*(2048*skoM*skoS*(skoS*(skoS + 3) - 3) - 10240*skoM + 2048*skoSINS*(skoS + 1) + 69765)/2048 <= skoM**3*(-4096*skoM*(4096*skoM - 209295) - skoS*(4096*skoM*skoS*(4096*skoM*skoS + 12288*skoM - 209295) + 24576*skoM*(2048*skoM - 69765) + 4867155225) - 4867155225)/8388608)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), StrictGreaterThan(Pow(Symbol('skoM'), Integer(2)), Integer(0)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(4850378009, 16777216))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Rational(-4850378009, 16777216))), LessThan(Mul(Rational(1, 2048), Pow(Symbol('skoM'), Integer(3)), Symbol('skoSINS'), Add(Mul(Integer(2048), Symbol('skoM'), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(3))), Integer(-3))), Mul(Integer(-1), Integer(10240), Symbol('skoM')), Mul(Integer(2048), Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(69765))), Mul(Rational(1, 8388608), Pow(Symbol('skoM'), Integer(3)), Add(Mul(Integer(-1), Integer(4096), Symbol('skoM'), Add(Mul(Integer(4096), Symbol('skoM')), Integer(-209295))), Mul(Integer(-1), Symbol('skoS'), Add(Mul(Integer(4096), Symbol('skoM'), Symbol('skoS'), Add(Mul(Integer(4096), Symbol('skoM'), Symbol('skoS')), Mul(Integer(12288), Symbol('skoM')), Integer(-209295))), Mul(Integer(24576), Symbol('skoM'), Add(Mul(Integer(2048), Symbol('skoM')), Integer(-69765))), Integer(4867155225))), Integer(-4867155225)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_27(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoM**2 > 0) & (delta >= skoSINS**2 + 4850378009/16777216) & (delta >= -skoSINS**2 - 4850378009/16777216) & (skoM**3*skoSINS*(81920*skoM + 8192*skoSINS + 69765)/2048 <= skoM**3*(-268435456*skoM**2 + 3429089280*skoM - 4867155225)/2097152)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), StrictGreaterThan(Pow(Symbol('skoM'), Integer(2)), Integer(0)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(4850378009, 16777216))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Rational(-4850378009, 16777216))), LessThan(Mul(Rational(1, 2048), Pow(Symbol('skoM'), Integer(3)), Symbol('skoSINS'), Add(Mul(Integer(81920), Symbol('skoM')), Mul(Integer(8192), Symbol('skoSINS')), Integer(69765))), Mul(Rational(1, 2097152), Pow(Symbol('skoM'), Integer(3)), Add(Mul(Integer(-1), Integer(268435456), Pow(Symbol('skoM'), Integer(2))), Mul(Integer(3429089280), Symbol('skoM')), Integer(-4867155225)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_28(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (skoM**2 > 0) & (delta >= skoSINS**2 + 19401232977/67108864) & (delta >= -skoSINS**2 - 19401232977/67108864) & (skoM**3*skoSINS*(4096*skoM*skoS*(skoS*(skoS + 3) - 3) - 20480*skoM + 4096*skoSINS*(skoS + 1) + 139529)/4096 <= skoM**3*(-8192*skoM*(8192*skoM - 418587) - skoS*(8192*skoM*skoS*(8192*skoM*skoS + 24576*skoM - 418587) + 49152*skoM*(4096*skoM - 139529) + 19468341841) - 19468341841)/33554432)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), StrictGreaterThan(Pow(Symbol('skoM'), Integer(2)), Integer(0)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(19401232977, 67108864))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Rational(-19401232977, 67108864))), LessThan(Mul(Rational(1, 4096), Pow(Symbol('skoM'), Integer(3)), Symbol('skoSINS'), Add(Mul(Integer(4096), Symbol('skoM'), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(3))), Integer(-3))), Mul(Integer(-1), Integer(20480), Symbol('skoM')), Mul(Integer(4096), Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(139529))), Mul(Rational(1, 33554432), Pow(Symbol('skoM'), Integer(3)), Add(Mul(Integer(-1), Integer(8192), Symbol('skoM'), Add(Mul(Integer(8192), Symbol('skoM')), Integer(-418587))), Mul(Integer(-1), Symbol('skoS'), Add(Mul(Integer(8192), Symbol('skoM'), Symbol('skoS'), Add(Mul(Integer(8192), Symbol('skoM'), Symbol('skoS')), Mul(Integer(24576), Symbol('skoM')), Integer(-418587))), Mul(Integer(49152), Symbol('skoM'), Add(Mul(Integer(4096), Symbol('skoM')), Integer(-139529))), Integer(19468341841))), Integer(-19468341841)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_29(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoM**2 > 0) & (delta >= skoSINS**2 + 19401232977/67108864) & (delta >= -skoSINS**2 - 19401232977/67108864) & (skoM**3*skoSINS*(163840*skoM + 16384*skoSINS + 139529)/4096 <= skoM**3*(-1073741824*skoM**2 + 13716258816*skoM - 19468341841)/8388608)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), StrictGreaterThan(Pow(Symbol('skoM'), Integer(2)), Integer(0)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(19401232977, 67108864))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Rational(-19401232977, 67108864))), LessThan(Mul(Rational(1, 4096), Pow(Symbol('skoM'), Integer(3)), Symbol('skoSINS'), Add(Mul(Integer(163840), Symbol('skoM')), Mul(Integer(16384), Symbol('skoSINS')), Integer(139529))), Mul(Rational(1, 8388608), Pow(Symbol('skoM'), Integer(3)), Add(Mul(Integer(-1), Integer(1073741824), Pow(Symbol('skoM'), Integer(2))), Mul(Integer(13716258816), Symbol('skoM')), Integer(-19468341841)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_30(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (skoM**2 > 0) & (delta >= skoSINS**2 + 77604373793/268435456) & (delta >= -skoSINS**2 - 77604373793/268435456) & (skoM**3*skoSINS*(8192*skoM*skoS*(skoS*(skoS + 3) - 3) - 40960*skoM + 8192*skoSINS*(skoS + 1) + 279057)/8192 <= skoM**3*(-16384*skoM*(16384*skoM - 837171) - skoS*(16384*skoM*skoS*(16384*skoM*skoS + 49152*skoM - 837171) + 98304*skoM*(8192*skoM - 279057) + 77872809249) - 77872809249)/134217728)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), StrictGreaterThan(Pow(Symbol('skoM'), Integer(2)), Integer(0)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(77604373793, 268435456))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Rational(-77604373793, 268435456))), LessThan(Mul(Rational(1, 8192), Pow(Symbol('skoM'), Integer(3)), Symbol('skoSINS'), Add(Mul(Integer(8192), Symbol('skoM'), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(3))), Integer(-3))), Mul(Integer(-1), Integer(40960), Symbol('skoM')), Mul(Integer(8192), Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(279057))), Mul(Rational(1, 134217728), Pow(Symbol('skoM'), Integer(3)), Add(Mul(Integer(-1), Integer(16384), Symbol('skoM'), Add(Mul(Integer(16384), Symbol('skoM')), Integer(-837171))), Mul(Integer(-1), Symbol('skoS'), Add(Mul(Integer(16384), Symbol('skoM'), Symbol('skoS'), Add(Mul(Integer(16384), Symbol('skoM'), Symbol('skoS')), Mul(Integer(49152), Symbol('skoM')), Integer(-837171))), Mul(Integer(98304), Symbol('skoM'), Add(Mul(Integer(8192), Symbol('skoM')), Integer(-279057))), Integer(77872809249))), Integer(-77872809249)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_31(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoM**2 > 0) & (delta >= skoSINS**2 + 77604373793/268435456) & (delta >= -skoSINS**2 - 77604373793/268435456) & (skoM**3*skoSINS*(327680*skoM + 32768*skoSINS + 279057)/8192 <= skoM**3*(-4294967296*skoM**2 + 54864838656*skoM - 77872809249)/33554432)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), StrictGreaterThan(Pow(Symbol('skoM'), Integer(2)), Integer(0)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(77604373793, 268435456))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Rational(-77604373793, 268435456))), LessThan(Mul(Rational(1, 8192), Pow(Symbol('skoM'), Integer(3)), Symbol('skoSINS'), Add(Mul(Integer(327680), Symbol('skoM')), Mul(Integer(32768), Symbol('skoSINS')), Integer(279057))), Mul(Rational(1, 33554432), Pow(Symbol('skoM'), Integer(3)), Add(Mul(Integer(-1), Integer(4294967296), Pow(Symbol('skoM'), Integer(2))), Mul(Integer(54864838656), Symbol('skoM')), Integer(-77872809249)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_32(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (skoM**2 > 0) & (delta >= skoSINS**2 + 1241667748233/4294967296) & (delta >= -skoSINS**2 - 1241667748233/4294967296) & (skoM**3*skoSINS*(32768*skoM*skoS*(skoS*(skoS + 3) - 3) - 163840*skoM + 32768*skoSINS*(skoS + 1) + 1116227)/32768 <= skoM**3*(-65536*skoM*(65536*skoM - 3348681) - skoS*(65536*skoM*skoS*(65536*skoM*skoS + 196608*skoM - 3348681) + 393216*skoM*(32768*skoM - 1116227) + 1245962715529) - 1245962715529)/2147483648)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), StrictGreaterThan(Pow(Symbol('skoM'), Integer(2)), Integer(0)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(1241667748233, 4294967296))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Rational(-1241667748233, 4294967296))), LessThan(Mul(Rational(1, 32768), Pow(Symbol('skoM'), Integer(3)), Symbol('skoSINS'), Add(Mul(Integer(32768), Symbol('skoM'), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(3))), Integer(-3))), Mul(Integer(-1), Integer(163840), Symbol('skoM')), Mul(Integer(32768), Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(1116227))), Mul(Rational(1, 2147483648), Pow(Symbol('skoM'), Integer(3)), Add(Mul(Integer(-1), Integer(65536), Symbol('skoM'), Add(Mul(Integer(65536), Symbol('skoM')), Integer(-3348681))), Mul(Integer(-1), Symbol('skoS'), Add(Mul(Integer(65536), Symbol('skoM'), Symbol('skoS'), Add(Mul(Integer(65536), Symbol('skoM'), Symbol('skoS')), Mul(Integer(196608), Symbol('skoM')), Integer(-3348681))), Mul(Integer(393216), Symbol('skoM'), Add(Mul(Integer(32768), Symbol('skoM')), Integer(-1116227))), Integer(1245962715529))), Integer(-1245962715529)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_33(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoM**2 > 0) & (delta >= skoSINS**2 + 1241667748233/4294967296) & (delta >= -skoSINS**2 - 1241667748233/4294967296) & (skoM**3*skoSINS*(1310720*skoM + 131072*skoSINS + 1116227)/32768 <= skoM**3*(-68719476736*skoM**2 + 877836632064*skoM - 1245962715529)/536870912)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), StrictGreaterThan(Pow(Symbol('skoM'), Integer(2)), Integer(0)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(1241667748233, 4294967296))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Rational(-1241667748233, 4294967296))), LessThan(Mul(Rational(1, 32768), Pow(Symbol('skoM'), Integer(3)), Symbol('skoSINS'), Add(Mul(Integer(1310720), Symbol('skoM')), Mul(Integer(131072), Symbol('skoSINS')), Integer(1116227))), Mul(Rational(1, 536870912), Pow(Symbol('skoM'), Integer(3)), Add(Mul(Integer(-1), Integer(68719476736), Pow(Symbol('skoM'), Integer(2))), Mul(Integer(877836632064), Symbol('skoM')), Integer(-1245962715529)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_34(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (skoM**2 > 0) & (delta >= skoSINS**2 + 4966666528025/17179869184) & (delta >= -skoSINS**2 - 4966666528025/17179869184) & (skoM**3*skoSINS*(65536*skoM*skoS*(skoS*(skoS + 3) - 3) - 327680*skoM + 65536*skoSINS*(skoS + 1) + 2232453)/65536 <= skoM**3*(-131072*skoM*(131072*skoM - 6697359) - skoS*(131072*skoM*skoS*(131072*skoM*skoS + 393216*skoM - 6697359) + 786432*skoM*(65536*skoM - 2232453) + 4983846397209) - 4983846397209)/8589934592)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), StrictGreaterThan(Pow(Symbol('skoM'), Integer(2)), Integer(0)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(4966666528025, 17179869184))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Rational(-4966666528025, 17179869184))), LessThan(Mul(Rational(1, 65536), Pow(Symbol('skoM'), Integer(3)), Symbol('skoSINS'), Add(Mul(Integer(65536), Symbol('skoM'), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(3))), Integer(-3))), Mul(Integer(-1), Integer(327680), Symbol('skoM')), Mul(Integer(65536), Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(2232453))), Mul(Rational(1, 8589934592), Pow(Symbol('skoM'), Integer(3)), Add(Mul(Integer(-1), Integer(131072), Symbol('skoM'), Add(Mul(Integer(131072), Symbol('skoM')), Integer(-6697359))), Mul(Integer(-1), Symbol('skoS'), Add(Mul(Integer(131072), Symbol('skoM'), Symbol('skoS'), Add(Mul(Integer(131072), Symbol('skoM'), Symbol('skoS')), Mul(Integer(393216), Symbol('skoM')), Integer(-6697359))), Mul(Integer(786432), Symbol('skoM'), Add(Mul(Integer(65536), Symbol('skoM')), Integer(-2232453))), Integer(4983846397209))), Integer(-4983846397209)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_35(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoM**2 > 0) & (delta >= skoSINS**2 + 4966666528025/17179869184) & (delta >= -skoSINS**2 - 4966666528025/17179869184) & (skoM**3*skoSINS*(2621440*skoM + 262144*skoSINS + 2232453)/65536 <= skoM**3*(-274877906944*skoM**2 + 3511344955392*skoM - 4983846397209)/2147483648)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), StrictGreaterThan(Pow(Symbol('skoM'), Integer(2)), Integer(0)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(4966666528025, 17179869184))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Rational(-4966666528025, 17179869184))), LessThan(Mul(Rational(1, 65536), Pow(Symbol('skoM'), Integer(3)), Symbol('skoSINS'), Add(Mul(Integer(2621440), Symbol('skoM')), Mul(Integer(262144), Symbol('skoSINS')), Integer(2232453))), Mul(Rational(1, 2147483648), Pow(Symbol('skoM'), Integer(3)), Add(Mul(Integer(-1), Integer(274877906944), Pow(Symbol('skoM'), Integer(2))), Mul(Integer(3511344955392), Symbol('skoM')), Integer(-4983846397209)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_36(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (skoM**2 > 0) & (delta >= skoSINS**2 + 19866657182289/68719476736) & (delta >= -skoSINS**2 - 19866657182289/68719476736) & (skoM**3*skoSINS*(131072*skoM*skoS*(skoS*(skoS + 3) - 3) - 655360*skoM + 131072*skoSINS*(skoS + 1) + 4464905)/131072 <= skoM**3*(-262144*skoM*(262144*skoM - 13394715) - skoS*(262144*skoM*skoS*(262144*skoM*skoS + 786432*skoM - 13394715) + 1572864*skoM*(131072*skoM - 4464905) + 19935376659025) - 19935376659025)/34359738368)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), StrictGreaterThan(Pow(Symbol('skoM'), Integer(2)), Integer(0)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(19866657182289, 68719476736))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Rational(-19866657182289, 68719476736))), LessThan(Mul(Rational(1, 131072), Pow(Symbol('skoM'), Integer(3)), Symbol('skoSINS'), Add(Mul(Integer(131072), Symbol('skoM'), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(3))), Integer(-3))), Mul(Integer(-1), Integer(655360), Symbol('skoM')), Mul(Integer(131072), Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(4464905))), Mul(Rational(1, 34359738368), Pow(Symbol('skoM'), Integer(3)), Add(Mul(Integer(-1), Integer(262144), Symbol('skoM'), Add(Mul(Integer(262144), Symbol('skoM')), Integer(-13394715))), Mul(Integer(-1), Symbol('skoS'), Add(Mul(Integer(262144), Symbol('skoM'), Symbol('skoS'), Add(Mul(Integer(262144), Symbol('skoM'), Symbol('skoS')), Mul(Integer(786432), Symbol('skoM')), Integer(-13394715))), Mul(Integer(1572864), Symbol('skoM'), Add(Mul(Integer(131072), Symbol('skoM')), Integer(-4464905))), Integer(19935376659025))), Integer(-19935376659025)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_37(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoM**2 > 0) & (delta >= skoSINS**2 + 19866657182289/68719476736) & (delta >= -skoSINS**2 - 19866657182289/68719476736) & (skoM**3*skoSINS*(5242880*skoM + 524288*skoSINS + 4464905)/131072 <= skoM**3*(-1099511627776*skoM**2 + 14045376675840*skoM - 19935376659025)/8589934592)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), StrictGreaterThan(Pow(Symbol('skoM'), Integer(2)), Integer(0)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(19866657182289, 68719476736))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Rational(-19866657182289, 68719476736))), LessThan(Mul(Rational(1, 131072), Pow(Symbol('skoM'), Integer(3)), Symbol('skoSINS'), Add(Mul(Integer(5242880), Symbol('skoM')), Mul(Integer(524288), Symbol('skoSINS')), Integer(4464905))), Mul(Rational(1, 8589934592), Pow(Symbol('skoM'), Integer(3)), Add(Mul(Integer(-1), Integer(1099511627776), Pow(Symbol('skoM'), Integer(2))), Mul(Integer(14045376675840), Symbol('skoM')), Integer(-19935376659025)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_38(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (skoM**2 > 0) & (delta >= skoSINS**2 + 79466610869537/274877906944) & (delta >= -skoSINS**2 - 79466610869537/274877906944) & (skoM**3*skoSINS*(262144*skoM*skoS*(skoS*(skoS + 3) - 3) - 1310720*skoM + 262144*skoSINS*(skoS + 1) + 8929809)/262144 <= skoM**3*(-524288*skoM*(524288*skoM - 26789427) - skoS*(524288*skoM*skoS*(524288*skoM*skoS + 1572864*skoM - 26789427) + 3145728*skoM*(262144*skoM - 8929809) + 79741488776481) - 79741488776481)/137438953472)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), StrictGreaterThan(Pow(Symbol('skoM'), Integer(2)), Integer(0)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(79466610869537, 274877906944))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Rational(-79466610869537, 274877906944))), LessThan(Mul(Rational(1, 262144), Pow(Symbol('skoM'), Integer(3)), Symbol('skoSINS'), Add(Mul(Integer(262144), Symbol('skoM'), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(3))), Integer(-3))), Mul(Integer(-1), Integer(1310720), Symbol('skoM')), Mul(Integer(262144), Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(8929809))), Mul(Rational(1, 137438953472), Pow(Symbol('skoM'), Integer(3)), Add(Mul(Integer(-1), Integer(524288), Symbol('skoM'), Add(Mul(Integer(524288), Symbol('skoM')), Integer(-26789427))), Mul(Integer(-1), Symbol('skoS'), Add(Mul(Integer(524288), Symbol('skoM'), Symbol('skoS'), Add(Mul(Integer(524288), Symbol('skoM'), Symbol('skoS')), Mul(Integer(1572864), Symbol('skoM')), Integer(-26789427))), Mul(Integer(3145728), Symbol('skoM'), Add(Mul(Integer(262144), Symbol('skoM')), Integer(-8929809))), Integer(79741488776481))), Integer(-79741488776481)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_39(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoM**2 > 0) & (delta >= skoSINS**2 + 79466610869537/274877906944) & (delta >= -skoSINS**2 - 79466610869537/274877906944) & (skoM**3*skoSINS*(10485760*skoM + 1048576*skoSINS + 8929809)/262144 <= skoM**3*(-4398046511104*skoM**2 + 56181500411904*skoM - 79741488776481)/34359738368)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), StrictGreaterThan(Pow(Symbol('skoM'), Integer(2)), Integer(0)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(79466610869537, 274877906944))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Rational(-79466610869537, 274877906944))), LessThan(Mul(Rational(1, 262144), Pow(Symbol('skoM'), Integer(3)), Symbol('skoSINS'), Add(Mul(Integer(10485760), Symbol('skoM')), Mul(Integer(1048576), Symbol('skoSINS')), Integer(8929809))), Mul(Rational(1, 34359738368), Pow(Symbol('skoM'), Integer(3)), Add(Mul(Integer(-1), Integer(4398046511104), Pow(Symbol('skoM'), Integer(2))), Mul(Integer(56181500411904), Symbol('skoM')), Integer(-79741488776481)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_40(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (skoM**2 > 0) & (delta >= skoSINS**2 + 1271465702474121/4398046511104) & (delta >= -skoSINS**2 - 1271465702474121/4398046511104) & (skoM**3*skoSINS*(1048576*skoM*skoS*(skoS*(skoS + 3) - 3) - 5242880*skoM + 1048576*skoSINS*(skoS + 1) + 35719235)/1048576 <= skoM**3*(-2097152*skoM*(2097152*skoM - 107157705) - skoS*(2097152*skoM*skoS*(2097152*skoM*skoS + 6291456*skoM - 107157705) + 12582912*skoM*(1048576*skoM - 35719235) + 1275863748985225) - 1275863748985225)/2199023255552)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), StrictGreaterThan(Pow(Symbol('skoM'), Integer(2)), Integer(0)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(1271465702474121, 4398046511104))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Rational(-1271465702474121, 4398046511104))), LessThan(Mul(Rational(1, 1048576), Pow(Symbol('skoM'), Integer(3)), Symbol('skoSINS'), Add(Mul(Integer(1048576), Symbol('skoM'), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(3))), Integer(-3))), Mul(Integer(-1), Integer(5242880), Symbol('skoM')), Mul(Integer(1048576), Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(35719235))), Mul(Rational(1, 2199023255552), Pow(Symbol('skoM'), Integer(3)), Add(Mul(Integer(-1), Integer(2097152), Symbol('skoM'), Add(Mul(Integer(2097152), Symbol('skoM')), Integer(-107157705))), Mul(Integer(-1), Symbol('skoS'), Add(Mul(Integer(2097152), Symbol('skoM'), Symbol('skoS'), Add(Mul(Integer(2097152), Symbol('skoM'), Symbol('skoS')), Mul(Integer(6291456), Symbol('skoM')), Integer(-107157705))), Mul(Integer(12582912), Symbol('skoM'), Add(Mul(Integer(1048576), Symbol('skoM')), Integer(-35719235))), Integer(1275863748985225))), Integer(-1275863748985225)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_41(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoM**2 > 0) & (delta >= skoSINS**2 + 1271465702474121/4398046511104) & (delta >= -skoSINS**2 - 1271465702474121/4398046511104) & (skoM**3*skoSINS*(41943040*skoM + 4194304*skoSINS + 35719235)/1048576 <= skoM**3*(-70368744177664*skoM**2 + 898903981424640*skoM - 1275863748985225)/549755813888)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), StrictGreaterThan(Pow(Symbol('skoM'), Integer(2)), Integer(0)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(1271465702474121, 4398046511104))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Rational(-1271465702474121, 4398046511104))), LessThan(Mul(Rational(1, 1048576), Pow(Symbol('skoM'), Integer(3)), Symbol('skoSINS'), Add(Mul(Integer(41943040), Symbol('skoM')), Mul(Integer(4194304), Symbol('skoSINS')), Integer(35719235))), Mul(Rational(1, 549755813888), Pow(Symbol('skoM'), Integer(3)), Add(Mul(Integer(-1), Integer(70368744177664), Pow(Symbol('skoM'), Integer(2))), Mul(Integer(898903981424640), Symbol('skoM')), Integer(-1275863748985225)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_42(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (skoM**2 > 0) & (delta >= skoSINS**2 + 5085862667019545/17592186044416) & (delta >= -skoSINS**2 - 5085862667019545/17592186044416) & (skoM**3*skoSINS*(2097152*skoM*skoS*(skoS*(skoS + 3) - 3) - 10485760*skoM + 2097152*skoSINS*(skoS + 1) + 71438469)/2097152 <= skoM**3*(-4194304*skoM*(4194304*skoM - 214315407) - skoS*(4194304*skoM*skoS*(4194304*skoM*skoS + 12582912*skoM - 214315407) + 25165824*skoM*(2097152*skoM - 71438469) + 5103454853063961) - 5103454853063961)/8796093022208)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), StrictGreaterThan(Pow(Symbol('skoM'), Integer(2)), Integer(0)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(5085862667019545, 17592186044416))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Rational(-5085862667019545, 17592186044416))), LessThan(Mul(Rational(1, 2097152), Pow(Symbol('skoM'), Integer(3)), Symbol('skoSINS'), Add(Mul(Integer(2097152), Symbol('skoM'), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(3))), Integer(-3))), Mul(Integer(-1), Integer(10485760), Symbol('skoM')), Mul(Integer(2097152), Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(71438469))), Mul(Rational(1, 8796093022208), Pow(Symbol('skoM'), Integer(3)), Add(Mul(Integer(-1), Integer(4194304), Symbol('skoM'), Add(Mul(Integer(4194304), Symbol('skoM')), Integer(-214315407))), Mul(Integer(-1), Symbol('skoS'), Add(Mul(Integer(4194304), Symbol('skoM'), Symbol('skoS'), Add(Mul(Integer(4194304), Symbol('skoM'), Symbol('skoS')), Mul(Integer(12582912), Symbol('skoM')), Integer(-214315407))), Mul(Integer(25165824), Symbol('skoM'), Add(Mul(Integer(2097152), Symbol('skoM')), Integer(-71438469))), Integer(5103454853063961))), Integer(-5103454853063961)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_43(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoM**2 > 0) & (delta >= skoSINS**2 + 5085862667019545/17592186044416) & (delta >= -skoSINS**2 - 5085862667019545/17592186044416) & (skoM**3*skoSINS*(83886080*skoM + 8388608*skoSINS + 71438469)/2097152 <= skoM**3*(-281474976710656*skoM**2 + 3595615875366912*skoM - 5103454853063961)/2199023255552)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), StrictGreaterThan(Pow(Symbol('skoM'), Integer(2)), Integer(0)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(5085862667019545, 17592186044416))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Rational(-5085862667019545, 17592186044416))), LessThan(Mul(Rational(1, 2097152), Pow(Symbol('skoM'), Integer(3)), Symbol('skoSINS'), Add(Mul(Integer(83886080), Symbol('skoM')), Mul(Integer(8388608), Symbol('skoSINS')), Integer(71438469))), Mul(Rational(1, 2199023255552), Pow(Symbol('skoM'), Integer(3)), Add(Mul(Integer(-1), Integer(281474976710656), Pow(Symbol('skoM'), Integer(2))), Mul(Integer(3595615875366912), Symbol('skoM')), Integer(-5103454853063961)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_44(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (skoM**2 > 0) & (delta >= skoSINS**2 + 20343450382324305/70368744177664) & (delta >= -skoSINS**2 - 20343450382324305/70368744177664) & (skoM**3*skoSINS*(4194304*skoM*skoS*(skoS*(skoS + 3) - 3) - 20971520*skoM + 4194304*skoSINS*(skoS + 1) + 142876937)/4194304 <= skoM**3*(-8388608*skoM*(8388608*skoM - 428630811) - skoS*(8388608*skoM*skoS*(8388608*skoM*skoS + 25165824*skoM - 428630811) + 50331648*skoM*(4194304*skoM - 142876937) + 20413819126501969) - 20413819126501969)/35184372088832)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), StrictGreaterThan(Pow(Symbol('skoM'), Integer(2)), Integer(0)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(20343450382324305, 70368744177664))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Rational(-20343450382324305, 70368744177664))), LessThan(Mul(Rational(1, 4194304), Pow(Symbol('skoM'), Integer(3)), Symbol('skoSINS'), Add(Mul(Integer(4194304), Symbol('skoM'), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(3))), Integer(-3))), Mul(Integer(-1), Integer(20971520), Symbol('skoM')), Mul(Integer(4194304), Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(142876937))), Mul(Rational(1, 35184372088832), Pow(Symbol('skoM'), Integer(3)), Add(Mul(Integer(-1), Integer(8388608), Symbol('skoM'), Add(Mul(Integer(8388608), Symbol('skoM')), Integer(-428630811))), Mul(Integer(-1), Symbol('skoS'), Add(Mul(Integer(8388608), Symbol('skoM'), Symbol('skoS'), Add(Mul(Integer(8388608), Symbol('skoM'), Symbol('skoS')), Mul(Integer(25165824), Symbol('skoM')), Integer(-428630811))), Mul(Integer(50331648), Symbol('skoM'), Add(Mul(Integer(4194304), Symbol('skoM')), Integer(-142876937))), Integer(20413819126501969))), Integer(-20413819126501969)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_45(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoM**2 > 0) & (delta >= skoSINS**2 + 20343450382324305/70368744177664) & (delta >= -skoSINS**2 - 20343450382324305/70368744177664) & (skoM**3*skoSINS*(167772160*skoM + 16777216*skoSINS + 142876937)/4194304 <= skoM**3*(-1125899906842624*skoM**2 + 14382463400804352*skoM - 20413819126501969)/8796093022208)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), StrictGreaterThan(Pow(Symbol('skoM'), Integer(2)), Integer(0)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(20343450382324305, 70368744177664))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Rational(-20343450382324305, 70368744177664))), LessThan(Mul(Rational(1, 4194304), Pow(Symbol('skoM'), Integer(3)), Symbol('skoSINS'), Add(Mul(Integer(167772160), Symbol('skoM')), Mul(Integer(16777216), Symbol('skoSINS')), Integer(142876937))), Mul(Rational(1, 8796093022208), Pow(Symbol('skoM'), Integer(3)), Add(Mul(Integer(-1), Integer(1125899906842624), Pow(Symbol('skoM'), Integer(2))), Mul(Integer(14382463400804352), Symbol('skoM')), Integer(-20413819126501969)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_46(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (skoM**2 > 0) & (delta >= skoSINS**2 + 81373800957789473/281474976710656) & (delta >= -skoSINS**2 - 81373800957789473/281474976710656) & (skoM**3*skoSINS*(8388608*skoM*skoS*(skoS*(skoS + 3) - 3) - 41943040*skoM + 8388608*skoSINS*(skoS + 1) + 285753873)/8388608 <= skoM**3*(-16777216*skoM*(16777216*skoM - 857261619) - skoS*(16777216*skoM*skoS*(16777216*skoM*skoS + 50331648*skoM - 857261619) + 100663296*skoM*(8388608*skoM - 285753873) + 81655275934500129) - 81655275934500129)/140737488355328)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), StrictGreaterThan(Pow(Symbol('skoM'), Integer(2)), Integer(0)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(81373800957789473, 281474976710656))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Rational(-81373800957789473, 281474976710656))), LessThan(Mul(Rational(1, 8388608), Pow(Symbol('skoM'), Integer(3)), Symbol('skoSINS'), Add(Mul(Integer(8388608), Symbol('skoM'), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(3))), Integer(-3))), Mul(Integer(-1), Integer(41943040), Symbol('skoM')), Mul(Integer(8388608), Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(285753873))), Mul(Rational(1, 140737488355328), Pow(Symbol('skoM'), Integer(3)), Add(Mul(Integer(-1), Integer(16777216), Symbol('skoM'), Add(Mul(Integer(16777216), Symbol('skoM')), Integer(-857261619))), Mul(Integer(-1), Symbol('skoS'), Add(Mul(Integer(16777216), Symbol('skoM'), Symbol('skoS'), Add(Mul(Integer(16777216), Symbol('skoM'), Symbol('skoS')), Mul(Integer(50331648), Symbol('skoM')), Integer(-857261619))), Mul(Integer(100663296), Symbol('skoM'), Add(Mul(Integer(8388608), Symbol('skoM')), Integer(-285753873))), Integer(81655275934500129))), Integer(-81655275934500129)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_47(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoM**2 > 0) & (delta >= skoSINS**2 + 81373800957789473/281474976710656) & (delta >= -skoSINS**2 - 81373800957789473/281474976710656) & (skoM**3*skoSINS*(335544320*skoM + 33554432*skoSINS + 285753873)/8388608 <= skoM**3*(-4503599627370496*skoM**2 + 57529853401890816*skoM - 81655275934500129)/35184372088832)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), StrictGreaterThan(Pow(Symbol('skoM'), Integer(2)), Integer(0)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(81373800957789473, 281474976710656))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Rational(-81373800957789473, 281474976710656))), LessThan(Mul(Rational(1, 8388608), Pow(Symbol('skoM'), Integer(3)), Symbol('skoSINS'), Add(Mul(Integer(335544320), Symbol('skoM')), Mul(Integer(33554432), Symbol('skoSINS')), Integer(285753873))), Mul(Rational(1, 35184372088832), Pow(Symbol('skoM'), Integer(3)), Add(Mul(Integer(-1), Integer(4503599627370496), Pow(Symbol('skoM'), Integer(2))), Mul(Integer(57529853401890816), Symbol('skoM')), Integer(-81655275934500129)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_48(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoS >= 2) & (skoM**2 > 0) & (delta >= skoSINS**2 + 224) & (delta >= -skoSINS**2 - 224) & (skoM**3*skoSINS*(skoM*skoS*(skoS*(skoS + 3) - 3) - 5*skoM + skoSINS*(skoS + 1) + 30) <= 2*skoM**3*(-skoM*(skoM - 45) - skoS*(skoM*skoS*(skoM*skoS + 3*skoM - 45) + 3*skoM*(skoM - 30) + 225) - 225))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), StrictGreaterThan(Pow(Symbol('skoM'), Integer(2)), Integer(0)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(224))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-224))), LessThan(Mul(Pow(Symbol('skoM'), Integer(3)), Symbol('skoSINS'), Add(Mul(Symbol('skoM'), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(3))), Integer(-3))), Mul(Integer(-1), Integer(5), Symbol('skoM')), Mul(Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(30))), Mul(Integer(2), Pow(Symbol('skoM'), Integer(3)), Add(Mul(Integer(-1), Symbol('skoM'), Add(Symbol('skoM'), Integer(-45))), Mul(Integer(-1), Symbol('skoS'), Add(Mul(Symbol('skoM'), Symbol('skoS'), Add(Mul(Symbol('skoM'), Symbol('skoS')), Mul(Integer(3), Symbol('skoM')), Integer(-45))), Mul(Integer(3), Symbol('skoM'), Add(Symbol('skoM'), Integer(-30))), Integer(225))), Integer(-225)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_49(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM >= 2) & (skoM**2 > 0) & (delta >= skoSINS**2 + 224) & (delta >= -skoSINS**2 - 224) & (skoM**3*skoSINS*(175*skoM + 28*skoSINS + 240)/8 <= 7*skoM**3*(-49*skoM**2 + 630*skoM - 900)/4)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoM'), Integer(2)), StrictGreaterThan(Pow(Symbol('skoM'), Integer(2)), Integer(0)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(224))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-224))), LessThan(Mul(Rational(1, 8), Pow(Symbol('skoM'), Integer(3)), Symbol('skoSINS'), Add(Mul(Integer(175), Symbol('skoM')), Mul(Integer(28), Symbol('skoSINS')), Integer(240))), Mul(Rational(7, 4), Pow(Symbol('skoM'), Integer(3)), Add(Mul(Integer(-1), Integer(49), Pow(Symbol('skoM'), Integer(2))), Mul(Integer(630), Symbol('skoM')), Integer(-900)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(delta:sympy.Rational, skoSINS:sympy.Rational, skoM:sympy.Rational, skoCOSS:sympy.Rational, skoS:sympy.Rational):
	# (0 <= delta) & (2 <= skoM) & (2 <= skoS) & (skoM**2 > 0) & (skoCOSS**2 + skoSINS**2 - 1 <= delta) & (-skoCOSS**2 - skoSINS**2 + 1 <= delta) & (skoSINS*(skoM**3*(-2*skoCOSS - 5*skoM) + skoS*(-3*skoM**4 + skoS*(skoM**4*skoS + 3*skoM**4)) + skoSINS*(skoM**3*skoS + skoM**3)) <= skoM**3*(-2*skoCOSS**2 + skoM*(-6*skoCOSS - 2*skoM)) + skoS*(skoM**3*(-2*skoCOSS**2 + skoM*(-12*skoCOSS - 6*skoM)) + skoS*(-2*skoM**5*skoS + skoM**4*(-6*skoCOSS - 6*skoM))))

	post_cond =  And(LessThan(Integer(0), Symbol('delta')), LessThan(Integer(2), Symbol('skoM')), LessThan(Integer(2), Symbol('skoS')), StrictGreaterThan(Pow(Symbol('skoM'), Integer(2)), Integer(0)), LessThan(Add(Pow(Symbol('skoCOSS'), Integer(2)), Pow(Symbol('skoSINS'), Integer(2)), Integer(-1)), Symbol('delta')), LessThan(Add(Mul(Integer(-1), Pow(Symbol('skoCOSS'), Integer(2))), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(1)), Symbol('delta')), LessThan(Mul(Symbol('skoSINS'), Add(Mul(Pow(Symbol('skoM'), Integer(3)), Add(Mul(Integer(-1), Integer(2), Symbol('skoCOSS')), Mul(Integer(-1), Integer(5), Symbol('skoM')))), Mul(Symbol('skoS'), Add(Mul(Integer(-1), Integer(3), Pow(Symbol('skoM'), Integer(4))), Mul(Symbol('skoS'), Add(Mul(Pow(Symbol('skoM'), Integer(4)), Symbol('skoS')), Mul(Integer(3), Pow(Symbol('skoM'), Integer(4))))))), Mul(Symbol('skoSINS'), Add(Mul(Pow(Symbol('skoM'), Integer(3)), Symbol('skoS')), Pow(Symbol('skoM'), Integer(3)))))), Add(Mul(Pow(Symbol('skoM'), Integer(3)), Add(Mul(Integer(-1), Integer(2), Pow(Symbol('skoCOSS'), Integer(2))), Mul(Symbol('skoM'), Add(Mul(Integer(-1), Integer(6), Symbol('skoCOSS')), Mul(Integer(-1), Integer(2), Symbol('skoM')))))), Mul(Symbol('skoS'), Add(Mul(Pow(Symbol('skoM'), Integer(3)), Add(Mul(Integer(-1), Integer(2), Pow(Symbol('skoCOSS'), Integer(2))), Mul(Symbol('skoM'), Add(Mul(Integer(-1), Integer(12), Symbol('skoCOSS')), Mul(Integer(-1), Integer(6), Symbol('skoM')))))), Mul(Symbol('skoS'), Add(Mul(Integer(-1), Integer(2), Pow(Symbol('skoM'), Integer(5)), Symbol('skoS')), Mul(Pow(Symbol('skoM'), Integer(4)), Add(Mul(Integer(-1), Integer(6), Symbol('skoCOSS')), Mul(Integer(-1), Integer(6), Symbol('skoM')))))))))))

	eval = post_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM, 'skoCOSS':skoCOSS, 'skoS':skoS })

	return eval == sympy.logic.boolalg.BooleanTrue





if __name__=="__main__":
	
	ip_0=int(input("enter integer numerator of delta:\n"))
	ip_1=int(input("enter integer denominator of delta:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	delta=sympy.Rational(ip_0,ip_1)
	
	
	ip_0=int(input("enter integer numerator of skoSINS:\n"))
	ip_1=int(input("enter integer denominator of skoSINS:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	skoSINS=sympy.Rational(ip_0,ip_1)
	
	
	ip_0=int(input("enter integer numerator of skoM:\n"))
	ip_1=int(input("enter integer denominator of skoM:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	skoM=sympy.Rational(ip_0,ip_1)
	
	
	
	
	if pre_condition_0(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_0 SAT")
		print('delta = 2693')
		print('skoM = 3')
		print('skoS = 3')
		print('skoCOSS = -22')
		print('skoSINS = -47')
		exit(0)
	
	
	if pre_condition_1(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_1 SAT")
		print('delta = 2693')
		print('skoM = 3')
		print('skoS = 3')
		print('skoCOSS = -22')
		print('skoSINS = -47')
		exit(0)
	
	
	if pre_condition_2(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_2 SAT")
		print('delta = 444889')
		print('skoM = 15')
		print('skoS = 16')
		print('skoCOSS = -667')
		print('skoSINS = 0')
		exit(0)
	
	
	if pre_condition_3(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_3 SAT")
		print('delta = 444889')
		print('skoM = 15')
		print('skoS = 16')
		print('skoCOSS = -667')
		print('skoSINS = 0')
		exit(0)
	
	
	if pre_condition_4(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_4 SAT")
		print('delta = 410')
		print('skoM = 3')
		print('skoS = 3')
		print('skoCOSS = -19')
		print('skoSINS = 7')
		exit(0)
	
	
	if pre_condition_5(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_5 SAT")
		print('delta = 410')
		print('skoM = 3')
		print('skoS = 3')
		print('skoCOSS = -19')
		print('skoSINS = 7')
		exit(0)
	
	
	if pre_condition_6(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_6 SAT")
		print('delta = 382')
		print('skoM = 3')
		print('skoS = 3')
		print('skoCOSS = -18')
		print('skoSINS = 61/8')
		exit(0)
	
	
	if pre_condition_7(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_7 SAT")
		print('delta = 382')
		print('skoM = 3')
		print('skoS = 3')
		print('skoCOSS = -18')
		print('skoSINS = 61/8')
		exit(0)
	
	
	if pre_condition_8(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_8 SAT")
		print('delta = 365')
		print('skoM = 3')
		print('skoS = 3')
		print('skoCOSS = -35/2')
		print('skoSINS = 247/32')
		exit(0)
	
	
	if pre_condition_9(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_9 SAT")
		print('delta = 365')
		print('skoM = 3')
		print('skoS = 3')
		print('skoCOSS = -35/2')
		print('skoSINS = 247/32')
		exit(0)
	
	
	if pre_condition_10(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_10 SAT")
		print('delta = 357')
		print('skoM = 3')
		print('skoS = 3')
		print('skoCOSS = -69/4')
		print('skoSINS = 495/64')
		exit(0)
	
	
	if pre_condition_11(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_11 SAT")
		print('delta = 357')
		print('skoM = 3')
		print('skoS = 3')
		print('skoCOSS = -69/4')
		print('skoSINS = 495/64')
		exit(0)
	
	
	if pre_condition_12(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_12 SAT")
		print('delta = 353')
		print('skoM = 3')
		print('skoS = 3')
		print('skoCOSS = -137/8')
		print('skoSINS = 3963/512')
		exit(0)
	
	
	if pre_condition_13(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_13 SAT")
		print('delta = 353')
		print('skoM = 3')
		print('skoS = 3')
		print('skoCOSS = -137/8')
		print('skoSINS = 3963/512')
		exit(0)
	
	
	if pre_condition_14(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_14 SAT")
		print('delta = 351')
		print('skoM = 3')
		print('skoS = 3')
		print('skoCOSS = -273/16')
		print('skoSINS = 15855/2048')
		exit(0)
	
	
	if pre_condition_15(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_15 SAT")
		print('delta = 351')
		print('skoM = 3')
		print('skoS = 3')
		print('skoCOSS = -273/16')
		print('skoSINS = 15855/2048')
		exit(0)
	
	
	if pre_condition_16(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_16 SAT")
		print('delta = 350')
		print('skoM = 3')
		print('skoS = 3')
		print('skoCOSS = -1091/64')
		print('skoSINS = 253687/32768')
		exit(0)
	
	
	if pre_condition_17(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_17 SAT")
		print('delta = 350')
		print('skoM = 3')
		print('skoS = 3')
		print('skoCOSS = -1091/64')
		print('skoSINS = 253687/32768')
		exit(0)
	
	
	if pre_condition_18(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_18 SAT")
		print('delta = 350')
		print('skoM = 3')
		print('skoS = 3')
		print('skoCOSS = -2181/128')
		print('skoSINS = 507375/65536')
		exit(0)
	
	
	if pre_condition_19(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_19 SAT")
		print('delta = 350')
		print('skoM = 3')
		print('skoS = 3')
		print('skoCOSS = -2181/128')
		print('skoSINS = 507375/65536')
		exit(0)
	
	
	if pre_condition_20(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_20 SAT")
		print('delta = 1397/4')
		print('skoM = 3')
		print('skoS = 3')
		print('skoCOSS = -4361/256')
		print('skoSINS = 4059003/524288')
		exit(0)
	
	
	if pre_condition_21(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_21 SAT")
		print('delta = 1397/4')
		print('skoM = 3')
		print('skoS = 3')
		print('skoCOSS = -4361/256')
		print('skoSINS = 4059003/524288')
		exit(0)
	
	
	if pre_condition_22(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_22 SAT")
		print('delta = 2793/8')
		print('skoM = 3')
		print('skoS = 3')
		print('skoCOSS = -8721/512')
		print('skoSINS = 16236015/2097152')
		exit(0)
	
	
	if pre_condition_23(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_23 SAT")
		print('delta = 2793/8')
		print('skoM = 3')
		print('skoS = 3')
		print('skoCOSS = -8721/512')
		print('skoSINS = 16236015/2097152')
		exit(0)
	
	
	if pre_condition_24(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_24 SAT")
		print('delta = 5585/16')
		print('skoM = 3')
		print('skoS = 3')
		print('skoCOSS = -34883/2048')
		print('skoSINS = 259776247/33554432')
		exit(0)
	
	
	if pre_condition_25(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_25 SAT")
		print('delta = 5585/16')
		print('skoM = 3')
		print('skoS = 3')
		print('skoCOSS = -34883/2048')
		print('skoSINS = 259776247/33554432')
		exit(0)
	
	
	if pre_condition_26(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_26 SAT")
		print('delta = 22339/64')
		print('skoM = 3')
		print('skoS = 3')
		print('skoCOSS = -69765/4096')
		print('skoSINS = 519552495/67108864')
		exit(0)
	
	
	if pre_condition_27(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_27 SAT")
		print('delta = 22339/64')
		print('skoM = 3')
		print('skoS = 3')
		print('skoCOSS = -69765/4096')
		print('skoSINS = 519552495/67108864')
		exit(0)
	
	
	if pre_condition_28(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_28 SAT")
		print('delta = 44677/128')
		print('skoM = 3')
		print('skoS = 3')
		print('skoCOSS = -139529/8192')
		print('skoSINS = 4156419963/536870912')
		exit(0)
	
	
	if pre_condition_29(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_29 SAT")
		print('delta = 44677/128')
		print('skoM = 3')
		print('skoS = 3')
		print('skoCOSS = -139529/8192')
		print('skoSINS = 4156419963/536870912')
		exit(0)
	
	
	if pre_condition_30(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_30 SAT")
		print('delta = 178707/512')
		print('skoM = 3')
		print('skoS = 3')
		print('skoCOSS = -279057/16384')
		print('skoSINS = 16625679855/2147483648')
		exit(0)
	
	
	if pre_condition_31(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_31 SAT")
		print('delta = 178707/512')
		print('skoM = 3')
		print('skoS = 3')
		print('skoCOSS = -279057/16384')
		print('skoSINS = 16625679855/2147483648')
		exit(0)
	
	
	if pre_condition_32(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_32 SAT")
		print('delta = 178707/512')
		print('skoM = 3')
		print('skoS = 3')
		print('skoCOSS = -1116227/65536')
		print('skoSINS = 266010877687/34359738368')
		exit(0)
	
	
	if pre_condition_33(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_33 SAT")
		print('delta = 178707/512')
		print('skoM = 3')
		print('skoS = 3')
		print('skoCOSS = -1116227/65536')
		print('skoSINS = 266010877687/34359738368')
		exit(0)
	
	
	if pre_condition_34(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_34 SAT")
		print('delta = 178707/512')
		print('skoM = 3')
		print('skoS = 3')
		print('skoCOSS = -2232453/131072')
		print('skoSINS = 532021755375/68719476736')
		exit(0)
	
	
	if pre_condition_35(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_35 SAT")
		print('delta = 178707/512')
		print('skoM = 3')
		print('skoS = 3')
		print('skoCOSS = -2232453/131072')
		print('skoSINS = 532021755375/68719476736')
		exit(0)
	
	
	if pre_condition_36(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_36 SAT")
		print('delta = 2859299/8192')
		print('skoM = 3')
		print('skoS = 3')
		print('skoCOSS = -4464905/262144')
		print('skoSINS = 4256174043003/549755813888')
		exit(0)
	
	
	if pre_condition_37(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_37 SAT")
		print('delta = 2859299/8192')
		print('skoM = 3')
		print('skoS = 3')
		print('skoCOSS = -4464905/262144')
		print('skoSINS = 4256174043003/549755813888')
		exit(0)
	
	
	if pre_condition_38(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_38 SAT")
		print('delta = 2859299/8192')
		print('skoM = 3')
		print('skoS = 3')
		print('skoCOSS = -8929809/524288')
		print('skoSINS = 17024696172015/2199023255552')
		exit(0)
	
	
	if pre_condition_39(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_39 SAT")
		print('delta = 2859299/8192')
		print('skoM = 3')
		print('skoS = 3')
		print('skoCOSS = -8929809/524288')
		print('skoSINS = 17024696172015/2199023255552')
		exit(0)
	
	
	if pre_condition_40(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_40 SAT")
		print('delta = 1429649/4096')
		print('skoM = 3')
		print('skoS = 3')
		print('skoCOSS = -35719235/2097152')
		print('skoSINS = 272395138752247/35184372088832')
		exit(0)
	
	
	if pre_condition_41(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_41 SAT")
		print('delta = 1429649/4096')
		print('skoM = 3')
		print('skoS = 3')
		print('skoCOSS = -35719235/2097152')
		print('skoSINS = 272395138752247/35184372088832')
		exit(0)
	
	
	if pre_condition_42(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_42 SAT")
		print('delta = 1429649/4096')
		print('skoM = 3')
		print('skoS = 3')
		print('skoCOSS = -71438469/4194304')
		print('skoSINS = 544790277504495/70368744177664')
		exit(0)
	
	
	if pre_condition_43(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_43 SAT")
		print('delta = 1429649/4096')
		print('skoM = 3')
		print('skoS = 3')
		print('skoCOSS = -71438469/4194304')
		print('skoSINS = 544790277504495/70368744177664')
		exit(0)
	
	
	if pre_condition_44(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_44 SAT")
		print('delta = 22874383/65536')
		print('skoM = 3')
		print('skoS = 3')
		print('skoCOSS = -142876937/8388608')
		print('skoSINS = 4358322220035963/562949953421312')
		exit(0)
	
	
	if pre_condition_45(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_45 SAT")
		print('delta = 22874383/65536')
		print('skoM = 3')
		print('skoS = 3')
		print('skoCOSS = -142876937/8388608')
		print('skoSINS = 4358322220035963/562949953421312')
		exit(0)
	
	
	if pre_condition_46(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_46 SAT")
		print('delta = 91497531/262144')
		print('skoM = 3')
		print('skoS = 3')
		print('skoCOSS = -285753873/16777216')
		print('skoSINS = 8716644440071927/1125899906842624')
		exit(0)
	
	
	if pre_condition_47(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_47 SAT")
		print('delta = 91497531/262144')
		print('skoM = 3')
		print('skoS = 3')
		print('skoCOSS = -285753873/16777216')
		print('skoSINS = 8716644440071927/1125899906842624')
		exit(0)
	
	
	if pre_condition_48(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_48 SAT")
		print('delta = 285')
		print('skoM = 3')
		print('skoS = 5/2')
		print('skoCOSS = -15')
		print('skoSINS = 31/4')
		exit(0)
	
	
	if pre_condition_49(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_49 SAT")
		print('delta = 285')
		print('skoM = 3')
		print('skoS = 5/2')
		print('skoCOSS = -15')
		print('skoSINS = 31/4')
		exit(0)


	print("UNKNOWN")
	exit(0)
