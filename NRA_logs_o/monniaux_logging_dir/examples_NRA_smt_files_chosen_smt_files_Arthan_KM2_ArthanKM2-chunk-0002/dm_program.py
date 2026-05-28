import sympy
from sympy import *

def pre_condition_0(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 9/20) & (skoS*(2*skoS*(2*skoS - 39) + 57)/2 + 139/2 <= -skoSINS*(2*skoS*(skoS*(skoS + 3) - 3) + skoSINS*(skoS + 1) + 20)/4)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(9, 20)), LessThan(Add(Mul(Rational(1, 2), Symbol('skoS'), Add(Mul(Integer(2), Symbol('skoS'), Add(Mul(Integer(2), Symbol('skoS')), Integer(-39))), Integer(57))), Rational(139, 2)), Mul(Integer(-1), Rational(1, 4), Symbol('skoSINS'), Add(Mul(Integer(2), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(3))), Integer(-3))), Mul(Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(20)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 9/20) & (528*skoS**3 - 9936*skoS**2 + 7249*skoS <= -17953)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(9, 20)), LessThan(Add(Mul(Integer(528), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(-1), Integer(9936), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(7249), Symbol('skoS'))), Integer(-17953)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 9/20) & (2*skoS*(skoS*(skoS - 12) - 2) + 22 <= -skoSINS*(2*skoS*(skoS*(skoS + 3) - 3) + skoSINS*(skoS + 1) + 10)/4)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(9, 20)), LessThan(Add(Mul(Integer(2), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(-12))), Integer(-2))), Integer(22)), Mul(Integer(-1), Rational(1, 4), Symbol('skoSINS'), Add(Mul(Integer(2), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(3))), Integer(-3))), Mul(Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(10)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 9/20) & (-10*skoS**3 + 90*skoS**2 + 21*skoS >= 99)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(9, 20)), GreaterThan(Add(Mul(Integer(-1), Integer(10), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(90), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(21), Symbol('skoS'))), Integer(99)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_4(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 9/20) & (skoS*(2*skoS*(2*skoS + 3) + 1)/2 - 1/2 <= -skoSINS*(2*skoS*(skoS*(skoS + 3) - 3) + skoSINS*(skoS + 1) - 8)/4)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(9, 20)), LessThan(Add(Mul(Rational(1, 2), Symbol('skoS'), Add(Mul(Integer(2), Symbol('skoS'), Add(Mul(Integer(2), Symbol('skoS')), Integer(3))), Integer(1))), Rational(-1, 2)), Mul(Integer(-1), Rational(1, 4), Symbol('skoSINS'), Add(Mul(Integer(2), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(3))), Integer(-3))), Mul(Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(-8)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_5(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 9/20) & (10*skoS**3 + 18*skoS**2 - 3*skoS <= 9)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(9, 20)), LessThan(Add(Mul(Integer(10), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(18), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(3), Symbol('skoS'))), Integer(9)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_6(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 9/20) & (skoS*(2*skoS*(2*skoS - 15) - 23)/2 + 11/2 <= -skoSINS*(2*skoS*(skoS*(skoS + 3) - 3) + skoSINS*(skoS + 1) + 4)/4)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(9, 20)), LessThan(Add(Mul(Rational(1, 2), Symbol('skoS'), Add(Mul(Integer(2), Symbol('skoS'), Add(Mul(Integer(2), Symbol('skoS')), Integer(-15))), Integer(-23))), Rational(11, 2)), Mul(Integer(-1), Rational(1, 4), Symbol('skoSINS'), Add(Mul(Integer(2), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(3))), Integer(-3))), Mul(Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(4)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_7(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 9/20) & (-14*skoS**3 + 42*skoS**2 + 55*skoS >= 43)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(9, 20)), GreaterThan(Add(Mul(Integer(-1), Integer(14), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(42), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(55), Symbol('skoS'))), Integer(43)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_8(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 9/20) & (skoS*(2*skoS*(2*skoS - 279) + 7897)/2 + 8459/2 <= -skoSINS*(2*skoS*(skoS*(skoS + 3) - 3) + skoSINS*(skoS + 1) + 180)/4)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(9, 20)), LessThan(Add(Mul(Rational(1, 2), Symbol('skoS'), Add(Mul(Integer(2), Symbol('skoS'), Add(Mul(Integer(2), Symbol('skoS')), Integer(-279))), Integer(7897))), Rational(8459, 2)), Mul(Integer(-1), Rational(1, 4), Symbol('skoSINS'), Add(Mul(Integer(2), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(3))), Integer(-3))), Mul(Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(180)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_9(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 9/20) & (10*skoS**3 - 1110*skoS**2 + 15789*skoS <= -17099)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(9, 20)), LessThan(Add(Mul(Integer(10), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(-1), Integer(1110), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(15789), Symbol('skoS'))), Integer(-17099)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_10(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 9/20) & (2*skoS*(skoS*(skoS - 717) + 56163) + 113762 <= -skoSINS*(2*skoS*(skoS*(skoS + 3) - 3) + skoSINS*(skoS + 1) + 950)/4)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(9, 20)), LessThan(Add(Mul(Integer(2), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(-717))), Integer(56163))), Integer(113762)), Mul(Integer(-1), Rational(1, 4), Symbol('skoSINS'), Add(Mul(Integer(2), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(3))), Integer(-3))), Mul(Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(950)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_11(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 9/20) & (10*skoS**3 - 5730*skoS**2 + 449299*skoS <= -455999)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(9, 20)), LessThan(Add(Mul(Integer(10), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(-1), Integer(5730), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(449299), Symbol('skoS'))), Integer(-455999)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_12(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 9/20) & (skoS*(2*skoS*(2*skoS - 7209) + 5755177)/2 + 5769599/2 <= -skoSINS*(2*skoS*(skoS*(skoS + 3) - 3) + skoSINS*(skoS + 1) + 4800)/4)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(9, 20)), LessThan(Add(Mul(Rational(1, 2), Symbol('skoS'), Add(Mul(Integer(2), Symbol('skoS'), Add(Mul(Integer(2), Symbol('skoS')), Integer(-7209))), Integer(5755177))), Rational(5769599, 2)), Mul(Integer(-1), Rational(1, 4), Symbol('skoSINS'), Add(Mul(Integer(2), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(3))), Integer(-3))), Mul(Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(4800)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_13(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 9/20) & (10*skoS**3 - 28830*skoS**2 + 11510349*skoS <= -11543999)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(9, 20)), LessThan(Add(Mul(Integer(10), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(-1), Integer(28830), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(11510349), Symbol('skoS'))), Integer(-11543999)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_14(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 9/20) & (2*skoS*(skoS*(skoS - 18042) + 36144138) + 72324362 <= -skoSINS*(2*skoS*(skoS*(skoS + 3) - 3) + skoSINS*(skoS + 1) + 24050)/4)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(9, 20)), LessThan(Add(Mul(Integer(2), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(-18042))), Integer(36144138))), Integer(72324362)), Mul(Integer(-1), Rational(1, 4), Symbol('skoSINS'), Add(Mul(Integer(2), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(3))), Integer(-3))), Mul(Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(24050)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_15(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 9/20) & (10*skoS**3 - 144330*skoS**2 + 289153099*skoS <= -289321499)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(9, 20)), LessThan(Add(Mul(Integer(10), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(-1), Integer(144330), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(289153099), Symbol('skoS'))), Integer(-289321499)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_16(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 9/20) & (2*skoS*(skoS*(skoS - 3600) + 1435198) + 2877598 <= -skoSINS*(2*skoS*(skoS*(skoS + 3) - 3) + skoSINS*(skoS + 1) + 4794)/4)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(9, 20)), LessThan(Add(Mul(Integer(2), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(-3600))), Integer(1435198))), Integer(2877598)), Mul(Integer(-1), Rational(1, 4), Symbol('skoSINS'), Add(Mul(Integer(2), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(3))), Integer(-3))), Mul(Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(4794)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_17(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 9/20) & (10*skoS**3 - 28794*skoS**2 + 11481579*skoS <= -11515187)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(9, 20)), LessThan(Add(Mul(Integer(10), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(-1), Integer(28794), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(11481579), Symbol('skoS'))), Integer(-11515187)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_18(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 9/20) & (skoS*(2*skoS*(2*skoS - 7197) + 5736001)/2 + 5750399/2 <= -skoSINS*(2*skoS*(skoS*(skoS + 3) - 3) + skoSINS*(skoS + 1) + 4792)/4)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(9, 20)), LessThan(Add(Mul(Rational(1, 2), Symbol('skoS'), Add(Mul(Integer(2), Symbol('skoS'), Add(Mul(Integer(2), Symbol('skoS')), Integer(-7197))), Integer(5736001))), Rational(5750399, 2)), Mul(Integer(-1), Rational(1, 4), Symbol('skoSINS'), Add(Mul(Integer(2), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(3))), Integer(-3))), Mul(Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(4792)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_19(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 9/20) & (10*skoS**3 - 28782*skoS**2 + 11471997*skoS <= -11505591)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(9, 20)), LessThan(Add(Mul(Integer(10), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(-1), Integer(28782), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(11471997), Symbol('skoS'))), Integer(-11505591)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_20(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 9/20) & (2*skoS*(skoS*(skoS - 3597) + 1432803) + 2872802 <= -skoSINS*(2*skoS*(skoS*(skoS + 3) - 3) + skoSINS*(skoS + 1) + 4790)/4)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(9, 20)), LessThan(Add(Mul(Integer(2), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(-3597))), Integer(1432803))), Integer(2872802)), Mul(Integer(-1), Rational(1, 4), Symbol('skoSINS'), Add(Mul(Integer(2), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(3))), Integer(-3))), Mul(Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(4790)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_21(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 9/20) & (10*skoS**3 - 28770*skoS**2 + 11462419*skoS <= -11495999)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(9, 20)), LessThan(Add(Mul(Integer(10), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(-1), Integer(28770), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(11462419), Symbol('skoS'))), Integer(-11495999)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_22(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 9/20) & (skoS*(2*skoS*(2*skoS - 1425) + 221817)/2 + 224671/2 <= -skoSINS*(2*skoS*(skoS*(skoS + 3) - 3) + skoSINS*(skoS + 1) + 944)/4)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(9, 20)), LessThan(Add(Mul(Rational(1, 2), Symbol('skoS'), Add(Mul(Integer(2), Symbol('skoS'), Add(Mul(Integer(2), Symbol('skoS')), Integer(-1425))), Integer(221817))), Rational(224671, 2)), Mul(Integer(-1), Rational(1, 4), Symbol('skoSINS'), Add(Mul(Integer(2), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(3))), Integer(-3))), Mul(Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(944)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_23(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 9/20) & (10*skoS**3 - 5694*skoS**2 + 443629*skoS <= -450287)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(9, 20)), LessThan(Add(Mul(Integer(10), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(-1), Integer(5694), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(443629), Symbol('skoS'))), Integer(-450287)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_24(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 9/20) & (2*skoS*(skoS*(skoS - 711) + 55219) + 111862 <= -skoSINS*(2*skoS*(skoS*(skoS + 3) - 3) + skoSINS*(skoS + 1) + 942)/4)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(9, 20)), LessThan(Add(Mul(Integer(2), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(-711))), Integer(55219))), Integer(111862)), Mul(Integer(-1), Rational(1, 4), Symbol('skoSINS'), Add(Mul(Integer(2), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(3))), Integer(-3))), Mul(Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(942)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_25(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 9/20) & (10*skoS**3 - 5682*skoS**2 + 441747*skoS <= -448391)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(9, 20)), LessThan(Add(Mul(Integer(10), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(-1), Integer(5682), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(441747), Symbol('skoS'))), Integer(-448391)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_26(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 9/20) & (skoS*(2*skoS*(2*skoS - 1419) + 219937)/2 + 222779/2 <= -skoSINS*(2*skoS*(skoS*(skoS + 3) - 3) + skoSINS*(skoS + 1) + 940)/4)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(9, 20)), LessThan(Add(Mul(Rational(1, 2), Symbol('skoS'), Add(Mul(Integer(2), Symbol('skoS'), Add(Mul(Integer(2), Symbol('skoS')), Integer(-1419))), Integer(219937))), Rational(222779, 2)), Mul(Integer(-1), Rational(1, 4), Symbol('skoSINS'), Add(Mul(Integer(2), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(3))), Integer(-3))), Mul(Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(940)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_27(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 9/20) & (10*skoS**3 - 5670*skoS**2 + 439869*skoS <= -446499)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(9, 20)), LessThan(Add(Mul(Integer(10), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(-1), Integer(5670), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(439869), Symbol('skoS'))), Integer(-446499)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_28(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 9/20) & (skoS*(2*skoS*(2*skoS - 51) + 145)/2 + 251/2 <= -skoSINS*(2*skoS*(skoS*(skoS + 3) - 3) + skoSINS*(skoS + 1) + 28)/4)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(9, 20)), LessThan(Add(Mul(Rational(1, 2), Symbol('skoS'), Add(Mul(Integer(2), Symbol('skoS'), Add(Mul(Integer(2), Symbol('skoS')), Integer(-51))), Integer(145))), Rational(251, 2)), Mul(Integer(-1), Rational(1, 4), Symbol('skoSINS'), Add(Mul(Integer(2), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(3))), Integer(-3))), Mul(Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(28)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_29(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 9/20) & (10*skoS**3 - 198*skoS**2 + 285*skoS <= -531)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(9, 20)), LessThan(Add(Mul(Integer(10), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(-1), Integer(198), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(285), Symbol('skoS'))), Integer(-531)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(delta:sympy.Rational, skoS:sympy.Rational, skoCOSS:sympy.Rational, skoSINS:sympy.Rational):
	# (0 <= delta) & (9/20 <= skoS) & (skoSINS*(-skoCOSS/2 + skoS*(skoS*(skoS/2 + 3/2) - 3/2) + skoSINS*(skoS/4 + 1/4) - 5/2) <= skoCOSS*(-skoCOSS/2 - 3) + skoS*(skoCOSS*(-skoCOSS/2 - 6) + skoS*(-3*skoCOSS - 2*skoS - 6) - 6) - 2)

	post_cond =  And(LessThan(Integer(0), Symbol('delta')), LessThan(Rational(9, 20), Symbol('skoS')), LessThan(Mul(Symbol('skoSINS'), Add(Mul(Integer(-1), Rational(1, 2), Symbol('skoCOSS')), Mul(Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Mul(Rational(1, 2), Symbol('skoS')), Rational(3, 2))), Rational(-3, 2))), Mul(Symbol('skoSINS'), Add(Mul(Rational(1, 4), Symbol('skoS')), Rational(1, 4))), Rational(-5, 2))), Add(Mul(Symbol('skoCOSS'), Add(Mul(Integer(-1), Rational(1, 2), Symbol('skoCOSS')), Integer(-3))), Mul(Symbol('skoS'), Add(Mul(Symbol('skoCOSS'), Add(Mul(Integer(-1), Rational(1, 2), Symbol('skoCOSS')), Integer(-6))), Mul(Symbol('skoS'), Add(Mul(Integer(-1), Integer(3), Symbol('skoCOSS')), Mul(Integer(-1), Integer(2), Symbol('skoS')), Integer(-6))), Integer(-6))), Integer(-2))))

	eval = post_cond.subs( { 'delta':delta, 'skoS':skoS, 'skoCOSS':skoCOSS, 'skoSINS':skoSINS })

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
	
	
	
	
	if pre_condition_0(delta=delta,skoS=skoS)==True:
		print("pre_condition_0 SAT")
		print('delta = 0')
		print('skoS = 2')
		print('skoSINS = 1/8')
		print('skoCOSS = -15')
		exit(0)
	
	
	if pre_condition_1(delta=delta,skoS=skoS)==True:
		print("pre_condition_1 SAT")
		print('delta = 0')
		print('skoS = 2')
		print('skoSINS = 1/8')
		print('skoCOSS = -15')
		exit(0)
	
	
	if pre_condition_2(delta=delta,skoS=skoS)==True:
		print("pre_condition_2 SAT")
		print('delta = 0')
		print('skoS = 1')
		print('skoSINS = 1')
		print('skoCOSS = -10')
		exit(0)
	
	
	if pre_condition_3(delta=delta,skoS=skoS)==True:
		print("pre_condition_3 SAT")
		print('delta = 0')
		print('skoS = 1')
		print('skoSINS = 1')
		print('skoCOSS = -10')
		exit(0)
	
	
	if pre_condition_4(delta=delta,skoS=skoS)==True:
		print("pre_condition_4 SAT")
		print('delta = 0')
		print('skoS = 1/2')
		print('skoSINS = 1')
		print('skoCOSS = -1')
		exit(0)
	
	
	if pre_condition_5(delta=delta,skoS=skoS)==True:
		print("pre_condition_5 SAT")
		print('delta = 0')
		print('skoS = 1/2')
		print('skoSINS = 1')
		print('skoCOSS = -1')
		exit(0)
	
	
	if pre_condition_6(delta=delta,skoS=skoS)==True:
		print("pre_condition_6 SAT")
		print('delta = 0')
		print('skoS = 3/4')
		print('skoSINS = 3')
		print('skoCOSS = -7')
		exit(0)
	
	
	if pre_condition_7(delta=delta,skoS=skoS)==True:
		print("pre_condition_7 SAT")
		print('delta = 0')
		print('skoS = 3/4')
		print('skoSINS = 3')
		print('skoCOSS = -7')
		exit(0)
	
	
	if pre_condition_8(delta=delta,skoS=skoS)==True:
		print("pre_condition_8 SAT")
		print('delta = 0')
		print('skoS = 18')
		print('skoSINS = 1')
		print('skoCOSS = -95')
		exit(0)
	
	
	if pre_condition_9(delta=delta,skoS=skoS)==True:
		print("pre_condition_9 SAT")
		print('delta = 0')
		print('skoS = 18')
		print('skoSINS = 1')
		print('skoCOSS = -95')
		exit(0)
	
	
	if pre_condition_10(delta=delta,skoS=skoS)==True:
		print("pre_condition_10 SAT")
		print('delta = 0')
		print('skoS = 95')
		print('skoSINS = 1')
		print('skoCOSS = -480')
		exit(0)
	
	
	if pre_condition_11(delta=delta,skoS=skoS)==True:
		print("pre_condition_11 SAT")
		print('delta = 0')
		print('skoS = 95')
		print('skoSINS = 1')
		print('skoCOSS = -480')
		exit(0)
	
	
	if pre_condition_12(delta=delta,skoS=skoS)==True:
		print("pre_condition_12 SAT")
		print('delta = 0')
		print('skoS = 480')
		print('skoSINS = 1')
		print('skoCOSS = -2405')
		exit(0)
	
	
	if pre_condition_13(delta=delta,skoS=skoS)==True:
		print("pre_condition_13 SAT")
		print('delta = 0')
		print('skoS = 480')
		print('skoSINS = 1')
		print('skoCOSS = -2405')
		exit(0)
	
	
	if pre_condition_14(delta=delta,skoS=skoS)==True:
		print("pre_condition_14 SAT")
		print('delta = 0')
		print('skoS = 2405')
		print('skoSINS = 1')
		print('skoCOSS = -12030')
		exit(0)
	
	
	if pre_condition_15(delta=delta,skoS=skoS)==True:
		print("pre_condition_15 SAT")
		print('delta = 0')
		print('skoS = 2405')
		print('skoSINS = 1')
		print('skoCOSS = -12030')
		exit(0)
	
	
	if pre_condition_16(delta=delta,skoS=skoS)==True:
		print("pre_condition_16 SAT")
		print('delta = 0')
		print('skoS = 959/2')
		print('skoSINS = 1')
		print('skoCOSS = -2402')
		exit(0)
	
	
	if pre_condition_17(delta=delta,skoS=skoS)==True:
		print("pre_condition_17 SAT")
		print('delta = 0')
		print('skoS = 959/2')
		print('skoSINS = 1')
		print('skoCOSS = -2402')
		exit(0)
	
	
	if pre_condition_18(delta=delta,skoS=skoS)==True:
		print("pre_condition_18 SAT")
		print('delta = 0')
		print('skoS = 1917/4')
		print('skoSINS = 1')
		print('skoCOSS = -2401')
		exit(0)
	
	
	if pre_condition_19(delta=delta,skoS=skoS)==True:
		print("pre_condition_19 SAT")
		print('delta = 0')
		print('skoS = 1917/4')
		print('skoSINS = 1')
		print('skoCOSS = -2401')
		exit(0)
	
	
	if pre_condition_20(delta=delta,skoS=skoS)==True:
		print("pre_condition_20 SAT")
		print('delta = 0')
		print('skoS = 3833/8')
		print('skoSINS = 1')
		print('skoCOSS = -2400')
		exit(0)
	
	
	if pre_condition_21(delta=delta,skoS=skoS)==True:
		print("pre_condition_21 SAT")
		print('delta = 0')
		print('skoS = 3833/8')
		print('skoSINS = 1')
		print('skoCOSS = -2400')
		exit(0)
	
	
	if pre_condition_22(delta=delta,skoS=skoS)==True:
		print("pre_condition_22 SAT")
		print('delta = 0')
		print('skoS = 189/2')
		print('skoSINS = 1')
		print('skoCOSS = -477')
		exit(0)
	
	
	if pre_condition_23(delta=delta,skoS=skoS)==True:
		print("pre_condition_23 SAT")
		print('delta = 0')
		print('skoS = 189/2')
		print('skoSINS = 1')
		print('skoCOSS = -477')
		exit(0)
	
	
	if pre_condition_24(delta=delta,skoS=skoS)==True:
		print("pre_condition_24 SAT")
		print('delta = 0')
		print('skoS = 377/4')
		print('skoSINS = 1')
		print('skoCOSS = -476')
		exit(0)
	
	
	if pre_condition_25(delta=delta,skoS=skoS)==True:
		print("pre_condition_25 SAT")
		print('delta = 0')
		print('skoS = 377/4')
		print('skoSINS = 1')
		print('skoCOSS = -476')
		exit(0)
	
	
	if pre_condition_26(delta=delta,skoS=skoS)==True:
		print("pre_condition_26 SAT")
		print('delta = 0')
		print('skoS = 753/8')
		print('skoSINS = 1')
		print('skoCOSS = -475')
		exit(0)
	
	
	if pre_condition_27(delta=delta,skoS=skoS)==True:
		print("pre_condition_27 SAT")
		print('delta = 0')
		print('skoS = 753/8')
		print('skoSINS = 1')
		print('skoCOSS = -475')
		exit(0)
	
	
	if pre_condition_28(delta=delta,skoS=skoS)==True:
		print("pre_condition_28 SAT")
		print('delta = 0')
		print('skoS = 575/32')
		print('skoSINS = 1')
		print('skoCOSS = -19')
		exit(0)
	
	
	if pre_condition_29(delta=delta,skoS=skoS)==True:
		print("pre_condition_29 SAT")
		print('delta = 0')
		print('skoS = 575/32')
		print('skoSINS = 1')
		print('skoCOSS = -19')
		exit(0)


	print("UNKNOWN")
	exit(0)
