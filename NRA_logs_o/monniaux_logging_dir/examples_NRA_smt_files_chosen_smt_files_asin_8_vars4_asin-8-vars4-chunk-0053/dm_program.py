import sympy
from sympy import *

def pre_condition_0(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= skoX) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= -skoX) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (63*skoS2/20 - skoSM*(126*skoS2 + 61)/40 + 73/40 < skoX*(40*skoSM + skoX*(126*skoS2 - skoSM*(126*skoS2 + 61) + 73) + 200)/40)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(63, 20), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(73, 40)), Mul(Rational(1, 40), Symbol('skoX'), Add(Mul(Integer(40), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Mul(Integer(-1), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(73))), Integer(200)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= skoX) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= -skoX) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta >= 2 - skoS2**2) & (skoX**2 + 20*skoX > 1)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictGreaterThan(Add(Pow(Symbol('skoX'), Integer(2)), Mul(Integer(20), Symbol('skoX'))), Integer(1)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 17/64) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -17/64) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (567*skoS2/160 - skoSM*(126*skoS2 + 61)/40 + 649/320 < skoX*(320*skoSM + skoX*(1134*skoS2 - 8*skoSM*(126*skoS2 + 61) + 649) + 1640)/320)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(17, 64)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-17, 64)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(567, 160), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(649, 320)), Mul(Rational(1, 320), Symbol('skoX'), Add(Mul(Integer(320), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(1134), Symbol('skoS2')), Mul(Integer(-1), Integer(8), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(649))), Integer(1640)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 3/4) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -17/64) & (delta >= 2 - skoS2**2) & (63*skoS2/32 + 81/64 < 9*skoX*(skoX*(14*skoS2 + 9) + 40)/64)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(3, 4)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-17, 64)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(63, 32), Symbol('skoS2')), Rational(81, 64)), Mul(Rational(9, 64), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(14), Symbol('skoS2')), Integer(9))), Integer(40)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_4(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 70785/262144) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -70785/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (36351*skoS2/10240 - skoSM*(126*skoS2 + 61)/40 + 41601/20480 < skoX*(20480*skoSM + skoX*(72702*skoS2 - 512*skoSM*(126*skoS2 + 61) + 41601) + 105000)/20480)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(70785, 262144)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-70785, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(36351, 10240), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(41601, 20480)), Mul(Rational(1, 20480), Symbol('skoX'), Add(Mul(Integer(20480), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(72702), Symbol('skoS2')), Mul(Integer(-1), Integer(512), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(41601))), Integer(105000)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_5(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 7/16) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -70785/262144) & (delta >= 2 - skoS2**2) & (12159*skoS2/10240 + 18177/20480 < 3*skoX*(skoX*(8106*skoS2 + 6059) + 40120)/20480)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(7, 16)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-70785, 262144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(12159, 10240), Symbol('skoS2')), Rational(18177, 20480)), Mul(Rational(3, 20480), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(8106), Symbol('skoS2')), Integer(6059))), Integer(40120)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_6(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 105/256) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -105/256) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (1197*skoS2/320 - skoSM*(126*skoS2 + 61)/40 + 1363/640 < skoX*(640*skoSM + skoX*(2394*skoS2 - 16*skoSM*(126*skoS2 + 61) + 1363) + 3320)/640)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(105, 256)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-105, 256)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(1197, 320), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(1363, 640)), Mul(Rational(1, 640), Symbol('skoX'), Add(Mul(Integer(640), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(2394), Symbol('skoS2')), Mul(Integer(-1), Integer(16), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(1363))), Integer(3320)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_7(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 105/256) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -87/256) & (delta >= 2 - skoS2**2) & (189*skoS2/160 + 57/64 < 3*skoX*(skoX*(126*skoS2 + 95) + 640)/320)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(105, 256)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-87, 256)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(189, 160), Symbol('skoS2')), Rational(57, 64)), Mul(Rational(3, 320), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(95))), Integer(640)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_8(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 9/16) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -9/16) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (63*skoS2/16 - skoSM*(126*skoS2 + 61)/40 + 357/160 < skoX*(160*skoSM + skoX*(630*skoS2 - 4*skoSM*(126*skoS2 + 61) + 357) + 840)/160)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(9, 16)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-9, 16)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(63, 16), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(357, 160)), Mul(Rational(1, 160), Symbol('skoX'), Add(Mul(Integer(160), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(630), Symbol('skoS2')), Mul(Integer(-1), Integer(4), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(357))), Integer(840)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_9(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 9/16) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -7/16) & (delta >= 2 - skoS2**2) & (63*skoS2/40 + 87/80 < 3*skoX*(skoX*(42*skoS2 + 29) + 160)/80)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(9, 16)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-7, 16)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(63, 40), Symbol('skoS2')), Rational(87, 80)), Mul(Rational(3, 80), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(42), Symbol('skoS2')), Integer(29))), Integer(160)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_10(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 57/64) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -57/64) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (693*skoS2/160 - skoSM*(126*skoS2 + 61)/40 + 779/320 < skoX*(320*skoSM + skoX*(1386*skoS2 - 8*skoSM*(126*skoS2 + 61) + 779) + 1720)/320)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(57, 64)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-57, 64)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(693, 160), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(779, 320)), Mul(Rational(1, 320), Symbol('skoX'), Add(Mul(Integer(320), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(1386), Symbol('skoS2')), Mul(Integer(-1), Integer(8), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(779))), Integer(1720)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_11(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 57/64) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -3/4) & (delta >= 2 - skoS2**2) & (441*skoS2/160 + 107/64 < skoX*(skoX*(882*skoS2 + 535) + 1880)/320)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(57, 64)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-3, 4)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(441, 160), Symbol('skoS2')), Rational(107, 64)), Mul(Rational(1, 320), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(882), Symbol('skoS2')), Integer(535))), Integer(1880)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_12(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 1001/1024) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -1001/1024) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (567*skoS2/128 - skoSM*(126*skoS2 + 61)/40 + 3181/1280 < skoX*(1280*skoSM + skoX*(5670*skoS2 - 32*skoSM*(126*skoS2 + 61) + 3181) + 6920)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(1001, 1024)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-1001, 1024)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(567, 128), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(3181, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Integer(1280), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(5670), Symbol('skoS2')), Mul(Integer(-1), Integer(32), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(3181))), Integer(6920)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_13(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 1001/1024) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -15/16) & (delta >= 2 - skoS2**2) & (2331*skoS2/640 + 2693/1280 < skoX*(skoX*(4662*skoS2 + 2693) + 7240)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(1001, 1024)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-15, 16)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(2331, 640), Symbol('skoS2')), Rational(2693, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(4662), Symbol('skoS2')), Integer(2693))), Integer(7240)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_14(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 64785/65536) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -64785/65536) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (22743*skoS2/5120 - skoSM*(126*skoS2 + 61)/40 + 25513/10240 < skoX*(10240*skoSM + skoX*(45486*skoS2 - 256*skoSM*(126*skoS2 + 61) + 25513) + 55400)/10240)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(64785, 65536)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-64785, 65536)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(22743, 5120), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(25513, 10240)), Mul(Rational(1, 10240), Symbol('skoX'), Add(Mul(Integer(10240), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(45486), Symbol('skoS2')), Mul(Integer(-1), Integer(256), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(25513))), Integer(55400)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_15(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 64785/65536) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -63/64) & (delta >= 2 - skoS2**2) & (20727*skoS2/5120 + 23561/10240 < skoX*(skoX*(41454*skoS2 + 23561) + 56680)/10240)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(64785, 65536)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-63, 64)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(20727, 5120), Symbol('skoS2')), Rational(23561, 10240)), Mul(Rational(1, 10240), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(41454), Symbol('skoS2')), Integer(23561))), Integer(56680)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_16(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 260585/262144) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -260585/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (45549*skoS2/10240 - skoSM*(126*skoS2 + 61)/40 + 51091/20480 < skoX*(20480*skoSM + skoX*(91098*skoS2 - 512*skoSM*(126*skoS2 + 61) + 51091) + 110840)/20480)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(260585, 262144)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-260585, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(45549, 10240), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(51091, 20480)), Mul(Rational(1, 20480), Symbol('skoX'), Add(Mul(Integer(20480), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(91098), Symbol('skoS2')), Mul(Integer(-1), Integer(512), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(51091))), Integer(110840)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_17(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 260585/262144) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -1015/1024) & (delta >= 2 - skoS2**2) & (8505*skoS2/2048 + 48163/20480 < skoX*(skoX*(85050*skoS2 + 48163) + 112760)/20480)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(260585, 262144)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-1015, 1024)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(8505, 2048), Symbol('skoS2')), Rational(48163, 20480)), Mul(Rational(1, 20480), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(85050), Symbol('skoS2')), Integer(48163))), Integer(112760)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_18(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 260585/262144) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -260585/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (45549*skoS2/10240 - skoSM*(126*skoS2 + 61)/40 + 51091/20480 < skoX*(20480*skoSM + skoX*(91098*skoS2 - 512*skoSM*(126*skoS2 + 61) + 51091) + 110840)/20480)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(260585, 262144)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-260585, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(45549, 10240), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(51091, 20480)), Mul(Rational(1, 20480), Symbol('skoX'), Add(Mul(Integer(20480), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(91098), Symbol('skoS2')), Mul(Integer(-1), Integer(512), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(51091))), Integer(110840)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_19(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 255/256) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -260585/262144) & (delta >= 2 - skoS2**2) & (43533*skoS2/10240 + 49139/20480 < skoX*(skoX*(87066*skoS2 + 49139) + 112120)/20480)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(255, 256)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-260585, 262144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(43533, 10240), Symbol('skoS2')), Rational(49139, 20480)), Mul(Rational(1, 20480), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(87066), Symbol('skoS2')), Integer(49139))), Integer(112120)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_20(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 260585/262144) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -260585/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (45549*skoS2/10240 - skoSM*(126*skoS2 + 61)/40 + 51091/20480 < skoX*(20480*skoSM + skoX*(91098*skoS2 - 512*skoSM*(126*skoS2 + 61) + 51091) + 110840)/20480)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(260585, 262144)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-260585, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(45549, 10240), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(51091, 20480)), Mul(Rational(1, 20480), Symbol('skoX'), Add(Mul(Integer(20480), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(91098), Symbol('skoS2')), Mul(Integer(-1), Integer(512), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(51091))), Integer(110840)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_21(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 260623/262144) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -260585/262144) & (delta >= 2 - skoS2**2) & (10773*skoS2/2560 + 6089/2560 < skoX*(skoX*(10773*skoS2 + 6089) + 14050)/2560)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(260623, 262144)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-260585, 262144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(10773, 2560), Symbol('skoS2')), Rational(6089, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(10773), Symbol('skoS2')), Integer(6089))), Integer(14050)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_22(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 1067448705/1073741824) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -1067448705/1073741824) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (2915199*skoS2/655360 - skoSM*(126*skoS2 + 61)/40 + 3269889/1310720 < skoX*(1310720*skoSM + skoX*(5830398*skoS2 - 32768*skoSM*(126*skoS2 + 61) + 3269889) + 7093800)/1310720)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(1067448705, 1073741824)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-1067448705, 1073741824)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(2915199, 655360), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(3269889, 1310720)), Mul(Rational(1, 1310720), Symbol('skoX'), Add(Mul(Integer(1310720), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(5830398), Symbol('skoS2')), Mul(Integer(-1), Integer(32768), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(3269889))), Integer(7093800)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_23(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 260623/262144) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -1067448705/1073741824) & (delta >= 2 - skoS2**2) & (2757951*skoS2/655360 + 3117633/1310720 < 3*skoX*(skoX*(1838634*skoS2 + 1039211) + 2397880)/1310720)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(260623, 262144)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-1067448705, 1073741824)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(2757951, 655360), Symbol('skoS2')), Rational(3117633, 1310720)), Mul(Rational(3, 1310720), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(1838634), Symbol('skoS2')), Integer(1039211))), Integer(2397880)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_24(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 1045233/1048576) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -1045233/1048576) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (91161*skoS2/20480 - skoSM*(126*skoS2 + 61)/40 + 102247/40960 < skoX*(40960*skoSM + skoX*(182322*skoS2 - 1024*skoSM*(126*skoS2 + 61) + 102247) + 221720)/40960)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(1045233, 1048576)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-1045233, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(91161, 20480), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(102247, 40960)), Mul(Rational(1, 40960), Symbol('skoX'), Add(Mul(Integer(40960), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(182322), Symbol('skoS2')), Mul(Integer(-1), Integer(1024), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(102247))), Integer(221720)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_25(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 1045233/1048576) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -255/256) & (delta >= 2 - skoS2**2) & (87129*skoS2/20480 + 98343/40960 < 63*skoX*(skoX*(2766*skoS2 + 1561) + 3560)/40960)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(1045233, 1048576)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-255, 256)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(87129, 20480), Symbol('skoS2')), Rational(98343, 40960)), Mul(Rational(63, 40960), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(2766), Symbol('skoS2')), Integer(1561))), Integer(3560)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_26(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 1045233/1048576) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -1045233/1048576) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (91161*skoS2/20480 - skoSM*(126*skoS2 + 61)/40 + 102247/40960 < skoX*(40960*skoSM + skoX*(182322*skoS2 - 1024*skoSM*(126*skoS2 + 61) + 102247) + 221720)/40960)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(1045233, 1048576)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-1045233, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(91161, 20480), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(102247, 40960)), Mul(Rational(1, 40960), Symbol('skoX'), Add(Mul(Integer(40960), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(182322), Symbol('skoS2')), Mul(Integer(-1), Integer(1024), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(102247))), Integer(221720)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_27(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 1023/1024) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -1045233/1048576) & (delta >= 2 - skoS2**2) & (17829*skoS2/4096 + 20059/8192 < skoX*(skoX*(35658*skoS2 + 20059) + 44600)/8192)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(1023, 1024)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-1045233, 1048576)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(17829, 4096), Symbol('skoS2')), Rational(20059, 8192)), Mul(Rational(1, 8192), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(35658), Symbol('skoS2')), Integer(20059))), Integer(44600)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_28(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 4186721/4194304) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -4186721/4194304) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (36477*skoS2/8192 - skoSM*(126*skoS2 + 61)/40 + 204559/81920 < skoX*(81920*skoSM + skoX*(364770*skoS2 - 2048*skoSM*(126*skoS2 + 61) + 204559) + 443480)/81920)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(4186721, 4194304)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-4186721, 4194304)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(36477, 8192), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(204559, 81920)), Mul(Rational(1, 81920), Symbol('skoX'), Add(Mul(Integer(81920), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(364770), Symbol('skoS2')), Mul(Integer(-1), Integer(2048), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(204559))), Integer(443480)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_29(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 4186721/4194304) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -4087/4096) & (delta >= 2 - skoS2**2) & (176337*skoS2/40960 + 198703/81920 < skoX*(skoX*(352674*skoS2 + 198703) + 447320)/81920)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(4186721, 4194304)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-4087, 4096)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(176337, 40960), Symbol('skoS2')), Rational(198703, 81920)), Mul(Rational(1, 81920), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(352674), Symbol('skoS2')), Integer(198703))), Integer(447320)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_30(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 16377/16384) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -16377/16384) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (11403*skoS2/2560 - skoSM*(126*skoS2 + 61)/40 + 12789/5120 < skoX*(5120*skoSM + skoX*(22806*skoS2 - 128*skoSM*(126*skoS2 + 61) + 12789) + 27720)/5120)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(16377, 16384)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-16377, 16384)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(11403, 2560), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(12789, 5120)), Mul(Rational(1, 5120), Symbol('skoX'), Add(Mul(Integer(5120), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(22806), Symbol('skoS2')), Mul(Integer(-1), Integer(128), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(12789))), Integer(27720)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_31(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 16377/16384) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -1023/1024) & (delta >= 2 - skoS2**2) & (11151*skoS2/2560 + 2509/1024 < skoX*(skoX*(22302*skoS2 + 12545) + 27880)/5120)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(16377, 16384)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-1023, 1024)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(11151, 2560), Symbol('skoS2')), Rational(2509, 1024)), Mul(Rational(1, 5120), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(22302), Symbol('skoS2')), Integer(12545))), Integer(27880)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_32(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 67103361/67108864) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -67103361/67108864) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (145971*skoS2/32768 - skoSM*(126*skoS2 + 61)/40 + 818561/327680 < skoX*(327680*skoSM + skoX*(1459710*skoS2 - 8192*skoSM*(126*skoS2 + 61) + 818561) + 1774120)/327680)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(67103361, 67108864)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-67103361, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(145971, 32768), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(818561, 327680)), Mul(Rational(1, 327680), Symbol('skoX'), Add(Mul(Integer(327680), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(1459710), Symbol('skoS2')), Mul(Integer(-1), Integer(8192), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(818561))), Integer(1774120)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_33(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 67103361/67108864) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -4095/4096) & (delta >= 2 - skoS2**2) & (721791*skoS2/163840 + 810753/327680 < 3*skoX*(skoX*(481194*skoS2 + 270251) + 593080)/327680)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(67103361, 67108864)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-4095, 4096)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(721791, 163840), Symbol('skoS2')), Rational(810753, 327680)), Mul(Rational(3, 327680), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(481194), Symbol('skoS2')), Integer(270251))), Integer(593080)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_34(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 17178831137/17179869184) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -17178831137/17179869184) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (11677743*skoS2/2621440 - skoSM*(126*skoS2 + 61)/40 + 13097041/5242880 < skoX*(5242880*skoSM + skoX*(23355486*skoS2 - 131072*skoSM*(126*skoS2 + 61) + 13097041) + 28385960)/5242880)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(17178831137, 17179869184)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-17178831137, 17179869184)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(11677743, 2621440), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(13097041, 5242880)), Mul(Rational(1, 5242880), Symbol('skoX'), Add(Mul(Integer(5242880), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(23355486), Symbol('skoS2')), Mul(Integer(-1), Integer(131072), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(13097041))), Integer(28385960)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_35(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 17178831137/17179869184) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -16383/16384) & (delta >= 2 - skoS2**2) & (11613231*skoS2/2621440 + 13034577/5242880 < 3*skoX*(skoX*(7742154*skoS2 + 4344859) + 9475640)/5242880)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(17178831137, 17179869184)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-16383, 16384)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(11613231, 2621440), Symbol('skoS2')), Rational(13034577, 5242880)), Mul(Rational(3, 5242880), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(7742154), Symbol('skoS2')), Integer(4344859))), Integer(9475640)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_36(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 4294800465/4294967296) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -4294800465/4294967296) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (5838903*skoS2/1310720 - skoSM*(126*skoS2 + 61)/40 + 6548553/2621440 < skoX*(2621440*skoSM + skoX*(11677806*skoS2 - 65536*skoSM*(126*skoS2 + 61) + 6548553) + 14193000)/2621440)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(4294800465, 4294967296)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-4294800465, 4294967296)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(5838903, 1310720), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(6548553, 2621440)), Mul(Rational(1, 2621440), Symbol('skoX'), Add(Mul(Integer(2621440), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(11677806), Symbol('skoS2')), Mul(Integer(-1), Integer(65536), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(6548553))), Integer(14193000)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_37(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 65535/65536) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -4294800465/4294967296) & (delta >= 2 - skoS2**2) & (1164555*skoS2/262144 + 6532937/2621440 < skoX*(skoX*(11645550*skoS2 + 6532937) + 14203240)/2621440)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(65535, 65536)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-4294800465, 4294967296)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(1164555, 262144), Symbol('skoS2')), Rational(6532937, 2621440)), Mul(Rational(1, 2621440), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(11645550), Symbol('skoS2')), Integer(6532937))), Integer(14203240)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_38(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 68717548889/68719476736) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -68717548889/68719476736) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (4671135*skoS2/1048576 - skoSM*(126*skoS2 + 61)/40 + 26194277/10485760 < skoX*(10485760*skoSM + skoX*(46711350*skoS2 - 262144*skoSM*(126*skoS2 + 61) + 26194277) + 56772040)/10485760)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(68717548889, 68719476736)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-68717548889, 68719476736)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(4671135, 1048576), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(26194277, 10485760)), Mul(Rational(1, 10485760), Symbol('skoX'), Add(Mul(Integer(10485760), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(46711350), Symbol('skoS2')), Mul(Integer(-1), Integer(262144), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(26194277))), Integer(56772040)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_39(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 68717548889/68719476736) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -262135/262144) & (delta >= 2 - skoS2**2) & (23258907*skoS2/5242880 + 26100581/10485760 < skoX*(skoX*(46517814*skoS2 + 26100581) + 56833480)/10485760)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(68717548889, 68719476736)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-262135, 262144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(23258907, 5242880), Symbol('skoS2')), Rational(26100581, 10485760)), Mul(Rational(1, 10485760), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(46517814), Symbol('skoS2')), Integer(26100581))), Integer(56833480)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_40(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 17179572585/17179869184) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -17179572585/17179869184) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (11677869*skoS2/2621440 - skoSM*(126*skoS2 + 61)/40 + 13097171/5242880 < skoX*(5242880*skoSM + skoX*(23355738*skoS2 - 131072*skoSM*(126*skoS2 + 61) + 13097171) + 28386040)/5242880)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(17179572585, 17179869184)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-17179572585, 17179869184)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(11677869, 2621440), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(13097171, 5242880)), Mul(Rational(1, 5242880), Symbol('skoX'), Add(Mul(Integer(5242880), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(23355738), Symbol('skoS2')), Mul(Integer(-1), Integer(131072), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(13097171))), Integer(28386040)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_41(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 65535/65536) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -17179572585/17179869184) & (delta >= 2 - skoS2**2) & (11645613*skoS2/2621440 + 13065939/5242880 < 171*skoX*(skoX*(136206*skoS2 + 76409) + 166120)/5242880)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(65535, 65536)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-17179572585, 17179869184)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(11645613, 2621440), Symbol('skoS2')), Rational(13065939, 5242880)), Mul(Rational(171, 5242880), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(136206), Symbol('skoS2')), Integer(76409))), Integer(166120)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_42(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 17179572585/17179869184) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -17179572585/17179869184) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (11677869*skoS2/2621440 - skoSM*(126*skoS2 + 61)/40 + 13097171/5242880 < skoX*(5242880*skoSM + skoX*(23355738*skoS2 - 131072*skoSM*(126*skoS2 + 61) + 13097171) + 28386040)/5242880)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(17179572585, 17179869184)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-17179572585, 17179869184)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(11677869, 2621440), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(13097171, 5242880)), Mul(Rational(1, 5242880), Symbol('skoX'), Add(Mul(Integer(5242880), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(23355738), Symbol('skoS2')), Mul(Integer(-1), Integer(131072), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(13097171))), Integer(28386040)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_43(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 65535/65536) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -17179572585/17179869184) & (delta >= 2 - skoS2**2) & (11645613*skoS2/2621440 + 13065939/5242880 < 171*skoX*(skoX*(136206*skoS2 + 76409) + 166120)/5242880)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(65535, 65536)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-17179572585, 17179869184)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(11645613, 2621440), Symbol('skoS2')), Rational(13065939, 5242880)), Mul(Rational(171, 5242880), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(136206), Symbol('skoS2')), Integer(76409))), Integer(166120)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_44(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 17179572585/17179869184) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -17179572585/17179869184) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (11677869*skoS2/2621440 - skoSM*(126*skoS2 + 61)/40 + 13097171/5242880 < skoX*(5242880*skoSM + skoX*(23355738*skoS2 - 131072*skoSM*(126*skoS2 + 61) + 13097171) + 28386040)/5242880)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(17179572585, 17179869184)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-17179572585, 17179869184)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(11677869, 2621440), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(13097171, 5242880)), Mul(Rational(1, 5242880), Symbol('skoX'), Add(Mul(Integer(5242880), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(23355738), Symbol('skoS2')), Mul(Integer(-1), Integer(131072), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(13097171))), Integer(28386040)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_45(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 65535/65536) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -17179572585/17179869184) & (delta >= 2 - skoS2**2) & (11645613*skoS2/2621440 + 13065939/5242880 < 171*skoX*(skoX*(136206*skoS2 + 76409) + 166120)/5242880)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(65535, 65536)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-17179572585, 17179869184)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(11645613, 2621440), Symbol('skoS2')), Rational(13065939, 5242880)), Mul(Rational(171, 5242880), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(136206), Symbol('skoS2')), Integer(76409))), Integer(166120)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_46(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 17179572585/17179869184) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -17179572585/17179869184) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (11677869*skoS2/2621440 - skoSM*(126*skoS2 + 61)/40 + 13097171/5242880 < skoX*(5242880*skoSM + skoX*(23355738*skoS2 - 131072*skoSM*(126*skoS2 + 61) + 13097171) + 28386040)/5242880)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(17179572585, 17179869184)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-17179572585, 17179869184)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(11677869, 2621440), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(13097171, 5242880)), Mul(Rational(1, 5242880), Symbol('skoX'), Add(Mul(Integer(5242880), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(23355738), Symbol('skoS2')), Mul(Integer(-1), Integer(131072), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(13097171))), Integer(28386040)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_47(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 65535/65536) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -17179572585/17179869184) & (delta >= 2 - skoS2**2) & (11645613*skoS2/2621440 + 13065939/5242880 < 171*skoX*(skoX*(136206*skoS2 + 76409) + 166120)/5242880)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(65535, 65536)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-17179572585, 17179869184)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(11645613, 2621440), Symbol('skoS2')), Rational(13065939, 5242880)), Mul(Rational(171, 5242880), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(136206), Symbol('skoS2')), Integer(76409))), Integer(166120)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_48(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 17179572585/17179869184) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -17179572585/17179869184) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (11677869*skoS2/2621440 - skoSM*(126*skoS2 + 61)/40 + 13097171/5242880 < skoX*(5242880*skoSM + skoX*(23355738*skoS2 - 131072*skoSM*(126*skoS2 + 61) + 13097171) + 28386040)/5242880)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(17179572585, 17179869184)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-17179572585, 17179869184)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(11677869, 2621440), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(13097171, 5242880)), Mul(Rational(1, 5242880), Symbol('skoX'), Add(Mul(Integer(5242880), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(23355738), Symbol('skoS2')), Mul(Integer(-1), Integer(131072), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(13097171))), Integer(28386040)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_49(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 65535/65536) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -17179572585/17179869184) & (delta >= 2 - skoS2**2) & (11645613*skoS2/2621440 + 13065939/5242880 < 171*skoX*(skoX*(136206*skoS2 + 76409) + 166120)/5242880)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(65535, 65536)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-17179572585, 17179869184)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(11645613, 2621440), Symbol('skoS2')), Rational(13065939, 5242880)), Mul(Rational(171, 5242880), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(136206), Symbol('skoS2')), Integer(76409))), Integer(166120)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_50(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 17179572585/17179869184) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -17179572585/17179869184) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (11677869*skoS2/2621440 - skoSM*(126*skoS2 + 61)/40 + 13097171/5242880 < skoX*(5242880*skoSM + skoX*(23355738*skoS2 - 131072*skoSM*(126*skoS2 + 61) + 13097171) + 28386040)/5242880)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(17179572585, 17179869184)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-17179572585, 17179869184)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(11677869, 2621440), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(13097171, 5242880)), Mul(Rational(1, 5242880), Symbol('skoX'), Add(Mul(Integer(5242880), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(23355738), Symbol('skoS2')), Mul(Integer(-1), Integer(131072), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(13097171))), Integer(28386040)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_51(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 65535/65536) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -17179572585/17179869184) & (delta >= 2 - skoS2**2) & (11645613*skoS2/2621440 + 13065939/5242880 < 171*skoX*(skoX*(136206*skoS2 + 76409) + 166120)/5242880)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(65535, 65536)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-17179572585, 17179869184)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(11645613, 2621440), Symbol('skoS2')), Rational(13065939, 5242880)), Mul(Rational(171, 5242880), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(136206), Symbol('skoS2')), Integer(76409))), Integer(166120)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_52(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 17179572585/17179869184) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -17179572585/17179869184) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (11677869*skoS2/2621440 - skoSM*(126*skoS2 + 61)/40 + 13097171/5242880 < skoX*(5242880*skoSM + skoX*(23355738*skoS2 - 131072*skoSM*(126*skoS2 + 61) + 13097171) + 28386040)/5242880)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(17179572585, 17179869184)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-17179572585, 17179869184)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(11677869, 2621440), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(13097171, 5242880)), Mul(Rational(1, 5242880), Symbol('skoX'), Add(Mul(Integer(5242880), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(23355738), Symbol('skoS2')), Mul(Integer(-1), Integer(131072), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(13097171))), Integer(28386040)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_53(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 65535/65536) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -17179572585/17179869184) & (delta >= 2 - skoS2**2) & (11645613*skoS2/2621440 + 13065939/5242880 < 171*skoX*(skoX*(136206*skoS2 + 76409) + 166120)/5242880)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(65535, 65536)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-17179572585, 17179869184)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(11645613, 2621440), Symbol('skoS2')), Rational(13065939, 5242880)), Mul(Rational(171, 5242880), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(136206), Symbol('skoS2')), Integer(76409))), Integer(166120)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_54(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 17179572585/17179869184) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -17179572585/17179869184) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (11677869*skoS2/2621440 - skoSM*(126*skoS2 + 61)/40 + 13097171/5242880 < skoX*(5242880*skoSM + skoX*(23355738*skoS2 - 131072*skoSM*(126*skoS2 + 61) + 13097171) + 28386040)/5242880)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(17179572585, 17179869184)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-17179572585, 17179869184)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(11677869, 2621440), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(13097171, 5242880)), Mul(Rational(1, 5242880), Symbol('skoX'), Add(Mul(Integer(5242880), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(23355738), Symbol('skoS2')), Mul(Integer(-1), Integer(131072), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(13097171))), Integer(28386040)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_55(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 65535/65536) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -17179572585/17179869184) & (delta >= 2 - skoS2**2) & (11645613*skoS2/2621440 + 13065939/5242880 < 171*skoX*(skoX*(136206*skoS2 + 76409) + 166120)/5242880)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(65535, 65536)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-17179572585, 17179869184)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(11645613, 2621440), Symbol('skoS2')), Rational(13065939, 5242880)), Mul(Rational(171, 5242880), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(136206), Symbol('skoS2')), Integer(76409))), Integer(166120)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_56(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 17179572585/17179869184) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -17179572585/17179869184) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (11677869*skoS2/2621440 - skoSM*(126*skoS2 + 61)/40 + 13097171/5242880 < skoX*(5242880*skoSM + skoX*(23355738*skoS2 - 131072*skoSM*(126*skoS2 + 61) + 13097171) + 28386040)/5242880)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(17179572585, 17179869184)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-17179572585, 17179869184)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(11677869, 2621440), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(13097171, 5242880)), Mul(Rational(1, 5242880), Symbol('skoX'), Add(Mul(Integer(5242880), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(23355738), Symbol('skoS2')), Mul(Integer(-1), Integer(131072), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(13097171))), Integer(28386040)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_57(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 65535/65536) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -17179572585/17179869184) & (delta >= 2 - skoS2**2) & (11645613*skoS2/2621440 + 13065939/5242880 < 171*skoX*(skoX*(136206*skoS2 + 76409) + 166120)/5242880)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(65535, 65536)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-17179572585, 17179869184)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(11645613, 2621440), Symbol('skoS2')), Rational(13065939, 5242880)), Mul(Rational(171, 5242880), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(136206), Symbol('skoS2')), Integer(76409))), Integer(166120)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_58(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 17179572585/17179869184) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -17179572585/17179869184) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (11677869*skoS2/2621440 - skoSM*(126*skoS2 + 61)/40 + 13097171/5242880 < skoX*(5242880*skoSM + skoX*(23355738*skoS2 - 131072*skoSM*(126*skoS2 + 61) + 13097171) + 28386040)/5242880)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(17179572585, 17179869184)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-17179572585, 17179869184)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(11677869, 2621440), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(13097171, 5242880)), Mul(Rational(1, 5242880), Symbol('skoX'), Add(Mul(Integer(5242880), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(23355738), Symbol('skoS2')), Mul(Integer(-1), Integer(131072), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(13097171))), Integer(28386040)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_59(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 65535/65536) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -17179572585/17179869184) & (delta >= 2 - skoS2**2) & (11645613*skoS2/2621440 + 13065939/5242880 < 171*skoX*(skoX*(136206*skoS2 + 76409) + 166120)/5242880)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(65535, 65536)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-17179572585, 17179869184)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(11645613, 2621440), Symbol('skoS2')), Rational(13065939, 5242880)), Mul(Rational(171, 5242880), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(136206), Symbol('skoS2')), Integer(76409))), Integer(166120)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_60(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 17179572585/17179869184) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -17179572585/17179869184) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (11677869*skoS2/2621440 - skoSM*(126*skoS2 + 61)/40 + 13097171/5242880 < skoX*(5242880*skoSM + skoX*(23355738*skoS2 - 131072*skoSM*(126*skoS2 + 61) + 13097171) + 28386040)/5242880)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(17179572585, 17179869184)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-17179572585, 17179869184)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(11677869, 2621440), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(13097171, 5242880)), Mul(Rational(1, 5242880), Symbol('skoX'), Add(Mul(Integer(5242880), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(23355738), Symbol('skoS2')), Mul(Integer(-1), Integer(131072), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(13097171))), Integer(28386040)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_61(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 65535/65536) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -17179572585/17179869184) & (delta >= 2 - skoS2**2) & (11645613*skoS2/2621440 + 13065939/5242880 < 171*skoX*(skoX*(136206*skoS2 + 76409) + 166120)/5242880)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(65535, 65536)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-17179572585, 17179869184)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(11645613, 2621440), Symbol('skoS2')), Rational(13065939, 5242880)), Mul(Rational(171, 5242880), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(136206), Symbol('skoS2')), Integer(76409))), Integer(166120)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_62(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 17179572585/17179869184) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -17179572585/17179869184) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (11677869*skoS2/2621440 - skoSM*(126*skoS2 + 61)/40 + 13097171/5242880 < skoX*(5242880*skoSM + skoX*(23355738*skoS2 - 131072*skoSM*(126*skoS2 + 61) + 13097171) + 28386040)/5242880)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(17179572585, 17179869184)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-17179572585, 17179869184)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(11677869, 2621440), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(13097171, 5242880)), Mul(Rational(1, 5242880), Symbol('skoX'), Add(Mul(Integer(5242880), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(23355738), Symbol('skoS2')), Mul(Integer(-1), Integer(131072), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(13097171))), Integer(28386040)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_63(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 65535/65536) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -17179572585/17179869184) & (delta >= 2 - skoS2**2) & (11645613*skoS2/2621440 + 13065939/5242880 < 171*skoX*(skoX*(136206*skoS2 + 76409) + 166120)/5242880)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(65535, 65536)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-17179572585, 17179869184)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(11645613, 2621440), Symbol('skoS2')), Rational(13065939, 5242880)), Mul(Rational(171, 5242880), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(136206), Symbol('skoS2')), Integer(76409))), Integer(166120)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_64(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 17179572585/17179869184) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -17179572585/17179869184) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (11677869*skoS2/2621440 - skoSM*(126*skoS2 + 61)/40 + 13097171/5242880 < skoX*(5242880*skoSM + skoX*(23355738*skoS2 - 131072*skoSM*(126*skoS2 + 61) + 13097171) + 28386040)/5242880)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(17179572585, 17179869184)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-17179572585, 17179869184)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(11677869, 2621440), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(13097171, 5242880)), Mul(Rational(1, 5242880), Symbol('skoX'), Add(Mul(Integer(5242880), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(23355738), Symbol('skoS2')), Mul(Integer(-1), Integer(131072), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(13097171))), Integer(28386040)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_65(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 65535/65536) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -17179572585/17179869184) & (delta >= 2 - skoS2**2) & (11645613*skoS2/2621440 + 13065939/5242880 < 171*skoX*(skoX*(136206*skoS2 + 76409) + 166120)/5242880)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(65535, 65536)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-17179572585, 17179869184)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(11645613, 2621440), Symbol('skoS2')), Rational(13065939, 5242880)), Mul(Rational(171, 5242880), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(136206), Symbol('skoS2')), Integer(76409))), Integer(166120)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_66(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 17179572585/17179869184) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -17179572585/17179869184) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (11677869*skoS2/2621440 - skoSM*(126*skoS2 + 61)/40 + 13097171/5242880 < skoX*(5242880*skoSM + skoX*(23355738*skoS2 - 131072*skoSM*(126*skoS2 + 61) + 13097171) + 28386040)/5242880)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(17179572585, 17179869184)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-17179572585, 17179869184)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(11677869, 2621440), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(13097171, 5242880)), Mul(Rational(1, 5242880), Symbol('skoX'), Add(Mul(Integer(5242880), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(23355738), Symbol('skoS2')), Mul(Integer(-1), Integer(131072), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(13097171))), Integer(28386040)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_67(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 65535/65536) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -17179572585/17179869184) & (delta >= 2 - skoS2**2) & (11645613*skoS2/2621440 + 13065939/5242880 < 171*skoX*(skoX*(136206*skoS2 + 76409) + 166120)/5242880)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(65535, 65536)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-17179572585, 17179869184)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(11645613, 2621440), Symbol('skoS2')), Rational(13065939, 5242880)), Mul(Rational(171, 5242880), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(136206), Symbol('skoS2')), Integer(76409))), Integer(166120)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_68(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 17179572585/17179869184) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -17179572585/17179869184) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (11677869*skoS2/2621440 - skoSM*(126*skoS2 + 61)/40 + 13097171/5242880 < skoX*(5242880*skoSM + skoX*(23355738*skoS2 - 131072*skoSM*(126*skoS2 + 61) + 13097171) + 28386040)/5242880)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(17179572585, 17179869184)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-17179572585, 17179869184)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(11677869, 2621440), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(13097171, 5242880)), Mul(Rational(1, 5242880), Symbol('skoX'), Add(Mul(Integer(5242880), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(23355738), Symbol('skoS2')), Mul(Integer(-1), Integer(131072), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(13097171))), Integer(28386040)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_69(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 65535/65536) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -17179572585/17179869184) & (delta >= 2 - skoS2**2) & (11645613*skoS2/2621440 + 13065939/5242880 < 171*skoX*(skoX*(136206*skoS2 + 76409) + 166120)/5242880)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(65535, 65536)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-17179572585, 17179869184)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(11645613, 2621440), Symbol('skoS2')), Rational(13065939, 5242880)), Mul(Rational(171, 5242880), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(136206), Symbol('skoS2')), Integer(76409))), Integer(166120)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_70(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 17179572585/17179869184) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -17179572585/17179869184) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (11677869*skoS2/2621440 - skoSM*(126*skoS2 + 61)/40 + 13097171/5242880 < skoX*(5242880*skoSM + skoX*(23355738*skoS2 - 131072*skoSM*(126*skoS2 + 61) + 13097171) + 28386040)/5242880)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(17179572585, 17179869184)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-17179572585, 17179869184)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(11677869, 2621440), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(13097171, 5242880)), Mul(Rational(1, 5242880), Symbol('skoX'), Add(Mul(Integer(5242880), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(23355738), Symbol('skoS2')), Mul(Integer(-1), Integer(131072), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(13097171))), Integer(28386040)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_71(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 16776927/16777216) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -17179572585/17179869184) & (delta >= 2 - skoS2**2) & (11643597*skoS2/2621440 + 13063987/5242880 < skoX*(skoX*(23287194*skoS2 + 13063987) + 28407800)/5242880)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(16776927, 16777216)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-17179572585, 17179869184)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(11643597, 2621440), Symbol('skoS2')), Rational(13063987, 5242880)), Mul(Rational(1, 5242880), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(23287194), Symbol('skoS2')), Integer(13063987))), Integer(28407800)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_72(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 17179572585/17179869184) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -17179572585/17179869184) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (11677869*skoS2/2621440 - skoSM*(126*skoS2 + 61)/40 + 13097171/5242880 < skoX*(5242880*skoSM + skoX*(23355738*skoS2 - 131072*skoSM*(126*skoS2 + 61) + 13097171) + 28386040)/5242880)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(17179572585, 17179869184)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-17179572585, 17179869184)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(11677869, 2621440), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(13097171, 5242880)), Mul(Rational(1, 5242880), Symbol('skoX'), Add(Mul(Integer(5242880), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(23355738), Symbol('skoS2')), Mul(Integer(-1), Integer(131072), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(13097171))), Integer(28386040)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_73(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 68718290815/68719476736) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -17179572585/17179869184) & (delta >= 2 - skoS2**2) & (23287131*skoS2/5242880 + 26127913/10485760 < 7*skoX*(skoX*(6653466*skoS2 + 3732559) + 8116520)/10485760)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(68718290815, 68719476736)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-17179572585, 17179869184)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(23287131, 5242880), Symbol('skoS2')), Rational(26127913, 10485760)), Mul(Rational(7, 10485760), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(6653466), Symbol('skoS2')), Integer(3732559))), Integer(8116520)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_74(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 17179572585/17179869184) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -17179572585/17179869184) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (11677869*skoS2/2621440 - skoSM*(126*skoS2 + 61)/40 + 13097171/5242880 < skoX*(5242880*skoSM + skoX*(23355738*skoS2 - 131072*skoSM*(126*skoS2 + 61) + 13097171) + 28386040)/5242880)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(17179572585, 17179869184)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-17179572585, 17179869184)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(11677869, 2621440), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(13097171, 5242880)), Mul(Rational(1, 5242880), Symbol('skoX'), Add(Mul(Integer(5242880), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(23355738), Symbol('skoS2')), Mul(Integer(-1), Integer(131072), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(13097171))), Integer(28386040)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_75(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 17591882344087/17592186044416) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -17179572585/17179869184) & (delta >= 2 - skoS2**2) & (372593907*skoS2/83886080 + 83609285/33554432 < skoX*(skoX*(745187814*skoS2 + 418046425) + 909050360)/167772160)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(17591882344087, 17592186044416)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-17179572585, 17179869184)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(372593907, 83886080), Symbol('skoS2')), Rational(83609285, 33554432)), Mul(Rational(1, 167772160), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(745187814), Symbol('skoS2')), Integer(418046425))), Integer(909050360)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_76(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 17179572585/17179869184) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -17179572585/17179869184) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (11677869*skoS2/2621440 - skoSM*(126*skoS2 + 61)/40 + 13097171/5242880 < skoX*(5242880*skoSM + skoX*(23355738*skoS2 - 131072*skoSM*(126*skoS2 + 61) + 13097171) + 28386040)/5242880)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(17179572585, 17179869184)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-17179572585, 17179869184)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(11677869, 2621440), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(13097171, 5242880)), Mul(Rational(1, 5242880), Symbol('skoX'), Add(Mul(Integer(5242880), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(23355738), Symbol('skoS2')), Mul(Integer(-1), Integer(131072), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(13097171))), Integer(28386040)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_77(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 281470117365975/281474976710656) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -17179572585/17179869184) & (delta >= 2 - skoS2**2) & (298075113*skoS2/67108864 + 1672185639/671088640 < 3*skoX*(skoX*(993583710*skoS2 + 557395213) + 1212067160)/671088640)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(281470117365975, 281474976710656)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-17179572585, 17179869184)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(298075113, 67108864), Symbol('skoS2')), Rational(1672185639, 671088640)), Mul(Rational(3, 671088640), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(993583710), Symbol('skoS2')), Integer(557395213))), Integer(1212067160)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_78(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 1180571239075248865305/1180591620717411303424) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -1180571239075248865305/1180591620717411303424) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (3061283291451*skoS2/687194767360 - skoSM*(126*skoS2 + 61)/40 + 3433344794949/1374389534720 < skoX*(1374389534720*skoSM + skoX*(6122566582902*skoS2 - 34359738368*skoSM*(126*skoS2 + 61) + 3433344794949) + 7441230069960)/1374389534720)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(1180571239075248865305, 1180591620717411303424)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-1180571239075248865305, 1180591620717411303424)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(3061283291451, 687194767360), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(3433344794949, 1374389534720)), Mul(Rational(1, 1374389534720), Symbol('skoX'), Add(Mul(Integer(1374389534720), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(6122566582902), Symbol('skoS2')), Mul(Integer(-1), Integer(34359738368), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(3433344794949))), Integer(7441230069960)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_79(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 1180571239075248865305/1180591620717411303424) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -4503521877297927/4503599627370496) & (delta >= 2 - skoS2**2) & (3052289125179*skoS2/687194767360 + 684927231553/274877906944 < skoX*(skoX*(6104578250358*skoS2 + 3424636157765) + 7446940651720)/1374389534720)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(1180571239075248865305, 1180591620717411303424)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-4503521877297927, 4503599627370496)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(3052289125179, 687194767360), Symbol('skoS2')), Rational(684927231553, 274877906944)), Mul(Rational(1, 1374389534720), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(6104578250358), Symbol('skoS2')), Integer(3424636157765))), Integer(7446940651720)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_80(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 1099495611249/1099511627776) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -1099495611249/1099511627776) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (18684603*skoS2/4194304 - skoSM*(126*skoS2 + 61)/40 + 104777433/41943040 < skoX*(41943040*skoSM + skoX*(186846030*skoS2 - 1048576*skoSM*(126*skoS2 + 61) + 104777433) + 227088360)/41943040)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(1099495611249, 1099511627776)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-1099495611249, 1099511627776)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(18684603, 4194304), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(104777433, 41943040)), Mul(Rational(1, 41943040), Symbol('skoX'), Add(Mul(Integer(41943040), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(186846030), Symbol('skoS2')), Mul(Integer(-1), Integer(1048576), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(104777433))), Integer(227088360)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_81(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 1099495611249/1099511627776) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -65535/65536) & (delta >= 2 - skoS2**2) & (93164967*skoS2/20971520 + 104527577/41943040 < 7*skoX*(skoX*(26618562*skoS2 + 14932511) + 32464600)/41943040)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(1099495611249, 1099511627776)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-65535, 65536)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(93164967, 20971520), Symbol('skoS2')), Rational(104527577, 41943040)), Mul(Rational(7, 41943040), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(26618562), Symbol('skoS2')), Integer(14932511))), Integer(32464600)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_82(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 68719031793/68719476736) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -68719031793/68719476736) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (23355801*skoS2/5242880 - skoSM*(126*skoS2 + 61)/40 + 26194407/10485760 < skoX*(10485760*skoSM + skoX*(46711602*skoS2 - 262144*skoSM*(126*skoS2 + 61) + 26194407) + 56772120)/10485760)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(68719031793, 68719476736)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-68719031793, 68719476736)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(23355801, 5242880), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(26194407, 10485760)), Mul(Rational(1, 10485760), Symbol('skoX'), Add(Mul(Integer(10485760), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(46711602), Symbol('skoS2')), Mul(Integer(-1), Integer(262144), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(26194407))), Integer(56772120)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_83(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 262143/262144) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -68719031793/68719476736) & (delta >= 2 - skoS2**2) & (4664709*skoS2/1048576 + 5232635/2097152 < skoX*(skoX*(9329418*skoS2 + 5232635) + 11358520)/2097152)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(262143, 262144)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-68719031793, 68719476736)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(4664709, 1048576), Symbol('skoS2')), Rational(5232635, 2097152)), Mul(Rational(1, 2097152), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(9329418), Symbol('skoS2')), Integer(5232635))), Integer(11358520)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_84(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 5192277051494199101947468377480345/5192296858534827628530496329220096) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -5192277051494199101947468377480345/5192296858534827628530496329220096) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (6419997963310051323*skoS2/1441151880758558720 - skoSM*(126*skoS2 + 61)/40 + 7200268174766174853/2882303761517117440 < skoX*(2882303761517117440*skoSM + skoX*(12839995926620102646*skoS2 - 72057594037927936*skoSM*(126*skoS2 + 61) + 7200268174766174853) + 15605404229122470600)/2882303761517117440)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(5192277051494199101947468377480345, 5192296858534827628530496329220096)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-5192277051494199101947468377480345, 5192296858534827628530496329220096)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(6419997963310051323, 1441151880758558720), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(7200268174766174853, 2882303761517117440)), Mul(Rational(1, 2882303761517117440), Symbol('skoX'), Add(Mul(Integer(2882303761517117440), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(12839995926620102646), Symbol('skoS2')), Mul(Integer(-1), Integer(72057594037927936), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(7200268174766174853))), Integer(15605404229122470600)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_85(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 5192277051494199101947468377480345/5192296858534827628530496329220096) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -262143/262144) & (delta >= 2 - skoS2**2) & (6411131501543665659*skoS2/1441151880758558720 + 1438336637595299969/576460752303423488 < skoX*(skoX*(12822263003087331318*skoS2 + 7191683187976499845) + 15611033728656683720)/2882303761517117440)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(5192277051494199101947468377480345, 5192296858534827628530496329220096)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-262143, 262144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(6411131501543665659, 1441151880758558720), Symbol('skoS2')), Rational(1438336637595299969, 576460752303423488)), Mul(Rational(1, 2882303761517117440), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(12822263003087331318), Symbol('skoS2')), Integer(7191683187976499845))), Integer(15611033728656683720)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_86(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 274877610081/274877906944) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -274877610081/274877906944) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (9342333*skoS2/2097152 - skoSM*(126*skoS2 + 61)/40 + 52388879/20971520 < skoX*(20971520*skoSM + skoX*(93423330*skoS2 - 524288*skoSM*(126*skoS2 + 61) + 52388879) + 113544280)/20971520)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(274877610081, 274877906944)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-274877610081, 274877906944)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(9342333, 2097152), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(52388879, 20971520)), Mul(Rational(1, 20971520), Symbol('skoX'), Add(Mul(Integer(20971520), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(93423330), Symbol('skoS2')), Mul(Integer(-1), Integer(524288), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(52388879))), Integer(113544280)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_87(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 1048575/1048576) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -274877610081/274877906944) & (delta >= 2 - skoS2**2) & (46679409*skoS2/10485760 + 52357647/20971520 < 3*skoX*(skoX*(31119606*skoS2 + 17452549) + 37854920)/20971520)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(1048575, 1048576)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-274877610081, 274877906944)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(46679409, 10485760), Symbol('skoS2')), Rational(52357647, 20971520)), Mul(Rational(3, 20971520), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(31119606), Symbol('skoS2')), Integer(17452549))), Integer(37854920)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_88(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 5192291906774670504227799592646129/5192296858534827628530496329220096) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -5192291906774670504227799592646129/5192296858534827628530496329220096) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (1284000511051508859*skoS2/288230376151711744 - skoSM*(126*skoS2 + 61)/40 + 7200272912489778713/2882303761517117440 < skoX*(2882303761517117440*skoSM + skoX*(12840005110515088590*skoS2 - 72057594037927936*skoSM*(126*skoS2 + 61) + 7200272912489778713) + 15605407144644688360)/2882303761517117440)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(5192291906774670504227799592646129, 5192296858534827628530496329220096)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-5192291906774670504227799592646129, 5192296858534827628530496329220096)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(1284000511051508859, 288230376151711744), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(7200272912489778713, 2882303761517117440)), Mul(Rational(1, 2882303761517117440), Symbol('skoX'), Add(Mul(Integer(2882303761517117440), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(12840005110515088590), Symbol('skoS2')), Mul(Integer(-1), Integer(72057594037927936), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(7200272912489778713))), Integer(15605407144644688360)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_89(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 5192291906774670504227799592646129/5192296858534827628530496329220096) & (skoX**2 <= 2) & (delta >= skoS2**2 - 2) & (delta - skoX >= -1048575/1048576) & (delta >= 2 - skoS2**2) & (6415569324374351463*skoS2/1441151880758558720 + 7195980419094941209/2882303761517117440 < skoX*(skoX*(12831138648748702926*skoS2 + 7195980419094941209) + 15608221894411794920)/2882303761517117440)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(5192291906774670504227799592646129, 5192296858534827628530496329220096)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-1048575, 1048576)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(6415569324374351463, 1441151880758558720), Symbol('skoS2')), Rational(7195980419094941209, 2882303761517117440)), Mul(Rational(1, 2882303761517117440), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(12831138648748702926), Symbol('skoS2')), Integer(7195980419094941209))), Integer(15608221894411794920)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(delta:sympy.Rational, skoX:sympy.Rational, skoS2:sympy.Rational, skoSP:sympy.Rational, skoSM:sympy.Rational):
	# (0 <= delta) & (1 > skoX) & (skoS2 > 0) & (skoSM > 0) & (skoSP > 0) & (skoX > 0) & (skoX**2 <= 2) & (skoS2**2 - 2 <= delta) & (skoSM**2 + skoX - 1 <= delta) & (2 - skoS2**2 <= delta) & (-skoSP**2 + skoX + 1 <= delta) & (skoSP**2 - skoX - 1 <= delta) & (-skoSM**2 - skoX + 1 <= delta) & (skoX*(skoSM + skoSP + skoX*(skoSM*(-63*skoS2/20 - 61/40) + skoSP*(63*skoS2/20 + 13/8) + 1/5) + 4) > skoSM*(-63*skoS2/20 - 61/40) + skoSP*(63*skoS2/20 + 13/8) + 1/5)

	post_cond =  And(LessThan(Integer(0), Symbol('delta')), StrictGreaterThan(Integer(1), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoSP'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), LessThan(Pow(Symbol('skoX'), Integer(2)), Integer(2)), LessThan(Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Symbol('delta')), LessThan(Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1)), Symbol('delta')), LessThan(Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Symbol('delta')), LessThan(Add(Mul(Integer(-1), Pow(Symbol('skoSP'), Integer(2))), Symbol('skoX'), Integer(1)), Symbol('delta')), LessThan(Add(Pow(Symbol('skoSP'), Integer(2)), Mul(Integer(-1), Symbol('skoX')), Integer(-1)), Symbol('delta')), LessThan(Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)), Symbol('delta')), StrictGreaterThan(Mul(Symbol('skoX'), Add(Symbol('skoSM'), Symbol('skoSP'), Mul(Symbol('skoX'), Add(Mul(Symbol('skoSM'), Add(Mul(Integer(-1), Rational(63, 20), Symbol('skoS2')), Rational(-61, 40))), Mul(Symbol('skoSP'), Add(Mul(Rational(63, 20), Symbol('skoS2')), Rational(13, 8))), Rational(1, 5))), Integer(4))), Add(Mul(Symbol('skoSM'), Add(Mul(Integer(-1), Rational(63, 20), Symbol('skoS2')), Rational(-61, 40))), Mul(Symbol('skoSP'), Add(Mul(Rational(63, 20), Symbol('skoS2')), Rational(13, 8))), Rational(1, 5))))

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
		print('delta = 27/256')
		print('skoX = 3/8')
		print('skoS2 = 45/32')
		print('skoSM = 3/4')
		print('skoSP = 577/512')
		exit(0)
	
	
	if pre_condition_5(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_5 SAT")
		print('delta = 27/256')
		print('skoX = 3/8')
		print('skoS2 = 45/32')
		print('skoSM = 3/4')
		print('skoSP = 577/512')
		exit(0)
	
	
	if pre_condition_6(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_6 SAT")
		print('delta = 3/64')
		print('skoX = 3/8')
		print('skoS2 = 45/32')
		print('skoSM = 13/16')
		print('skoSP = 19/16')
		exit(0)
	
	
	if pre_condition_7(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_7 SAT")
		print('delta = 3/64')
		print('skoX = 3/8')
		print('skoS2 = 45/32')
		print('skoSM = 13/16')
		print('skoSP = 19/16')
		exit(0)
	
	
	if pre_condition_8(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_8 SAT")
		print('delta = 5/64')
		print('skoX = 1/2')
		print('skoS2 = 23/16')
		print('skoSM = 3/4')
		print('skoSP = 5/4')
		exit(0)
	
	
	if pre_condition_9(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_9 SAT")
		print('delta = 5/64')
		print('skoX = 1/2')
		print('skoS2 = 23/16')
		print('skoSM = 3/4')
		print('skoSP = 5/4')
		exit(0)
	
	
	if pre_condition_10(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_10 SAT")
		print('delta = 5/32')
		print('skoX = 3/4')
		print('skoS2 = 11/8')
		print('skoSM = 1/2')
		print('skoSP = 11/8')
		exit(0)
	
	
	if pre_condition_11(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_11 SAT")
		print('delta = 5/32')
		print('skoX = 3/4')
		print('skoS2 = 11/8')
		print('skoSM = 1/2')
		print('skoSP = 11/8')
		exit(0)
	
	
	if pre_condition_12(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_12 SAT")
		print('delta = 11/256')
		print('skoX = 15/16')
		print('skoS2 = 45/32')
		print('skoSM = 1/4')
		print('skoSP = 45/32')
		exit(0)
	
	
	if pre_condition_13(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_13 SAT")
		print('delta = 11/256')
		print('skoX = 15/16')
		print('skoS2 = 45/32')
		print('skoSM = 1/4')
		print('skoSP = 45/32')
		exit(0)
	
	
	if pre_condition_14(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_14 SAT")
		print('delta = 3/512')
		print('skoX = 63/64')
		print('skoS2 = 181/128')
		print('skoSM = 1/8')
		print('skoSP = 361/256')
		exit(0)
	
	
	if pre_condition_15(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_15 SAT")
		print('delta = 3/512')
		print('skoX = 63/64')
		print('skoS2 = 181/128')
		print('skoSM = 1/8')
		print('skoSP = 361/256')
		exit(0)
	
	
	if pre_condition_16(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_16 SAT")
		print('delta = 1/512')
		print('skoX = 127/128')
		print('skoS2 = 181/128')
		print('skoSM = 3/32')
		print('skoSP = 723/512')
		exit(0)
	
	
	if pre_condition_17(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_17 SAT")
		print('delta = 1/512')
		print('skoX = 127/128')
		print('skoS2 = 181/128')
		print('skoSM = 3/32')
		print('skoSP = 723/512')
		exit(0)
	
	
	if pre_condition_18(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_18 SAT")
		print('delta = 147059680215041/72057594037927936')
		print('skoX = 255/256')
		print('skoS2 = 181/128')
		print('skoSM = 1/16')
		print('skoSP = 723/512')
		exit(0)
	
	
	if pre_condition_19(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_19 SAT")
		print('delta = 147059680215041/72057594037927936')
		print('skoX = 255/256')
		print('skoS2 = 181/128')
		print('skoSM = 1/16')
		print('skoSP = 723/512')
		exit(0)
	
	
	if pre_condition_20(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_20 SAT")
		print('delta = 6322191859713/72057594037927936')
		print('skoX = 509/512')
		print('skoS2 = 11585/8192')
		print('skoSM = 39/512')
		print('skoSP = 723/512')
		exit(0)
	
	
	if pre_condition_21(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_21 SAT")
		print('delta = 6322191859713/72057594037927936')
		print('skoX = 509/512')
		print('skoS2 = 11585/8192')
		print('skoSM = 39/512')
		print('skoSP = 723/512')
		exit(0)
	
	
	if pre_condition_22(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_22 SAT")
		print('delta = 4123168604161/72057594037927936')
		print('skoX = 509/512')
		print('skoS2 = 46341/32768')
		print('skoSM = 39/512')
		print('skoSP = 46273/32768')
		exit(0)
	
	
	if pre_condition_23(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_23 SAT")
		print('delta = 4123168604161/72057594037927936')
		print('skoX = 509/512')
		print('skoS2 = 46341/32768')
		print('skoSM = 39/512')
		print('skoSP = 46273/32768')
		exit(0)
	
	
	if pre_condition_24(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_24 SAT")
		print('delta = 1/512')
		print('skoX = 255/256')
		print('skoS2 = 181/128')
		print('skoSM = 1/16')
		print('skoSP = 1447/1024')
		exit(0)
	
	
	if pre_condition_25(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_25 SAT")
		print('delta = 1/512')
		print('skoX = 255/256')
		print('skoS2 = 181/128')
		print('skoSM = 1/16')
		print('skoSP = 1447/1024')
		exit(0)
	
	
	if pre_condition_26(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_26 SAT")
		print('delta = 355966889492481/288230376151711744')
		print('skoX = 511/512')
		print('skoS2 = 181/128')
		print('skoSM = 1/32')
		print('skoSP = 1447/1024')
		exit(0)
	
	
	if pre_condition_27(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_27 SAT")
		print('delta = 355966889492481/288230376151711744')
		print('skoX = 511/512')
		print('skoS2 = 181/128')
		print('skoSM = 1/32')
		print('skoSP = 1447/1024')
		exit(0)
	
	
	if pre_condition_28(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_28 SAT")
		print('delta = 1/2048')
		print('skoX = 511/512')
		print('skoS2 = 181/128')
		print('skoSM = 3/64')
		print('skoSP = 2895/2048')
		exit(0)
	
	
	if pre_condition_29(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_29 SAT")
		print('delta = 1/2048')
		print('skoX = 511/512')
		print('skoS2 = 181/128')
		print('skoSM = 3/64')
		print('skoSP = 2895/2048')
		exit(0)
	
	
	if pre_condition_30(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_30 SAT")
		print('delta = 3/4096')
		print('skoX = 1023/1024')
		print('skoS2 = 181/128')
		print('skoSM = 1/32')
		print('skoSP = 181/128')
		exit(0)
	
	
	if pre_condition_31(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_31 SAT")
		print('delta = 3/4096')
		print('skoX = 1023/1024')
		print('skoS2 = 181/128')
		print('skoSM = 1/32')
		print('skoSP = 181/128')
		exit(0)
	
	
	if pre_condition_32(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_32 SAT")
		print('delta = 11/65536')
		print('skoX = 4095/4096')
		print('skoS2 = 11585/8192')
		print('skoSM = 1/64')
		print('skoSP = 11585/8192')
		exit(0)
	
	
	if pre_condition_33(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_33 SAT")
		print('delta = 11/65536')
		print('skoX = 4095/4096')
		print('skoS2 = 11585/8192')
		print('skoSM = 1/64')
		print('skoSP = 11585/8192')
		exit(0)
	
	
	if pre_condition_34(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_34 SAT")
		print('delta = 1/65536')
		print('skoX = 16383/16384')
		print('skoS2 = 46341/32768')
		print('skoSM = 1/128')
		print('skoSP = 185361/131072')
		exit(0)
	
	
	if pre_condition_35(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_35 SAT")
		print('delta = 1/65536')
		print('skoX = 16383/16384')
		print('skoS2 = 46341/32768')
		print('skoSM = 1/128')
		print('skoSP = 185361/131072')
		exit(0)
	
	
	if pre_condition_36(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_36 SAT")
		print('delta = 1/65536')
		print('skoX = 32767/32768')
		print('skoS2 = 46341/32768')
		print('skoSM = 1/256')
		print('skoSP = 92681/65536')
		exit(0)
	
	
	if pre_condition_37(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_37 SAT")
		print('delta = 1/65536')
		print('skoX = 32767/32768')
		print('skoS2 = 46341/32768')
		print('skoSM = 1/256')
		print('skoSP = 92681/65536')
		exit(0)
	
	
	if pre_condition_38(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_38 SAT")
		print('delta = 1/131072')
		print('skoX = 32767/32768')
		print('skoS2 = 46341/32768')
		print('skoSM = 3/512')
		print('skoSP = 370725/262144')
		exit(0)
	
	
	if pre_condition_39(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_39 SAT")
		print('delta = 1/131072')
		print('skoX = 32767/32768')
		print('skoS2 = 46341/32768')
		print('skoSM = 3/512')
		print('skoSP = 370725/262144')
		exit(0)
	
	
	if pre_condition_40(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_40 SAT")
		print('delta = 1/131072')
		print('skoX = 65535/65536')
		print('skoS2 = 46341/32768')
		print('skoSM = 1/256')
		print('skoSP = 185363/131072')
		exit(0)
	
	
	if pre_condition_41(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_41 SAT")
		print('delta = 1/131072')
		print('skoX = 65535/65536')
		print('skoS2 = 46341/32768')
		print('skoSM = 1/256')
		print('skoSP = 185363/131072')
		exit(0)
	
	
	if pre_condition_42(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_42 SAT")
		print('delta = 144514744321/72057594037927936')
		print('skoX = 65535/65536')
		print('skoS2 = 741455/524288')
		print('skoSM = 1/256')
		print('skoSP = 185363/131072')
		exit(0)
	
	
	if pre_condition_43(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_43 SAT")
		print('delta = 144514744321/72057594037927936')
		print('skoX = 65535/65536')
		print('skoS2 = 741455/524288')
		print('skoSM = 1/256')
		print('skoSP = 185363/131072')
		exit(0)
	
	
	if pre_condition_44(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_44 SAT")
		print('delta = 144514744321/72057594037927936')
		print('skoX = 65535/65536')
		print('skoS2 = 741455/524288')
		print('skoSM = 1/256')
		print('skoSP = 185363/131072')
		exit(0)
	
	
	if pre_condition_45(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_45 SAT")
		print('delta = 144514744321/72057594037927936')
		print('skoX = 65535/65536')
		print('skoS2 = 741455/524288')
		print('skoSM = 1/256')
		print('skoSP = 185363/131072')
		exit(0)
	
	
	if pre_condition_46(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_46 SAT")
		print('delta = 144514744321/72057594037927936')
		print('skoX = 65535/65536')
		print('skoS2 = 741455/524288')
		print('skoSM = 1/256')
		print('skoSP = 185363/131072')
		exit(0)
	
	
	if pre_condition_47(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_47 SAT")
		print('delta = 144514744321/72057594037927936')
		print('skoX = 65535/65536')
		print('skoS2 = 741455/524288')
		print('skoSM = 1/256')
		print('skoSP = 185363/131072')
		exit(0)
	
	
	if pre_condition_48(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_48 SAT")
		print('delta = 144514744321/72057594037927936')
		print('skoX = 65535/65536')
		print('skoS2 = 741455/524288')
		print('skoSM = 1/256')
		print('skoSP = 185363/131072')
		exit(0)
	
	
	if pre_condition_49(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_49 SAT")
		print('delta = 144514744321/72057594037927936')
		print('skoX = 65535/65536')
		print('skoS2 = 741455/524288')
		print('skoSM = 1/256')
		print('skoSP = 185363/131072')
		exit(0)
	
	
	if pre_condition_50(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_50 SAT")
		print('delta = 144514744321/72057594037927936')
		print('skoX = 65535/65536')
		print('skoS2 = 741455/524288')
		print('skoSM = 1/256')
		print('skoSP = 185363/131072')
		exit(0)
	
	
	if pre_condition_51(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_51 SAT")
		print('delta = 144514744321/72057594037927936')
		print('skoX = 65535/65536')
		print('skoS2 = 741455/524288')
		print('skoSM = 1/256')
		print('skoSP = 185363/131072')
		exit(0)
	
	
	if pre_condition_52(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_52 SAT")
		print('delta = 144514744321/72057594037927936')
		print('skoX = 65535/65536')
		print('skoS2 = 741455/524288')
		print('skoSM = 1/256')
		print('skoSP = 185363/131072')
		exit(0)
	
	
	if pre_condition_53(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_53 SAT")
		print('delta = 144514744321/72057594037927936')
		print('skoX = 65535/65536')
		print('skoS2 = 741455/524288')
		print('skoSM = 1/256')
		print('skoSP = 185363/131072')
		exit(0)
	
	
	if pre_condition_54(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_54 SAT")
		print('delta = 144514744321/72057594037927936')
		print('skoX = 65535/65536')
		print('skoS2 = 741455/524288')
		print('skoSM = 1/256')
		print('skoSP = 185363/131072')
		exit(0)
	
	
	if pre_condition_55(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_55 SAT")
		print('delta = 144514744321/72057594037927936')
		print('skoX = 65535/65536')
		print('skoS2 = 741455/524288')
		print('skoSM = 1/256')
		print('skoSP = 185363/131072')
		exit(0)
	
	
	if pre_condition_56(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_56 SAT")
		print('delta = 144514744321/72057594037927936')
		print('skoX = 65535/65536')
		print('skoS2 = 741455/524288')
		print('skoSM = 1/256')
		print('skoSP = 185363/131072')
		exit(0)
	
	
	if pre_condition_57(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_57 SAT")
		print('delta = 144514744321/72057594037927936')
		print('skoX = 65535/65536')
		print('skoS2 = 741455/524288')
		print('skoSM = 1/256')
		print('skoSP = 185363/131072')
		exit(0)
	
	
	if pre_condition_58(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_58 SAT")
		print('delta = 144514744321/72057594037927936')
		print('skoX = 65535/65536')
		print('skoS2 = 741455/524288')
		print('skoSM = 1/256')
		print('skoSP = 185363/131072')
		exit(0)
	
	
	if pre_condition_59(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_59 SAT")
		print('delta = 144514744321/72057594037927936')
		print('skoX = 65535/65536')
		print('skoS2 = 741455/524288')
		print('skoSM = 1/256')
		print('skoSP = 185363/131072')
		exit(0)
	
	
	if pre_condition_60(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_60 SAT")
		print('delta = 144514744321/72057594037927936')
		print('skoX = 65535/65536')
		print('skoS2 = 741455/524288')
		print('skoSM = 1/256')
		print('skoSP = 185363/131072')
		exit(0)
	
	
	if pre_condition_61(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_61 SAT")
		print('delta = 144514744321/72057594037927936')
		print('skoX = 65535/65536')
		print('skoS2 = 741455/524288')
		print('skoSM = 1/256')
		print('skoSP = 185363/131072')
		exit(0)
	
	
	if pre_condition_62(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_62 SAT")
		print('delta = 144514744321/72057594037927936')
		print('skoX = 65535/65536')
		print('skoS2 = 741455/524288')
		print('skoSM = 1/256')
		print('skoSP = 185363/131072')
		exit(0)
	
	
	if pre_condition_63(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_63 SAT")
		print('delta = 144514744321/72057594037927936')
		print('skoX = 65535/65536')
		print('skoS2 = 741455/524288')
		print('skoSM = 1/256')
		print('skoSP = 185363/131072')
		exit(0)
	
	
	if pre_condition_64(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_64 SAT")
		print('delta = 144514744321/72057594037927936')
		print('skoX = 65535/65536')
		print('skoS2 = 741455/524288')
		print('skoSM = 1/256')
		print('skoSP = 185363/131072')
		exit(0)
	
	
	if pre_condition_65(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_65 SAT")
		print('delta = 144514744321/72057594037927936')
		print('skoX = 65535/65536')
		print('skoS2 = 741455/524288')
		print('skoSM = 1/256')
		print('skoSP = 185363/131072')
		exit(0)
	
	
	if pre_condition_66(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_66 SAT")
		print('delta = 144514744321/72057594037927936')
		print('skoX = 65535/65536')
		print('skoS2 = 741455/524288')
		print('skoSM = 1/256')
		print('skoSP = 185363/131072')
		exit(0)
	
	
	if pre_condition_67(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_67 SAT")
		print('delta = 144514744321/72057594037927936')
		print('skoX = 65535/65536')
		print('skoS2 = 741455/524288')
		print('skoSM = 1/256')
		print('skoSP = 185363/131072')
		exit(0)
	
	
	if pre_condition_68(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_68 SAT")
		print('delta = 144514744321/72057594037927936')
		print('skoX = 65535/65536')
		print('skoS2 = 741455/524288')
		print('skoSM = 1/256')
		print('skoSP = 185363/131072')
		exit(0)
	
	
	if pre_condition_69(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_69 SAT")
		print('delta = 144514744321/72057594037927936')
		print('skoX = 65535/65536')
		print('skoS2 = 741455/524288')
		print('skoSM = 1/256')
		print('skoSP = 185363/131072')
		exit(0)
	
	
	if pre_condition_70(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_70 SAT")
		print('delta = 7075790849/72057594037927936')
		print('skoX = 524279/524288')
		print('skoS2 = 11863283/8388608')
		print('skoSM = 17/4096')
		print('skoSP = 185363/131072')
		exit(0)
	
	
	if pre_condition_71(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_71 SAT")
		print('delta = 7075790849/72057594037927936')
		print('skoX = 524279/524288')
		print('skoS2 = 11863283/8388608')
		print('skoSM = 17/4096')
		print('skoSP = 185363/131072')
		exit(0)
	
	
	if pre_condition_72(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_72 SAT")
		print('delta = 633339905/72057594037927936')
		print('skoX = 33553853/33554432')
		print('skoS2 = 189812531/134217728')
		print('skoSM = 1089/262144')
		print('skoSP = 185363/131072')
		exit(0)
	
	
	if pre_condition_73(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_73 SAT")
		print('delta = 633339905/72057594037927936')
		print('skoX = 33553853/33554432')
		print('skoS2 = 189812531/134217728')
		print('skoSM = 1089/262144')
		print('skoSP = 185363/131072')
		exit(0)
	
	
	if pre_condition_74(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_74 SAT")
		print('delta = 96468993/72057594037927936')
		print('skoX = 134215411/134217728')
		print('skoS2 = 759250125/536870912')
		print('skoSM = 17427/4194304')
		print('skoSP = 185363/131072')
		exit(0)
	
	
	if pre_condition_75(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_75 SAT")
		print('delta = 96468993/72057594037927936')
		print('skoX = 134215411/134217728')
		print('skoS2 = 759250125/536870912')
		print('skoSM = 17427/4194304')
		print('skoSP = 185363/131072')
		exit(0)
	
	
	if pre_condition_76(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_76 SAT")
		print('delta = 29360129/72057594037927936')
		print('skoX = 1073723287/1073741824')
		print('skoS2 = 759250125/536870912')
		print('skoSM = 69709/16777216')
		print('skoSP = 185363/131072')
		exit(0)
	
	
	if pre_condition_77(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_77 SAT")
		print('delta = 29360129/72057594037927936')
		print('skoX = 1073723287/1073741824')
		print('skoS2 = 759250125/536870912')
		print('skoSM = 69709/16777216')
		print('skoSP = 185363/131072')
		exit(0)
	
	
	if pre_condition_78(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_78 SAT")
		print('delta = 1/17179869184')
		print('skoX = 1073723287/1073741824')
		print('skoS2 = 759250125/536870912')
		print('skoSM = 278837/67108864')
		print('skoSP = 48591798277/34359738368')
		exit(0)
	
	
	if pre_condition_79(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_79 SAT")
		print('delta = 1/17179869184')
		print('skoX = 1073723287/1073741824')
		print('skoS2 = 759250125/536870912')
		print('skoSM = 278837/67108864')
		print('skoSP = 48591798277/34359738368')
		exit(0)
	
	
	if pre_condition_80(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_80 SAT")
		print('delta = 1/524288')
		print('skoX = 65535/65536')
		print('skoS2 = 741455/524288')
		print('skoSM = 1/256')
		print('skoSP = 1482905/1048576')
		exit(0)
	
	
	if pre_condition_81(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_81 SAT")
		print('delta = 1/524288')
		print('skoX = 65535/65536')
		print('skoS2 = 741455/524288')
		print('skoSM = 1/256')
		print('skoSP = 1482905/1048576')
		exit(0)
	
	
	if pre_condition_82(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_82 SAT")
		print('delta = 3/524288')
		print('skoX = 131071/131072')
		print('skoS2 = 46341/32768')
		print('skoSM = 1/512')
		print('skoSP = 370727/262144')
		exit(0)
	
	
	if pre_condition_83(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_83 SAT")
		print('delta = 3/524288')
		print('skoX = 131071/131072')
		print('skoS2 = 46341/32768')
		print('skoSM = 1/512')
		print('skoSP = 370727/262144')
		exit(0)
	
	
	if pre_condition_84(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_84 SAT")
		print('delta = 1/72057594037927936')
		print('skoX = 262143/262144')
		print('skoS2 = 101904826760412361/72057594037927936')
		print('skoSM = 1/512')
		print('skoSP = 101904729576350021/72057594037927936')
		exit(0)
	
	
	if pre_condition_85(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_85 SAT")
		print('delta = 1/72057594037927936')
		print('skoX = 262143/262144')
		print('skoS2 = 101904826760412361/72057594037927936')
		print('skoSM = 1/512')
		print('skoSP = 101904729576350021/72057594037927936')
		exit(0)
	
	
	if pre_condition_86(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_86 SAT")
		print('delta = 3/2097152')
		print('skoX = 524287/524288')
		print('skoS2 = 741455/524288')
		print('skoSM = 1/1024')
		print('skoSP = 741455/524288')
		exit(0)
	
	
	if pre_condition_87(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_87 SAT")
		print('delta = 3/2097152')
		print('skoX = 524287/524288')
		print('skoS2 = 741455/524288')
		print('skoSM = 1/1024')
		print('skoSP = 741455/524288')
		exit(0)
	
	
	if pre_condition_88(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_88 SAT")
		print('delta = 1/288230376151711744')
		print('skoX = 1048575/1048576')
		print('skoS2 = 101904826760412361/72057594037927936')
		print('skoSM = 1/1024')
		print('skoSP = 101904802464405465/72057594037927936')
		exit(0)
	
	
	if pre_condition_89(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_89 SAT")
		print('delta = 1/288230376151711744')
		print('skoX = 1048575/1048576')
		print('skoS2 = 101904826760412361/72057594037927936')
		print('skoSM = 1/1024')
		print('skoSP = 101904802464405465/72057594037927936')
		exit(0)


	print("UNKNOWN")
	exit(0)
