import sympy
from sympy import *

def pre_condition_0(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= -3/4) & (delta >= skoS2**2 - 2) & (delta - skoX >= 3/4) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (63*skoS2/40 + 13/16 < skoSM*(126*skoS2 + 61)/40 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-3, 4)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(3, 4)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(63, 40), Symbol('skoS2')), Rational(13, 16)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= skoX) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -3/4) & (delta >= skoS2**2 - 2) & (delta - skoX >= 3/4) & (delta >= 2 - skoS2**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-3, 4)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(3, 4)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= -7/16) & (delta >= skoS2**2 - 2) & (delta - skoX >= 7/16) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (189*skoS2/80 + 39/32 < skoSM*(126*skoS2 + 61)/40 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-7, 16)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(7, 16)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(189, 80), Symbol('skoS2')), Rational(39, 32)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= skoX) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -7/16) & (delta >= skoS2**2 - 2) & (delta - skoX >= 7/16) & (delta >= 2 - skoS2**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-7, 16)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(7, 16)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_4(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= -15/64) & (delta >= skoS2**2 - 2) & (delta - skoX >= 15/64) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (441*skoS2/160 + 91/64 < skoSM*(126*skoS2 + 61)/40 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-15, 64)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(15, 64)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(441, 160), Symbol('skoS2')), Rational(91, 64)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_5(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= skoX) & (skoS2 > 31/126) & (skoX > 0) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -15/64) & (delta >= skoS2**2 - 2) & (delta - skoX >= 15/64) & (delta >= 2 - skoS2**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Rational(31, 126)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-15, 64)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(15, 64)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_6(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= -183/1024) & (delta >= skoS2**2 - 2) & (delta - skoX >= 183/1024) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (1827*skoS2/640 + 377/256 < skoSM*(126*skoS2 + 61)/40 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-183, 1024)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(183, 1024)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(1827, 640), Symbol('skoS2')), Rational(377, 256)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_7(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= skoX) & (skoS2 > 1/2) & (skoX > 0) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -183/1024) & (delta >= skoS2**2 - 2) & (delta - skoX >= 183/1024) & (delta >= 2 - skoS2**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Rational(1, 2)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-183, 1024)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(183, 1024)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_8(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= -615/4096) & (delta >= skoS2**2 - 2) & (delta - skoX >= 615/4096) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (3717*skoS2/1280 + 767/512 < skoSM*(126*skoS2 + 61)/40 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-615, 4096)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(615, 4096)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(3717, 1280), Symbol('skoS2')), Rational(767, 512)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_9(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= skoX) & (skoS2 > 443/630) & (skoX > 0) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -615/4096) & (delta >= skoS2**2 - 2) & (delta - skoX >= 615/4096) & (delta >= 2 - skoS2**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Rational(443, 630)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-615, 4096)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(615, 4096)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_10(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= -2223/16384) & (delta >= skoS2**2 - 2) & (delta - skoX >= 2223/16384) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (7497*skoS2/2560 + 1547/1024 < skoSM*(126*skoS2 + 61)/40 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-2223, 16384)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(2223, 16384)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(7497, 2560), Symbol('skoS2')), Rational(1547, 1024)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_11(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= skoX) & (skoS2 > 317/378) & (skoX > 0) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -2223/16384) & (delta >= skoS2**2 - 2) & (delta - skoX >= 2223/16384) & (delta >= 2 - skoS2**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Rational(317, 378)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-2223, 16384)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(2223, 16384)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_12(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= -8415/65536) & (delta >= skoS2**2 - 2) & (delta - skoX >= 8415/65536) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (15057*skoS2/5120 + 3107/2048 < skoSM*(126*skoS2 + 61)/40 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-8415, 65536)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(8415, 65536)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(15057, 5120), Symbol('skoS2')), Rational(3107, 2048)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_13(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= skoX) & (skoS2 > 281/306) & (skoX > 0) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -8415/65536) & (delta >= skoS2**2 - 2) & (delta - skoX >= 8415/65536) & (delta >= 2 - skoS2**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Rational(281, 306)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-8415, 65536)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(8415, 65536)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_14(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (30177*skoS2/10240 + 6227/4096 < skoSM*(126*skoS2 + 61)/40 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(30177, 10240), Symbol('skoS2')), Rational(6227, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_15(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= skoX) & (skoS2 > 1333/1386) & (skoX > 0) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= 2 - skoS2**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Rational(1333, 1386)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_16(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (30177*skoS2/10240 + 6227/4096 < skoSM*(126*skoS2 + 61)/40 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(30177, 10240), Symbol('skoS2')), Rational(6227, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_17(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= skoX) & (skoS2 > 1333/1386) & (skoX > 0) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= 2 - skoS2**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Rational(1333, 1386)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_18(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (30177*skoS2/10240 + 6227/4096 < skoSM*(126*skoS2 + 61)/40 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(30177, 10240), Symbol('skoS2')), Rational(6227, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_19(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= skoX) & (skoS2 > 1333/1386) & (skoX > 0) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= 2 - skoS2**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Rational(1333, 1386)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_20(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (30177*skoS2/10240 + 6227/4096 < skoSM*(126*skoS2 + 61)/40 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(30177, 10240), Symbol('skoS2')), Rational(6227, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_21(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= skoX) & (skoS2 > 1333/1386) & (skoX > 0) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= 2 - skoS2**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Rational(1333, 1386)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_22(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (30177*skoS2/10240 + 6227/4096 < skoSM*(126*skoS2 + 61)/40 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(30177, 10240), Symbol('skoS2')), Rational(6227, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_23(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= skoX) & (skoS2 > 1333/1386) & (skoX > 0) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= 2 - skoS2**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Rational(1333, 1386)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_24(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (30177*skoS2/10240 + 6227/4096 < skoSM*(126*skoS2 + 61)/40 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(30177, 10240), Symbol('skoS2')), Rational(6227, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_25(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= skoX) & (skoS2 > 1333/1386) & (skoX > 0) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= 2 - skoS2**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Rational(1333, 1386)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_26(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (30177*skoS2/10240 + 6227/4096 < skoSM*(126*skoS2 + 61)/40 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(30177, 10240), Symbol('skoS2')), Rational(6227, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_27(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= skoX) & (skoS2 > 1333/1386) & (skoX > 0) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= 2 - skoS2**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Rational(1333, 1386)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_28(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (30177*skoS2/10240 + 6227/4096 < skoSM*(126*skoS2 + 61)/40 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(30177, 10240), Symbol('skoS2')), Rational(6227, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_29(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= skoX) & (skoS2 > 1333/1386) & (skoX > 0) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= 2 - skoS2**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Rational(1333, 1386)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_30(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (30177*skoS2/10240 + 6227/4096 < skoSM*(126*skoS2 + 61)/40 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(30177, 10240), Symbol('skoS2')), Rational(6227, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_31(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= skoX) & (skoS2 > 1333/1386) & (skoX > 0) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= 2 - skoS2**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Rational(1333, 1386)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_32(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (30177*skoS2/10240 + 6227/4096 < skoSM*(126*skoS2 + 61)/40 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(30177, 10240), Symbol('skoS2')), Rational(6227, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_33(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= skoX) & (skoS2 > 1333/1386) & (skoX > 0) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= 2 - skoS2**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Rational(1333, 1386)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_34(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (30177*skoS2/10240 + 6227/4096 < skoSM*(126*skoS2 + 61)/40 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(30177, 10240), Symbol('skoS2')), Rational(6227, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_35(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= skoX) & (skoS2 > 1333/1386) & (skoX > 0) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= 2 - skoS2**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Rational(1333, 1386)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_36(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (30177*skoS2/10240 + 6227/4096 < skoSM*(126*skoS2 + 61)/40 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(30177, 10240), Symbol('skoS2')), Rational(6227, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_37(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= skoX) & (skoS2 > 1333/1386) & (skoX > 0) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= 2 - skoS2**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Rational(1333, 1386)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_38(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (30177*skoS2/10240 + 6227/4096 < skoSM*(126*skoS2 + 61)/40 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(30177, 10240), Symbol('skoS2')), Rational(6227, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_39(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= skoX) & (skoS2 > 1333/1386) & (skoX > 0) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= 2 - skoS2**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Rational(1333, 1386)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_40(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (30177*skoS2/10240 + 6227/4096 < skoSM*(126*skoS2 + 61)/40 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(30177, 10240), Symbol('skoS2')), Rational(6227, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_41(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= skoX) & (skoS2 > 1333/1386) & (skoX > 0) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= 2 - skoS2**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Rational(1333, 1386)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_42(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (30177*skoS2/10240 + 6227/4096 < skoSM*(126*skoS2 + 61)/40 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(30177, 10240), Symbol('skoS2')), Rational(6227, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_43(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= skoX) & (skoS2 > 1333/1386) & (skoX > 0) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= 2 - skoS2**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Rational(1333, 1386)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_44(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (30177*skoS2/10240 + 6227/4096 < skoSM*(126*skoS2 + 61)/40 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(30177, 10240), Symbol('skoS2')), Rational(6227, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_45(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= skoX) & (skoS2 > 1333/1386) & (skoX > 0) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= 2 - skoS2**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Rational(1333, 1386)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_46(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (30177*skoS2/10240 + 6227/4096 < skoSM*(126*skoS2 + 61)/40 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(30177, 10240), Symbol('skoS2')), Rational(6227, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_47(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= skoX) & (skoS2 > 1333/1386) & (skoX > 0) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= 2 - skoS2**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Rational(1333, 1386)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_48(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (30177*skoS2/10240 + 6227/4096 < skoSM*(126*skoS2 + 61)/40 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(30177, 10240), Symbol('skoS2')), Rational(6227, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_49(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= skoX) & (skoS2 > 1333/1386) & (skoX > 0) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= 2 - skoS2**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Rational(1333, 1386)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_50(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (30177*skoS2/10240 + 6227/4096 < skoSM*(126*skoS2 + 61)/40 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(30177, 10240), Symbol('skoS2')), Rational(6227, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_51(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= skoX) & (skoS2 > 1333/1386) & (skoX > 0) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= 2 - skoS2**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Rational(1333, 1386)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_52(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (30177*skoS2/10240 + 6227/4096 < skoSM*(126*skoS2 + 61)/40 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(30177, 10240), Symbol('skoS2')), Rational(6227, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_53(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= skoX) & (skoS2 > 1333/1386) & (skoX > 0) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= 2 - skoS2**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Rational(1333, 1386)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_54(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (30177*skoS2/10240 + 6227/4096 < skoSM*(126*skoS2 + 61)/40 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(30177, 10240), Symbol('skoS2')), Rational(6227, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_55(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= skoX) & (skoS2 > 1333/1386) & (skoX > 0) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= 2 - skoS2**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Rational(1333, 1386)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_56(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (30177*skoS2/10240 + 6227/4096 < skoSM*(126*skoS2 + 61)/40 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(30177, 10240), Symbol('skoS2')), Rational(6227, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_57(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= skoX) & (skoS2 > 1333/1386) & (skoX > 0) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= 2 - skoS2**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Rational(1333, 1386)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_58(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (30177*skoS2/10240 + 6227/4096 < skoSM*(126*skoS2 + 61)/40 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(30177, 10240), Symbol('skoS2')), Rational(6227, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_59(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= skoX) & (skoS2 > 1333/1386) & (skoX > 0) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= 2 - skoS2**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Rational(1333, 1386)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_60(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (30177*skoS2/10240 + 6227/4096 < skoSM*(126*skoS2 + 61)/40 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(30177, 10240), Symbol('skoS2')), Rational(6227, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_61(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= skoX) & (skoS2 > 1333/1386) & (skoX > 0) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= 2 - skoS2**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Rational(1333, 1386)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_62(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (30177*skoS2/10240 + 6227/4096 < skoSM*(126*skoS2 + 61)/40 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(30177, 10240), Symbol('skoS2')), Rational(6227, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_63(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= skoX) & (skoS2 > 1333/1386) & (skoX > 0) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= 2 - skoS2**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Rational(1333, 1386)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_64(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (30177*skoS2/10240 + 6227/4096 < skoSM*(126*skoS2 + 61)/40 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(30177, 10240), Symbol('skoS2')), Rational(6227, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_65(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= skoX) & (skoS2 > 1333/1386) & (skoX > 0) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= 2 - skoS2**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Rational(1333, 1386)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_66(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (30177*skoS2/10240 + 6227/4096 < skoSM*(126*skoS2 + 61)/40 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(30177, 10240), Symbol('skoS2')), Rational(6227, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_67(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= skoX) & (skoS2 > 1333/1386) & (skoX > 0) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= 2 - skoS2**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Rational(1333, 1386)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_68(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (30177*skoS2/10240 + 6227/4096 < skoSM*(126*skoS2 + 61)/40 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(30177, 10240), Symbol('skoS2')), Rational(6227, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_69(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= skoX) & (skoS2 > 1333/1386) & (skoX > 0) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= 2 - skoS2**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Rational(1333, 1386)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_70(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (30177*skoS2/10240 + 6227/4096 < skoSM*(126*skoS2 + 61)/40 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(30177, 10240), Symbol('skoS2')), Rational(6227, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_71(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= skoX) & (skoS2 > 1333/1386) & (skoX > 0) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= 2 - skoS2**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Rational(1333, 1386)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_72(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (30177*skoS2/10240 + 6227/4096 < skoSM*(126*skoS2 + 61)/40 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(30177, 10240), Symbol('skoS2')), Rational(6227, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_73(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= skoX) & (skoS2 > 1333/1386) & (skoX > 0) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= 2 - skoS2**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Rational(1333, 1386)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_74(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (30177*skoS2/10240 + 6227/4096 < skoSM*(126*skoS2 + 61)/40 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(30177, 10240), Symbol('skoS2')), Rational(6227, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_75(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= skoX) & (skoS2 > 1333/1386) & (skoX > 0) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= 2 - skoS2**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Rational(1333, 1386)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_76(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (30177*skoS2/10240 + 6227/4096 < skoSM*(126*skoS2 + 61)/40 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(30177, 10240), Symbol('skoS2')), Rational(6227, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_77(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= skoX) & (skoS2 > 1333/1386) & (skoX > 0) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= 2 - skoS2**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Rational(1333, 1386)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_78(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (30177*skoS2/10240 + 6227/4096 < skoSM*(126*skoS2 + 61)/40 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(30177, 10240), Symbol('skoS2')), Rational(6227, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_79(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= skoX) & (skoS2 > 1333/1386) & (skoX > 0) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= 2 - skoS2**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Rational(1333, 1386)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_80(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (30177*skoS2/10240 + 6227/4096 < skoSM*(126*skoS2 + 61)/40 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(30177, 10240), Symbol('skoS2')), Rational(6227, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_81(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= skoX) & (skoS2 > 1333/1386) & (skoX > 0) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= 2 - skoS2**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Rational(1333, 1386)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_82(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (30177*skoS2/10240 + 6227/4096 < skoSM*(126*skoS2 + 61)/40 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(30177, 10240), Symbol('skoS2')), Rational(6227, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_83(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= skoX) & (skoS2 > 1333/1386) & (skoX > 0) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= 2 - skoS2**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Rational(1333, 1386)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_84(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (30177*skoS2/10240 + 6227/4096 < skoSM*(126*skoS2 + 61)/40 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(30177, 10240), Symbol('skoS2')), Rational(6227, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_85(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= skoX) & (skoS2 > 1333/1386) & (skoX > 0) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= 2 - skoS2**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Rational(1333, 1386)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_86(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (30177*skoS2/10240 + 6227/4096 < skoSM*(126*skoS2 + 61)/40 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(30177, 10240), Symbol('skoS2')), Rational(6227, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_87(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= skoX) & (skoS2 > 1333/1386) & (skoX > 0) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= 2 - skoS2**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Rational(1333, 1386)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_88(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (30177*skoS2/10240 + 6227/4096 < skoSM*(126*skoS2 + 61)/40 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(30177, 10240), Symbol('skoS2')), Rational(6227, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_89(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= skoX) & (skoS2 > 1333/1386) & (skoX > 0) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= 2 - skoS2**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Rational(1333, 1386)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_90(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (30177*skoS2/10240 + 6227/4096 < skoSM*(126*skoS2 + 61)/40 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(30177, 10240), Symbol('skoS2')), Rational(6227, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_91(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= skoX) & (skoS2 > 1333/1386) & (skoX > 0) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= 2 - skoS2**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Rational(1333, 1386)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_92(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (30177*skoS2/10240 + 6227/4096 < skoSM*(126*skoS2 + 61)/40 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(30177, 10240), Symbol('skoS2')), Rational(6227, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_93(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= skoX) & (skoS2 > 1333/1386) & (skoX > 0) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= 2 - skoS2**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Rational(1333, 1386)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_94(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (30177*skoS2/10240 + 6227/4096 < skoSM*(126*skoS2 + 61)/40 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(30177, 10240), Symbol('skoS2')), Rational(6227, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_95(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= skoX) & (skoS2 > 1333/1386) & (skoX > 0) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= 2 - skoS2**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Rational(1333, 1386)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_96(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (30177*skoS2/10240 + 6227/4096 < skoSM*(126*skoS2 + 61)/40 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(30177, 10240), Symbol('skoS2')), Rational(6227, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_97(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= skoX) & (skoS2 > 1333/1386) & (skoX > 0) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= 2 - skoS2**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Rational(1333, 1386)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_98(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (30177*skoS2/10240 + 6227/4096 < skoSM*(126*skoS2 + 61)/40 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(30177, 10240), Symbol('skoS2')), Rational(6227, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_99(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= skoX) & (skoS2 > 1333/1386) & (skoX > 0) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= 2 - skoS2**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Rational(1333, 1386)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_100(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (30177*skoS2/10240 + 6227/4096 < skoSM*(126*skoS2 + 61)/40 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(30177, 10240), Symbol('skoS2')), Rational(6227, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_101(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= skoX) & (skoS2 > 1333/1386) & (skoX > 0) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= 2 - skoS2**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Rational(1333, 1386)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_102(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (30177*skoS2/10240 + 6227/4096 < skoSM*(126*skoS2 + 61)/40 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(30177, 10240), Symbol('skoS2')), Rational(6227, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_103(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= skoX) & (skoS2 > 1333/1386) & (skoX > 0) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= 2 - skoS2**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Rational(1333, 1386)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_104(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= -32703/262144) & (delta >= skoS2**2 - 2) & (delta - skoX >= 32703/262144) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (30177*skoS2/10240 + 6227/4096 < skoSM*(126*skoS2 + 61)/40 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(-32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(32703, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), StrictLessThan(Add(Mul(Rational(30177, 10240), Symbol('skoS2')), Rational(6227, 4096)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))))

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
		print('skoSP = 1/2')
		exit(0)
	
	
	if pre_condition_1(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_1 SAT")
		print('delta = 2')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 1/2')
		exit(0)
	
	
	if pre_condition_2(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_2 SAT")
		print('delta = 1')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 3/4')
		exit(0)
	
	
	if pre_condition_3(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_3 SAT")
		print('delta = 1')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 3/4')
		exit(0)
	
	
	if pre_condition_4(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_4 SAT")
		print('delta = 1')
		print('skoX = 3/4')
		print('skoS2 = 3/2')
		print('skoSM = 1')
		print('skoSP = 7/8')
		exit(0)
	
	
	if pre_condition_5(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_5 SAT")
		print('delta = 1')
		print('skoX = 3/4')
		print('skoS2 = 3/2')
		print('skoSM = 1')
		print('skoSP = 7/8')
		exit(0)
	
	
	if pre_condition_6(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_6 SAT")
		print('delta = 1')
		print('skoX = 13/16')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 29/32')
		exit(0)
	
	
	if pre_condition_7(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_7 SAT")
		print('delta = 1')
		print('skoX = 13/16')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 29/32')
		exit(0)
	
	
	if pre_condition_8(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_8 SAT")
		print('delta = 1')
		print('skoX = 27/32')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 59/64')
		exit(0)
	
	
	if pre_condition_9(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_9 SAT")
		print('delta = 1')
		print('skoX = 27/32')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 59/64')
		exit(0)
	
	
	if pre_condition_10(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_10 SAT")
		print('delta = 1')
		print('skoX = 55/64')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 119/128')
		exit(0)
	
	
	if pre_condition_11(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_11 SAT")
		print('delta = 1')
		print('skoX = 55/64')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 119/128')
		exit(0)
	
	
	if pre_condition_12(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_12 SAT")
		print('delta = 1')
		print('skoX = 111/128')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 239/256')
		exit(0)
	
	
	if pre_condition_13(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_13 SAT")
		print('delta = 1')
		print('skoX = 111/128')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 239/256')
		exit(0)
	
	
	if pre_condition_14(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_14 SAT")
		print('delta = 1')
		print('skoX = 7/8')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_15(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_15 SAT")
		print('delta = 1')
		print('skoX = 7/8')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_16(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_16 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_17(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_17 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_18(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_18 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_19(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_19 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_20(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_20 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_21(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_21 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_22(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_22 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_23(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_23 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_24(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_24 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_25(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_25 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_26(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_26 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_27(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_27 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_28(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_28 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_29(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_29 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_30(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_30 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_31(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_31 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_32(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_32 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_33(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_33 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_34(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_34 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_35(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_35 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_36(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_36 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_37(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_37 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_38(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_38 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_39(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_39 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_40(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_40 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_41(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_41 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_42(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_42 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_43(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_43 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_44(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_44 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_45(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_45 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_46(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_46 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_47(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_47 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_48(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_48 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_49(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_49 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_50(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_50 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_51(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_51 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_52(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_52 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_53(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_53 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_54(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_54 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_55(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_55 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_56(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_56 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_57(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_57 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_58(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_58 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_59(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_59 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_60(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_60 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_61(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_61 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_62(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_62 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_63(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_63 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_64(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_64 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_65(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_65 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_66(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_66 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_67(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_67 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_68(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_68 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_69(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_69 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_70(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_70 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_71(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_71 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_72(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_72 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_73(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_73 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_74(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_74 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_75(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_75 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_76(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_76 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_77(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_77 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_78(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_78 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_79(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_79 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_80(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_80 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_81(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_81 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_82(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_82 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_83(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_83 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_84(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_84 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_85(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_85 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_86(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_86 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_87(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_87 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_88(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_88 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_89(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_89 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_90(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_90 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_91(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_91 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_92(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_92 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_93(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_93 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_94(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_94 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_95(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_95 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_96(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_96 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_97(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_97 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_98(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_98 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_99(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_99 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_100(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_100 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_101(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_101 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_102(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_102 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_103(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_103 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)
	
	
	if pre_condition_104(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_104 SAT")
		print('delta = 1')
		print('skoX = 252273047388553215/288230376151711744')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 479/512')
		exit(0)


	print("UNKNOWN")
	exit(0)
