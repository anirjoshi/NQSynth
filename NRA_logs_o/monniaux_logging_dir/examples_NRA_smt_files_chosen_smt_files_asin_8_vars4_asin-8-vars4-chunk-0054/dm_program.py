import sympy
from sympy import *

def pre_condition_0(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= skoX) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= -skoX) & (delta >= skoS2**2 - 2) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (63*skoS2/20 + 13/8 >= skoSM*(126*skoS2 + 61)/40 - 1/5) & (63*skoS2/20 - skoSM*(126*skoS2 + 61)/40 + 73/40 < skoX*(40*skoSM + skoX*(126*skoS2 - skoSM*(126*skoS2 + 61) + 73) + 200)/40)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(63, 20), Symbol('skoS2')), Rational(13, 8)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(63, 20), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(73, 40)), Mul(Rational(1, 40), Symbol('skoX'), Add(Mul(Integer(40), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Mul(Integer(-1), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(73))), Integer(200)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= skoX) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= -skoX) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & (skoX**2 + 20*skoX > 1)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictGreaterThan(Add(Pow(Symbol('skoX'), Integer(2)), Mul(Integer(20), Symbol('skoX'))), Integer(1)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 17/64) & (delta >= skoS2**2 - 2) & (delta - skoX >= -17/64) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (567*skoS2/160 + 117/64 >= skoSM*(126*skoS2 + 61)/40 - 1/5) & (567*skoS2/160 - skoSM*(126*skoS2 + 61)/40 + 649/320 < skoX*(320*skoSM + skoX*(1134*skoS2 - 8*skoSM*(126*skoS2 + 61) + 649) + 1640)/320)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(17, 64)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-17, 64)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(567, 160), Symbol('skoS2')), Rational(117, 64)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(567, 160), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(649, 320)), Mul(Rational(1, 320), Symbol('skoX'), Add(Mul(Integer(320), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(1134), Symbol('skoS2')), Mul(Integer(-1), Integer(8), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(649))), Integer(1640)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 3/4) & (delta >= skoS2**2 - 2) & (delta - skoX >= -17/64) & (delta >= 2 - skoS2**2) & (63*skoS2/32 + 81/64 < 9*skoX*(skoX*(14*skoS2 + 9) + 40)/64)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(3, 4)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-17, 64)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(63, 32), Symbol('skoS2')), Rational(81, 64)), Mul(Rational(9, 64), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(14), Symbol('skoS2')), Integer(9))), Integer(40)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_4(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 497/1024) & (delta >= skoS2**2 - 2) & (delta - skoX >= -497/1024) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (2457*skoS2/640 + 507/256 >= skoSM*(126*skoS2 + 61)/40 - 1/5) & (2457*skoS2/640 - skoSM*(126*skoS2 + 61)/40 + 2791/1280 < skoX*(1280*skoSM + skoX*(4914*skoS2 - 32*skoSM*(126*skoS2 + 61) + 2791) + 6680)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(497, 1024)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-497, 1024)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(2457, 640), Symbol('skoS2')), Rational(507, 256)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(2457, 640), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(2791, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Integer(1280), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(4914), Symbol('skoS2')), Mul(Integer(-1), Integer(32), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(2791))), Integer(6680)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_5(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 <= 39/14) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 497/1024) & (delta >= skoS2**2 - 2) & (delta - skoX >= 9/16) & (delta >= 2 - skoS2**2) & (63*skoS2/640 - 351/1280 > 9*skoX*(skoX*(14*skoS2 - 39) - 920)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), LessThan(Symbol('skoS2'), Rational(39, 14)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(497, 1024)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(9, 16)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictGreaterThan(Add(Mul(Rational(63, 640), Symbol('skoS2')), Rational(-351, 1280)), Mul(Rational(9, 1280), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(14), Symbol('skoS2')), Integer(-39))), Integer(-920)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_6(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 8265/16384) & (delta >= skoS2**2 - 2) & (delta - skoX >= -8265/16384) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (9891*skoS2/2560 + 2041/1024 >= skoSM*(126*skoS2 + 61)/40 - 1/5) & (9891*skoS2/2560 - skoSM*(126*skoS2 + 61)/40 + 11229/5120 < skoX*(5120*skoSM + skoX*(19782*skoS2 - 128*skoSM*(126*skoS2 + 61) + 11229) + 26760)/5120)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(8265, 16384)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-8265, 16384)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(9891, 2560), Symbol('skoS2')), Rational(2041, 1024)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(9891, 2560), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(11229, 5120)), Mul(Rational(1, 5120), Symbol('skoX'), Add(Mul(Integer(5120), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(19782), Symbol('skoS2')), Mul(Integer(-1), Integer(128), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(11229))), Integer(26760)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_7(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 2071/4096) & (delta >= skoS2**2 - 2) & (delta - skoX >= -8265/16384) & (delta >= 2 - skoS2**2) & (4221*skoS2/2560 + 5739/5120 < 3*skoX*(skoX*(2814*skoS2 + 1913) + 10120)/5120)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(2071, 4096)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-8265, 16384)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(4221, 2560), Symbol('skoS2')), Rational(5739, 5120)), Mul(Rational(3, 5120), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(2814), Symbol('skoS2')), Integer(1913))), Integer(10120)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_8(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 9/16) & (delta >= skoS2**2 - 2) & (delta - skoX >= -9/16) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (63*skoS2/16 + 65/32 >= skoSM*(126*skoS2 + 61)/40 - 1/5) & (63*skoS2/16 - skoSM*(126*skoS2 + 61)/40 + 357/160 < skoX*(160*skoSM + skoX*(630*skoS2 - 4*skoSM*(126*skoS2 + 61) + 357) + 840)/160)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(9, 16)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-9, 16)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(63, 16), Symbol('skoS2')), Rational(65, 32)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(63, 16), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(357, 160)), Mul(Rational(1, 160), Symbol('skoX'), Add(Mul(Integer(160), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(630), Symbol('skoS2')), Mul(Integer(-1), Integer(4), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(357))), Integer(840)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_9(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 3/4) & (delta >= skoS2**2 - 2) & (delta - skoX >= -9/16) & (delta >= 2 - skoS2**2) & (189*skoS2/80 + 47/32 < skoX*(skoX*(378*skoS2 + 235) + 920)/160)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(3, 4)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-9, 16)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(189, 80), Symbol('skoS2')), Rational(47, 32)), Mul(Rational(1, 160), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(378), Symbol('skoS2')), Integer(235))), Integer(920)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_10(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 345/1024) & (delta >= skoS2**2 - 2) & (delta - skoX >= -345/1024) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (2331*skoS2/640 + 481/256 >= skoSM*(126*skoS2 + 61)/40 - 1/5) & (2331*skoS2/640 - skoSM*(126*skoS2 + 61)/40 + 2661/1280 < skoX*(1280*skoSM + skoX*(4662*skoS2 - 32*skoSM*(126*skoS2 + 61) + 2661) + 6600)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(345, 1024)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-345, 1024)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(2331, 640), Symbol('skoS2')), Rational(481, 256)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(2331, 640), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(2661, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Integer(1280), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(4662), Symbol('skoS2')), Mul(Integer(-1), Integer(32), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(2661))), Integer(6600)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_11(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 <= 49/18) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 345/1024) & (delta >= skoS2**2 - 2) & (delta - skoX >= 105/256) & (delta >= 2 - skoS2**2) & (63*skoS2/640 - 343/1280 > 7*skoX*(skoX*(18*skoS2 - 49) - 1160)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), LessThan(Symbol('skoS2'), Rational(49, 18)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(345, 1024)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(105, 256)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictGreaterThan(Add(Mul(Rational(63, 640), Symbol('skoS2')), Rational(-343, 1280)), Mul(Rational(7, 1280), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(18), Symbol('skoS2')), Integer(-49))), Integer(-1160)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_12(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 5817/16384) & (delta >= skoS2**2 - 2) & (delta - skoX >= -5817/16384) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (9387*skoS2/2560 + 1937/1024 >= skoSM*(126*skoS2 + 61)/40 - 1/5) & (9387*skoS2/2560 - skoSM*(126*skoS2 + 61)/40 + 10709/5120 < skoX*(5120*skoSM + skoX*(18774*skoS2 - 128*skoSM*(126*skoS2 + 61) + 10709) + 26440)/5120)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(5817, 16384)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-5817, 16384)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(9387, 2560), Symbol('skoS2')), Rational(1937, 1024)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(9387, 2560), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(10709, 5120)), Mul(Rational(1, 5120), Symbol('skoX'), Add(Mul(Integer(5120), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(18774), Symbol('skoS2')), Mul(Integer(-1), Integer(128), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(10709))), Integer(26440)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_13(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 <= 4147/2142) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 5817/16384) & (delta >= skoS2**2 - 2) & (delta - skoX >= 1901657/4194304) & (delta >= 2 - skoS2**2) & (1071*skoS2/8192 - 4147/16384 > skoX*(skoX*(2142*skoS2 - 4147) - 104360)/16384)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), LessThan(Symbol('skoS2'), Rational(4147, 2142)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(5817, 16384)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(1901657, 4194304)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictGreaterThan(Add(Mul(Rational(1071, 8192), Symbol('skoS2')), Rational(-4147, 16384)), Mul(Rational(1, 16384), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(2142), Symbol('skoS2')), Integer(-4147))), Integer(-104360)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_14(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 23865/65536) & (delta >= skoS2**2 - 2) & (delta - skoX >= -23865/65536) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (18837*skoS2/5120 + 3887/2048 >= skoSM*(126*skoS2 + 61)/40 - 1/5) & (18837*skoS2/5120 - skoSM*(126*skoS2 + 61)/40 + 21483/10240 < skoX*(10240*skoSM + skoX*(37674*skoS2 - 256*skoSM*(126*skoS2 + 61) + 21483) + 52920)/10240)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(23865, 65536)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-23865, 65536)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(18837, 5120), Symbol('skoS2')), Rational(3887, 2048)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(18837, 5120), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(21483, 10240)), Mul(Rational(1, 10240), Symbol('skoX'), Add(Mul(Integer(10240), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(37674), Symbol('skoS2')), Mul(Integer(-1), Integer(256), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(21483))), Integer(52920)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_15(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 <= 314/189) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 23865/65536) & (delta >= skoS2**2 - 2) & (delta - skoX >= 31185/65536) & (delta >= 2 - skoS2**2) & (189*skoS2/1280 - 157/640 > skoX*(skoX*(189*skoS2 - 314) - 8170)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), LessThan(Symbol('skoS2'), Rational(314, 189)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(23865, 65536)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(31185, 65536)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictGreaterThan(Add(Mul(Rational(189, 1280), Symbol('skoS2')), Rational(-157, 640)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(189), Symbol('skoS2')), Integer(-314))), Integer(-8170)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_16(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 94265/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= -94265/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (37611*skoS2/10240 + 7761/4096 >= skoSM*(126*skoS2 + 61)/40 - 1/5) & (37611*skoS2/10240 - skoSM*(126*skoS2 + 61)/40 + 42901/20480 < skoX*(20480*skoSM + skoX*(75222*skoS2 - 512*skoSM*(126*skoS2 + 61) + 42901) + 105800)/20480)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(94265, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-94265, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(37611, 10240), Symbol('skoS2')), Rational(7761, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(37611, 10240), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(42901, 20480)), Mul(Rational(1, 20480), Symbol('skoX'), Add(Mul(Integer(20480), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(75222), Symbol('skoS2')), Mul(Integer(-1), Integer(512), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(42901))), Integer(105800)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_17(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 <= 2545/1546) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 94265/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 126659673/268435456) & (delta >= 2 - skoS2**2) & (48699*skoS2/327680 - 32067/131072 > 63*skoX*(skoX*(1546*skoS2 - 2545) - 66360)/655360)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), LessThan(Symbol('skoS2'), Rational(2545, 1546)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(94265, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(126659673, 268435456)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictGreaterThan(Add(Mul(Rational(48699, 327680), Symbol('skoS2')), Rational(-32067, 131072)), Mul(Rational(63, 655360), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(1546), Symbol('skoS2')), Integer(-2545))), Integer(-66360)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_18(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 374673/1048576) & (delta >= skoS2**2 - 2) & (delta - skoX >= -374673/1048576) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (75159*skoS2/20480 + 15509/8192 >= skoSM*(126*skoS2 + 61)/40 - 1/5) & (75159*skoS2/20480 - skoSM*(126*skoS2 + 61)/40 + 85737/40960 < skoX*(40960*skoSM + skoX*(150318*skoS2 - 1024*skoSM*(126*skoS2 + 61) + 85737) + 211560)/40960)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(374673, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-374673, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(75159, 20480), Symbol('skoS2')), Rational(15509, 8192)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(75159, 20480), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(85737, 40960)), Mul(Rational(1, 40960), Symbol('skoX'), Add(Mul(Integer(40960), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(150318), Symbol('skoS2')), Mul(Integer(-1), Integer(1024), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(85737))), Integer(211560)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_19(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 <= 106217/66234) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 374673/1048576) & (delta >= skoS2**2 - 2) & (delta - skoX >= 506559185/1073741824) & (delta >= 2 - skoS2**2) & (99351*skoS2/655360 - 318651/1310720 > 3*skoX*(skoX*(66234*skoS2 - 106217) - 2786680)/1310720)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), LessThan(Symbol('skoS2'), Rational(106217, 66234)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(374673, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(506559185, 1073741824)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictGreaterThan(Add(Mul(Rational(99351, 655360), Symbol('skoS2')), Rational(-318651, 1310720)), Mul(Rational(3, 1310720), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(66234), Symbol('skoS2')), Integer(-106217))), Integer(-2786680)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_20(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 1493921/4194304) & (delta >= skoS2**2 - 2) & (delta - skoX >= -1493921/4194304) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (30051*skoS2/8192 + 31005/16384 >= skoSM*(126*skoS2 + 61)/40 - 1/5) & (30051*skoS2/8192 - skoSM*(126*skoS2 + 61)/40 + 171409/81920 < skoX*(81920*skoSM + skoX*(300510*skoS2 - 2048*skoSM*(126*skoS2 + 61) + 171409) + 423080)/81920)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(1493921, 4194304)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-1493921, 4194304)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(30051, 8192), Symbol('skoS2')), Rational(31005, 16384)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(30051, 8192), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(171409, 81920)), Mul(Rational(1, 81920), Symbol('skoX'), Add(Mul(Integer(81920), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(300510), Symbol('skoS2')), Mul(Integer(-1), Integer(2048), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(171409))), Integer(423080)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_21(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 <= 45373/28674) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 1493921/4194304) & (delta >= skoS2**2 - 2) & (delta - skoX >= 506559185/1073741824) & (delta >= 2 - skoS2**2) & (100359*skoS2/655360 - 317611/1310720 > 7*skoX*(skoX*(28674*skoS2 - 45373) - 1194200)/1310720)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), LessThan(Symbol('skoS2'), Rational(45373, 28674)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(1493921, 4194304)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(506559185, 1073741824)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictGreaterThan(Add(Mul(Rational(100359, 655360), Symbol('skoS2')), Rational(-317611, 1310720)), Mul(Rational(7, 1310720), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(28674), Symbol('skoS2')), Integer(-45373))), Integer(-1194200)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_22(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 5966145/16777216) & (delta >= skoS2**2 - 2) & (delta - skoX >= -5966145/16777216) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (300447*skoS2/81920 + 61997/32768 >= skoSM*(126*skoS2 + 61)/40 - 1/5) & (300447*skoS2/81920 - skoSM*(126*skoS2 + 61)/40 + 342753/163840 < skoX*(163840*skoSM + skoX*(600894*skoS2 - 4096*skoSM*(126*skoS2 + 61) + 342753) + 846120)/163840)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(5966145, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-5966145, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(300447, 81920), Symbol('skoS2')), Rational(61997, 32768)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(300447, 81920), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(342753, 163840)), Mul(Rational(1, 163840), Symbol('skoX'), Add(Mul(Integer(163840), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(600894), Symbol('skoS2')), Mul(Integer(-1), Integer(4096), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(342753))), Integer(846120)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_23(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 <= 634243/403326) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 5966145/16777216) & (delta >= skoS2**2 - 2) & (delta - skoX >= 2026077729/4294967296) & (delta >= 2 - skoS2**2) & (201663*skoS2/1310720 - 634243/2621440 > skoX*(skoX*(403326*skoS2 - 634243) - 16718120)/2621440)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), LessThan(Symbol('skoS2'), Rational(634243, 403326)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(5966145, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(2026077729, 4294967296)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictGreaterThan(Add(Mul(Rational(201663, 1310720), Symbol('skoS2')), Rational(-634243, 2621440)), Mul(Rational(1, 2621440), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(403326), Symbol('skoS2')), Integer(-634243))), Integer(-16718120)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_24(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 23845505/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -23845505/67108864) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (600831*skoS2/163840 + 123981/65536 >= skoSM*(126*skoS2 + 61)/40 - 1/5) & (600831*skoS2/163840 - skoSM*(126*skoS2 + 61)/40 + 685441/327680 < skoX*(327680*skoSM + skoX*(1201662*skoS2 - 8192*skoSM*(126*skoS2 + 61) + 685441) + 1692200)/327680)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(23845505, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-23845505, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(600831, 163840), Symbol('skoS2')), Rational(123981, 65536)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(600831, 163840), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(685441, 327680)), Mul(Rational(1, 327680), Symbol('skoX'), Add(Mul(Integer(327680), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(1201662), Symbol('skoS2')), Mul(Integer(-1), Integer(8192), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(685441))), Integer(1692200)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_25(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 <= 55109/35154) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 23845505/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= 8103992897/17179869184) & (delta >= 2 - skoS2**2) & (404271*skoS2/2621440 - 1267507/5242880 > 23*skoX*(skoX*(35154*skoS2 - 55109) - 1453720)/5242880)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), LessThan(Symbol('skoS2'), Rational(55109, 35154)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(23845505, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(8103992897, 17179869184)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictGreaterThan(Add(Mul(Rational(404271, 2621440), Symbol('skoS2')), Rational(-1267507, 5242880)), Mul(Rational(23, 5242880), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(35154), Symbol('skoS2')), Integer(-55109))), Integer(-1453720)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_26(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 95420169/268435456) & (delta >= skoS2**2 - 2) & (delta - skoX >= -95420169/268435456) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (240345*skoS2/65536 + 247975/131072 >= skoSM*(126*skoS2 + 61)/40 - 1/5) & (240345*skoS2/65536 - skoSM*(126*skoS2 + 61)/40 + 1370947/655360 < skoX*(655360*skoSM + skoX*(2403450*skoS2 - 16384*skoSM*(126*skoS2 + 61) + 1370947) + 3384440)/655360)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(95420169, 268435456)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-95420169, 268435456)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(240345, 65536), Symbol('skoS2')), Rational(247975, 131072)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(240345, 65536), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(1370947, 655360)), Mul(Rational(1, 655360), Symbol('skoX'), Add(Mul(Integer(655360), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(2403450), Symbol('skoS2')), Mul(Integer(-1), Integer(16384), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(1370947))), Integer(3384440)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_27(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 <= 1268515/806526) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 95420169/268435456) & (delta >= skoS2**2 - 2) & (delta - skoX >= 8101448817/17179869184) & (delta >= 2 - skoS2**2) & (403263*skoS2/2621440 - 253703/1048576 > skoX*(skoX*(806526*skoS2 - 1268515) - 33435560)/5242880)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), LessThan(Symbol('skoS2'), Rational(1268515, 806526)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(95420169, 268435456)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(8101448817, 17179869184)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictGreaterThan(Add(Mul(Rational(403263, 2621440), Symbol('skoS2')), Rational(-253703, 1048576)), Mul(Rational(1, 5242880), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(806526), Symbol('skoS2')), Integer(-1268515))), Integer(-33435560)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_28(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 381604377/1073741824) & (delta >= skoS2**2 - 2) & (delta - skoX >= -381604377/1073741824) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (2403387*skoS2/655360 + 495937/262144 >= skoSM*(126*skoS2 + 61)/40 - 1/5) & (2403387*skoS2/655360 - skoSM*(126*skoS2 + 61)/40 + 2741829/1310720 < skoX*(1310720*skoSM + skoX*(4806774*skoS2 - 32768*skoSM*(126*skoS2 + 61) + 2741829) + 6768840)/1310720)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(381604377, 1073741824)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-381604377, 1073741824)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(2403387, 655360), Symbol('skoS2')), Rational(495937, 262144)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(2403387, 655360), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(2741829, 1310720)), Mul(Rational(1, 1310720), Symbol('skoX'), Add(Mul(Integer(1310720), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(4806774), Symbol('skoS2')), Mul(Integer(-1), Integer(32768), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(2741829))), Integer(6768840)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_29(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 <= 1691027/1075998) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 381604377/1073741824) & (delta >= skoS2**2 - 2) & (delta - skoX >= 129621909065/274877906944) & (delta >= 2 - skoS2**2) & (1613997*skoS2/10485760 - 5073081/20971520 > 3*skoX*(skoX*(1075998*skoS2 - 1691027) - 44580520)/20971520)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), LessThan(Symbol('skoS2'), Rational(1691027, 1075998)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(381604377, 1073741824)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(129621909065, 274877906944)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictGreaterThan(Add(Mul(Rational(1613997, 10485760), Symbol('skoS2')), Rational(-5073081, 20971520)), Mul(Rational(3, 20971520), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(1075998), Symbol('skoS2')), Integer(-1691027))), Integer(-44580520)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_30(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 1526570105/4294967296) & (delta >= skoS2**2 - 2) & (delta - skoX >= -1526570105/4294967296) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (4806837*skoS2/1310720 + 991887/524288 >= skoSM*(126*skoS2 + 61)/40 - 1/5) & (4806837*skoS2/1310720 - skoSM*(126*skoS2 + 61)/40 + 5483723/2621440 < skoX*(2621440*skoSM + skoX*(9613674*skoS2 - 65536*skoSM*(126*skoS2 + 61) + 5483723) + 13537720)/2621440)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(1526570105, 4294967296)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-1526570105, 4294967296)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(4806837, 1310720), Symbol('skoS2')), Rational(991887, 524288)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(4806837, 1310720), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(5483723, 2621440)), Mul(Rational(1, 2621440), Symbol('skoX'), Add(Mul(Integer(2621440), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(9613674), Symbol('skoS2')), Mul(Integer(-1), Integer(65536), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(5483723))), Integer(13537720)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_31(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 <= 563747/358526) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 1526570105/4294967296) & (delta >= skoS2**2 - 2) & (delta - skoX >= 129619365057/274877906944) & (delta >= 2 - skoS2**2) & (1613367*skoS2/10485760 - 5073723/20971520 > 9*skoX*(skoX*(358526*skoS2 - 563747) - 14860200)/20971520)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), LessThan(Symbol('skoS2'), Rational(563747, 358526)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(1526570105, 4294967296)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(129619365057, 274877906944)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictGreaterThan(Add(Mul(Rational(1613367, 10485760), Symbol('skoS2')), Rational(-5073723, 20971520)), Mul(Rational(9, 20971520), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(358526), Symbol('skoS2')), Integer(-563747))), Integer(-14860200)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_32(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 6105975225/17179869184) & (delta >= skoS2**2 - 2) & (delta - skoX >= -6105975225/17179869184) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (9613611*skoS2/2621440 + 1983761/1048576 >= skoSM*(126*skoS2 + 61)/40 - 1/5) & (9613611*skoS2/2621440 - skoSM*(126*skoS2 + 61)/40 + 10967381/5242880 < skoX*(5242880*skoSM + skoX*(19227222*skoS2 - 131072*skoSM*(126*skoS2 + 61) + 10967381) + 27075400)/5242880)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(6105975225, 17179869184)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-6105975225, 17179869184)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(9613611, 2621440), Symbol('skoS2')), Rational(1983761, 1048576)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(9613611, 2621440), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(10967381, 5242880)), Mul(Rational(1, 5242880), Symbol('skoX'), Add(Mul(Integer(5242880), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(19227222), Symbol('skoS2')), Mul(Integer(-1), Integer(131072), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(10967381))), Integer(27075400)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_33(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 <= 20293913/12908826) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 6105975225/17179869184) & (delta >= skoS2**2 - 2) & (delta - skoX >= 2073904752905/4398046511104) & (delta >= 2 - skoS2**2) & (6454413*skoS2/41943040 - 20293913/83886080 > skoX*(skoX*(12908826*skoS2 - 20293913) - 534966520)/83886080)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), LessThan(Symbol('skoS2'), Rational(20293913, 12908826)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(6105975225, 17179869184)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(2073904752905, 4398046511104)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictGreaterThan(Add(Mul(Rational(6454413, 41943040), Symbol('skoS2')), Rational(-20293913, 83886080)), Mul(Rational(1, 83886080), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(12908826), Symbol('skoS2')), Integer(-20293913))), Integer(-534966520)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_34(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 24424511289/68719476736) & (delta >= skoS2**2 - 2) & (delta - skoX >= -24424511289/68719476736) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (3845457*skoS2/1048576 + 3967535/2097152 >= skoSM*(126*skoS2 + 61)/40 - 1/5) & (3845457*skoS2/1048576 - skoSM*(126*skoS2 + 61)/40 + 21934827/10485760 < skoX*(10485760*skoSM + skoX*(38454570*skoS2 - 262144*skoSM*(126*skoS2 + 61) + 21934827) + 54150840)/10485760)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(24424511289, 68719476736)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-24424511289, 68719476736)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(3845457, 1048576), Symbol('skoS2')), Rational(3967535, 2097152)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(3845457, 1048576), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(21934827, 10485760)), Mul(Rational(1, 10485760), Symbol('skoX'), Add(Mul(Integer(10485760), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(38454570), Symbol('skoS2')), Mul(Integer(-1), Integer(262144), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(21934827))), Integer(54150840)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_35(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 <= 40588927/25815510) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 24424511289/68719476736) & (delta >= skoS2**2 - 2) & (delta - skoX >= 8295608835609/17592186044416) & (delta >= 2 - skoS2**2) & (2581551*skoS2/16777216 - 40588927/167772160 > skoX*(skoX*(25815510*skoS2 - 40588927) - 1069933640)/167772160)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), LessThan(Symbol('skoS2'), Rational(40588927, 25815510)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(24424511289, 68719476736)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(8295608835609, 17592186044416)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictGreaterThan(Add(Mul(Rational(2581551, 16777216), Symbol('skoS2')), Rational(-40588927, 167772160)), Mul(Rational(1, 167772160), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(25815510), Symbol('skoS2')), Integer(-40588927))), Integer(-1069933640)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_36(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 97696824377/274877906944) & (delta >= skoS2**2 - 2) & (delta - skoX >= -97696824377/274877906944) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (38454507*skoS2/10485760 + 7935057/4194304 >= skoSM*(126*skoS2 + 61)/40 - 1/5) & (38454507*skoS2/10485760 - skoSM*(126*skoS2 + 61)/40 + 43869589/20971520 < skoX*(20971520*skoSM + skoX*(76909014*skoS2 - 524288*skoSM*(126*skoS2 + 61) + 43869589) + 108301640)/20971520)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(97696824377, 274877906944)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-97696824377, 274877906944)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(38454507, 10485760), Symbol('skoS2')), Rational(7935057, 4194304)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(38454507, 10485760), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(43869589, 20971520)), Mul(Rational(1, 20971520), Symbol('skoX'), Add(Mul(Integer(20971520), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(76909014), Symbol('skoS2')), Mul(Integer(-1), Integer(524288), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(43869589))), Integer(108301640)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_37(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 <= 16235375/10326582) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 97696824377/274877906944) & (delta >= skoS2**2 - 2) & (delta - skoX >= 33182414990417/70368744177664) & (delta >= 2 - skoS2**2) & (5163291*skoS2/33554432 - 16235375/67108864 > skoX*(skoX*(10326582*skoS2 - 16235375) - 427973320)/67108864)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), LessThan(Symbol('skoS2'), Rational(16235375, 10326582)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(97696824377, 274877906944)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(33182414990417, 70368744177664)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictGreaterThan(Add(Mul(Rational(5163291, 33554432), Symbol('skoS2')), Rational(-16235375, 67108864)), Mul(Rational(1, 67108864), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(10326582), Symbol('skoS2')), Integer(-16235375))), Integer(-427973320)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_38(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 390784855953/1099511627776) & (delta >= skoS2**2 - 2) & (delta - skoX >= -390784855953/1099511627776) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (76908951*skoS2/20971520 + 15870101/8388608 >= skoSM*(126*skoS2 + 61)/40 - 1/5) & (76908951*skoS2/20971520 - skoSM*(126*skoS2 + 61)/40 + 87739113/41943040 < skoX*(41943040*skoSM + skoX*(153817902*skoS2 - 1048576*skoSM*(126*skoS2 + 61) + 87739113) + 216603240)/41943040)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(390784855953, 1099511627776)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-390784855953, 1099511627776)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(76908951, 20971520), Symbol('skoS2')), Rational(15870101, 8388608)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(76908951, 20971520), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(87739113, 41943040)), Mul(Rational(1, 41943040), Symbol('skoX'), Add(Mul(Integer(41943040), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(153817902), Symbol('skoS2')), Mul(Integer(-1), Integer(1048576), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(87739113))), Integer(216603240)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_39(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 <= 9019595/5737102) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 390784855953/1099511627776) & (delta >= skoS2**2 - 2) & (delta - skoX >= 33182414990417/70368744177664) & (delta >= 2 - skoS2**2) & (25816959*skoS2/167772160 - 16235271/67108864 > 9*skoX*(skoX*(5737102*skoS2 - 9019595) - 237762920)/335544320)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), LessThan(Symbol('skoS2'), Rational(9019595, 5737102)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(390784855953, 1099511627776)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(33182414990417, 70368744177664)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictGreaterThan(Add(Mul(Rational(25816959, 167772160), Symbol('skoS2')), Rational(-16235271, 67108864)), Mul(Rational(9, 335544320), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(5737102), Symbol('skoS2')), Integer(-9019595))), Integer(-237762920)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_40(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 1563134540705/4398046511104) & (delta >= skoS2**2 - 2) & (delta - skoX >= -1563134540705/4398046511104) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (153817839*skoS2/41943040 + 31740189/16777216 >= skoSM*(126*skoS2 + 61)/40 - 1/5) & (153817839*skoS2/41943040 - skoSM*(126*skoS2 + 61)/40 + 175478161/83886080 < skoX*(83886080*skoSM + skoX*(307635678*skoS2 - 2097152*skoSM*(126*skoS2 + 61) + 175478161) + 433206440)/83886080)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(1563134540705, 4398046511104)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-1563134540705, 4398046511104)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(153817839, 41943040), Symbol('skoS2')), Rational(31740189, 16777216)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(153817839, 41943040), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(175478161, 83886080)), Mul(Rational(1, 83886080), Symbol('skoX'), Add(Mul(Integer(83886080), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(307635678), Symbol('skoS2')), Mul(Integer(-1), Integer(2097152), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(175478161))), Integer(433206440)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_41(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 <= 324704441/206537562) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 1563134540705/4398046511104) & (delta >= skoS2**2 - 2) & (delta - skoX >= 530918558438601/1125899906842624) & (delta >= 2 - skoS2**2) & (103268781*skoS2/671088640 - 324704441/1342177280 > skoX*(skoX*(206537562*skoS2 - 324704441) - 8559464440)/1342177280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), LessThan(Symbol('skoS2'), Rational(324704441, 206537562)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(1563134540705, 4398046511104)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(530918558438601, 1125899906842624)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictGreaterThan(Add(Mul(Rational(103268781, 671088640), Symbol('skoS2')), Rational(-324704441, 1342177280)), Mul(Rational(1, 1342177280), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(206537562), Symbol('skoS2')), Integer(-324704441))), Integer(-8559464440)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_42(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 6252528396609/17592186044416) & (delta >= skoS2**2 - 2) & (delta - skoX >= -6252528396609/17592186044416) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (61527123*skoS2/16777216 + 63480365/33554432 >= skoSM*(126*skoS2 + 61)/40 - 1/5) & (61527123*skoS2/16777216 - skoSM*(126*skoS2 + 61)/40 + 350956257/167772160 < skoX*(167772160*skoSM + skoX*(615271230*skoS2 - 4194304*skoSM*(126*skoS2 + 61) + 350956257) + 866412840)/167772160)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(6252528396609, 17592186044416)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-6252528396609, 17592186044416)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(61527123, 16777216), Symbol('skoS2')), Rational(63480365, 33554432)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(61527123, 16777216), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(350956257, 167772160)), Mul(Rational(1, 167772160), Symbol('skoX'), Add(Mul(Integer(167772160), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(615271230), Symbol('skoS2')), Mul(Integer(-1), Integer(4194304), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(350956257))), Integer(866412840)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_43(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 <= 216469301/137692338) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 6252528396609/17592186044416) & (delta >= skoS2**2 - 2) & (delta - skoX >= 2123674070938265/4503599627370496) & (delta >= 2 - skoS2**2) & (206538507*skoS2/1342177280 - 649407903/2684354560 > 3*skoX*(skoX*(137692338*skoS2 - 216469301) - 5706309400)/2684354560)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), LessThan(Symbol('skoS2'), Rational(216469301, 137692338)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(6252528396609, 17592186044416)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(2123674070938265, 4503599627370496)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictGreaterThan(Add(Mul(Rational(206538507, 1342177280), Symbol('skoS2')), Rational(-649407903, 2684354560)), Mul(Rational(3, 2684354560), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(137692338), Symbol('skoS2')), Integer(-216469301))), Integer(-5706309400)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_44(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 25010094054017/70368744177664) & (delta >= skoS2**2 - 2) & (delta - skoX >= -25010094054017/70368744177664) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (615271167*skoS2/167772160 + 126960717/67108864 >= skoSM*(126*skoS2 + 61)/40 - 1/5) & (615271167*skoS2/167772160 - skoSM*(126*skoS2 + 61)/40 + 701912449/335544320 < skoX*(335544320*skoSM + skoX*(1230542334*skoS2 - 8388608*skoSM*(126*skoS2 + 61) + 701912449) + 1732825640)/335544320)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(25010094054017, 70368744177664)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-25010094054017, 70368744177664)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(615271167, 167772160), Symbol('skoS2')), Rational(126960717, 67108864)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(615271167, 167772160), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(701912449, 335544320)), Mul(Rational(1, 335544320), Symbol('skoX'), Add(Mul(Integer(335544320), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(1230542334), Symbol('skoS2')), Mul(Integer(-1), Integer(8388608), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(701912449))), Integer(1732825640)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_45(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 <= 865876531/550770654) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 25010094054017/70368744177664) & (delta >= skoS2**2 - 2) & (delta - skoX >= 33978784483747689/72057594037927936) & (delta >= 2 - skoS2**2) & (826155981*skoS2/5368709120 - 2597629593/10737418240 > 3*skoX*(skoX*(550770654*skoS2 - 865876531) - 22825237160)/10737418240)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), LessThan(Symbol('skoS2'), Rational(865876531, 550770654)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(25010094054017, 70368744177664)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(33978784483747689, 72057594037927936)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictGreaterThan(Add(Mul(Rational(826155981, 5368709120), Symbol('skoS2')), Rational(-2597629593, 10737418240)), Mul(Rational(3, 10737418240), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(550770654), Symbol('skoS2')), Integer(-865876531))), Integer(-22825237160)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_46(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 100040337151233/281474976710656) & (delta >= skoS2**2 - 2) & (delta - skoX >= -100040337151233/281474976710656) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (1230542271*skoS2/335544320 + 253921421/134217728 >= skoSM*(126*skoS2 + 61)/40 - 1/5) & (1230542271*skoS2/335544320 - skoSM*(126*skoS2 + 61)/40 + 1403824833/671088640 < skoX*(671088640*skoSM + skoX*(2461084542*skoS2 - 16777216*skoSM*(126*skoS2 + 61) + 1403824833) + 3465651240)/671088640)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(100040337151233, 281474976710656)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-100040337151233, 281474976710656)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(1230542271, 335544320), Symbol('skoS2')), Rational(253921421, 134217728)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(1230542271, 335544320), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(1403824833, 671088640)), Mul(Rational(1, 671088640), Symbol('skoX'), Add(Mul(Integer(671088640), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(2461084542), Symbol('skoS2')), Mul(Integer(-1), Integer(16777216), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(1403824833))), Integer(3465651240)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_47(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 <= 110832151615/70498729686) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 100040337151233/281474976710656) & (delta >= skoS2**2 - 2) & (delta - skoX >= 556708404898360274177/1180591620717411303424) & (delta >= 2 - skoS2**2) & (105748094529*skoS2/687194767360 - 66499290969/274877906944 > 3*skoX*(skoX*(70498729686*skoS2 - 110832151615) - 2921630329160)/1374389534720)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), LessThan(Symbol('skoS2'), Rational(110832151615, 70498729686)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(100040337151233, 281474976710656)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(556708404898360274177, 1180591620717411303424)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictGreaterThan(Add(Mul(Rational(105748094529, 687194767360), Symbol('skoS2')), Rational(-66499290969, 274877906944)), Mul(Rational(3, 1374389534720), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(70498729686), Symbol('skoS2')), Integer(-110832151615))), Integer(-2921630329160)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_48(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 400161426734601/1125899906842624) & (delta >= skoS2**2 - 2) & (delta - skoX >= -400161426734601/1125899906842624) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (492216921*skoS2/134217728 + 507842855/268435456 >= skoSM*(126*skoS2 + 61)/40 - 1/5) & (492216921*skoS2/134217728 - skoSM*(126*skoS2 + 61)/40 + 2807649731/1342177280 < skoX*(1342177280*skoSM + skoX*(4922169210*skoS2 - 33554432*skoSM*(126*skoS2 + 61) + 2807649731) + 6931302520)/1342177280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(400161426734601, 1125899906842624)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-400161426734601, 1125899906842624)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(492216921, 134217728), Symbol('skoS2')), Rational(507842855, 268435456)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(492216921, 134217728), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(2807649731, 1342177280)), Mul(Rational(1, 1342177280), Symbol('skoX'), Add(Mul(Integer(1342177280), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(4922169210), Symbol('skoS2')), Mul(Integer(-1), Integer(33554432), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(2807649731))), Integer(6931302520)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_49(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 <= 371089885/236044674) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 400161426734601/1125899906842624) & (delta >= skoS2**2 - 2) & (delta - skoX >= 33978783181218593/72057594037927936) & (delta >= 2 - skoS2**2) & (826156359*skoS2/5368709120 - 519525839/2147483648 > 7*skoX*(skoX*(236044674*skoS2 - 371089885) - 9782244440)/10737418240)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), LessThan(Symbol('skoS2'), Rational(371089885, 236044674)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(400161426734601, 1125899906842624)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(33978783181218593, 72057594037927936)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictGreaterThan(Add(Mul(Rational(826156359, 5368709120), Symbol('skoS2')), Rational(-519525839, 2147483648)), Mul(Rational(7, 10737418240), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(236044674), Symbol('skoS2')), Integer(-371089885))), Integer(-9782244440)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_50(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 1600645550679065/4503599627370496) & (delta >= skoS2**2 - 2) & (delta - skoX >= -1600645550679065/4503599627370496) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (4922169147*skoS2/1342177280 + 1015685697/536870912 >= skoSM*(126*skoS2 + 61)/40 - 1/5) & (4922169147*skoS2/1342177280 - skoSM*(126*skoS2 + 61)/40 + 5615299397/2684354560 < skoX*(2684354560*skoSM + skoX*(9844338294*skoS2 - 67108864*skoSM*(126*skoS2 + 61) + 5615299397) + 13862605000)/2684354560)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(1600645550679065, 4503599627370496)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-1600645550679065, 4503599627370496)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(4922169147, 1342177280), Symbol('skoS2')), Rational(1015685697, 536870912)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(4922169147, 1342177280), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(5615299397, 2684354560)), Mul(Rational(1, 2684354560), Symbol('skoX'), Add(Mul(Integer(2684354560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(9844338294), Symbol('skoS2')), Mul(Integer(-1), Integer(67108864), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(5615299397))), Integer(13862605000)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_51(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 <= 332496503741/211496092290) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 1600645550679065/4503599627370496) & (delta >= skoS2**2 - 2) & (delta - skoX >= 556708383557723565825/1180591620717411303424) & (delta >= 2 - skoS2**2) & (21149609229*skoS2/137438953472 - 332496503741/1374389534720 > skoX*(skoX*(211496092290*skoS2 - 332496503741) - 8764890997720)/1374389534720)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), LessThan(Symbol('skoS2'), Rational(332496503741, 211496092290)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(1600645550679065, 4503599627370496)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(556708383557723565825, 1180591620717411303424)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictGreaterThan(Add(Mul(Rational(21149609229, 137438953472), Symbol('skoS2')), Rational(-332496503741, 1374389534720)), Mul(Rational(1, 1374389534720), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(211496092290), Symbol('skoS2')), Integer(-332496503741))), Integer(-8764890997720)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_52(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 6402581890197585/18014398509481984) & (delta >= skoS2**2 - 2) & (delta - skoX >= -6402581890197585/18014398509481984) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (9844338231*skoS2/2684354560 + 2031371381/1073741824 >= skoSM*(126*skoS2 + 61)/40 - 1/5) & (9844338231*skoS2/2684354560 - skoSM*(126*skoS2 + 61)/40 + 11230598729/5368709120 < skoX*(5368709120*skoSM + skoX*(19688676462*skoS2 - 134217728*skoSM*(126*skoS2 + 61) + 11230598729) + 27725209960)/5368709120)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(6402581890197585, 18014398509481984)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-6402581890197585, 18014398509481984)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(9844338231, 2684354560), Symbol('skoS2')), Rational(2031371381, 1073741824)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(9844338231, 2684354560), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(11230598729, 5368709120)), Mul(Rational(1, 5368709120), Symbol('skoX'), Add(Mul(Integer(5368709120), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(19688676462), Symbol('skoS2')), Mul(Integer(-1), Integer(134217728), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(11230598729))), Integer(27725209960)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_53(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 <= 379995985267/241709856606) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 6402581890197585/18014398509481984) & (delta >= skoS2**2 - 2) & (delta - skoX >= 35629336547027413317713/75557863725914323419136) & (delta >= 2 - skoS2**2) & (845984498121*skoS2/5497558138880 - 2659971896869/10995116277760 > 7*skoX*(skoX*(241709856606*skoS2 - 379995985267) - 10017018271400)/10995116277760)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), LessThan(Symbol('skoS2'), Rational(379995985267, 241709856606)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(6402581890197585, 18014398509481984)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(35629336547027413317713, 75557863725914323419136)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictGreaterThan(Add(Mul(Rational(845984498121, 5497558138880), Symbol('skoS2')), Rational(-2659971896869, 10995116277760)), Mul(Rational(7, 10995116277760), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(241709856606), Symbol('skoS2')), Integer(-379995985267))), Integer(-10017018271400)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_54(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 25610328185827689/72057594037927936) & (delta >= skoS2**2 - 2) & (delta - skoX >= -25610328185827689/72057594037927936) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (3937735305*skoS2/1073741824 + 4062742775/2147483648 >= skoSM*(126*skoS2 + 61)/40 - 1/5) & (3937735305*skoS2/1073741824 - skoSM*(126*skoS2 + 61)/40 + 22461197523/10737418240 < skoX*(10737418240*skoSM + skoX*(39377353050*skoS2 - 268435456*skoSM*(126*skoS2 + 61) + 22461197523) + 55450419960)/10737418240)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(25610328185827689, 72057594037927936)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-25610328185827689, 72057594037927936)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(3937735305, 1073741824), Symbol('skoS2')), Rational(4062742775, 2147483648)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(3937735305, 1073741824), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(22461197523, 10737418240)), Mul(Rational(1, 10737418240), Symbol('skoX'), Add(Mul(Integer(10737418240), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(39377353050), Symbol('skoS2')), Mul(Integer(-1), Integer(268435456), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(22461197523))), Integer(55450419960)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_55(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 <= 2597628931/1652313222) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 25610328185827689/72057594037927936) & (delta >= skoS2**2 - 2) & (delta - skoX >= 132729619257633/281474976710656) & (delta >= 2 - skoS2**2) & (826156611*skoS2/5368709120 - 2597628931/10737418240 > skoX*(skoX*(1652313222*skoS2 - 2597628931) - 68475710840)/10737418240)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), LessThan(Symbol('skoS2'), Rational(2597628931, 1652313222)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(25610328185827689, 72057594037927936)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(132729619257633, 281474976710656)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictGreaterThan(Add(Mul(Rational(826156611, 5368709120), Symbol('skoS2')), Rational(-2597628931, 10737418240)), Mul(Rational(1, 10737418240), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(1652313222), Symbol('skoS2')), Integer(-2597628931))), Integer(-68475710840)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_56(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 102441311493236057/288230376151711744) & (delta >= skoS2**2 - 2) & (delta - skoX >= -102441311493236057/288230376151711744) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (39377352987*skoS2/10737418240 + 8125485537/4294967296 >= skoSM*(126*skoS2 + 61)/40 - 1/5) & (39377352987*skoS2/10737418240 - skoSM*(126*skoS2 + 61)/40 + 44922394981/21474836480 < skoX*(21474836480*skoSM + skoX*(78754705974*skoS2 - 536870912*skoSM*(126*skoS2 + 61) + 44922394981) + 110900839880)/21474836480)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(102441311493236057, 288230376151711744)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-102441311493236057, 288230376151711744)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(39377352987, 10737418240), Symbol('skoS2')), Rational(8125485537, 4294967296)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(39377352987, 10737418240), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(44922394981, 21474836480)), Mul(Rational(1, 21474836480), Symbol('skoX'), Add(Mul(Integer(21474836480), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(78754705974), Symbol('skoS2')), Mul(Integer(-1), Integer(536870912), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(44922394981))), Integer(110900839880)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_57(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 <= 1731752599/1101542190) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 102441311493236057/288230376151711744) & (delta >= skoS2**2 - 2) & (delta - skoX >= 132729619257633/281474976710656) & (delta >= 2 - skoS2**2) & (330462657*skoS2/2147483648 - 5195257797/21474836480 > 3*skoX*(skoX*(1101542190*skoS2 - 1731752599) - 45650473880)/21474836480)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), LessThan(Symbol('skoS2'), Rational(1731752599, 1101542190)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(102441311493236057, 288230376151711744)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(132729619257633, 281474976710656)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictGreaterThan(Add(Mul(Rational(330462657, 2147483648), Symbol('skoS2')), Rational(-5195257797, 21474836480)), Mul(Rational(3, 21474836480), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(1101542190), Symbol('skoS2')), Integer(-1731752599))), Integer(-45650473880)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_58(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 409765248473093625/1152921504606846976) & (delta >= skoS2**2 - 2) & (delta - skoX >= -409765248473093625/1152921504606846976) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (78754706037*skoS2/21474836480 + 16250971087/8589934592 >= skoSM*(126*skoS2 + 61)/40 - 1/5) & (78754706037*skoS2/21474836480 - skoSM*(126*skoS2 + 61)/40 + 89844790027/42949672960 < skoX*(42949672960*skoSM + skoX*(157509412074*skoS2 - 1073741824*skoSM*(126*skoS2 + 61) + 89844790027) + 221801679800)/42949672960)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(409765248473093625, 1152921504606846976)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-409765248473093625, 1152921504606846976)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(78754706037, 21474836480), Symbol('skoS2')), Rational(16250971087, 8589934592)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(78754706037, 21474836480), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(89844790027, 42949672960)), Mul(Rational(1, 42949672960), Symbol('skoX'), Add(Mul(Integer(42949672960), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(157509412074), Symbol('skoS2')), Mul(Integer(-1), Integer(1073741824), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(89844790027))), Integer(221801679800)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_59(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 <= 166248251581/105748046082) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 409765248473093625/1152921504606846976) & (delta >= skoS2**2 - 2) & (delta - skoX >= 139177092534115957025/295147905179352825856) & (delta >= 2 - skoS2**2) & (52874023041*skoS2/343597383680 - 166248251581/687194767360 > skoX*(skoX*(105748046082*skoS2 - 166248251581) - 4382445492440)/687194767360)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), LessThan(Symbol('skoS2'), Rational(166248251581, 105748046082)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(409765248473093625, 1152921504606846976)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(139177092534115957025, 295147905179352825856)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictGreaterThan(Add(Mul(Rational(52874023041, 343597383680), Symbol('skoS2')), Rational(-166248251581, 687194767360)), Mul(Rational(1, 687194767360), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(105748046082), Symbol('skoS2')), Integer(-166248251581))), Integer(-4382445492440)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_60(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 1639060988892075705/4611686018427387904) & (delta >= skoS2**2 - 2) & (delta - skoX >= -1639060988892075705/4611686018427387904) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (157509412011*skoS2/42949672960 + 32501942161/17179869184 >= skoSM*(126*skoS2 + 61)/40 - 1/5) & (157509412011*skoS2/42949672960 - skoSM*(126*skoS2 + 61)/40 + 179689579989/85899345920 < skoX*(85899345920*skoSM + skoX*(315018824022*skoS2 - 2147483648*skoSM*(126*skoS2 + 61) + 179689579989) + 443603359560)/85899345920)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(1639060988892075705, 4611686018427387904)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-1639060988892075705, 4611686018427387904)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(157509412011, 42949672960), Symbol('skoS2')), Rational(32501942161, 17179869184)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(157509412011, 42949672960), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(179689579989, 85899345920)), Mul(Rational(1, 85899345920), Symbol('skoX'), Add(Mul(Integer(85899345920), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(315018824022), Symbol('skoS2')), Mul(Integer(-1), Integer(2147483648), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(179689579989))), Integer(443603359560)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_61(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 <= 55416083687/35249349030) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 1639060988892075705/4611686018427387904) & (delta >= skoS2**2 - 2) & (delta - skoX >= 139177092534115957025/295147905179352825856) & (delta >= 2 - skoS2**2) & (10574804709*skoS2/68719476736 - 166248251061/687194767360 > 3*skoX*(skoX*(35249349030*skoS2 - 55416083687) - 1460815164040)/687194767360)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), LessThan(Symbol('skoS2'), Rational(55416083687, 35249349030)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(1639060988892075705, 4611686018427387904)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(139177092534115957025, 295147905179352825856)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictGreaterThan(Add(Mul(Rational(10574804709, 68719476736), Symbol('skoS2')), Rational(-166248251061, 687194767360)), Mul(Rational(3, 687194767360), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(35249349030), Symbol('skoS2')), Integer(-55416083687))), Integer(-1460815164040)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_62(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 6556243965568900409/18446744073709551616) & (delta >= skoS2**2 - 2) & (delta - skoX >= -6556243965568900409/18446744073709551616) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (63003764817*skoS2/17179869184 + 65003884335/34359738368 >= skoSM*(126*skoS2 + 61)/40 - 1/5) & (63003764817*skoS2/17179869184 - skoSM*(126*skoS2 + 61)/40 + 359379160043/171798691840 < skoX*(171798691840*skoSM + skoX*(630037648170*skoS2 - 4294967296*skoSM*(126*skoS2 + 61) + 359379160043) + 887206719160)/171798691840)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(6556243965568900409, 18446744073709551616)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-6556243965568900409, 18446744073709551616)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(63003764817, 17179869184), Symbol('skoS2')), Rational(65003884335, 34359738368)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(63003764817, 17179869184), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(359379160043, 171798691840)), Mul(Rational(1, 171798691840), Symbol('skoX'), Add(Mul(Integer(171798691840), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(630037648170), Symbol('skoS2')), Mul(Integer(-1), Integer(4294967296), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(359379160043))), Integer(887206719160)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_63(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 <= 166248251321/105748046586) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 6556243965568900409/18446744073709551616) & (delta >= skoS2**2 - 2) & (delta - skoX >= 139177092534115957025/295147905179352825856) & (delta >= 2 - skoS2**2) & (52874023293*skoS2/343597383680 - 166248251321/687194767360 > skoX*(skoX*(105748046586*skoS2 - 166248251321) - 4382445492280)/687194767360)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), LessThan(Symbol('skoS2'), Rational(166248251321, 105748046586)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(6556243965568900409, 18446744073709551616)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(139177092534115957025, 295147905179352825856)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictGreaterThan(Add(Mul(Rational(52874023293, 343597383680), Symbol('skoS2')), Rational(-166248251321, 687194767360)), Mul(Rational(1, 687194767360), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(105748046586), Symbol('skoS2')), Integer(-166248251321))), Integer(-4382445492280)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_64(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 26224975842274406457/73786976294838206464) & (delta >= skoS2**2 - 2) & (delta - skoX >= -26224975842274406457/73786976294838206464) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (630037648107*skoS2/171798691840 + 130007768657/68719476736 >= skoSM*(126*skoS2 + 61)/40 - 1/5) & (630037648107*skoS2/171798691840 - skoSM*(126*skoS2 + 61)/40 + 718758320021/343597383680 < skoX*(343597383680*skoSM + skoX*(1260075296214*skoS2 - 8589934592*skoSM*(126*skoS2 + 61) + 718758320021) + 1774413438280)/343597383680)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(26224975842274406457, 73786976294838206464)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-26224975842274406457, 73786976294838206464)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(630037648107, 171798691840), Symbol('skoS2')), Rational(130007768657, 68719476736)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(630037648107, 171798691840), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(718758320021, 343597383680)), Mul(Rational(1, 343597383680), Symbol('skoX'), Add(Mul(Integer(343597383680), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(1260075296214), Symbol('skoS2')), Mul(Integer(-1), Integer(8589934592), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(718758320021))), Integer(1774413438280)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_65(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 <= 166248251191/105748046838) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 26224975842274406457/73786976294838206464) & (delta >= skoS2**2 - 2) & (delta - skoX >= 139177092534115957025/295147905179352825856) & (delta >= 2 - skoS2**2) & (52874023419*skoS2/343597383680 - 166248251191/687194767360 > skoX*(skoX*(105748046838*skoS2 - 166248251191) - 4382445492200)/687194767360)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), LessThan(Symbol('skoS2'), Rational(166248251191, 105748046838)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(26224975842274406457, 73786976294838206464)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(139177092534115957025, 295147905179352825856)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictGreaterThan(Add(Mul(Rational(52874023419, 343597383680), Symbol('skoS2')), Rational(-166248251191, 687194767360)), Mul(Rational(1, 687194767360), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(105748046838), Symbol('skoS2')), Integer(-166248251191))), Integer(-4382445492200)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_66(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 104899903329095235473/295147905179352825856) & (delta >= skoS2**2 - 2) & (delta - skoX >= -104899903329095235473/295147905179352825856) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (1260075296151*skoS2/343597383680 + 260015537301/137438953472 >= skoSM*(126*skoS2 + 61)/40 - 1/5) & (1260075296151*skoS2/343597383680 - skoSM*(126*skoS2 + 61)/40 + 1437516639977/687194767360 < skoX*(687194767360*skoSM + skoX*(2520150592302*skoS2 - 17179869184*skoSM*(126*skoS2 + 61) + 1437516639977) + 3548826876520)/687194767360)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(104899903329095235473, 295147905179352825856)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-104899903329095235473, 295147905179352825856)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(1260075296151, 343597383680), Symbol('skoS2')), Rational(260015537301, 137438953472)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(1260075296151, 343597383680), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(1437516639977, 687194767360)), Mul(Rational(1, 687194767360), Symbol('skoX'), Add(Mul(Integer(687194767360), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(2520150592302), Symbol('skoS2')), Mul(Integer(-1), Integer(17179869184), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(1437516639977))), Integer(3548826876520)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_67(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 <= 83124125563/52874023482) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 104899903329095235473/295147905179352825856) & (delta >= skoS2**2 - 2) & (delta - skoX >= 139177092534115957025/295147905179352825856) & (delta >= 2 - skoS2**2) & (26437011741*skoS2/171798691840 - 83124125563/343597383680 > skoX*(skoX*(52874023482*skoS2 - 83124125563) - 2191222746080)/343597383680)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), LessThan(Symbol('skoS2'), Rational(83124125563, 52874023482)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(104899903329095235473, 295147905179352825856)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(139177092534115957025, 295147905179352825856)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictGreaterThan(Add(Mul(Rational(26437011741, 171798691840), Symbol('skoS2')), Rational(-83124125563, 343597383680)), Mul(Rational(1, 343597383680), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(52874023482), Symbol('skoS2')), Integer(-83124125563))), Integer(-2191222746080)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_68(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 419599613236376161185/1180591620717411303424) & (delta >= skoS2**2 - 2) & (delta - skoX >= -419599613236376161185/1180591620717411303424) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (2520150592239*skoS2/687194767360 + 520031074589/274877906944 >= skoSM*(126*skoS2 + 61)/40 - 1/5) & (2520150592239*skoS2/687194767360 - skoSM*(126*skoS2 + 61)/40 + 2875033279889/1374389534720 < skoX*(1374389534720*skoSM + skoX*(5040301184478*skoS2 - 34359738368*skoSM*(126*skoS2 + 61) + 2875033279889) + 7097653753000)/1374389534720)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(419599613236376161185, 1180591620717411303424)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-419599613236376161185, 1180591620717411303424)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(2520150592239, 687194767360), Symbol('skoS2')), Rational(520031074589, 274877906944)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(2520150592239, 687194767360), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(2875033279889, 1374389534720)), Mul(Rational(1, 1374389534720), Symbol('skoX'), Add(Mul(Integer(1374389534720), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(5040301184478), Symbol('skoS2')), Mul(Integer(-1), Integer(34359738368), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(2875033279889))), Integer(7097653753000)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_69(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 <= 1773314678351/1127979168246) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 419599613236376161185/1180591620717411303424) & (delta >= skoS2**2 - 2) & (delta - skoX >= 142517342753600950208577/302231454903657293676544) & (delta >= 2 - skoS2**2) & (1691968752369*skoS2/10995116277760 - 5319944035053/21990232555520 > 3*skoX*(skoX*(1127979168246*skoS2 - 1773314678351) - 46746085249480)/21990232555520)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), LessThan(Symbol('skoS2'), Rational(1773314678351, 1127979168246)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(419599613236376161185, 1180591620717411303424)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(142517342753600950208577, 302231454903657293676544)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictGreaterThan(Add(Mul(Rational(1691968752369, 10995116277760), Symbol('skoS2')), Rational(-5319944035053, 21990232555520)), Mul(Rational(3, 21990232555520), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(1127979168246), Symbol('skoS2')), Integer(-1773314678351))), Integer(-46746085249480)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_70(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 1678398452785495083329/4722366482869645213696) & (delta >= skoS2**2 - 2) & (delta - skoX >= -1678398452785495083329/4722366482869645213696) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (1008060236883*skoS2/274877906944 + 1040062149165/549755813888 >= skoSM*(126*skoS2 + 61)/40 - 1/5) & (1008060236883*skoS2/274877906944 - skoSM*(126*skoS2 + 61)/40 + 5750066559713/2748779069440 < skoX*(2748779069440*skoSM + skoX*(10080602368830*skoS2 - 68719476736*skoSM*(126*skoS2 + 61) + 5750066559713) + 14195307505960)/2748779069440)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(1678398452785495083329, 4722366482869645213696)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-1678398452785495083329, 4722366482869645213696)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(1008060236883, 274877906944), Symbol('skoS2')), Rational(1040062149165, 549755813888)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(1008060236883, 274877906944), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(5750066559713, 2748779069440)), Mul(Rational(1, 2748779069440), Symbol('skoX'), Add(Mul(Integer(2748779069440), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(10080602368830), Symbol('skoS2')), Mul(Integer(-1), Integer(68719476736), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(5750066559713))), Integer(14195307505960)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_71(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 <= 10639888069127/6767875011366) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 1678398452785495083329/4722366482869645213696) & (delta >= skoS2**2 - 2) & (delta - skoX >= 570069371011736221264265/1208925819614629174706176) & (delta >= 2 - skoS2**2) & (3383937505683*skoS2/21990232555520 - 10639888069127/43980465111040 > skoX*(skoX*(6767875011366*skoS2 - 10639888069127) - 280476511496200)/43980465111040)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), LessThan(Symbol('skoS2'), Rational(10639888069127, 6767875011366)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(1678398452785495083329, 4722366482869645213696)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(570069371011736221264265, 1208925819614629174706176)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictGreaterThan(Add(Mul(Rational(3383937505683, 21990232555520), Symbol('skoS2')), Rational(-10639888069127, 43980465111040)), Mul(Rational(1, 43980465111040), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(6767875011366), Symbol('skoS2')), Integer(-10639888069127))), Integer(-280476511496200)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_72(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 6713593810821961210497/18889465931478580854784) & (delta >= skoS2**2 - 2) & (delta - skoX >= -6713593810821961210497/18889465931478580854784) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (10080602368767*skoS2/2748779069440 + 2080124298317/1099511627776 >= skoSM*(126*skoS2 + 61)/40 - 1/5) & (10080602368767*skoS2/2748779069440 - skoSM*(126*skoS2 + 61)/40 + 11500133119361/5497558138880 < skoX*(5497558138880*skoSM + skoX*(20161204737534*skoS2 - 137438953472*skoSM*(126*skoS2 + 61) + 11500133119361) + 28390615011880)/5497558138880)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(6713593810821961210497, 18889465931478580854784)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-6713593810821961210497, 18889465931478580854784)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(10080602368767, 2748779069440), Symbol('skoS2')), Rational(2080124298317, 1099511627776)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(10080602368767, 2748779069440), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(11500133119361, 5497558138880)), Mul(Rational(1, 5497558138880), Symbol('skoX'), Add(Mul(Integer(5497558138880), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(20161204737534), Symbol('skoS2')), Mul(Integer(-1), Integer(137438953472), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(11500133119361))), Integer(28390615011880)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_73(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 <= 7093258712425/4511916674874) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 6713593810821961210497/18889465931478580854784) & (delta >= skoS2**2 - 2) & (delta - skoX >= 2280277484041609725916977/4835703278458516698824704) & (delta >= 2 - skoS2**2) & (6767875012311*skoS2/43980465111040 - 4255955227455/17592186044416 > 3*skoX*(skoX*(4511916674874*skoS2 - 7093258712425) - 186984340997240)/87960930222080)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), LessThan(Symbol('skoS2'), Rational(7093258712425, 4511916674874)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(6713593810821961210497, 18889465931478580854784)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(2280277484041609725916977, 4835703278458516698824704)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictGreaterThan(Add(Mul(Rational(6767875012311, 43980465111040), Symbol('skoS2')), Rational(-4255955227455, 17592186044416)), Mul(Rational(3, 87960930222080), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(4511916674874), Symbol('skoS2')), Integer(-7093258712425))), Integer(-186984340997240)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_74(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 26854375242647806596353/75557863725914323419136) & (delta >= skoS2**2 - 2) & (delta - skoX >= -26854375242647806596353/75557863725914323419136) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (20161204737471*skoS2/5497558138880 + 4160248596621/2199023255552 >= skoSM*(126*skoS2 + 61)/40 - 1/5) & (20161204737471*skoS2/5497558138880 - skoSM*(126*skoS2 + 61)/40 + 23000266238657/10995116277760 < skoX*(10995116277760*skoSM + skoX*(40322409474942*skoS2 - 274877906944*skoSM*(126*skoS2 + 61) + 23000266238657) + 56781230023720)/10995116277760)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(26854375242647806596353, 75557863725914323419136)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-26854375242647806596353, 75557863725914323419136)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(20161204737471, 5497558138880), Symbol('skoS2')), Rational(4160248596621, 2199023255552)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(20161204737471, 5497558138880), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(23000266238657, 10995116277760)), Mul(Rational(1, 10995116277760), Symbol('skoX'), Add(Mul(Integer(10995116277760), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(40322409474942), Symbol('skoS2')), Mul(Integer(-1), Integer(274877906944), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(23000266238657))), Integer(56781230023720)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_75(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 <= 42559552273571/27071500051134) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 26854375242647806596353/75557863725914323419136) & (delta >= skoS2**2 - 2) & (delta - skoX >= 9121109936155768585387745/19342813113834066795298816) & (delta >= 2 - skoS2**2) & (13535750025567*skoS2/87960930222080 - 42559552273571/175921860444160 > skoX*(skoX*(27071500051134*skoS2 - 42559552273571) - 1121906045982760)/175921860444160)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), LessThan(Symbol('skoS2'), Rational(42559552273571, 27071500051134)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(26854375242647806596353, 75557863725914323419136)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(9121109936155768585387745, 19342813113834066795298816)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictGreaterThan(Add(Mul(Rational(13535750025567, 87960930222080), Symbol('skoS2')), Rational(-42559552273571, 175921860444160)), Mul(Rational(1, 175921860444160), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(27071500051134), Symbol('skoS2')), Integer(-42559552273571))), Integer(-1121906045982760)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_76(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 107417500969311149894145/302231454903657293676544) & (delta >= skoS2**2 - 2) & (delta - skoX >= -107417500969311149894145/302231454903657293676544) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (40322409474879*skoS2/10995116277760 + 8320497193229/4398046511104 >= skoSM*(126*skoS2 + 61)/40 - 1/5) & (40322409474879*skoS2/10995116277760 - skoSM*(126*skoS2 + 61)/40 + 46000532477249/21990232555520 < skoX*(21990232555520*skoSM + skoX*(80644818949758*skoS2 - 549755813888*skoSM*(126*skoS2 + 61) + 46000532477249) + 113562460047400)/21990232555520)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(107417500969311149894145, 302231454903657293676544)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-107417500969311149894145, 302231454903657293676544)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(40322409474879, 10995116277760), Symbol('skoS2')), Rational(8320497193229, 4398046511104)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(40322409474879, 10995116277760), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(46000532477249, 21990232555520)), Mul(Rational(1, 21990232555520), Symbol('skoX'), Add(Mul(Integer(21990232555520), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(80644818949758), Symbol('skoS2')), Mul(Integer(-1), Integer(549755813888), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(46000532477249))), Integer(113562460047400)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_77(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 <= 16213162770689/10312952400810) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 107417500969311149894145/302231454903657293676544) & (delta >= skoS2**2 - 2) & (delta - skoX >= 583751035913883826918574385/1237940039285380274899124224) & (delta >= 2 - skoS2**2) & (21657200041701*skoS2/140737488355328 - 340476418184469/1407374883553280 > 21*skoX*(skoX*(10312952400810*skoS2 - 16213162770689) - 427392779421880)/1407374883553280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), LessThan(Symbol('skoS2'), Rational(16213162770689, 10312952400810)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(107417500969311149894145, 302231454903657293676544)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(583751035913883826918574385, 1237940039285380274899124224)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictGreaterThan(Add(Mul(Rational(21657200041701, 140737488355328), Symbol('skoS2')), Rational(-340476418184469, 1407374883553280)), Mul(Rational(21, 1407374883553280), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(10312952400810), Symbol('skoS2')), Integer(-16213162770689))), Integer(-427392779421880)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_78(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 429670003874684446594049/1208925819614629174706176) & (delta >= skoS2**2 - 2) & (delta - skoX >= -429670003874684446594049/1208925819614629174706176) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (16128963789939*skoS2/4398046511104 + 16640994386445/8796093022208 >= skoSM*(126*skoS2 + 61)/40 - 1/5) & (16128963789939*skoS2/4398046511104 - skoSM*(126*skoS2 + 61)/40 + 92001064954433/43980465111040 < skoX*(43980465111040*skoSM + skoX*(161289637899390*skoS2 - 1099511627776*skoSM*(126*skoS2 + 61) + 92001064954433) + 227124920094760)/43980465111040)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(429670003874684446594049, 1208925819614629174706176)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-429670003874684446594049, 1208925819614629174706176)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(16128963789939, 4398046511104), Symbol('skoS2')), Rational(16640994386445, 8796093022208)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(16128963789939, 4398046511104), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(92001064954433, 43980465111040)), Mul(Rational(1, 43980465111040), Symbol('skoX'), Add(Mul(Integer(43980465111040), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(161289637899390), Symbol('skoS2')), Mul(Integer(-1), Integer(1099511627776), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(92001064954433))), Integer(227124920094760)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(delta:sympy.Rational, skoX:sympy.Rational, skoS2:sympy.Rational, skoSP:sympy.Rational, skoSM:sympy.Rational):
	# (0 <= delta) & (1 > skoX) & (skoS2 > 0) & (skoSM > 0) & (skoSP > 0) & (skoX > 0) & (skoS2**2 - 2 <= delta) & (skoSM**2 + skoX - 1 <= delta) & (2 - skoS2**2 <= delta) & (-skoSP**2 + skoX + 1 <= delta) & (skoSP**2 - skoX - 1 <= delta) & (-skoSM**2 - skoX + 1 <= delta) & (skoSP*(-63*skoS2/20 - 13/8) <= skoSM*(-63*skoS2/20 - 61/40) + 1/5) & (skoX*(skoSM + skoSP + skoX*(skoSM*(-63*skoS2/20 - 61/40) + skoSP*(63*skoS2/20 + 13/8) + 1/5) + 4) > skoSM*(-63*skoS2/20 - 61/40) + skoSP*(63*skoS2/20 + 13/8) + 1/5)

	post_cond =  And(LessThan(Integer(0), Symbol('delta')), StrictGreaterThan(Integer(1), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoSP'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), LessThan(Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Symbol('delta')), LessThan(Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1)), Symbol('delta')), LessThan(Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Symbol('delta')), LessThan(Add(Mul(Integer(-1), Pow(Symbol('skoSP'), Integer(2))), Symbol('skoX'), Integer(1)), Symbol('delta')), LessThan(Add(Pow(Symbol('skoSP'), Integer(2)), Mul(Integer(-1), Symbol('skoX')), Integer(-1)), Symbol('delta')), LessThan(Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)), Symbol('delta')), LessThan(Mul(Symbol('skoSP'), Add(Mul(Integer(-1), Rational(63, 20), Symbol('skoS2')), Rational(-13, 8))), Add(Mul(Symbol('skoSM'), Add(Mul(Integer(-1), Rational(63, 20), Symbol('skoS2')), Rational(-61, 40))), Rational(1, 5))), StrictGreaterThan(Mul(Symbol('skoX'), Add(Symbol('skoSM'), Symbol('skoSP'), Mul(Symbol('skoX'), Add(Mul(Symbol('skoSM'), Add(Mul(Integer(-1), Rational(63, 20), Symbol('skoS2')), Rational(-61, 40))), Mul(Symbol('skoSP'), Add(Mul(Rational(63, 20), Symbol('skoS2')), Rational(13, 8))), Rational(1, 5))), Integer(4))), Add(Mul(Symbol('skoSM'), Add(Mul(Integer(-1), Rational(63, 20), Symbol('skoS2')), Rational(-61, 40))), Mul(Symbol('skoSP'), Add(Mul(Rational(63, 20), Symbol('skoS2')), Rational(13, 8))), Rational(1, 5))))

	eval = post_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'skoSP':skoSP, 'skoSM':skoSM })

	return eval == sympy.logic.boolalg.BooleanTrue





if __name__=="__main__":
	
	ip_0=int(input("enter integer numerator of delta:\n"))
	ip_1=int(input("enter integer denominator of delta:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	delta=sympy.Rational(ip_0,ip_1)
	
	
	ip_0=int(input("enter integer numerator of skoX:\n"))
	ip_1=int(input("enter integer denominator of skoX:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	skoX=sympy.Rational(ip_0,ip_1)
	
	
	ip_0=int(input("enter integer numerator of skoS2:\n"))
	ip_1=int(input("enter integer denominator of skoS2:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	skoS2=sympy.Rational(ip_0,ip_1)
	
	
	
	
	if pre_condition_0(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_0 SAT")
		print('delta = 2')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 1')
		exit(0)
	
	
	if pre_condition_1(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_1 SAT")
		print('delta = 2')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 1')
		exit(0)
	
	
	if pre_condition_2(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_2 SAT")
		print('delta = 15/32')
		print('skoX = 1/2')
		print('skoS2 = 5/4')
		print('skoSM = 1/2')
		print('skoSP = 9/8')
		exit(0)
	
	
	if pre_condition_3(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_3 SAT")
		print('delta = 15/32')
		print('skoX = 1/2')
		print('skoS2 = 5/4')
		print('skoSM = 1/2')
		print('skoSP = 9/8')
		exit(0)
	
	
	if pre_condition_4(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_4 SAT")
		print('delta = 5/8')
		print('skoX = 1/32')
		print('skoS2 = 3/2')
		print('skoSM = 5/4')
		print('skoSP = 39/32')
		exit(0)
	
	
	if pre_condition_5(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_5 SAT")
		print('delta = 5/8')
		print('skoX = 1/32')
		print('skoS2 = 3/2')
		print('skoSM = 5/4')
		print('skoSP = 39/32')
		exit(0)
	
	
	if pre_condition_6(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_6 SAT")
		print('delta = 1/128')
		print('skoX = 1/2')
		print('skoS2 = 181/128')
		print('skoSM = 45/64')
		print('skoSP = 157/128')
		exit(0)
	
	
	if pre_condition_7(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_7 SAT")
		print('delta = 1/128')
		print('skoX = 1/2')
		print('skoS2 = 181/128')
		print('skoSM = 45/64')
		print('skoSP = 157/128')
		exit(0)
	
	
	if pre_condition_8(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_8 SAT")
		print('delta = 7/32')
		print('skoX = 3/4')
		print('skoS2 = 11/8')
		print('skoSM = 1/2')
		print('skoSP = 5/4')
		exit(0)
	
	
	if pre_condition_9(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_9 SAT")
		print('delta = 7/32')
		print('skoX = 3/4')
		print('skoS2 = 11/8')
		print('skoSM = 1/2')
		print('skoSP = 5/4')
		exit(0)
	
	
	if pre_condition_10(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_10 SAT")
		print('delta = 29/64')
		print('skoX = 1/32')
		print('skoS2 = 3/2')
		print('skoSM = 19/16')
		print('skoSP = 37/32')
		exit(0)
	
	
	if pre_condition_11(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_11 SAT")
		print('delta = 29/64')
		print('skoX = 1/32')
		print('skoS2 = 3/2')
		print('skoSM = 19/16')
		print('skoSP = 37/32')
		exit(0)
	
	
	if pre_condition_12(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_12 SAT")
		print('delta = 961/2048')
		print('skoX = 1/64')
		print('skoS2 = 25/16')
		print('skoSM = 2469/2048')
		print('skoSP = 149/128')
		exit(0)
	
	
	if pre_condition_13(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_13 SAT")
		print('delta = 961/2048')
		print('skoX = 1/64')
		print('skoS2 = 25/16')
		print('skoSM = 2469/2048')
		print('skoSP = 149/128')
		exit(0)
	
	
	if pre_condition_14(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_14 SAT")
		print('delta = 123/256')
		print('skoX = 1/256')
		print('skoS2 = 3/2')
		print('skoSM = 311/256')
		print('skoSP = 299/256')
		exit(0)
	
	
	if pre_condition_15(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_15 SAT")
		print('delta = 123/256')
		print('skoX = 1/256')
		print('skoS2 = 3/2')
		print('skoSM = 311/256')
		print('skoSP = 299/256')
		exit(0)
	
	
	if pre_condition_16(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_16 SAT")
		print('delta = 61/128')
		print('skoX = 1/256')
		print('skoS2 = 25/16')
		print('skoSM = 19877/16384')
		print('skoSP = 597/512')
		exit(0)
	
	
	if pre_condition_17(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_17 SAT")
		print('delta = 61/128')
		print('skoX = 1/256')
		print('skoS2 = 25/16')
		print('skoSM = 19877/16384')
		print('skoSP = 597/512')
		exit(0)
	
	
	if pre_condition_18(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_18 SAT")
		print('delta = 3881/8192')
		print('skoX = 1/512')
		print('skoS2 = 25/16')
		print('skoSM = 39753/32768')
		print('skoSP = 1193/1024')
		exit(0)
	
	
	if pre_condition_19(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_19 SAT")
		print('delta = 3881/8192')
		print('skoX = 1/512')
		print('skoS2 = 25/16')
		print('skoSM = 39753/32768')
		print('skoSP = 1193/1024')
		exit(0)
	
	
	if pre_condition_20(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_20 SAT")
		print('delta = 34064980198293505/72057594037927936')
		print('skoX = 1/1024')
		print('skoS2 = 25/16')
		print('skoSM = 39753/32768')
		print('skoSP = 2385/2048')
		exit(0)
	
	
	if pre_condition_21(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_21 SAT")
		print('delta = 34064980198293505/72057594037927936')
		print('skoX = 1/1024')
		print('skoS2 = 25/16')
		print('skoSM = 39753/32768')
		print('skoSP = 2385/2048')
		exit(0)
	
	
	if pre_condition_22(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_22 SAT")
		print('delta = 7737/16384')
		print('skoX = 1/2048')
		print('skoS2 = 25/16')
		print('skoSM = 79505/65536')
		print('skoSP = 4769/4096')
		exit(0)
	
	
	if pre_condition_23(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_23 SAT")
		print('delta = 7737/16384')
		print('skoX = 1/2048')
		print('skoS2 = 25/16')
		print('skoSM = 79505/65536')
		print('skoSP = 4769/4096')
		exit(0)
	
	
	if pre_condition_24(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_24 SAT")
		print('delta = 30931/65536')
		print('skoX = 1/4096')
		print('skoS2 = 25/16')
		print('skoSM = 159009/131072')
		print('skoSP = 9537/8192')
		exit(0)
	
	
	if pre_condition_25(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_25 SAT")
		print('delta = 30931/65536')
		print('skoX = 1/4096')
		print('skoS2 = 25/16')
		print('skoSM = 159009/131072')
		print('skoSP = 9537/8192')
		exit(0)
	
	
	if pre_condition_26(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_26 SAT")
		print('delta = 3865/8192')
		print('skoX = 1/8192')
		print('skoS2 = 201/128')
		print('skoSM = 159001/131072')
		print('skoSP = 19075/16384')
		exit(0)
	
	
	if pre_condition_27(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_27 SAT")
		print('delta = 3865/8192')
		print('skoX = 1/8192')
		print('skoS2 = 201/128')
		print('skoSM = 159001/131072')
		print('skoSP = 19075/16384')
		exit(0)
	
	
	if pre_condition_28(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_28 SAT")
		print('delta = 61817/131072')
		print('skoX = 1/16384')
		print('skoS2 = 201/128')
		print('skoSM = 636003/524288')
		print('skoSP = 38149/32768')
		exit(0)
	
	
	if pre_condition_29(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_29 SAT")
		print('delta = 61817/131072')
		print('skoX = 1/16384')
		print('skoS2 = 201/128')
		print('skoSM = 636003/524288')
		print('skoSP = 38149/32768')
		exit(0)
	
	
	if pre_condition_30(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_30 SAT")
		print('delta = 15453/32768')
		print('skoX = 1/32768')
		print('skoS2 = 3219/2048')
		print('skoSM = 636001/524288')
		print('skoSP = 76299/65536')
		exit(0)
	
	
	if pre_condition_31(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_31 SAT")
		print('delta = 15453/32768')
		print('skoX = 1/32768')
		print('skoS2 = 3219/2048')
		print('skoSM = 636001/524288')
		print('skoSP = 76299/65536')
		exit(0)
	
	
	if pre_condition_32(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_32 SAT")
		print('delta = 247237/524288')
		print('skoX = 1/65536')
		print('skoS2 = 3219/2048')
		print('skoSM = 2544003/2097152')
		print('skoSP = 152597/131072')
		exit(0)
	
	
	if pre_condition_33(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_33 SAT")
		print('delta = 247237/524288')
		print('skoX = 1/65536')
		print('skoS2 = 3219/2048')
		print('skoSM = 2544003/2097152')
		print('skoSP = 152597/131072')
		exit(0)
	
	
	if pre_condition_34(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_34 SAT")
		print('delta = 494465/1048576')
		print('skoX = 1/131072')
		print('skoS2 = 51515/32768')
		print('skoSM = 5088005/4194304')
		print('skoSP = 305195/262144')
		exit(0)
	
	
	if pre_condition_35(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_35 SAT")
		print('delta = 494465/1048576')
		print('skoX = 1/131072')
		print('skoS2 = 51515/32768')
		print('skoSM = 5088005/4194304')
		print('skoSP = 305195/262144')
		exit(0)
	
	
	if pre_condition_36(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_36 SAT")
		print('delta = 1977843/4194304')
		print('skoX = 1/262144')
		print('skoS2 = 51515/32768')
		print('skoSM = 10176009/8388608')
		print('skoSP = 610389/524288')
		exit(0)
	
	
	if pre_condition_37(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_37 SAT")
		print('delta = 1977843/4194304')
		print('skoX = 1/262144')
		print('skoS2 = 51515/32768')
		print('skoSM = 10176009/8388608')
		print('skoSP = 610389/524288')
		exit(0)
	
	
	if pre_condition_38(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_38 SAT")
		print('delta = 33978930389140481/72057594037927936')
		print('skoX = 1/524288')
		print('skoS2 = 51515/32768')
		print('skoSM = 10176009/8388608')
		print('skoSP = 1220777/1048576')
		exit(0)
	
	
	if pre_condition_39(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_39 SAT")
		print('delta = 33978930389140481/72057594037927936')
		print('skoX = 1/524288')
		print('skoS2 = 51515/32768')
		print('skoSM = 10176009/8388608')
		print('skoSP = 1220777/1048576')
		exit(0)
	
	
	if pre_condition_40(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_40 SAT")
		print('delta = 988915/2097152')
		print('skoX = 1/1048576')
		print('skoS2 = 51515/32768')
		print('skoSM = 40704035/33554432')
		print('skoSP = 2441553/2097152')
		exit(0)
	
	
	if pre_condition_41(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_41 SAT")
		print('delta = 988915/2097152')
		print('skoX = 1/1048576')
		print('skoS2 = 51515/32768')
		print('skoSM = 40704035/33554432')
		print('skoSP = 2441553/2097152')
		exit(0)
	
	
	if pre_condition_42(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_42 SAT")
		print('delta = 7911311/16777216')
		print('skoX = 1/2097152')
		print('skoS2 = 51515/32768')
		print('skoSM = 81408069/67108864')
		print('skoSP = 4883105/4194304')
		exit(0)
	
	
	if pre_condition_43(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_43 SAT")
		print('delta = 7911311/16777216')
		print('skoX = 1/2097152')
		print('skoS2 = 51515/32768')
		print('skoSM = 81408069/67108864')
		print('skoSP = 4883105/4194304')
		exit(0)
	
	
	if pre_condition_44(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_44 SAT")
		print('delta = 63290451/134217728')
		print('skoX = 1/4194304')
		print('skoS2 = 51515/32768')
		print('skoSM = 325632275/268435456')
		print('skoSP = 9766209/8388608')
		exit(0)
	
	
	if pre_condition_45(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_45 SAT")
		print('delta = 63290451/134217728')
		print('skoX = 1/4194304')
		print('skoS2 = 51515/32768')
		print('skoSM = 325632275/268435456')
		print('skoSP = 9766209/8388608')
		exit(0)
	
	
	if pre_condition_46(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_46 SAT")
		print('delta = 2025293891/4294967296')
		print('skoX = 1/8388608')
		print('skoS2 = 51515/32768')
		print('skoSM = 41680931199/34359738368')
		print('skoSP = 19532417/16777216')
		exit(0)
	
	
	if pre_condition_47(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_47 SAT")
		print('delta = 2025293891/4294967296')
		print('skoX = 1/8388608')
		print('skoS2 = 51515/32768')
		print('skoSM = 41680931199/34359738368')
		print('skoSP = 19532417/16777216')
		exit(0)
	
	
	if pre_condition_48(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_48 SAT")
		print('delta = 7911303/16777216')
		print('skoX = 1/16777216')
		print('skoS2 = 1648483/1048576')
		print('skoSM = 325632273/268435456')
		print('skoSP = 39064835/33554432')
		exit(0)
	
	
	if pre_condition_49(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_49 SAT")
		print('delta = 7911303/16777216')
		print('skoX = 1/16777216')
		print('skoS2 = 1648483/1048576')
		print('skoSM = 325632273/268435456')
		print('skoSP = 39064835/33554432')
		exit(0)
	
	
	if pre_condition_50(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_50 SAT")
		print('delta = 8101173717/17179869184')
		print('skoX = 1/33554432')
		print('skoS2 = 1648483/1048576')
		print('skoSM = 41680930943/34359738368')
		print('skoSP = 78129669/67108864')
		exit(0)
	
	
	if pre_condition_51(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_51 SAT")
		print('delta = 8101173717/17179869184')
		print('skoX = 1/33554432')
		print('skoS2 = 1648483/1048576')
		print('skoSM = 41680930943/34359738368')
		print('skoSP = 78129669/67108864')
		exit(0)
	
	
	if pre_condition_52(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_52 SAT")
		print('delta = 64809387683/137438953472')
		print('skoX = 1/67108864')
		print('skoS2 = 1648483/1048576')
		print('skoSM = 333447447543/274877906944')
		print('skoSP = 156259337/134217728')
		exit(0)
	
	
	if pre_condition_53(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_53 SAT")
		print('delta = 64809387683/137438953472')
		print('skoX = 1/67108864')
		print('skoS2 = 1648483/1048576')
		print('skoSM = 333447447543/274877906944')
		print('skoSP = 156259337/134217728')
		exit(0)
	
	
	if pre_condition_54(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_54 SAT")
		print('delta = 3955651/8388608')
		print('skoX = 1/134217728')
		print('skoS2 = 3296967/2097152')
		print('skoSM = 20352017/16777216')
		print('skoSP = 312518675/268435456')
		exit(0)
	
	
	if pre_condition_55(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_55 SAT")
		print('delta = 3955651/8388608')
		print('skoX = 1/134217728')
		print('skoS2 = 3296967/2097152')
		print('skoSM = 20352017/16777216')
		print('skoSP = 312518675/268435456')
		exit(0)
	
	
	if pre_condition_56(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_56 SAT")
		print('delta = 543660524774232065/1152921504606846976')
		print('skoX = 1/268435456')
		print('skoS2 = 3296967/2097152')
		print('skoSM = 20352017/16777216')
		print('skoSP = 625037349/536870912')
		exit(0)
	
	
	if pre_condition_57(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_57 SAT")
		print('delta = 543660524774232065/1152921504606846976')
		print('skoX = 1/268435456')
		print('skoS2 = 3296967/2097152')
		print('skoSM = 20352017/16777216')
		print('skoSP = 625037349/536870912')
		exit(0)
	
	
	if pre_condition_58(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_58 SAT")
		print('delta = 126580829/268435456')
		print('skoX = 1/536870912')
		print('skoS2 = 13187869/8388608')
		print('skoSM = 20840465391/17179869184')
		print('skoSP = 1250074699/1073741824')
		exit(0)
	
	
	if pre_condition_59(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_59 SAT")
		print('delta = 126580829/268435456')
		print('skoX = 1/536870912')
		print('skoS2 = 13187869/8388608')
		print('skoSM = 20840465391/17179869184')
		print('skoSP = 1250074699/1073741824')
		exit(0)
	
	
	if pre_condition_60(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_60 SAT")
		print('delta = 2123673901504423/4503599627370496')
		print('skoX = 1/1073741824')
		print('skoS2 = 13187869/8388608')
		print('skoSM = 20840465391/17179869184')
		print('skoSP = 2500149397/2147483648')
		exit(0)
	
	
	if pre_condition_61(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_61 SAT")
		print('delta = 2123673901504423/4503599627370496')
		print('skoX = 1/1073741824')
		print('skoS2 = 13187869/8388608')
		print('skoSM = 20840465391/17179869184')
		print('skoSP = 2500149397/2147483648')
		exit(0)
	
	
	if pre_condition_62(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_62 SAT")
		print('delta = 2123673899407271/4503599627370496')
		print('skoX = 1/2147483648')
		print('skoS2 = 3376094505/2147483648')
		print('skoSM = 20840465391/17179869184')
		print('skoSP = 5000298795/4294967296')
		exit(0)
	
	
	if pre_condition_63(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_63 SAT")
		print('delta = 2123673899407271/4503599627370496')
		print('skoX = 1/2147483648')
		print('skoS2 = 3376094505/2147483648')
		print('skoSM = 20840465391/17179869184')
		print('skoSP = 5000298795/4294967296')
		exit(0)
	
	
	if pre_condition_64(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_64 SAT")
		print('delta = 2123673898358695/4503599627370496')
		print('skoX = 1/4294967296')
		print('skoS2 = 3376094505/2147483648')
		print('skoSM = 20840465391/17179869184')
		print('skoSP = 10000597589/8589934592')
		exit(0)
	
	
	if pre_condition_65(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_65 SAT")
		print('delta = 2123673898358695/4503599627370496')
		print('skoX = 1/4294967296')
		print('skoS2 = 3376094505/2147483648')
		print('skoSM = 20840465391/17179869184')
		print('skoSP = 10000597589/8589934592')
		exit(0)
	
	
	if pre_condition_66(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_66 SAT")
		print('delta = 2123673897834407/4503599627370496')
		print('skoX = 1/8589934592')
		print('skoS2 = 3376094505/2147483648')
		print('skoSM = 20840465391/17179869184')
		print('skoSP = 20001195177/17179869184')
		exit(0)
	
	
	if pre_condition_67(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_67 SAT")
		print('delta = 2123673897834407/4503599627370496')
		print('skoX = 1/8589934592')
		print('skoS2 = 3376094505/2147483648')
		print('skoSM = 20840465391/17179869184')
		print('skoSP = 20001195177/17179869184')
		exit(0)
	
	
	if pre_condition_68(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_68 SAT")
		print('delta = 64809384081/137438953472')
		print('skoX = 1/17179869184')
		print('skoS2 = 3376094505/2147483648')
		print('skoSM = 666894892511/549755813888')
		print('skoSP = 40002390353/34359738368')
		exit(0)
	
	
	if pre_condition_69(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_69 SAT")
		print('delta = 64809384081/137438953472')
		print('skoX = 1/17179869184')
		print('skoS2 = 3376094505/2147483648')
		print('skoSM = 666894892511/549755813888')
		print('skoSP = 40002390353/34359738368')
		exit(0)
	
	
	if pre_condition_70(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_70 SAT")
		print('delta = 129618768153/274877906944')
		print('skoX = 1/34359738368')
		print('skoS2 = 3376094505/2147483648')
		print('skoSM = 1333789785021/1099511627776')
		print('skoSP = 80004780705/68719476736')
		exit(0)
	
	
	if pre_condition_71(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_71 SAT")
		print('delta = 129618768153/274877906944')
		print('skoX = 1/34359738368')
		print('skoS2 = 3376094505/2147483648')
		print('skoSM = 1333789785021/1099511627776')
		print('skoSP = 80004780705/68719476736')
		exit(0)
	
	
	if pre_condition_72(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_72 SAT")
		print('delta = 259237536297/549755813888')
		print('skoX = 1/68719476736')
		print('skoS2 = 3376094505/2147483648')
		print('skoSM = 2667579570041/2199023255552')
		print('skoSP = 160009561409/137438953472')
		exit(0)
	
	
	if pre_condition_73(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_73 SAT")
		print('delta = 259237536297/549755813888')
		print('skoX = 1/68719476736')
		print('skoS2 = 3376094505/2147483648')
		print('skoSM = 2667579570041/2199023255552')
		print('skoSP = 160009561409/137438953472')
		exit(0)
	
	
	if pre_condition_74(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_74 SAT")
		print('delta = 1036950145169/2199023255552')
		print('skoX = 1/137438953472')
		print('skoS2 = 3376094505/2147483648')
		print('skoSM = 5335159140081/4398046511104')
		print('skoSP = 320019122817/274877906944')
		exit(0)
	
	
	if pre_condition_75(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_75 SAT")
		print('delta = 1036950145169/2199023255552')
		print('skoX = 1/137438953472')
		print('skoS2 = 3376094505/2147483648')
		print('skoSM = 5335159140081/4398046511104')
		print('skoSP = 320019122817/274877906944')
		exit(0)
	
	
	if pre_condition_76(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_76 SAT")
		print('delta = 4147800580643/8796093022208')
		print('skoX = 1/274877906944')
		print('skoS2 = 3376094505/2147483648')
		print('skoSM = 42681273120647/35184372088832')
		print('skoSP = 640038245633/549755813888')
		exit(0)
	
	
	if pre_condition_77(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_77 SAT")
		print('delta = 4147800580643/8796093022208')
		print('skoX = 1/274877906944')
		print('skoS2 = 3376094505/2147483648')
		print('skoSM = 42681273120647/35184372088832')
		print('skoSP = 640038245633/549755813888')
		exit(0)
	
	
	if pre_condition_78(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_78 SAT")
		print('delta = 33978782356491757/72057594037927936')
		print('skoX = 1/549755813888')
		print('skoS2 = 3376094505/2147483648')
		print('skoSM = 42681273120647/35184372088832')
		print('skoSP = 1280076491265/1099511627776')
		exit(0)


	print("UNKNOWN")
	exit(0)
