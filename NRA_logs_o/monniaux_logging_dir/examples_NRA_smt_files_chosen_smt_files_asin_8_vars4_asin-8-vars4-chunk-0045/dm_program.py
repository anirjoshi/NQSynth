import sympy
from sympy import *

def pre_condition_0(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= skoX) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta >= -skoX) & (delta >= skoS2**2 - 2) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (63*skoS2/20 + 13/8 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (63*skoS2/20 - skoSM*(126*skoS2 + 61)/40 + 73/40 < skoX*(40*skoSM + skoX*(126*skoS2 - skoSM*(126*skoS2 + 61) + 73) + 200)/40)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictGreaterThan(Add(Mul(Rational(63, 20), Symbol('skoS2')), Rational(13, 8)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(63, 20), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(73, 40)), Mul(Rational(1, 40), Symbol('skoX'), Add(Mul(Integer(40), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Mul(Integer(-1), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(73))), Integer(200)))))

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
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 17/64) & (delta >= skoS2**2 - 2) & (delta - skoX >= -17/64) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (567*skoS2/160 + 117/64 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (567*skoS2/160 - skoSM*(126*skoS2 + 61)/40 + 649/320 < skoX*(320*skoSM + skoX*(1134*skoS2 - 8*skoSM*(126*skoS2 + 61) + 649) + 1640)/320)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(17, 64)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-17, 64)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictGreaterThan(Add(Mul(Rational(567, 160), Symbol('skoS2')), Rational(117, 64)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(567, 160), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(649, 320)), Mul(Rational(1, 320), Symbol('skoX'), Add(Mul(Integer(320), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(1134), Symbol('skoS2')), Mul(Integer(-1), Integer(8), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(649))), Integer(1640)))))

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
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 9/16) & (delta >= skoS2**2 - 2) & (delta - skoX >= -9/16) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (63*skoS2/16 + 65/32 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (63*skoS2/16 - skoSM*(126*skoS2 + 61)/40 + 357/160 < skoX*(160*skoSM + skoX*(630*skoS2 - 4*skoSM*(126*skoS2 + 61) + 357) + 840)/160)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(9, 16)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-9, 16)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictGreaterThan(Add(Mul(Rational(63, 16), Symbol('skoS2')), Rational(65, 32)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(63, 16), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(357, 160)), Mul(Rational(1, 160), Symbol('skoX'), Add(Mul(Integer(160), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(630), Symbol('skoS2')), Mul(Integer(-1), Integer(4), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(357))), Integer(840)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_5(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 9/16) & (delta >= skoS2**2 - 2) & (delta - skoX >= -7/16) & (delta >= 2 - skoS2**2) & (63*skoS2/40 + 87/80 < 3*skoX*(skoX*(42*skoS2 + 29) + 160)/80)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(9, 16)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-7, 16)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(63, 40), Symbol('skoS2')), Rational(87, 80)), Mul(Rational(3, 80), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(42), Symbol('skoS2')), Integer(29))), Integer(160)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_6(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 57/64) & (delta >= skoS2**2 - 2) & (delta - skoX >= -57/64) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (693*skoS2/160 + 143/64 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (693*skoS2/160 - skoSM*(126*skoS2 + 61)/40 + 779/320 < skoX*(320*skoSM + skoX*(1386*skoS2 - 8*skoSM*(126*skoS2 + 61) + 779) + 1720)/320)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(57, 64)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-57, 64)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictGreaterThan(Add(Mul(Rational(693, 160), Symbol('skoS2')), Rational(143, 64)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(693, 160), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(779, 320)), Mul(Rational(1, 320), Symbol('skoX'), Add(Mul(Integer(320), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(1386), Symbol('skoS2')), Mul(Integer(-1), Integer(8), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(779))), Integer(1720)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_7(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 57/64) & (delta >= skoS2**2 - 2) & (delta - skoX >= -3/4) & (delta >= 2 - skoS2**2) & (441*skoS2/160 + 107/64 < skoX*(skoX*(882*skoS2 + 535) + 1880)/320)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(57, 64)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-3, 4)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(441, 160), Symbol('skoS2')), Rational(107, 64)), Mul(Rational(1, 320), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(882), Symbol('skoS2')), Integer(535))), Integer(1880)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_8(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 185/256) & (delta >= skoS2**2 - 2) & (delta - skoX >= -185/256) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (1323*skoS2/320 + 273/128 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (1323*skoS2/320 - skoSM*(126*skoS2 + 61)/40 + 1493/640 < skoX*(640*skoSM + skoX*(2646*skoS2 - 16*skoSM*(126*skoS2 + 61) + 1493) + 3400)/640)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(185, 256)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-185, 256)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictGreaterThan(Add(Mul(Rational(1323, 320), Symbol('skoS2')), Rational(273, 128)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(1323, 320), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(1493, 640)), Mul(Rational(1, 640), Symbol('skoX'), Add(Mul(Integer(640), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(2646), Symbol('skoS2')), Mul(Integer(-1), Integer(16), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(1493))), Integer(3400)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_9(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 3/4) & (delta >= skoS2**2 - 2) & (delta - skoX >= -185/256) & (delta >= 2 - skoS2**2) & (819*skoS2/320 + 201/128 < 3*skoX*(skoX*(546*skoS2 + 335) + 1240)/640)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(3, 4)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-185, 256)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(819, 320), Symbol('skoS2')), Rational(201, 128)), Mul(Rational(3, 640), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(546), Symbol('skoS2')), Integer(335))), Integer(1240)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_10(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 12177/16384) & (delta >= skoS2**2 - 2) & (delta - skoX >= -12177/16384) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (10647*skoS2/2560 + 2197/1024 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (10647*skoS2/2560 - skoSM*(126*skoS2 + 61)/40 + 12009/5120 < skoX*(5120*skoSM + skoX*(21294*skoS2 - 128*skoSM*(126*skoS2 + 61) + 12009) + 27240)/5120)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(12177, 16384)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-12177, 16384)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictGreaterThan(Add(Mul(Rational(10647, 2560), Symbol('skoS2')), Rational(2197, 1024)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(10647, 2560), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(12009, 5120)), Mul(Rational(1, 5120), Symbol('skoX'), Add(Mul(Integer(5120), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(21294), Symbol('skoS2')), Mul(Integer(-1), Integer(128), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(12009))), Integer(27240)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_11(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 12177/16384) & (delta >= skoS2**2 - 2) & (delta - skoX >= -3007/4096) & (delta >= 2 - skoS2**2) & (6489*skoS2/2560 + 7983/5120 < 9*skoX*(skoX*(1442*skoS2 + 887) + 3320)/5120)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(12177, 16384)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-3007, 4096)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(6489, 2560), Symbol('skoS2')), Rational(7983, 5120)), Mul(Rational(9, 5120), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(1442), Symbol('skoS2')), Integer(887))), Integer(3320)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_12(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 196185/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= -196185/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (42651*skoS2/10240 + 8801/4096 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (42651*skoS2/10240 - skoSM*(126*skoS2 + 61)/40 + 48101/20480 < skoX*(20480*skoSM + skoX*(85302*skoS2 - 512*skoSM*(126*skoS2 + 61) + 48101) + 109000)/20480)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictGreaterThan(Add(Mul(Rational(42651, 10240), Symbol('skoS2')), Rational(8801, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(42651, 10240), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(48101, 20480)), Mul(Rational(1, 20480), Symbol('skoX'), Add(Mul(Integer(20480), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(85302), Symbol('skoS2')), Mul(Integer(-1), Integer(512), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(48101))), Integer(109000)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_13(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 196185/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= -48895/65536) & (delta >= 2 - skoS2**2) & (26397*skoS2/10240 + 32363/20480 < skoX*(skoX*(52794*skoS2 + 32363) + 119320)/20480)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-48895, 65536)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(26397, 10240), Symbol('skoS2')), Rational(32363, 20480)), Mul(Rational(1, 20480), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(52794), Symbol('skoS2')), Integer(32363))), Integer(119320)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_14(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 196185/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= -196185/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (42651*skoS2/10240 + 8801/4096 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (42651*skoS2/10240 - skoSM*(126*skoS2 + 61)/40 + 48101/20480 < skoX*(20480*skoSM + skoX*(85302*skoS2 - 512*skoSM*(126*skoS2 + 61) + 48101) + 109000)/20480)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictGreaterThan(Add(Mul(Rational(42651, 10240), Symbol('skoS2')), Rational(8801, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(42651, 10240), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(48101, 20480)), Mul(Rational(1, 20480), Symbol('skoX'), Add(Mul(Integer(20480), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(85302), Symbol('skoS2')), Mul(Integer(-1), Integer(512), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(48101))), Integer(109000)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_15(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 785407/1048576) & (delta >= skoS2**2 - 2) & (delta - skoX >= -196185/262144) & (delta >= 2 - skoS2**2) & (52983*skoS2/20480 + 64909/40960 < skoX*(skoX*(105966*skoS2 + 64909) + 238520)/40960)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(785407, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-196185, 262144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(52983, 20480), Symbol('skoS2')), Rational(64909, 40960)), Mul(Rational(1, 40960), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(105966), Symbol('skoS2')), Integer(64909))), Integer(238520)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_16(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 196185/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= -196185/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (42651*skoS2/10240 + 8801/4096 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (42651*skoS2/10240 - skoSM*(126*skoS2 + 61)/40 + 48101/20480 < skoX*(20480*skoSM + skoX*(85302*skoS2 - 512*skoSM*(126*skoS2 + 61) + 48101) + 109000)/20480)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictGreaterThan(Add(Mul(Rational(42651, 10240), Symbol('skoS2')), Rational(8801, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(42651, 10240), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(48101, 20480)), Mul(Rational(1, 20480), Symbol('skoX'), Add(Mul(Integer(20480), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(85302), Symbol('skoS2')), Mul(Integer(-1), Integer(512), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(48101))), Integer(109000)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_17(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 3139575/4194304) & (delta >= skoS2**2 - 2) & (delta - skoX >= -196185/262144) & (delta >= 2 - skoS2**2) & (105903*skoS2/40960 + 129757/81920 < skoX*(skoX*(211806*skoS2 + 129757) + 477080)/81920)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(3139575, 4194304)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-196185, 262144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(105903, 40960), Symbol('skoS2')), Rational(129757, 81920)), Mul(Rational(1, 81920), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(211806), Symbol('skoS2')), Integer(129757))), Integer(477080)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_18(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 196185/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= -196185/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (42651*skoS2/10240 + 8801/4096 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (42651*skoS2/10240 - skoSM*(126*skoS2 + 61)/40 + 48101/20480 < skoX*(20480*skoSM + skoX*(85302*skoS2 - 512*skoSM*(126*skoS2 + 61) + 48101) + 109000)/20480)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictGreaterThan(Add(Mul(Rational(42651, 10240), Symbol('skoS2')), Rational(8801, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(42651, 10240), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(48101, 20480)), Mul(Rational(1, 20480), Symbol('skoX'), Add(Mul(Integer(20480), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(85302), Symbol('skoS2')), Mul(Integer(-1), Integer(512), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(48101))), Integer(109000)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_19(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 50224983/67108864) & (delta >= skoS2**2 - 2) & (delta - skoX >= -196185/262144) & (delta >= 2 - skoS2**2) & (423549*skoS2/163840 + 518967/327680 < 81*skoX*(skoX*(10458*skoS2 + 6407) + 23560)/327680)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(50224983, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-196185, 262144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(423549, 163840), Symbol('skoS2')), Rational(518967, 327680)), Mul(Rational(81, 327680), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(10458), Symbol('skoS2')), Integer(6407))), Integer(23560)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_20(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 196185/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= -196185/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (42651*skoS2/10240 + 8801/4096 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (42651*skoS2/10240 - skoSM*(126*skoS2 + 61)/40 + 48101/20480 < skoX*(20480*skoSM + skoX*(85302*skoS2 - 512*skoSM*(126*skoS2 + 61) + 48101) + 109000)/20480)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictGreaterThan(Add(Mul(Rational(42651, 10240), Symbol('skoS2')), Rational(8801, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(42651, 10240), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(48101, 20480)), Mul(Rational(1, 20480), Symbol('skoX'), Add(Mul(Integer(20480), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(85302), Symbol('skoS2')), Mul(Integer(-1), Integer(512), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(48101))), Integer(109000)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_21(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 3214333167/4294967296) & (delta >= skoS2**2 - 2) & (delta - skoX >= -196185/262144) & (delta >= 2 - skoS2**2) & (3388329*skoS2/1310720 + 830335/524288 < skoX*(skoX*(6776658*skoS2 + 4151675) + 15266920)/2621440)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(3214333167, 4294967296)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-196185, 262144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(3388329, 1310720), Symbol('skoS2')), Rational(830335, 524288)), Mul(Rational(1, 2621440), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(6776658), Symbol('skoS2')), Integer(4151675))), Integer(15266920)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_22(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 196185/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= -196185/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (42651*skoS2/10240 + 8801/4096 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (42651*skoS2/10240 - skoSM*(126*skoS2 + 61)/40 + 48101/20480 < skoX*(20480*skoSM + skoX*(85302*skoS2 - 512*skoSM*(126*skoS2 + 61) + 48101) + 109000)/20480)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictGreaterThan(Add(Mul(Rational(42651, 10240), Symbol('skoS2')), Rational(8801, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(42651, 10240), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(48101, 20480)), Mul(Rational(1, 20480), Symbol('skoX'), Add(Mul(Integer(20480), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(85302), Symbol('skoS2')), Mul(Integer(-1), Integer(512), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(48101))), Integer(109000)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_23(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 12857201175/17179869184) & (delta >= skoS2**2 - 2) & (delta - skoX >= -196185/262144) & (delta >= 2 - skoS2**2) & (1355319*skoS2/524288 + 8303289/5242880 < 3*skoX*(skoX*(4517730*skoS2 + 2767763) + 10177960)/5242880)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(12857201175, 17179869184)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-196185, 262144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(1355319, 524288), Symbol('skoS2')), Rational(8303289, 5242880)), Mul(Rational(3, 5242880), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(4517730), Symbol('skoS2')), Integer(2767763))), Integer(10177960)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_24(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 196185/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= -196185/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (42651*skoS2/10240 + 8801/4096 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (42651*skoS2/10240 - skoSM*(126*skoS2 + 61)/40 + 48101/20480 < skoX*(20480*skoSM + skoX*(85302*skoS2 - 512*skoSM*(126*skoS2 + 61) + 48101) + 109000)/20480)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictGreaterThan(Add(Mul(Rational(42651, 10240), Symbol('skoS2')), Rational(8801, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(42651, 10240), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(48101, 20480)), Mul(Rational(1, 20480), Symbol('skoX'), Add(Mul(Integer(20480), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(85302), Symbol('skoS2')), Mul(Integer(-1), Integer(512), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(48101))), Integer(109000)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_25(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 196185/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= -242865266607202326324835163945631/324518553658426726783156020576256) & (delta >= 2 - skoS2**2) & (931366741103611407*skoS2/360287970189639680 + 1141194010665750957/720575940379279360 < 9*skoX*(skoX*(206970386911913646*skoS2 + 126799334518416773) + 466282821249199000)/720575940379279360)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-242865266607202326324835163945631, 324518553658426726783156020576256)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(931366741103611407, 360287970189639680), Symbol('skoS2')), Rational(1141194010665750957, 720575940379279360)), Mul(Rational(9, 720575940379279360), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(206970386911913646), Symbol('skoS2')), Integer(126799334518416773))), Integer(466282821249199000)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_26(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 196185/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= -196185/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (42651*skoS2/10240 + 8801/4096 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (42651*skoS2/10240 - skoSM*(126*skoS2 + 61)/40 + 48101/20480 < skoX*(20480*skoSM + skoX*(85302*skoS2 - 512*skoSM*(126*skoS2 + 61) + 48101) + 109000)/20480)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictGreaterThan(Add(Mul(Rational(42651, 10240), Symbol('skoS2')), Rational(8801, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(42651, 10240), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(48101, 20480)), Mul(Rational(1, 20480), Symbol('skoX'), Add(Mul(Integer(20480), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(85302), Symbol('skoS2')), Mul(Integer(-1), Integer(512), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(48101))), Integer(109000)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_27(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 196185/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= -242865266607202326324835163945631/324518553658426726783156020576256) & (delta >= 2 - skoS2**2) & (931366741103611407*skoS2/360287970189639680 + 1141194010665750957/720575940379279360 < 9*skoX*(skoX*(206970386911913646*skoS2 + 126799334518416773) + 466282821249199000)/720575940379279360)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-242865266607202326324835163945631, 324518553658426726783156020576256)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(931366741103611407, 360287970189639680), Symbol('skoS2')), Rational(1141194010665750957, 720575940379279360)), Mul(Rational(9, 720575940379279360), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(206970386911913646), Symbol('skoS2')), Integer(126799334518416773))), Integer(466282821249199000)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_28(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 196185/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= -196185/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (42651*skoS2/10240 + 8801/4096 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (42651*skoS2/10240 - skoSM*(126*skoS2 + 61)/40 + 48101/20480 < skoX*(20480*skoSM + skoX*(85302*skoS2 - 512*skoSM*(126*skoS2 + 61) + 48101) + 109000)/20480)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictGreaterThan(Add(Mul(Rational(42651, 10240), Symbol('skoS2')), Rational(8801, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(42651, 10240), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(48101, 20480)), Mul(Rational(1, 20480), Symbol('skoX'), Add(Mul(Integer(20480), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(85302), Symbol('skoS2')), Mul(Integer(-1), Integer(512), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(48101))), Integer(109000)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_29(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 196185/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= -242865266607202326324835163945631/324518553658426726783156020576256) & (delta >= 2 - skoS2**2) & (931366741103611407*skoS2/360287970189639680 + 1141194010665750957/720575940379279360 < 9*skoX*(skoX*(206970386911913646*skoS2 + 126799334518416773) + 466282821249199000)/720575940379279360)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-242865266607202326324835163945631, 324518553658426726783156020576256)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(931366741103611407, 360287970189639680), Symbol('skoS2')), Rational(1141194010665750957, 720575940379279360)), Mul(Rational(9, 720575940379279360), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(206970386911913646), Symbol('skoS2')), Integer(126799334518416773))), Integer(466282821249199000)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_30(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 196185/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= -196185/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (42651*skoS2/10240 + 8801/4096 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (42651*skoS2/10240 - skoSM*(126*skoS2 + 61)/40 + 48101/20480 < skoX*(20480*skoSM + skoX*(85302*skoS2 - 512*skoSM*(126*skoS2 + 61) + 48101) + 109000)/20480)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictGreaterThan(Add(Mul(Rational(42651, 10240), Symbol('skoS2')), Rational(8801, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(42651, 10240), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(48101, 20480)), Mul(Rational(1, 20480), Symbol('skoX'), Add(Mul(Integer(20480), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(85302), Symbol('skoS2')), Mul(Integer(-1), Integer(512), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(48101))), Integer(109000)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_31(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 196185/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= -242865266607202326324835163945631/324518553658426726783156020576256) & (delta >= 2 - skoS2**2) & (931366741103611407*skoS2/360287970189639680 + 1141194010665750957/720575940379279360 < 9*skoX*(skoX*(206970386911913646*skoS2 + 126799334518416773) + 466282821249199000)/720575940379279360)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-242865266607202326324835163945631, 324518553658426726783156020576256)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(931366741103611407, 360287970189639680), Symbol('skoS2')), Rational(1141194010665750957, 720575940379279360)), Mul(Rational(9, 720575940379279360), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(206970386911913646), Symbol('skoS2')), Integer(126799334518416773))), Integer(466282821249199000)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_32(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 196185/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= -196185/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (42651*skoS2/10240 + 8801/4096 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (42651*skoS2/10240 - skoSM*(126*skoS2 + 61)/40 + 48101/20480 < skoX*(20480*skoSM + skoX*(85302*skoS2 - 512*skoSM*(126*skoS2 + 61) + 48101) + 109000)/20480)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictGreaterThan(Add(Mul(Rational(42651, 10240), Symbol('skoS2')), Rational(8801, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(42651, 10240), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(48101, 20480)), Mul(Rational(1, 20480), Symbol('skoX'), Add(Mul(Integer(20480), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(85302), Symbol('skoS2')), Mul(Integer(-1), Integer(512), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(48101))), Integer(109000)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_33(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 196185/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= -242865266607202326324835163945631/324518553658426726783156020576256) & (delta >= 2 - skoS2**2) & (931366741103611407*skoS2/360287970189639680 + 1141194010665750957/720575940379279360 < 9*skoX*(skoX*(206970386911913646*skoS2 + 126799334518416773) + 466282821249199000)/720575940379279360)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-242865266607202326324835163945631, 324518553658426726783156020576256)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(931366741103611407, 360287970189639680), Symbol('skoS2')), Rational(1141194010665750957, 720575940379279360)), Mul(Rational(9, 720575940379279360), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(206970386911913646), Symbol('skoS2')), Integer(126799334518416773))), Integer(466282821249199000)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_34(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 196185/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= -196185/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (42651*skoS2/10240 + 8801/4096 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (42651*skoS2/10240 - skoSM*(126*skoS2 + 61)/40 + 48101/20480 < skoX*(20480*skoSM + skoX*(85302*skoS2 - 512*skoSM*(126*skoS2 + 61) + 48101) + 109000)/20480)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictGreaterThan(Add(Mul(Rational(42651, 10240), Symbol('skoS2')), Rational(8801, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(42651, 10240), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(48101, 20480)), Mul(Rational(1, 20480), Symbol('skoX'), Add(Mul(Integer(20480), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(85302), Symbol('skoS2')), Mul(Integer(-1), Integer(512), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(48101))), Integer(109000)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_35(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 196185/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= -242865266607202326324835163945631/324518553658426726783156020576256) & (delta >= 2 - skoS2**2) & (931366741103611407*skoS2/360287970189639680 + 1141194010665750957/720575940379279360 < 9*skoX*(skoX*(206970386911913646*skoS2 + 126799334518416773) + 466282821249199000)/720575940379279360)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-242865266607202326324835163945631, 324518553658426726783156020576256)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(931366741103611407, 360287970189639680), Symbol('skoS2')), Rational(1141194010665750957, 720575940379279360)), Mul(Rational(9, 720575940379279360), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(206970386911913646), Symbol('skoS2')), Integer(126799334518416773))), Integer(466282821249199000)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_36(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 196185/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= -196185/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (42651*skoS2/10240 + 8801/4096 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (42651*skoS2/10240 - skoSM*(126*skoS2 + 61)/40 + 48101/20480 < skoX*(20480*skoSM + skoX*(85302*skoS2 - 512*skoSM*(126*skoS2 + 61) + 48101) + 109000)/20480)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictGreaterThan(Add(Mul(Rational(42651, 10240), Symbol('skoS2')), Rational(8801, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(42651, 10240), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(48101, 20480)), Mul(Rational(1, 20480), Symbol('skoX'), Add(Mul(Integer(20480), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(85302), Symbol('skoS2')), Mul(Integer(-1), Integer(512), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(48101))), Integer(109000)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_37(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 196185/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= -242865266607202326324835163945631/324518553658426726783156020576256) & (delta >= 2 - skoS2**2) & (931366741103611407*skoS2/360287970189639680 + 1141194010665750957/720575940379279360 < 9*skoX*(skoX*(206970386911913646*skoS2 + 126799334518416773) + 466282821249199000)/720575940379279360)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-242865266607202326324835163945631, 324518553658426726783156020576256)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(931366741103611407, 360287970189639680), Symbol('skoS2')), Rational(1141194010665750957, 720575940379279360)), Mul(Rational(9, 720575940379279360), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(206970386911913646), Symbol('skoS2')), Integer(126799334518416773))), Integer(466282821249199000)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_38(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 196185/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= -196185/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (42651*skoS2/10240 + 8801/4096 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (42651*skoS2/10240 - skoSM*(126*skoS2 + 61)/40 + 48101/20480 < skoX*(20480*skoSM + skoX*(85302*skoS2 - 512*skoSM*(126*skoS2 + 61) + 48101) + 109000)/20480)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictGreaterThan(Add(Mul(Rational(42651, 10240), Symbol('skoS2')), Rational(8801, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(42651, 10240), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(48101, 20480)), Mul(Rational(1, 20480), Symbol('skoX'), Add(Mul(Integer(20480), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(85302), Symbol('skoS2')), Mul(Integer(-1), Integer(512), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(48101))), Integer(109000)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_39(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 196185/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= -242865266607202326324835163945631/324518553658426726783156020576256) & (delta >= 2 - skoS2**2) & (931366741103611407*skoS2/360287970189639680 + 1141194010665750957/720575940379279360 < 9*skoX*(skoX*(206970386911913646*skoS2 + 126799334518416773) + 466282821249199000)/720575940379279360)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-242865266607202326324835163945631, 324518553658426726783156020576256)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(931366741103611407, 360287970189639680), Symbol('skoS2')), Rational(1141194010665750957, 720575940379279360)), Mul(Rational(9, 720575940379279360), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(206970386911913646), Symbol('skoS2')), Integer(126799334518416773))), Integer(466282821249199000)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_40(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 196185/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= -196185/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (42651*skoS2/10240 + 8801/4096 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (42651*skoS2/10240 - skoSM*(126*skoS2 + 61)/40 + 48101/20480 < skoX*(20480*skoSM + skoX*(85302*skoS2 - 512*skoSM*(126*skoS2 + 61) + 48101) + 109000)/20480)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictGreaterThan(Add(Mul(Rational(42651, 10240), Symbol('skoS2')), Rational(8801, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(42651, 10240), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(48101, 20480)), Mul(Rational(1, 20480), Symbol('skoX'), Add(Mul(Integer(20480), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(85302), Symbol('skoS2')), Mul(Integer(-1), Integer(512), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(48101))), Integer(109000)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_41(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 196185/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= -242865266607202326324835163945631/324518553658426726783156020576256) & (delta >= 2 - skoS2**2) & (931366741103611407*skoS2/360287970189639680 + 1141194010665750957/720575940379279360 < 9*skoX*(skoX*(206970386911913646*skoS2 + 126799334518416773) + 466282821249199000)/720575940379279360)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-242865266607202326324835163945631, 324518553658426726783156020576256)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(931366741103611407, 360287970189639680), Symbol('skoS2')), Rational(1141194010665750957, 720575940379279360)), Mul(Rational(9, 720575940379279360), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(206970386911913646), Symbol('skoS2')), Integer(126799334518416773))), Integer(466282821249199000)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_42(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 196185/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= -196185/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (42651*skoS2/10240 + 8801/4096 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (42651*skoS2/10240 - skoSM*(126*skoS2 + 61)/40 + 48101/20480 < skoX*(20480*skoSM + skoX*(85302*skoS2 - 512*skoSM*(126*skoS2 + 61) + 48101) + 109000)/20480)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictGreaterThan(Add(Mul(Rational(42651, 10240), Symbol('skoS2')), Rational(8801, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(42651, 10240), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(48101, 20480)), Mul(Rational(1, 20480), Symbol('skoX'), Add(Mul(Integer(20480), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(85302), Symbol('skoS2')), Mul(Integer(-1), Integer(512), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(48101))), Integer(109000)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_43(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 196185/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= -242865266607202326324835163945631/324518553658426726783156020576256) & (delta >= 2 - skoS2**2) & (931366741103611407*skoS2/360287970189639680 + 1141194010665750957/720575940379279360 < 9*skoX*(skoX*(206970386911913646*skoS2 + 126799334518416773) + 466282821249199000)/720575940379279360)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-242865266607202326324835163945631, 324518553658426726783156020576256)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(931366741103611407, 360287970189639680), Symbol('skoS2')), Rational(1141194010665750957, 720575940379279360)), Mul(Rational(9, 720575940379279360), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(206970386911913646), Symbol('skoS2')), Integer(126799334518416773))), Integer(466282821249199000)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_44(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 196185/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= -196185/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (42651*skoS2/10240 + 8801/4096 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (42651*skoS2/10240 - skoSM*(126*skoS2 + 61)/40 + 48101/20480 < skoX*(20480*skoSM + skoX*(85302*skoS2 - 512*skoSM*(126*skoS2 + 61) + 48101) + 109000)/20480)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictGreaterThan(Add(Mul(Rational(42651, 10240), Symbol('skoS2')), Rational(8801, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(42651, 10240), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(48101, 20480)), Mul(Rational(1, 20480), Symbol('skoX'), Add(Mul(Integer(20480), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(85302), Symbol('skoS2')), Mul(Integer(-1), Integer(512), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(48101))), Integer(109000)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_45(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 196185/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= -242865266607202326324835163945631/324518553658426726783156020576256) & (delta >= 2 - skoS2**2) & (931366741103611407*skoS2/360287970189639680 + 1141194010665750957/720575940379279360 < 9*skoX*(skoX*(206970386911913646*skoS2 + 126799334518416773) + 466282821249199000)/720575940379279360)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-242865266607202326324835163945631, 324518553658426726783156020576256)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(931366741103611407, 360287970189639680), Symbol('skoS2')), Rational(1141194010665750957, 720575940379279360)), Mul(Rational(9, 720575940379279360), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(206970386911913646), Symbol('skoS2')), Integer(126799334518416773))), Integer(466282821249199000)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_46(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 196185/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= -196185/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (42651*skoS2/10240 + 8801/4096 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (42651*skoS2/10240 - skoSM*(126*skoS2 + 61)/40 + 48101/20480 < skoX*(20480*skoSM + skoX*(85302*skoS2 - 512*skoSM*(126*skoS2 + 61) + 48101) + 109000)/20480)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictGreaterThan(Add(Mul(Rational(42651, 10240), Symbol('skoS2')), Rational(8801, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(42651, 10240), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(48101, 20480)), Mul(Rational(1, 20480), Symbol('skoX'), Add(Mul(Integer(20480), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(85302), Symbol('skoS2')), Mul(Integer(-1), Integer(512), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(48101))), Integer(109000)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_47(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 196185/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= -242865266607202326324835163945631/324518553658426726783156020576256) & (delta >= 2 - skoS2**2) & (931366741103611407*skoS2/360287970189639680 + 1141194010665750957/720575940379279360 < 9*skoX*(skoX*(206970386911913646*skoS2 + 126799334518416773) + 466282821249199000)/720575940379279360)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-242865266607202326324835163945631, 324518553658426726783156020576256)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(931366741103611407, 360287970189639680), Symbol('skoS2')), Rational(1141194010665750957, 720575940379279360)), Mul(Rational(9, 720575940379279360), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(206970386911913646), Symbol('skoS2')), Integer(126799334518416773))), Integer(466282821249199000)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_48(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 196185/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= -196185/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (42651*skoS2/10240 + 8801/4096 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (42651*skoS2/10240 - skoSM*(126*skoS2 + 61)/40 + 48101/20480 < skoX*(20480*skoSM + skoX*(85302*skoS2 - 512*skoSM*(126*skoS2 + 61) + 48101) + 109000)/20480)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictGreaterThan(Add(Mul(Rational(42651, 10240), Symbol('skoS2')), Rational(8801, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(42651, 10240), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(48101, 20480)), Mul(Rational(1, 20480), Symbol('skoX'), Add(Mul(Integer(20480), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(85302), Symbol('skoS2')), Mul(Integer(-1), Integer(512), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(48101))), Integer(109000)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_49(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 196185/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= -242865266607202326324835163945631/324518553658426726783156020576256) & (delta >= 2 - skoS2**2) & (931366741103611407*skoS2/360287970189639680 + 1141194010665750957/720575940379279360 < 9*skoX*(skoX*(206970386911913646*skoS2 + 126799334518416773) + 466282821249199000)/720575940379279360)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-242865266607202326324835163945631, 324518553658426726783156020576256)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(931366741103611407, 360287970189639680), Symbol('skoS2')), Rational(1141194010665750957, 720575940379279360)), Mul(Rational(9, 720575940379279360), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(206970386911913646), Symbol('skoS2')), Integer(126799334518416773))), Integer(466282821249199000)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_50(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 196185/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= -196185/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (42651*skoS2/10240 + 8801/4096 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (42651*skoS2/10240 - skoSM*(126*skoS2 + 61)/40 + 48101/20480 < skoX*(20480*skoSM + skoX*(85302*skoS2 - 512*skoSM*(126*skoS2 + 61) + 48101) + 109000)/20480)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictGreaterThan(Add(Mul(Rational(42651, 10240), Symbol('skoS2')), Rational(8801, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(42651, 10240), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(48101, 20480)), Mul(Rational(1, 20480), Symbol('skoX'), Add(Mul(Integer(20480), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(85302), Symbol('skoS2')), Mul(Integer(-1), Integer(512), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(48101))), Integer(109000)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_51(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 196185/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= -242865266607202326324835163945631/324518553658426726783156020576256) & (delta >= 2 - skoS2**2) & (931366741103611407*skoS2/360287970189639680 + 1141194010665750957/720575940379279360 < 9*skoX*(skoX*(206970386911913646*skoS2 + 126799334518416773) + 466282821249199000)/720575940379279360)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-242865266607202326324835163945631, 324518553658426726783156020576256)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(931366741103611407, 360287970189639680), Symbol('skoS2')), Rational(1141194010665750957, 720575940379279360)), Mul(Rational(9, 720575940379279360), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(206970386911913646), Symbol('skoS2')), Integer(126799334518416773))), Integer(466282821249199000)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_52(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 196185/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= -196185/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (42651*skoS2/10240 + 8801/4096 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (42651*skoS2/10240 - skoSM*(126*skoS2 + 61)/40 + 48101/20480 < skoX*(20480*skoSM + skoX*(85302*skoS2 - 512*skoSM*(126*skoS2 + 61) + 48101) + 109000)/20480)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictGreaterThan(Add(Mul(Rational(42651, 10240), Symbol('skoS2')), Rational(8801, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(42651, 10240), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(48101, 20480)), Mul(Rational(1, 20480), Symbol('skoX'), Add(Mul(Integer(20480), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(85302), Symbol('skoS2')), Mul(Integer(-1), Integer(512), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(48101))), Integer(109000)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_53(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 196185/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= -242865266607202326324835163945631/324518553658426726783156020576256) & (delta >= 2 - skoS2**2) & (931366741103611407*skoS2/360287970189639680 + 1141194010665750957/720575940379279360 < 9*skoX*(skoX*(206970386911913646*skoS2 + 126799334518416773) + 466282821249199000)/720575940379279360)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-242865266607202326324835163945631, 324518553658426726783156020576256)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(931366741103611407, 360287970189639680), Symbol('skoS2')), Rational(1141194010665750957, 720575940379279360)), Mul(Rational(9, 720575940379279360), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(206970386911913646), Symbol('skoS2')), Integer(126799334518416773))), Integer(466282821249199000)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_54(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 196185/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= -196185/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (42651*skoS2/10240 + 8801/4096 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (42651*skoS2/10240 - skoSM*(126*skoS2 + 61)/40 + 48101/20480 < skoX*(20480*skoSM + skoX*(85302*skoS2 - 512*skoSM*(126*skoS2 + 61) + 48101) + 109000)/20480)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictGreaterThan(Add(Mul(Rational(42651, 10240), Symbol('skoS2')), Rational(8801, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(42651, 10240), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(48101, 20480)), Mul(Rational(1, 20480), Symbol('skoX'), Add(Mul(Integer(20480), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(85302), Symbol('skoS2')), Mul(Integer(-1), Integer(512), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(48101))), Integer(109000)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_55(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 196185/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= -242865266607202326324835163945631/324518553658426726783156020576256) & (delta >= 2 - skoS2**2) & (931366741103611407*skoS2/360287970189639680 + 1141194010665750957/720575940379279360 < 9*skoX*(skoX*(206970386911913646*skoS2 + 126799334518416773) + 466282821249199000)/720575940379279360)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-242865266607202326324835163945631, 324518553658426726783156020576256)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(931366741103611407, 360287970189639680), Symbol('skoS2')), Rational(1141194010665750957, 720575940379279360)), Mul(Rational(9, 720575940379279360), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(206970386911913646), Symbol('skoS2')), Integer(126799334518416773))), Integer(466282821249199000)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_56(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 196185/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= -196185/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (42651*skoS2/10240 + 8801/4096 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (42651*skoS2/10240 - skoSM*(126*skoS2 + 61)/40 + 48101/20480 < skoX*(20480*skoSM + skoX*(85302*skoS2 - 512*skoSM*(126*skoS2 + 61) + 48101) + 109000)/20480)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictGreaterThan(Add(Mul(Rational(42651, 10240), Symbol('skoS2')), Rational(8801, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(42651, 10240), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(48101, 20480)), Mul(Rational(1, 20480), Symbol('skoX'), Add(Mul(Integer(20480), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(85302), Symbol('skoS2')), Mul(Integer(-1), Integer(512), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(48101))), Integer(109000)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_57(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 12857201175/17179869184) & (delta >= skoS2**2 - 2) & (delta - skoX >= -196185/262144) & (delta >= 2 - skoS2**2) & (1355319*skoS2/524288 + 8303289/5242880 < 3*skoX*(skoX*(4517730*skoS2 + 2767763) + 10177960)/5242880)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(12857201175, 17179869184)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-196185, 262144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(1355319, 524288), Symbol('skoS2')), Rational(8303289, 5242880)), Mul(Rational(3, 5242880), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(4517730), Symbol('skoS2')), Integer(2767763))), Integer(10177960)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_58(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 196185/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= -196185/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (42651*skoS2/10240 + 8801/4096 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (42651*skoS2/10240 - skoSM*(126*skoS2 + 61)/40 + 48101/20480 < skoX*(20480*skoSM + skoX*(85302*skoS2 - 512*skoSM*(126*skoS2 + 61) + 48101) + 109000)/20480)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictGreaterThan(Add(Mul(Rational(42651, 10240), Symbol('skoS2')), Rational(8801, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(42651, 10240), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(48101, 20480)), Mul(Rational(1, 20480), Symbol('skoX'), Add(Mul(Integer(20480), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(85302), Symbol('skoS2')), Mul(Integer(-1), Integer(512), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(48101))), Integer(109000)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_59(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 12857201175/17179869184) & (delta >= skoS2**2 - 2) & (delta - skoX >= -196185/262144) & (delta >= 2 - skoS2**2) & (1355319*skoS2/524288 + 8303289/5242880 < 3*skoX*(skoX*(4517730*skoS2 + 2767763) + 10177960)/5242880)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(12857201175, 17179869184)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-196185, 262144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(1355319, 524288), Symbol('skoS2')), Rational(8303289, 5242880)), Mul(Rational(3, 5242880), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(4517730), Symbol('skoS2')), Integer(2767763))), Integer(10177960)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_60(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 196185/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= -196185/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (42651*skoS2/10240 + 8801/4096 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (42651*skoS2/10240 - skoSM*(126*skoS2 + 61)/40 + 48101/20480 < skoX*(20480*skoSM + skoX*(85302*skoS2 - 512*skoSM*(126*skoS2 + 61) + 48101) + 109000)/20480)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictGreaterThan(Add(Mul(Rational(42651, 10240), Symbol('skoS2')), Rational(8801, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(42651, 10240), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(48101, 20480)), Mul(Rational(1, 20480), Symbol('skoX'), Add(Mul(Integer(20480), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(85302), Symbol('skoS2')), Mul(Integer(-1), Integer(512), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(48101))), Integer(109000)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_61(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 12857201175/17179869184) & (delta >= skoS2**2 - 2) & (delta - skoX >= -196185/262144) & (delta >= 2 - skoS2**2) & (1355319*skoS2/524288 + 8303289/5242880 < 3*skoX*(skoX*(4517730*skoS2 + 2767763) + 10177960)/5242880)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(12857201175, 17179869184)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-196185, 262144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(1355319, 524288), Symbol('skoS2')), Rational(8303289, 5242880)), Mul(Rational(3, 5242880), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(4517730), Symbol('skoS2')), Integer(2767763))), Integer(10177960)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_62(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 196185/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= -196185/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (42651*skoS2/10240 + 8801/4096 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (42651*skoS2/10240 - skoSM*(126*skoS2 + 61)/40 + 48101/20480 < skoX*(20480*skoSM + skoX*(85302*skoS2 - 512*skoSM*(126*skoS2 + 61) + 48101) + 109000)/20480)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictGreaterThan(Add(Mul(Rational(42651, 10240), Symbol('skoS2')), Rational(8801, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(42651, 10240), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(48101, 20480)), Mul(Rational(1, 20480), Symbol('skoX'), Add(Mul(Integer(20480), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(85302), Symbol('skoS2')), Mul(Integer(-1), Integer(512), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(48101))), Integer(109000)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_63(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 12857201175/17179869184) & (delta >= skoS2**2 - 2) & (delta - skoX >= -196185/262144) & (delta >= 2 - skoS2**2) & (1355319*skoS2/524288 + 8303289/5242880 < 3*skoX*(skoX*(4517730*skoS2 + 2767763) + 10177960)/5242880)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(12857201175, 17179869184)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-196185, 262144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(1355319, 524288), Symbol('skoS2')), Rational(8303289, 5242880)), Mul(Rational(3, 5242880), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(4517730), Symbol('skoS2')), Integer(2767763))), Integer(10177960)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_64(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 196185/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= -196185/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (42651*skoS2/10240 + 8801/4096 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (42651*skoS2/10240 - skoSM*(126*skoS2 + 61)/40 + 48101/20480 < skoX*(20480*skoSM + skoX*(85302*skoS2 - 512*skoSM*(126*skoS2 + 61) + 48101) + 109000)/20480)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictGreaterThan(Add(Mul(Rational(42651, 10240), Symbol('skoS2')), Rational(8801, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(42651, 10240), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(48101, 20480)), Mul(Rational(1, 20480), Symbol('skoX'), Add(Mul(Integer(20480), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(85302), Symbol('skoS2')), Mul(Integer(-1), Integer(512), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(48101))), Integer(109000)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_65(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 12857201175/17179869184) & (delta >= skoS2**2 - 2) & (delta - skoX >= -196185/262144) & (delta >= 2 - skoS2**2) & (1355319*skoS2/524288 + 8303289/5242880 < 3*skoX*(skoX*(4517730*skoS2 + 2767763) + 10177960)/5242880)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(12857201175, 17179869184)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-196185, 262144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(1355319, 524288), Symbol('skoS2')), Rational(8303289, 5242880)), Mul(Rational(3, 5242880), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(4517730), Symbol('skoS2')), Integer(2767763))), Integer(10177960)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_66(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 196185/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= -196185/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (42651*skoS2/10240 + 8801/4096 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (42651*skoS2/10240 - skoSM*(126*skoS2 + 61)/40 + 48101/20480 < skoX*(20480*skoSM + skoX*(85302*skoS2 - 512*skoSM*(126*skoS2 + 61) + 48101) + 109000)/20480)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictGreaterThan(Add(Mul(Rational(42651, 10240), Symbol('skoS2')), Rational(8801, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(42651, 10240), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(48101, 20480)), Mul(Rational(1, 20480), Symbol('skoX'), Add(Mul(Integer(20480), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(85302), Symbol('skoS2')), Mul(Integer(-1), Integer(512), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(48101))), Integer(109000)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_67(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 12857201175/17179869184) & (delta >= skoS2**2 - 2) & (delta - skoX >= -196185/262144) & (delta >= 2 - skoS2**2) & (1355319*skoS2/524288 + 8303289/5242880 < 3*skoX*(skoX*(4517730*skoS2 + 2767763) + 10177960)/5242880)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(12857201175, 17179869184)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-196185, 262144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(1355319, 524288), Symbol('skoS2')), Rational(8303289, 5242880)), Mul(Rational(3, 5242880), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(4517730), Symbol('skoS2')), Integer(2767763))), Integer(10177960)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_68(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 196185/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= -196185/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (42651*skoS2/10240 + 8801/4096 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (42651*skoS2/10240 - skoSM*(126*skoS2 + 61)/40 + 48101/20480 < skoX*(20480*skoSM + skoX*(85302*skoS2 - 512*skoSM*(126*skoS2 + 61) + 48101) + 109000)/20480)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictGreaterThan(Add(Mul(Rational(42651, 10240), Symbol('skoS2')), Rational(8801, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(42651, 10240), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(48101, 20480)), Mul(Rational(1, 20480), Symbol('skoX'), Add(Mul(Integer(20480), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(85302), Symbol('skoS2')), Mul(Integer(-1), Integer(512), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(48101))), Integer(109000)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_69(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 12857201175/17179869184) & (delta >= skoS2**2 - 2) & (delta - skoX >= -196185/262144) & (delta >= 2 - skoS2**2) & (1355319*skoS2/524288 + 8303289/5242880 < 3*skoX*(skoX*(4517730*skoS2 + 2767763) + 10177960)/5242880)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(12857201175, 17179869184)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-196185, 262144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(1355319, 524288), Symbol('skoS2')), Rational(8303289, 5242880)), Mul(Rational(3, 5242880), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(4517730), Symbol('skoS2')), Integer(2767763))), Integer(10177960)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_70(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 196185/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= -196185/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (42651*skoS2/10240 + 8801/4096 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (42651*skoS2/10240 - skoSM*(126*skoS2 + 61)/40 + 48101/20480 < skoX*(20480*skoSM + skoX*(85302*skoS2 - 512*skoSM*(126*skoS2 + 61) + 48101) + 109000)/20480)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictGreaterThan(Add(Mul(Rational(42651, 10240), Symbol('skoS2')), Rational(8801, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(42651, 10240), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(48101, 20480)), Mul(Rational(1, 20480), Symbol('skoX'), Add(Mul(Integer(20480), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(85302), Symbol('skoS2')), Mul(Integer(-1), Integer(512), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(48101))), Integer(109000)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_71(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 12857201175/17179869184) & (delta >= skoS2**2 - 2) & (delta - skoX >= -196185/262144) & (delta >= 2 - skoS2**2) & (1355319*skoS2/524288 + 8303289/5242880 < 3*skoX*(skoX*(4517730*skoS2 + 2767763) + 10177960)/5242880)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(12857201175, 17179869184)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-196185, 262144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(1355319, 524288), Symbol('skoS2')), Rational(8303289, 5242880)), Mul(Rational(3, 5242880), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(4517730), Symbol('skoS2')), Integer(2767763))), Integer(10177960)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_72(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 196185/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= -196185/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (42651*skoS2/10240 + 8801/4096 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (42651*skoS2/10240 - skoSM*(126*skoS2 + 61)/40 + 48101/20480 < skoX*(20480*skoSM + skoX*(85302*skoS2 - 512*skoSM*(126*skoS2 + 61) + 48101) + 109000)/20480)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictGreaterThan(Add(Mul(Rational(42651, 10240), Symbol('skoS2')), Rational(8801, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(42651, 10240), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(48101, 20480)), Mul(Rational(1, 20480), Symbol('skoX'), Add(Mul(Integer(20480), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(85302), Symbol('skoS2')), Mul(Integer(-1), Integer(512), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(48101))), Integer(109000)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_73(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 12857201175/17179869184) & (delta >= skoS2**2 - 2) & (delta - skoX >= -196185/262144) & (delta >= 2 - skoS2**2) & (1355319*skoS2/524288 + 8303289/5242880 < 3*skoX*(skoX*(4517730*skoS2 + 2767763) + 10177960)/5242880)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(12857201175, 17179869184)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-196185, 262144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(1355319, 524288), Symbol('skoS2')), Rational(8303289, 5242880)), Mul(Rational(3, 5242880), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(4517730), Symbol('skoS2')), Integer(2767763))), Integer(10177960)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_74(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 196185/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= -196185/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (42651*skoS2/10240 + 8801/4096 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (42651*skoS2/10240 - skoSM*(126*skoS2 + 61)/40 + 48101/20480 < skoX*(20480*skoSM + skoX*(85302*skoS2 - 512*skoSM*(126*skoS2 + 61) + 48101) + 109000)/20480)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictGreaterThan(Add(Mul(Rational(42651, 10240), Symbol('skoS2')), Rational(8801, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(42651, 10240), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(48101, 20480)), Mul(Rational(1, 20480), Symbol('skoX'), Add(Mul(Integer(20480), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(85302), Symbol('skoS2')), Mul(Integer(-1), Integer(512), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(48101))), Integer(109000)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_75(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 12857201175/17179869184) & (delta >= skoS2**2 - 2) & (delta - skoX >= -196185/262144) & (delta >= 2 - skoS2**2) & (1355319*skoS2/524288 + 8303289/5242880 < 3*skoX*(skoX*(4517730*skoS2 + 2767763) + 10177960)/5242880)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(12857201175, 17179869184)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-196185, 262144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(1355319, 524288), Symbol('skoS2')), Rational(8303289, 5242880)), Mul(Rational(3, 5242880), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(4517730), Symbol('skoS2')), Integer(2767763))), Integer(10177960)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_76(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 196185/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= -196185/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (42651*skoS2/10240 + 8801/4096 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (42651*skoS2/10240 - skoSM*(126*skoS2 + 61)/40 + 48101/20480 < skoX*(20480*skoSM + skoX*(85302*skoS2 - 512*skoSM*(126*skoS2 + 61) + 48101) + 109000)/20480)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictGreaterThan(Add(Mul(Rational(42651, 10240), Symbol('skoS2')), Rational(8801, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(42651, 10240), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(48101, 20480)), Mul(Rational(1, 20480), Symbol('skoX'), Add(Mul(Integer(20480), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(85302), Symbol('skoS2')), Mul(Integer(-1), Integer(512), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(48101))), Integer(109000)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_77(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 12857201175/17179869184) & (delta >= skoS2**2 - 2) & (delta - skoX >= -196185/262144) & (delta >= 2 - skoS2**2) & (1355319*skoS2/524288 + 8303289/5242880 < 3*skoX*(skoX*(4517730*skoS2 + 2767763) + 10177960)/5242880)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(12857201175, 17179869184)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-196185, 262144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(1355319, 524288), Symbol('skoS2')), Rational(8303289, 5242880)), Mul(Rational(3, 5242880), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(4517730), Symbol('skoS2')), Integer(2767763))), Integer(10177960)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_78(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 196185/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= -196185/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (42651*skoS2/10240 + 8801/4096 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (42651*skoS2/10240 - skoSM*(126*skoS2 + 61)/40 + 48101/20480 < skoX*(20480*skoSM + skoX*(85302*skoS2 - 512*skoSM*(126*skoS2 + 61) + 48101) + 109000)/20480)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictGreaterThan(Add(Mul(Rational(42651, 10240), Symbol('skoS2')), Rational(8801, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(42651, 10240), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(48101, 20480)), Mul(Rational(1, 20480), Symbol('skoX'), Add(Mul(Integer(20480), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(85302), Symbol('skoS2')), Mul(Integer(-1), Integer(512), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(48101))), Integer(109000)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_79(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 12857201175/17179869184) & (delta >= skoS2**2 - 2) & (delta - skoX >= -196185/262144) & (delta >= 2 - skoS2**2) & (1355319*skoS2/524288 + 8303289/5242880 < 3*skoX*(skoX*(4517730*skoS2 + 2767763) + 10177960)/5242880)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(12857201175, 17179869184)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-196185, 262144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(1355319, 524288), Symbol('skoS2')), Rational(8303289, 5242880)), Mul(Rational(3, 5242880), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(4517730), Symbol('skoS2')), Integer(2767763))), Integer(10177960)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_80(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 196185/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= -196185/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (42651*skoS2/10240 + 8801/4096 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (42651*skoS2/10240 - skoSM*(126*skoS2 + 61)/40 + 48101/20480 < skoX*(20480*skoSM + skoX*(85302*skoS2 - 512*skoSM*(126*skoS2 + 61) + 48101) + 109000)/20480)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictGreaterThan(Add(Mul(Rational(42651, 10240), Symbol('skoS2')), Rational(8801, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(42651, 10240), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(48101, 20480)), Mul(Rational(1, 20480), Symbol('skoX'), Add(Mul(Integer(20480), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(85302), Symbol('skoS2')), Mul(Integer(-1), Integer(512), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(48101))), Integer(109000)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_81(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 12857201175/17179869184) & (delta >= skoS2**2 - 2) & (delta - skoX >= -196185/262144) & (delta >= 2 - skoS2**2) & (1355319*skoS2/524288 + 8303289/5242880 < 3*skoX*(skoX*(4517730*skoS2 + 2767763) + 10177960)/5242880)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(12857201175, 17179869184)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-196185, 262144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(1355319, 524288), Symbol('skoS2')), Rational(8303289, 5242880)), Mul(Rational(3, 5242880), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(4517730), Symbol('skoS2')), Integer(2767763))), Integer(10177960)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_82(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 196185/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= -196185/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (42651*skoS2/10240 + 8801/4096 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (42651*skoS2/10240 - skoSM*(126*skoS2 + 61)/40 + 48101/20480 < skoX*(20480*skoSM + skoX*(85302*skoS2 - 512*skoSM*(126*skoS2 + 61) + 48101) + 109000)/20480)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictGreaterThan(Add(Mul(Rational(42651, 10240), Symbol('skoS2')), Rational(8801, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(42651, 10240), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(48101, 20480)), Mul(Rational(1, 20480), Symbol('skoX'), Add(Mul(Integer(20480), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(85302), Symbol('skoS2')), Mul(Integer(-1), Integer(512), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(48101))), Integer(109000)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_83(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 12857201175/17179869184) & (delta >= skoS2**2 - 2) & (delta - skoX >= -196185/262144) & (delta >= 2 - skoS2**2) & (1355319*skoS2/524288 + 8303289/5242880 < 3*skoX*(skoX*(4517730*skoS2 + 2767763) + 10177960)/5242880)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(12857201175, 17179869184)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-196185, 262144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(1355319, 524288), Symbol('skoS2')), Rational(8303289, 5242880)), Mul(Rational(3, 5242880), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(4517730), Symbol('skoS2')), Integer(2767763))), Integer(10177960)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_84(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 196185/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= -196185/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (42651*skoS2/10240 + 8801/4096 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (42651*skoS2/10240 - skoSM*(126*skoS2 + 61)/40 + 48101/20480 < skoX*(20480*skoSM + skoX*(85302*skoS2 - 512*skoSM*(126*skoS2 + 61) + 48101) + 109000)/20480)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-196185, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictGreaterThan(Add(Mul(Rational(42651, 10240), Symbol('skoS2')), Rational(8801, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(42651, 10240), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(48101, 20480)), Mul(Rational(1, 20480), Symbol('skoX'), Add(Mul(Integer(20480), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(85302), Symbol('skoS2')), Mul(Integer(-1), Integer(512), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(48101))), Integer(109000)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_85(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 12857201175/17179869184) & (delta >= skoS2**2 - 2) & (delta - skoX >= -196185/262144) & (delta >= 2 - skoS2**2) & (1355319*skoS2/524288 + 8303289/5242880 < 3*skoX*(skoX*(4517730*skoS2 + 2767763) + 10177960)/5242880)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(12857201175, 17179869184)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-196185, 262144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), StrictLessThan(Add(Mul(Rational(1355319, 524288), Symbol('skoS2')), Rational(8303289, 5242880)), Mul(Rational(3, 5242880), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(4517730), Symbol('skoS2')), Integer(2767763))), Integer(10177960)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(delta:sympy.Rational, skoX:sympy.Rational, skoS2:sympy.Rational, skoSP:sympy.Rational, skoSM:sympy.Rational):
	# (0 <= delta) & (1 > skoX) & (skoS2 > 0) & (skoSM > 0) & (skoSP > 0) & (skoX > 0) & (skoS2**2 - 2 <= delta) & (skoSM**2 + skoX - 1 <= delta) & (2 - skoS2**2 <= delta) & (-skoSP**2 + skoX + 1 <= delta) & (skoSP**2 - skoX - 1 <= delta) & (-skoSM**2 - skoX + 1 <= delta) & (skoSP*(63*skoS2/20 + 13/8) > skoSM*(63*skoS2/20 + 61/40) - 1/5) & (skoX*(skoSM + skoSP + skoX*(skoSM*(-63*skoS2/20 - 61/40) + skoSP*(63*skoS2/20 + 13/8) + 1/5) + 4) > skoSM*(-63*skoS2/20 - 61/40) + skoSP*(63*skoS2/20 + 13/8) + 1/5)

	post_cond =  And(LessThan(Integer(0), Symbol('delta')), StrictGreaterThan(Integer(1), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoSP'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), LessThan(Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Symbol('delta')), LessThan(Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1)), Symbol('delta')), LessThan(Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Symbol('delta')), LessThan(Add(Mul(Integer(-1), Pow(Symbol('skoSP'), Integer(2))), Symbol('skoX'), Integer(1)), Symbol('delta')), LessThan(Add(Pow(Symbol('skoSP'), Integer(2)), Mul(Integer(-1), Symbol('skoX')), Integer(-1)), Symbol('delta')), LessThan(Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)), Symbol('delta')), StrictGreaterThan(Mul(Symbol('skoSP'), Add(Mul(Rational(63, 20), Symbol('skoS2')), Rational(13, 8))), Add(Mul(Symbol('skoSM'), Add(Mul(Rational(63, 20), Symbol('skoS2')), Rational(61, 40))), Rational(-1, 5))), StrictGreaterThan(Mul(Symbol('skoX'), Add(Symbol('skoSM'), Symbol('skoSP'), Mul(Symbol('skoX'), Add(Mul(Symbol('skoSM'), Add(Mul(Integer(-1), Rational(63, 20), Symbol('skoS2')), Rational(-61, 40))), Mul(Symbol('skoSP'), Add(Mul(Rational(63, 20), Symbol('skoS2')), Rational(13, 8))), Rational(1, 5))), Integer(4))), Add(Mul(Symbol('skoSM'), Add(Mul(Integer(-1), Rational(63, 20), Symbol('skoS2')), Rational(-61, 40))), Mul(Symbol('skoSP'), Add(Mul(Rational(63, 20), Symbol('skoS2')), Rational(13, 8))), Rational(1, 5))))

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
		print('delta = 1/8')
		print('skoX = 1/2')
		print('skoS2 = 11/8')
		print('skoSM = 3/4')
		print('skoSP = 5/4')
		exit(0)
	
	
	if pre_condition_5(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_5 SAT")
		print('delta = 1/8')
		print('skoX = 1/2')
		print('skoS2 = 11/8')
		print('skoSM = 3/4')
		print('skoSP = 5/4')
		exit(0)
	
	
	if pre_condition_6(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_6 SAT")
		print('delta = 5/32')
		print('skoX = 3/4')
		print('skoS2 = 11/8')
		print('skoSM = 1/2')
		print('skoSP = 11/8')
		exit(0)
	
	
	if pre_condition_7(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_7 SAT")
		print('delta = 5/32')
		print('skoX = 3/4')
		print('skoS2 = 11/8')
		print('skoSM = 1/2')
		print('skoSP = 11/8')
		exit(0)
	
	
	if pre_condition_8(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_8 SAT")
		print('delta = 1/8')
		print('skoX = 3/4')
		print('skoS2 = 11/8')
		print('skoSM = 1/2')
		print('skoSP = 21/16')
		exit(0)
	
	
	if pre_condition_9(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_9 SAT")
		print('delta = 1/8')
		print('skoX = 3/4')
		print('skoS2 = 11/8')
		print('skoSM = 1/2')
		print('skoSP = 21/16')
		exit(0)
	
	
	if pre_condition_10(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_10 SAT")
		print('delta = 5/512')
		print('skoX = 47/64')
		print('skoS2 = 181/128')
		print('skoSM = 33/64')
		print('skoSP = 169/128')
		exit(0)
	
	
	if pre_condition_11(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_11 SAT")
		print('delta = 5/512')
		print('skoX = 47/64')
		print('skoS2 = 181/128')
		print('skoSM = 33/64')
		print('skoSP = 169/128')
		exit(0)
	
	
	if pre_condition_12(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_12 SAT")
		print('delta = 5/2048')
		print('skoX = 191/256')
		print('skoS2 = 181/128')
		print('skoSM = 129/256')
		print('skoSP = 677/512')
		exit(0)
	
	
	if pre_condition_13(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_13 SAT")
		print('delta = 5/2048')
		print('skoX = 191/256')
		print('skoS2 = 181/128')
		print('skoSM = 129/256')
		print('skoSP = 677/512')
		exit(0)
	
	
	if pre_condition_14(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_14 SAT")
		print('delta = 45904610459649/72057594037927936')
		print('skoX = 767/1024')
		print('skoS2 = 181/128')
		print('skoSM = 513/1024')
		print('skoSP = 677/512')
		exit(0)
	
	
	if pre_condition_15(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_15 SAT")
		print('delta = 45904610459649/72057594037927936')
		print('skoX = 767/1024')
		print('skoS2 = 181/128')
		print('skoSM = 513/1024')
		print('skoSP = 677/512')
		exit(0)
	
	
	if pre_condition_16(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_16 SAT")
		print('delta = 10720238370817/72057594037927936')
		print('skoX = 1533/2048')
		print('skoS2 = 11585/8192')
		print('skoSM = 1027/2048')
		print('skoSP = 677/512')
		exit(0)
	
	
	if pre_condition_17(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_17 SAT")
		print('delta = 10720238370817/72057594037927936')
		print('skoX = 1533/2048')
		print('skoS2 = 11585/8192')
		print('skoSM = 1027/2048')
		print('skoSP = 677/512')
		exit(0)
	
	
	if pre_condition_18(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_18 SAT")
		print('delta = 1924145348609/72057594037927936')
		print('skoX = 6131/8192')
		print('skoS2 = 46341/32768')
		print('skoSM = 4109/8192')
		print('skoSP = 677/512')
		exit(0)
	
	
	if pre_condition_19(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_19 SAT")
		print('delta = 1924145348609/72057594037927936')
		print('skoX = 6131/8192')
		print('skoS2 = 46341/32768')
		print('skoSM = 4109/8192')
		print('skoSP = 677/512')
		exit(0)
	
	
	if pre_condition_20(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_20 SAT")
		print('delta = 824633720833/72057594037927936')
		print('skoX = 49047/65536')
		print('skoS2 = 46341/32768')
		print('skoSM = 32873/65536')
		print('skoSP = 677/512')
		exit(0)
	
	
	if pre_condition_21(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_21 SAT")
		print('delta = 824633720833/72057594037927936')
		print('skoX = 49047/65536')
		print('skoS2 = 46341/32768')
		print('skoSM = 32873/65536')
		print('skoSP = 677/512')
		exit(0)
	
	
	if pre_condition_22(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_22 SAT")
		print('delta = 274877906945/72057594037927936')
		print('skoX = 98093/131072')
		print('skoS2 = 741455/524288')
		print('skoSM = 65747/131072')
		print('skoSP = 677/512')
		exit(0)
	
	
	if pre_condition_23(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_23 SAT")
		print('delta = 274877906945/72057594037927936')
		print('skoX = 98093/131072')
		print('skoS2 = 741455/524288')
		print('skoSM = 65747/131072')
		print('skoSP = 677/512')
		exit(0)
	
	
	if pre_condition_24(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_24 SAT")
		print('delta = 1/72057594037927936')
		print('skoX = 196185/262144')
		print('skoS2 = 101904826760412361/72057594037927936')
		print('skoSM = 9036220839002575/18014398509481984')
		print('skoSP = 677/512')
		exit(0)
	
	
	if pre_condition_25(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_25 SAT")
		print('delta = 1/72057594037927936')
		print('skoX = 196185/262144')
		print('skoS2 = 101904826760412361/72057594037927936')
		print('skoSM = 9036220839002575/18014398509481984')
		print('skoSP = 677/512')
		exit(0)
	
	
	if pre_condition_26(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_26 SAT")
		print('delta = 1/72057594037927936')
		print('skoX = 196185/262144')
		print('skoS2 = 101904826760412361/72057594037927936')
		print('skoSM = 9036220839002575/18014398509481984')
		print('skoSP = 677/512')
		exit(0)
	
	
	if pre_condition_27(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_27 SAT")
		print('delta = 1/72057594037927936')
		print('skoX = 196185/262144')
		print('skoS2 = 101904826760412361/72057594037927936')
		print('skoSM = 9036220839002575/18014398509481984')
		print('skoSP = 677/512')
		exit(0)
	
	
	if pre_condition_28(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_28 SAT")
		print('delta = 1/72057594037927936')
		print('skoX = 196185/262144')
		print('skoS2 = 101904826760412361/72057594037927936')
		print('skoSM = 9036220839002575/18014398509481984')
		print('skoSP = 677/512')
		exit(0)
	
	
	if pre_condition_29(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_29 SAT")
		print('delta = 1/72057594037927936')
		print('skoX = 196185/262144')
		print('skoS2 = 101904826760412361/72057594037927936')
		print('skoSM = 9036220839002575/18014398509481984')
		print('skoSP = 677/512')
		exit(0)
	
	
	if pre_condition_30(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_30 SAT")
		print('delta = 1/72057594037927936')
		print('skoX = 196185/262144')
		print('skoS2 = 101904826760412361/72057594037927936')
		print('skoSM = 9036220839002575/18014398509481984')
		print('skoSP = 677/512')
		exit(0)
	
	
	if pre_condition_31(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_31 SAT")
		print('delta = 1/72057594037927936')
		print('skoX = 196185/262144')
		print('skoS2 = 101904826760412361/72057594037927936')
		print('skoSM = 9036220839002575/18014398509481984')
		print('skoSP = 677/512')
		exit(0)
	
	
	if pre_condition_32(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_32 SAT")
		print('delta = 1/72057594037927936')
		print('skoX = 196185/262144')
		print('skoS2 = 101904826760412361/72057594037927936')
		print('skoSM = 9036220839002575/18014398509481984')
		print('skoSP = 677/512')
		exit(0)
	
	
	if pre_condition_33(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_33 SAT")
		print('delta = 1/72057594037927936')
		print('skoX = 196185/262144')
		print('skoS2 = 101904826760412361/72057594037927936')
		print('skoSM = 9036220839002575/18014398509481984')
		print('skoSP = 677/512')
		exit(0)
	
	
	if pre_condition_34(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_34 SAT")
		print('delta = 1/72057594037927936')
		print('skoX = 196185/262144')
		print('skoS2 = 101904826760412361/72057594037927936')
		print('skoSM = 9036220839002575/18014398509481984')
		print('skoSP = 677/512')
		exit(0)
	
	
	if pre_condition_35(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_35 SAT")
		print('delta = 1/72057594037927936')
		print('skoX = 196185/262144')
		print('skoS2 = 101904826760412361/72057594037927936')
		print('skoSM = 9036220839002575/18014398509481984')
		print('skoSP = 677/512')
		exit(0)
	
	
	if pre_condition_36(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_36 SAT")
		print('delta = 1/72057594037927936')
		print('skoX = 196185/262144')
		print('skoS2 = 101904826760412361/72057594037927936')
		print('skoSM = 9036220839002575/18014398509481984')
		print('skoSP = 677/512')
		exit(0)
	
	
	if pre_condition_37(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_37 SAT")
		print('delta = 1/72057594037927936')
		print('skoX = 196185/262144')
		print('skoS2 = 101904826760412361/72057594037927936')
		print('skoSM = 9036220839002575/18014398509481984')
		print('skoSP = 677/512')
		exit(0)
	
	
	if pre_condition_38(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_38 SAT")
		print('delta = 1/72057594037927936')
		print('skoX = 196185/262144')
		print('skoS2 = 101904826760412361/72057594037927936')
		print('skoSM = 9036220839002575/18014398509481984')
		print('skoSP = 677/512')
		exit(0)
	
	
	if pre_condition_39(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_39 SAT")
		print('delta = 1/72057594037927936')
		print('skoX = 196185/262144')
		print('skoS2 = 101904826760412361/72057594037927936')
		print('skoSM = 9036220839002575/18014398509481984')
		print('skoSP = 677/512')
		exit(0)
	
	
	if pre_condition_40(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_40 SAT")
		print('delta = 1/72057594037927936')
		print('skoX = 196185/262144')
		print('skoS2 = 101904826760412361/72057594037927936')
		print('skoSM = 9036220839002575/18014398509481984')
		print('skoSP = 677/512')
		exit(0)
	
	
	if pre_condition_41(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_41 SAT")
		print('delta = 1/72057594037927936')
		print('skoX = 196185/262144')
		print('skoS2 = 101904826760412361/72057594037927936')
		print('skoSM = 9036220839002575/18014398509481984')
		print('skoSP = 677/512')
		exit(0)
	
	
	if pre_condition_42(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_42 SAT")
		print('delta = 1/72057594037927936')
		print('skoX = 196185/262144')
		print('skoS2 = 101904826760412361/72057594037927936')
		print('skoSM = 9036220839002575/18014398509481984')
		print('skoSP = 677/512')
		exit(0)
	
	
	if pre_condition_43(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_43 SAT")
		print('delta = 1/72057594037927936')
		print('skoX = 196185/262144')
		print('skoS2 = 101904826760412361/72057594037927936')
		print('skoSM = 9036220839002575/18014398509481984')
		print('skoSP = 677/512')
		exit(0)
	
	
	if pre_condition_44(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_44 SAT")
		print('delta = 1/72057594037927936')
		print('skoX = 196185/262144')
		print('skoS2 = 101904826760412361/72057594037927936')
		print('skoSM = 9036220839002575/18014398509481984')
		print('skoSP = 677/512')
		exit(0)
	
	
	if pre_condition_45(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_45 SAT")
		print('delta = 1/72057594037927936')
		print('skoX = 196185/262144')
		print('skoS2 = 101904826760412361/72057594037927936')
		print('skoSM = 9036220839002575/18014398509481984')
		print('skoSP = 677/512')
		exit(0)
	
	
	if pre_condition_46(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_46 SAT")
		print('delta = 1/72057594037927936')
		print('skoX = 196185/262144')
		print('skoS2 = 101904826760412361/72057594037927936')
		print('skoSM = 9036220839002575/18014398509481984')
		print('skoSP = 677/512')
		exit(0)
	
	
	if pre_condition_47(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_47 SAT")
		print('delta = 1/72057594037927936')
		print('skoX = 196185/262144')
		print('skoS2 = 101904826760412361/72057594037927936')
		print('skoSM = 9036220839002575/18014398509481984')
		print('skoSP = 677/512')
		exit(0)
	
	
	if pre_condition_48(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_48 SAT")
		print('delta = 1/72057594037927936')
		print('skoX = 196185/262144')
		print('skoS2 = 101904826760412361/72057594037927936')
		print('skoSM = 9036220839002575/18014398509481984')
		print('skoSP = 677/512')
		exit(0)
	
	
	if pre_condition_49(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_49 SAT")
		print('delta = 1/72057594037927936')
		print('skoX = 196185/262144')
		print('skoS2 = 101904826760412361/72057594037927936')
		print('skoSM = 9036220839002575/18014398509481984')
		print('skoSP = 677/512')
		exit(0)
	
	
	if pre_condition_50(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_50 SAT")
		print('delta = 1/72057594037927936')
		print('skoX = 196185/262144')
		print('skoS2 = 101904826760412361/72057594037927936')
		print('skoSM = 9036220839002575/18014398509481984')
		print('skoSP = 677/512')
		exit(0)
	
	
	if pre_condition_51(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_51 SAT")
		print('delta = 1/72057594037927936')
		print('skoX = 196185/262144')
		print('skoS2 = 101904826760412361/72057594037927936')
		print('skoSM = 9036220839002575/18014398509481984')
		print('skoSP = 677/512')
		exit(0)
	
	
	if pre_condition_52(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_52 SAT")
		print('delta = 1/72057594037927936')
		print('skoX = 196185/262144')
		print('skoS2 = 101904826760412361/72057594037927936')
		print('skoSM = 9036220839002575/18014398509481984')
		print('skoSP = 677/512')
		exit(0)
	
	
	if pre_condition_53(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_53 SAT")
		print('delta = 1/72057594037927936')
		print('skoX = 196185/262144')
		print('skoS2 = 101904826760412361/72057594037927936')
		print('skoSM = 9036220839002575/18014398509481984')
		print('skoSP = 677/512')
		exit(0)
	
	
	if pre_condition_54(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_54 SAT")
		print('delta = 1/72057594037927936')
		print('skoX = 196185/262144')
		print('skoS2 = 101904826760412361/72057594037927936')
		print('skoSM = 9036220839002575/18014398509481984')
		print('skoSP = 677/512')
		exit(0)
	
	
	if pre_condition_55(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_55 SAT")
		print('delta = 1/72057594037927936')
		print('skoX = 196185/262144')
		print('skoS2 = 101904826760412361/72057594037927936')
		print('skoSM = 9036220839002575/18014398509481984')
		print('skoSP = 677/512')
		exit(0)
	
	
	if pre_condition_56(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_56 SAT")
		print('delta = 274877906945/72057594037927936')
		print('skoX = 98093/131072')
		print('skoS2 = 741455/524288')
		print('skoSM = 65747/131072')
		print('skoSP = 677/512')
		exit(0)
	
	
	if pre_condition_57(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_57 SAT")
		print('delta = 274877906945/72057594037927936')
		print('skoX = 98093/131072')
		print('skoS2 = 741455/524288')
		print('skoSM = 65747/131072')
		print('skoSP = 677/512')
		exit(0)
	
	
	if pre_condition_58(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_58 SAT")
		print('delta = 274877906945/72057594037927936')
		print('skoX = 98093/131072')
		print('skoS2 = 741455/524288')
		print('skoSM = 65747/131072')
		print('skoSP = 677/512')
		exit(0)
	
	
	if pre_condition_59(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_59 SAT")
		print('delta = 274877906945/72057594037927936')
		print('skoX = 98093/131072')
		print('skoS2 = 741455/524288')
		print('skoSM = 65747/131072')
		print('skoSP = 677/512')
		exit(0)
	
	
	if pre_condition_60(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_60 SAT")
		print('delta = 274877906945/72057594037927936')
		print('skoX = 98093/131072')
		print('skoS2 = 741455/524288')
		print('skoSM = 65747/131072')
		print('skoSP = 677/512')
		exit(0)
	
	
	if pre_condition_61(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_61 SAT")
		print('delta = 274877906945/72057594037927936')
		print('skoX = 98093/131072')
		print('skoS2 = 741455/524288')
		print('skoSM = 65747/131072')
		print('skoSP = 677/512')
		exit(0)
	
	
	if pre_condition_62(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_62 SAT")
		print('delta = 274877906945/72057594037927936')
		print('skoX = 98093/131072')
		print('skoS2 = 741455/524288')
		print('skoSM = 65747/131072')
		print('skoSP = 677/512')
		exit(0)
	
	
	if pre_condition_63(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_63 SAT")
		print('delta = 274877906945/72057594037927936')
		print('skoX = 98093/131072')
		print('skoS2 = 741455/524288')
		print('skoSM = 65747/131072')
		print('skoSP = 677/512')
		exit(0)
	
	
	if pre_condition_64(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_64 SAT")
		print('delta = 274877906945/72057594037927936')
		print('skoX = 98093/131072')
		print('skoS2 = 741455/524288')
		print('skoSM = 65747/131072')
		print('skoSP = 677/512')
		exit(0)
	
	
	if pre_condition_65(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_65 SAT")
		print('delta = 274877906945/72057594037927936')
		print('skoX = 98093/131072')
		print('skoS2 = 741455/524288')
		print('skoSM = 65747/131072')
		print('skoSP = 677/512')
		exit(0)
	
	
	if pre_condition_66(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_66 SAT")
		print('delta = 274877906945/72057594037927936')
		print('skoX = 98093/131072')
		print('skoS2 = 741455/524288')
		print('skoSM = 65747/131072')
		print('skoSP = 677/512')
		exit(0)
	
	
	if pre_condition_67(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_67 SAT")
		print('delta = 274877906945/72057594037927936')
		print('skoX = 98093/131072')
		print('skoS2 = 741455/524288')
		print('skoSM = 65747/131072')
		print('skoSP = 677/512')
		exit(0)
	
	
	if pre_condition_68(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_68 SAT")
		print('delta = 274877906945/72057594037927936')
		print('skoX = 98093/131072')
		print('skoS2 = 741455/524288')
		print('skoSM = 65747/131072')
		print('skoSP = 677/512')
		exit(0)
	
	
	if pre_condition_69(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_69 SAT")
		print('delta = 274877906945/72057594037927936')
		print('skoX = 98093/131072')
		print('skoS2 = 741455/524288')
		print('skoSM = 65747/131072')
		print('skoSP = 677/512')
		exit(0)
	
	
	if pre_condition_70(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_70 SAT")
		print('delta = 274877906945/72057594037927936')
		print('skoX = 98093/131072')
		print('skoS2 = 741455/524288')
		print('skoSM = 65747/131072')
		print('skoSP = 677/512')
		exit(0)
	
	
	if pre_condition_71(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_71 SAT")
		print('delta = 274877906945/72057594037927936')
		print('skoX = 98093/131072')
		print('skoS2 = 741455/524288')
		print('skoSM = 65747/131072')
		print('skoSP = 677/512')
		exit(0)
	
	
	if pre_condition_72(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_72 SAT")
		print('delta = 274877906945/72057594037927936')
		print('skoX = 98093/131072')
		print('skoS2 = 741455/524288')
		print('skoSM = 65747/131072')
		print('skoSP = 677/512')
		exit(0)
	
	
	if pre_condition_73(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_73 SAT")
		print('delta = 274877906945/72057594037927936')
		print('skoX = 98093/131072')
		print('skoS2 = 741455/524288')
		print('skoSM = 65747/131072')
		print('skoSP = 677/512')
		exit(0)
	
	
	if pre_condition_74(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_74 SAT")
		print('delta = 274877906945/72057594037927936')
		print('skoX = 98093/131072')
		print('skoS2 = 741455/524288')
		print('skoSM = 65747/131072')
		print('skoSP = 677/512')
		exit(0)
	
	
	if pre_condition_75(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_75 SAT")
		print('delta = 274877906945/72057594037927936')
		print('skoX = 98093/131072')
		print('skoS2 = 741455/524288')
		print('skoSM = 65747/131072')
		print('skoSP = 677/512')
		exit(0)
	
	
	if pre_condition_76(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_76 SAT")
		print('delta = 274877906945/72057594037927936')
		print('skoX = 98093/131072')
		print('skoS2 = 741455/524288')
		print('skoSM = 65747/131072')
		print('skoSP = 677/512')
		exit(0)
	
	
	if pre_condition_77(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_77 SAT")
		print('delta = 274877906945/72057594037927936')
		print('skoX = 98093/131072')
		print('skoS2 = 741455/524288')
		print('skoSM = 65747/131072')
		print('skoSP = 677/512')
		exit(0)
	
	
	if pre_condition_78(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_78 SAT")
		print('delta = 274877906945/72057594037927936')
		print('skoX = 98093/131072')
		print('skoS2 = 741455/524288')
		print('skoSM = 65747/131072')
		print('skoSP = 677/512')
		exit(0)
	
	
	if pre_condition_79(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_79 SAT")
		print('delta = 274877906945/72057594037927936')
		print('skoX = 98093/131072')
		print('skoS2 = 741455/524288')
		print('skoSM = 65747/131072')
		print('skoSP = 677/512')
		exit(0)
	
	
	if pre_condition_80(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_80 SAT")
		print('delta = 274877906945/72057594037927936')
		print('skoX = 98093/131072')
		print('skoS2 = 741455/524288')
		print('skoSM = 65747/131072')
		print('skoSP = 677/512')
		exit(0)
	
	
	if pre_condition_81(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_81 SAT")
		print('delta = 274877906945/72057594037927936')
		print('skoX = 98093/131072')
		print('skoS2 = 741455/524288')
		print('skoSM = 65747/131072')
		print('skoSP = 677/512')
		exit(0)
	
	
	if pre_condition_82(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_82 SAT")
		print('delta = 274877906945/72057594037927936')
		print('skoX = 98093/131072')
		print('skoS2 = 741455/524288')
		print('skoSM = 65747/131072')
		print('skoSP = 677/512')
		exit(0)
	
	
	if pre_condition_83(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_83 SAT")
		print('delta = 274877906945/72057594037927936')
		print('skoX = 98093/131072')
		print('skoS2 = 741455/524288')
		print('skoSM = 65747/131072')
		print('skoSP = 677/512')
		exit(0)
	
	
	if pre_condition_84(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_84 SAT")
		print('delta = 274877906945/72057594037927936')
		print('skoX = 98093/131072')
		print('skoS2 = 741455/524288')
		print('skoSM = 65747/131072')
		print('skoSP = 677/512')
		exit(0)
	
	
	if pre_condition_85(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_85 SAT")
		print('delta = 274877906945/72057594037927936')
		print('skoX = 98093/131072')
		print('skoS2 = 741455/524288')
		print('skoSM = 65747/131072')
		print('skoSP = 677/512')
		exit(0)


	print("UNKNOWN")
	exit(0)
