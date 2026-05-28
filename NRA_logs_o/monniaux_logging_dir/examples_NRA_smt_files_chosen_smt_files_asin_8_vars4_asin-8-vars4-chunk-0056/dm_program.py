import sympy
from sympy import *

def pre_condition_0(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (63*skoS2/20 + 13/8 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (63*skoS2/20 - skoSM*(126*skoS2 + 61)/40 + 73/40 < skoX*(40*skoSM + skoX*(126*skoS2 - skoSM*(126*skoS2 + 61) + 73) + 200)/40) & (63*skoS2/10 - skoSM*(126*skoS2 + 61)/20 + 73/20 < skoX*(40*skoSM + skoX*(126*skoS2 - skoSM*(126*skoS2 + 61) - 20*skoX*(skoSM + 5) + 73) + 200)/20)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(63, 20), Symbol('skoS2')), Rational(13, 8)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(63, 20), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(73, 40)), Mul(Rational(1, 40), Symbol('skoX'), Add(Mul(Integer(40), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Mul(Integer(-1), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(73))), Integer(200)))), StrictLessThan(Add(Mul(Rational(63, 10), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(73, 20)), Mul(Rational(1, 20), Symbol('skoX'), Add(Mul(Integer(40), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Mul(Integer(-1), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Mul(Integer(-1), Integer(20), Symbol('skoX'), Add(Symbol('skoSM'), Integer(5))), Integer(73))), Integer(200)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (skoX**2 + 20*skoX > 1) & (-10*skoX**3 + skoX**2 + 20*skoX > 1)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Pow(Symbol('skoX'), Integer(2)), Mul(Integer(20), Symbol('skoX'))), Integer(1)), StrictGreaterThan(Add(Mul(Integer(-1), Integer(10), Pow(Symbol('skoX'), Integer(3))), Pow(Symbol('skoX'), Integer(2)), Mul(Integer(20), Symbol('skoX'))), Integer(1)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (189*skoS2/32 + 195/64 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (189*skoS2/32 - skoSM*(126*skoS2 + 61)/40 + 1039/320 < skoX*(320*skoSM + skoX*(1890*skoS2 - 8*skoSM*(126*skoS2 + 61) + 1039) + 1880)/320) & (189*skoS2/16 - skoSM*(126*skoS2 + 61)/20 + 1039/160 < skoX*(320*skoSM + skoX*(1890*skoS2 - 8*skoSM*(126*skoS2 + 61) - 20*skoX*(8*skoSM + 47) + 1039) + 1880)/160)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(189, 32), Symbol('skoS2')), Rational(195, 64)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(189, 32), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(1039, 320)), Mul(Rational(1, 320), Symbol('skoX'), Add(Mul(Integer(320), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(1890), Symbol('skoS2')), Mul(Integer(-1), Integer(8), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(1039))), Integer(1880)))), StrictLessThan(Add(Mul(Rational(189, 16), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(1039, 160)), Mul(Rational(1, 160), Symbol('skoX'), Add(Mul(Integer(320), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(1890), Symbol('skoS2')), Mul(Integer(-1), Integer(8), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Mul(Integer(-1), Integer(20), Symbol('skoX'), Add(Mul(Integer(8), Symbol('skoSM')), Integer(47))), Integer(1039))), Integer(1880)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoS2 < 1/2) & (skoX < 1) & (63*skoS2/160 - 63/320 > 63*skoX*(2*skoS2*skoX - skoX - 40)/320) & (63*skoS2/80 - 63/160 > 63*skoX*(skoX*(2*skoS2 + 20*skoX - 1) - 40)/160)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoS2'), Rational(1, 2)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(63, 160), Symbol('skoS2')), Rational(-63, 320)), Mul(Rational(63, 320), Symbol('skoX'), Add(Mul(Integer(2), Symbol('skoS2'), Symbol('skoX')), Mul(Integer(-1), Symbol('skoX')), Integer(-40)))), StrictGreaterThan(Add(Mul(Rational(63, 80), Symbol('skoS2')), Rational(-63, 160)), Mul(Rational(63, 160), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(2), Symbol('skoS2')), Mul(Integer(20), Symbol('skoX')), Integer(-1))), Integer(-40)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_4(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (2961*skoS2/320 + 611/128 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (2961*skoS2/320 - skoSM*(126*skoS2 + 61)/40 + 3183/640 < skoX*(640*skoSM + skoX*(5922*skoS2 - 16*skoSM*(126*skoS2 + 61) + 3183) + 4440)/640) & (2961*skoS2/160 - skoSM*(126*skoS2 + 61)/20 + 3183/320 < skoX*(640*skoSM + skoX*(5922*skoS2 - 16*skoSM*(126*skoS2 + 61) - 20*skoX*(16*skoSM + 111) + 3183) + 4440)/320)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(2961, 320), Symbol('skoS2')), Rational(611, 128)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(2961, 320), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(3183, 640)), Mul(Rational(1, 640), Symbol('skoX'), Add(Mul(Integer(640), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(5922), Symbol('skoS2')), Mul(Integer(-1), Integer(16), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(3183))), Integer(4440)))), StrictLessThan(Add(Mul(Rational(2961, 160), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(3183, 320)), Mul(Rational(1, 320), Symbol('skoX'), Add(Mul(Integer(640), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(5922), Symbol('skoS2')), Mul(Integer(-1), Integer(16), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Mul(Integer(-1), Integer(20), Symbol('skoX'), Add(Mul(Integer(16), Symbol('skoSM')), Integer(111))), Integer(3183))), Integer(4440)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_5(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoS2 < 85/42) & (skoX < 1) & (63*skoS2/320 - 51/128 > 3*skoX*(skoX*(42*skoS2 - 85) - 2120)/640) & (63*skoS2/160 - 51/64 > 3*skoX*(skoX*(42*skoS2 + 1060*skoX - 85) - 2120)/320)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoS2'), Rational(85, 42)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(63, 320), Symbol('skoS2')), Rational(-51, 128)), Mul(Rational(3, 640), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(42), Symbol('skoS2')), Integer(-85))), Integer(-2120)))), StrictGreaterThan(Add(Mul(Rational(63, 160), Symbol('skoS2')), Rational(-51, 64)), Mul(Rational(3, 320), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(42), Symbol('skoS2')), Mul(Integer(1060), Symbol('skoX')), Integer(-85))), Integer(-2120)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_6(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (8001*skoS2/640 + 1651/256 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (8001*skoS2/640 - skoSM*(126*skoS2 + 61)/40 + 8511/1280 < skoX*(1280*skoSM + skoX*(16002*skoS2 - 32*skoSM*(126*skoS2 + 61) + 8511) + 10200)/1280) & (8001*skoS2/320 - skoSM*(126*skoS2 + 61)/20 + 8511/640 < skoX*(1280*skoSM + skoX*(16002*skoS2 - 32*skoSM*(126*skoS2 + 61) - 20*skoX*(32*skoSM + 255) + 8511) + 10200)/640)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(8001, 640), Symbol('skoS2')), Rational(1651, 256)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(8001, 640), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(8511, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Integer(1280), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(16002), Symbol('skoS2')), Mul(Integer(-1), Integer(32), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(8511))), Integer(10200)))), StrictLessThan(Add(Mul(Rational(8001, 320), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(8511, 640)), Mul(Rational(1, 640), Symbol('skoX'), Add(Mul(Integer(1280), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(16002), Symbol('skoS2')), Mul(Integer(-1), Integer(32), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Mul(Integer(-1), Integer(20), Symbol('skoX'), Add(Mul(Integer(32), Symbol('skoSM')), Integer(255))), Integer(8511))), Integer(10200)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_7(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoS2 < 703/126) & (skoX < 1) & (63*skoS2/640 - 703/1280 > skoX*(skoX*(126*skoS2 - 703) - 15320)/1280) & (63*skoS2/320 - 703/640 > skoX*(skoX*(126*skoS2 + 7660*skoX - 703) - 15320)/640)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoS2'), Rational(703, 126)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(63, 640), Symbol('skoS2')), Rational(-703, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(-703))), Integer(-15320)))), StrictGreaterThan(Add(Mul(Rational(63, 320), Symbol('skoS2')), Rational(-703, 640)), Mul(Rational(1, 640), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Mul(Integer(7660), Symbol('skoX')), Integer(-703))), Integer(-15320)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_8(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (20097*skoS2/1280 + 4147/512 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (20097*skoS2/1280 - skoSM*(126*skoS2 + 61)/40 + 21247/2560 < skoX*(2560*skoSM + skoX*(40194*skoS2 - 64*skoSM*(126*skoS2 + 61) + 21247) + 23000)/2560) & (20097*skoS2/640 - skoSM*(126*skoS2 + 61)/20 + 21247/1280 < skoX*(2560*skoSM + skoX*(40194*skoS2 - 64*skoSM*(126*skoS2 + 61) - 20*skoX*(64*skoSM + 575) + 21247) + 23000)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(20097, 1280), Symbol('skoS2')), Rational(4147, 512)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(20097, 1280), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(21247, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(40194), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(21247))), Integer(23000)))), StrictLessThan(Add(Mul(Rational(20097, 640), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(21247, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(40194), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Mul(Integer(-1), Integer(20), Symbol('skoX'), Add(Mul(Integer(64), Symbol('skoSM')), Integer(575))), Integer(21247))), Integer(23000)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_9(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoS2 < 1727/126) & (skoX < 1) & (63*skoS2/1280 - 1727/2560 > skoX*(skoX*(126*skoS2 - 1727) - 35800)/2560) & (63*skoS2/640 - 1727/1280 > skoX*(skoX*(126*skoS2 + 17900*skoX - 1727) - 35800)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoS2'), Rational(1727, 126)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(63, 1280), Symbol('skoS2')), Rational(-1727, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(-1727))), Integer(-35800)))), StrictGreaterThan(Add(Mul(Rational(63, 640), Symbol('skoS2')), Rational(-1727, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Mul(Integer(17900), Symbol('skoX')), Integer(-1727))), Integer(-35800)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_10(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (24129*skoS2/1280 + 4979/512 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (24129*skoS2/1280 - skoSM*(126*skoS2 + 61)/40 + 25407/2560 < skoX*(2560*skoSM + skoX*(48258*skoS2 - 64*skoSM*(126*skoS2 + 61) + 25407) + 25560)/2560) & (24129*skoS2/640 - skoSM*(126*skoS2 + 61)/20 + 25407/1280 < skoX*(2560*skoSM + skoX*(48258*skoS2 - 64*skoSM*(126*skoS2 + 61) - 20*skoX*(64*skoSM + 639) + 25407) + 25560)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(24129, 1280), Symbol('skoS2')), Rational(4979, 512)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(24129, 1280), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(25407, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(48258), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(25407))), Integer(25560)))), StrictLessThan(Add(Mul(Rational(24129, 640), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(25407, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(48258), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Mul(Integer(-1), Integer(20), Symbol('skoX'), Add(Mul(Integer(64), Symbol('skoSM')), Integer(639))), Integer(25407))), Integer(25560)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_11(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoS2 < 661/42) & (skoX < 1) & (63*skoS2/1280 - 1983/2560 > 3*skoX*(skoX*(42*skoS2 - 661) - 13640)/2560) & (63*skoS2/640 - 1983/1280 > 3*skoX*(skoX*(42*skoS2 + 6820*skoX - 661) - 13640)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoS2'), Rational(661, 42)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(63, 1280), Symbol('skoS2')), Rational(-1983, 2560)), Mul(Rational(3, 2560), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(42), Symbol('skoS2')), Integer(-661))), Integer(-13640)))), StrictGreaterThan(Add(Mul(Rational(63, 640), Symbol('skoS2')), Rational(-1983, 1280)), Mul(Rational(3, 1280), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(42), Symbol('skoS2')), Mul(Integer(6820), Symbol('skoX')), Integer(-661))), Integer(-13640)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_12(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (28161*skoS2/1280 + 5811/512 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (28161*skoS2/1280 - skoSM*(126*skoS2 + 61)/40 + 29567/2560 < skoX*(2560*skoSM + skoX*(56322*skoS2 - 64*skoSM*(126*skoS2 + 61) + 29567) + 28120)/2560) & (28161*skoS2/640 - skoSM*(126*skoS2 + 61)/20 + 29567/1280 < skoX*(2560*skoSM + skoX*(56322*skoS2 - 64*skoSM*(126*skoS2 + 61) - 20*skoX*(64*skoSM + 703) + 29567) + 28120)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(28161, 1280), Symbol('skoS2')), Rational(5811, 512)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(28161, 1280), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(29567, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(56322), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(29567))), Integer(28120)))), StrictLessThan(Add(Mul(Rational(28161, 640), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(29567, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(56322), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Mul(Integer(-1), Integer(20), Symbol('skoX'), Add(Mul(Integer(64), Symbol('skoSM')), Integer(703))), Integer(29567))), Integer(28120)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_13(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoS2 < 2239/126) & (skoX < 1) & (63*skoS2/1280 - 2239/2560 > skoX*(skoX*(126*skoS2 - 2239) - 46040)/2560) & (63*skoS2/640 - 2239/1280 > skoX*(skoX*(126*skoS2 + 23020*skoX - 2239) - 46040)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoS2'), Rational(2239, 126)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(63, 1280), Symbol('skoS2')), Rational(-2239, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(-2239))), Integer(-46040)))), StrictGreaterThan(Add(Mul(Rational(63, 640), Symbol('skoS2')), Rational(-2239, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Mul(Integer(23020), Symbol('skoX')), Integer(-2239))), Integer(-46040)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_14(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (32193*skoS2/1280 + 6643/512 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (32193*skoS2/1280 - skoSM*(126*skoS2 + 61)/40 + 33727/2560 < skoX*(2560*skoSM + skoX*(64386*skoS2 - 64*skoSM*(126*skoS2 + 61) + 33727) + 30680)/2560) & (32193*skoS2/640 - skoSM*(126*skoS2 + 61)/20 + 33727/1280 < skoX*(2560*skoSM + skoX*(64386*skoS2 - 64*skoSM*(126*skoS2 + 61) - 20*skoX*(64*skoSM + 767) + 33727) + 30680)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(32193, 1280), Symbol('skoS2')), Rational(6643, 512)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(32193, 1280), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(33727, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(64386), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(33727))), Integer(30680)))), StrictLessThan(Add(Mul(Rational(32193, 640), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(33727, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(64386), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Mul(Integer(-1), Integer(20), Symbol('skoX'), Add(Mul(Integer(64), Symbol('skoSM')), Integer(767))), Integer(33727))), Integer(30680)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_15(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoS2 < 2495/126) & (skoX < 1) & (63*skoS2/1280 - 499/512 > skoX*(skoX*(126*skoS2 - 2495) - 51160)/2560) & (63*skoS2/640 - 499/256 > skoX*(skoX*(126*skoS2 + 25580*skoX - 2495) - 51160)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoS2'), Rational(2495, 126)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(63, 1280), Symbol('skoS2')), Rational(-499, 512)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(-2495))), Integer(-51160)))), StrictGreaterThan(Add(Mul(Rational(63, 640), Symbol('skoS2')), Rational(-499, 256)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Mul(Integer(25580), Symbol('skoX')), Integer(-2495))), Integer(-51160)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_16(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (7245*skoS2/256 + 7475/512 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (7245*skoS2/256 - skoSM*(126*skoS2 + 61)/40 + 37887/2560 < skoX*(2560*skoSM + skoX*(72450*skoS2 - 64*skoSM*(126*skoS2 + 61) + 37887) + 33240)/2560) & (7245*skoS2/128 - skoSM*(126*skoS2 + 61)/20 + 37887/1280 < skoX*(2560*skoSM + skoX*(72450*skoS2 - 64*skoSM*(126*skoS2 + 61) - 20*skoX*(64*skoSM + 831) + 37887) + 33240)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(7245, 256), Symbol('skoS2')), Rational(7475, 512)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(7245, 256), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(37887, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(72450), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(37887))), Integer(33240)))), StrictLessThan(Add(Mul(Rational(7245, 128), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(37887, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(72450), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Mul(Integer(-1), Integer(20), Symbol('skoX'), Add(Mul(Integer(64), Symbol('skoSM')), Integer(831))), Integer(37887))), Integer(33240)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_17(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoS2 < 131/6) & (skoX < 1) & (63*skoS2/1280 - 2751/2560 > 21*skoX*(skoX*(6*skoS2 - 131) - 2680)/2560) & (63*skoS2/640 - 2751/1280 > 21*skoX*(skoX*(6*skoS2 + 1340*skoX - 131) - 2680)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoS2'), Rational(131, 6)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(63, 1280), Symbol('skoS2')), Rational(-2751, 2560)), Mul(Rational(21, 2560), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(6), Symbol('skoS2')), Integer(-131))), Integer(-2680)))), StrictGreaterThan(Add(Mul(Rational(63, 640), Symbol('skoS2')), Rational(-2751, 1280)), Mul(Rational(21, 1280), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(6), Symbol('skoS2')), Mul(Integer(1340), Symbol('skoX')), Integer(-131))), Integer(-2680)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_18(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (40257*skoS2/1280 + 8307/512 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (40257*skoS2/1280 - skoSM*(126*skoS2 + 61)/40 + 42047/2560 < skoX*(2560*skoSM + skoX*(80514*skoS2 - 64*skoSM*(126*skoS2 + 61) + 42047) + 35800)/2560) & (40257*skoS2/640 - skoSM*(126*skoS2 + 61)/20 + 42047/1280 < skoX*(2560*skoSM + skoX*(80514*skoS2 - 64*skoSM*(126*skoS2 + 61) - 20*skoX*(64*skoSM + 895) + 42047) + 35800)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(40257, 1280), Symbol('skoS2')), Rational(8307, 512)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(40257, 1280), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(42047, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(80514), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(42047))), Integer(35800)))), StrictLessThan(Add(Mul(Rational(40257, 640), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(42047, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(80514), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Mul(Integer(-1), Integer(20), Symbol('skoX'), Add(Mul(Integer(64), Symbol('skoSM')), Integer(895))), Integer(42047))), Integer(35800)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_19(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoS2 < 3007/126) & (skoX < 1) & (63*skoS2/1280 - 3007/2560 > skoX*(skoX*(126*skoS2 - 3007) - 61400)/2560) & (63*skoS2/640 - 3007/1280 > skoX*(skoX*(126*skoS2 + 30700*skoX - 3007) - 61400)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoS2'), Rational(3007, 126)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(63, 1280), Symbol('skoS2')), Rational(-3007, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(-3007))), Integer(-61400)))), StrictGreaterThan(Add(Mul(Rational(63, 640), Symbol('skoS2')), Rational(-3007, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Mul(Integer(30700), Symbol('skoX')), Integer(-3007))), Integer(-61400)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_20(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (44289*skoS2/1280 + 9139/512 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (44289*skoS2/1280 - skoSM*(126*skoS2 + 61)/40 + 46207/2560 < skoX*(2560*skoSM + skoX*(88578*skoS2 - 64*skoSM*(126*skoS2 + 61) + 46207) + 38360)/2560) & (44289*skoS2/640 - skoSM*(126*skoS2 + 61)/20 + 46207/1280 < skoX*(2560*skoSM + skoX*(88578*skoS2 - 64*skoSM*(126*skoS2 + 61) - 20*skoX*(64*skoSM + 959) + 46207) + 38360)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(44289, 1280), Symbol('skoS2')), Rational(9139, 512)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(44289, 1280), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(46207, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(88578), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(46207))), Integer(38360)))), StrictLessThan(Add(Mul(Rational(44289, 640), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(46207, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(88578), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Mul(Integer(-1), Integer(20), Symbol('skoX'), Add(Mul(Integer(64), Symbol('skoSM')), Integer(959))), Integer(46207))), Integer(38360)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_21(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoS2 < 3263/126) & (skoX < 1) & (63*skoS2/1280 - 3263/2560 > skoX*(skoX*(126*skoS2 - 3263) - 66520)/2560) & (63*skoS2/640 - 3263/1280 > skoX*(skoX*(126*skoS2 + 33260*skoX - 3263) - 66520)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoS2'), Rational(3263, 126)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(63, 1280), Symbol('skoS2')), Rational(-3263, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(-3263))), Integer(-66520)))), StrictGreaterThan(Add(Mul(Rational(63, 640), Symbol('skoS2')), Rational(-3263, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Mul(Integer(33260), Symbol('skoX')), Integer(-3263))), Integer(-66520)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_22(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (48321*skoS2/1280 + 9971/512 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (48321*skoS2/1280 - skoSM*(126*skoS2 + 61)/40 + 50367/2560 < skoX*(2560*skoSM + skoX*(96642*skoS2 - 64*skoSM*(126*skoS2 + 61) + 50367) + 40920)/2560) & (48321*skoS2/640 - skoSM*(126*skoS2 + 61)/20 + 50367/1280 < skoX*(2560*skoSM + skoX*(96642*skoS2 - 64*skoSM*(126*skoS2 + 61) - 20*skoX*(64*skoSM + 1023) + 50367) + 40920)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(48321, 1280), Symbol('skoS2')), Rational(9971, 512)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(48321, 1280), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(50367, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(96642), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(50367))), Integer(40920)))), StrictLessThan(Add(Mul(Rational(48321, 640), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(50367, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(96642), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Mul(Integer(-1), Integer(20), Symbol('skoX'), Add(Mul(Integer(64), Symbol('skoSM')), Integer(1023))), Integer(50367))), Integer(40920)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_23(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoS2 < 391/14) & (skoX < 1) & (63*skoS2/1280 - 3519/2560 > 9*skoX*(skoX*(14*skoS2 - 391) - 7960)/2560) & (63*skoS2/640 - 3519/1280 > 9*skoX*(skoX*(14*skoS2 + 3980*skoX - 391) - 7960)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoS2'), Rational(391, 14)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(63, 1280), Symbol('skoS2')), Rational(-3519, 2560)), Mul(Rational(9, 2560), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(14), Symbol('skoS2')), Integer(-391))), Integer(-7960)))), StrictGreaterThan(Add(Mul(Rational(63, 640), Symbol('skoS2')), Rational(-3519, 1280)), Mul(Rational(9, 1280), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(14), Symbol('skoS2')), Mul(Integer(3980), Symbol('skoX')), Integer(-391))), Integer(-7960)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_24(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (52353*skoS2/1280 + 10803/512 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (52353*skoS2/1280 - skoSM*(126*skoS2 + 61)/40 + 54527/2560 < skoX*(2560*skoSM + skoX*(104706*skoS2 - 64*skoSM*(126*skoS2 + 61) + 54527) + 43480)/2560) & (52353*skoS2/640 - skoSM*(126*skoS2 + 61)/20 + 54527/1280 < skoX*(2560*skoSM + skoX*(104706*skoS2 - 64*skoSM*(126*skoS2 + 61) - 20*skoX*(64*skoSM + 1087) + 54527) + 43480)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(52353, 1280), Symbol('skoS2')), Rational(10803, 512)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(52353, 1280), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(54527, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(104706), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(54527))), Integer(43480)))), StrictLessThan(Add(Mul(Rational(52353, 640), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(54527, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(104706), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Mul(Integer(-1), Integer(20), Symbol('skoX'), Add(Mul(Integer(64), Symbol('skoSM')), Integer(1087))), Integer(54527))), Integer(43480)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_25(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoS2 < 3775/126) & (skoX < 1) & (63*skoS2/1280 - 755/512 > skoX*(skoX*(126*skoS2 - 3775) - 76760)/2560) & (63*skoS2/640 - 755/256 > skoX*(skoX*(126*skoS2 + 38380*skoX - 3775) - 76760)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoS2'), Rational(3775, 126)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(63, 1280), Symbol('skoS2')), Rational(-755, 512)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(-3775))), Integer(-76760)))), StrictGreaterThan(Add(Mul(Rational(63, 640), Symbol('skoS2')), Rational(-755, 256)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Mul(Integer(38380), Symbol('skoX')), Integer(-3775))), Integer(-76760)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_26(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (11277*skoS2/256 + 11635/512 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (11277*skoS2/256 - skoSM*(126*skoS2 + 61)/40 + 58687/2560 < skoX*(2560*skoSM + skoX*(112770*skoS2 - 64*skoSM*(126*skoS2 + 61) + 58687) + 46040)/2560) & (11277*skoS2/128 - skoSM*(126*skoS2 + 61)/20 + 58687/1280 < skoX*(2560*skoSM + skoX*(112770*skoS2 - 64*skoSM*(126*skoS2 + 61) - 20*skoX*(64*skoSM + 1151) + 58687) + 46040)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(11277, 256), Symbol('skoS2')), Rational(11635, 512)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(11277, 256), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(58687, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(112770), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(58687))), Integer(46040)))), StrictLessThan(Add(Mul(Rational(11277, 128), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(58687, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(112770), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Mul(Integer(-1), Integer(20), Symbol('skoX'), Add(Mul(Integer(64), Symbol('skoSM')), Integer(1151))), Integer(58687))), Integer(46040)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_27(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoS2 < 4031/126) & (skoX < 1) & (63*skoS2/1280 - 4031/2560 > skoX*(skoX*(126*skoS2 - 4031) - 81880)/2560) & (63*skoS2/640 - 4031/1280 > skoX*(skoX*(126*skoS2 + 40940*skoX - 4031) - 81880)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoS2'), Rational(4031, 126)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(63, 1280), Symbol('skoS2')), Rational(-4031, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(-4031))), Integer(-81880)))), StrictGreaterThan(Add(Mul(Rational(63, 640), Symbol('skoS2')), Rational(-4031, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Mul(Integer(40940), Symbol('skoX')), Integer(-4031))), Integer(-81880)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_28(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (60417*skoS2/1280 + 12467/512 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (60417*skoS2/1280 - skoSM*(126*skoS2 + 61)/40 + 62847/2560 < skoX*(2560*skoSM + skoX*(120834*skoS2 - 64*skoSM*(126*skoS2 + 61) + 62847) + 48600)/2560) & (60417*skoS2/640 - skoSM*(126*skoS2 + 61)/20 + 62847/1280 < skoX*(2560*skoSM + skoX*(120834*skoS2 - 64*skoSM*(126*skoS2 + 61) - 20*skoX*(64*skoSM + 1215) + 62847) + 48600)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(60417, 1280), Symbol('skoS2')), Rational(12467, 512)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(60417, 1280), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(62847, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(120834), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(62847))), Integer(48600)))), StrictLessThan(Add(Mul(Rational(60417, 640), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(62847, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(120834), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Mul(Integer(-1), Integer(20), Symbol('skoX'), Add(Mul(Integer(64), Symbol('skoSM')), Integer(1215))), Integer(62847))), Integer(48600)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_29(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoS2 < 1429/42) & (skoX < 1) & (63*skoS2/1280 - 4287/2560 > 3*skoX*(skoX*(42*skoS2 - 1429) - 29000)/2560) & (63*skoS2/640 - 4287/1280 > 3*skoX*(skoX*(42*skoS2 + 14500*skoX - 1429) - 29000)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoS2'), Rational(1429, 42)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(63, 1280), Symbol('skoS2')), Rational(-4287, 2560)), Mul(Rational(3, 2560), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(42), Symbol('skoS2')), Integer(-1429))), Integer(-29000)))), StrictGreaterThan(Add(Mul(Rational(63, 640), Symbol('skoS2')), Rational(-4287, 1280)), Mul(Rational(3, 1280), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(42), Symbol('skoS2')), Mul(Integer(14500), Symbol('skoX')), Integer(-1429))), Integer(-29000)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_30(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (64449*skoS2/1280 + 13299/512 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (64449*skoS2/1280 - skoSM*(126*skoS2 + 61)/40 + 67007/2560 < skoX*(2560*skoSM + skoX*(128898*skoS2 - 64*skoSM*(126*skoS2 + 61) + 67007) + 51160)/2560) & (64449*skoS2/640 - skoSM*(126*skoS2 + 61)/20 + 67007/1280 < skoX*(2560*skoSM + skoX*(128898*skoS2 - 64*skoSM*(126*skoS2 + 61) - 20*skoX*(64*skoSM + 1279) + 67007) + 51160)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(64449, 1280), Symbol('skoS2')), Rational(13299, 512)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(64449, 1280), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(67007, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(128898), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(67007))), Integer(51160)))), StrictLessThan(Add(Mul(Rational(64449, 640), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(67007, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(128898), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Mul(Integer(-1), Integer(20), Symbol('skoX'), Add(Mul(Integer(64), Symbol('skoSM')), Integer(1279))), Integer(67007))), Integer(51160)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_31(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoS2 < 649/18) & (skoX < 1) & (63*skoS2/1280 - 4543/2560 > 7*skoX*(skoX*(18*skoS2 - 649) - 13160)/2560) & (63*skoS2/640 - 4543/1280 > 7*skoX*(skoX*(18*skoS2 + 6580*skoX - 649) - 13160)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoS2'), Rational(649, 18)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(63, 1280), Symbol('skoS2')), Rational(-4543, 2560)), Mul(Rational(7, 2560), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(18), Symbol('skoS2')), Integer(-649))), Integer(-13160)))), StrictGreaterThan(Add(Mul(Rational(63, 640), Symbol('skoS2')), Rational(-4543, 1280)), Mul(Rational(7, 1280), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(18), Symbol('skoS2')), Mul(Integer(6580), Symbol('skoX')), Integer(-649))), Integer(-13160)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_32(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (68481*skoS2/1280 + 14131/512 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (68481*skoS2/1280 - skoSM*(126*skoS2 + 61)/40 + 71167/2560 < skoX*(2560*skoSM + skoX*(136962*skoS2 - 64*skoSM*(126*skoS2 + 61) + 71167) + 53720)/2560) & (68481*skoS2/640 - skoSM*(126*skoS2 + 61)/20 + 71167/1280 < skoX*(2560*skoSM + skoX*(136962*skoS2 - 64*skoSM*(126*skoS2 + 61) - 20*skoX*(64*skoSM + 1343) + 71167) + 53720)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(68481, 1280), Symbol('skoS2')), Rational(14131, 512)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(68481, 1280), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(71167, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(136962), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(71167))), Integer(53720)))), StrictLessThan(Add(Mul(Rational(68481, 640), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(71167, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(136962), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Mul(Integer(-1), Integer(20), Symbol('skoX'), Add(Mul(Integer(64), Symbol('skoSM')), Integer(1343))), Integer(71167))), Integer(53720)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_33(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoS2 < 4799/126) & (skoX < 1) & (63*skoS2/1280 - 4799/2560 > skoX*(skoX*(126*skoS2 - 4799) - 97240)/2560) & (63*skoS2/640 - 4799/1280 > skoX*(skoX*(126*skoS2 + 48620*skoX - 4799) - 97240)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoS2'), Rational(4799, 126)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(63, 1280), Symbol('skoS2')), Rational(-4799, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(-4799))), Integer(-97240)))), StrictGreaterThan(Add(Mul(Rational(63, 640), Symbol('skoS2')), Rational(-4799, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Mul(Integer(48620), Symbol('skoX')), Integer(-4799))), Integer(-97240)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_34(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (72513*skoS2/1280 + 14963/512 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (72513*skoS2/1280 - skoSM*(126*skoS2 + 61)/40 + 75327/2560 < skoX*(2560*skoSM + skoX*(145026*skoS2 - 64*skoSM*(126*skoS2 + 61) + 75327) + 56280)/2560) & (72513*skoS2/640 - skoSM*(126*skoS2 + 61)/20 + 75327/1280 < skoX*(2560*skoSM + skoX*(145026*skoS2 - 64*skoSM*(126*skoS2 + 61) - 20*skoX*(64*skoSM + 1407) + 75327) + 56280)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(72513, 1280), Symbol('skoS2')), Rational(14963, 512)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(72513, 1280), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(75327, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(145026), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(75327))), Integer(56280)))), StrictLessThan(Add(Mul(Rational(72513, 640), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(75327, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(145026), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Mul(Integer(-1), Integer(20), Symbol('skoX'), Add(Mul(Integer(64), Symbol('skoSM')), Integer(1407))), Integer(75327))), Integer(56280)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_35(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoS2 < 1685/42) & (skoX < 1) & (63*skoS2/1280 - 1011/512 > 3*skoX*(skoX*(42*skoS2 - 1685) - 34120)/2560) & (63*skoS2/640 - 1011/256 > 3*skoX*(skoX*(42*skoS2 + 17060*skoX - 1685) - 34120)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoS2'), Rational(1685, 42)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(63, 1280), Symbol('skoS2')), Rational(-1011, 512)), Mul(Rational(3, 2560), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(42), Symbol('skoS2')), Integer(-1685))), Integer(-34120)))), StrictGreaterThan(Add(Mul(Rational(63, 640), Symbol('skoS2')), Rational(-1011, 256)), Mul(Rational(3, 1280), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(42), Symbol('skoS2')), Mul(Integer(17060), Symbol('skoX')), Integer(-1685))), Integer(-34120)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_36(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (15309*skoS2/256 + 15795/512 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (15309*skoS2/256 - skoSM*(126*skoS2 + 61)/40 + 79487/2560 < skoX*(2560*skoSM + skoX*(153090*skoS2 - 64*skoSM*(126*skoS2 + 61) + 79487) + 58840)/2560) & (15309*skoS2/128 - skoSM*(126*skoS2 + 61)/20 + 79487/1280 < skoX*(2560*skoSM + skoX*(153090*skoS2 - 64*skoSM*(126*skoS2 + 61) - 20*skoX*(64*skoSM + 1471) + 79487) + 58840)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(15309, 256), Symbol('skoS2')), Rational(15795, 512)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(15309, 256), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(79487, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(153090), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(79487))), Integer(58840)))), StrictLessThan(Add(Mul(Rational(15309, 128), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(79487, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(153090), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Mul(Integer(-1), Integer(20), Symbol('skoX'), Add(Mul(Integer(64), Symbol('skoSM')), Integer(1471))), Integer(79487))), Integer(58840)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_37(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoS2 < 5311/126) & (skoX < 1) & (63*skoS2/1280 - 5311/2560 > skoX*(skoX*(126*skoS2 - 5311) - 107480)/2560) & (63*skoS2/640 - 5311/1280 > skoX*(skoX*(126*skoS2 + 53740*skoX - 5311) - 107480)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoS2'), Rational(5311, 126)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(63, 1280), Symbol('skoS2')), Rational(-5311, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(-5311))), Integer(-107480)))), StrictGreaterThan(Add(Mul(Rational(63, 640), Symbol('skoS2')), Rational(-5311, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Mul(Integer(53740), Symbol('skoX')), Integer(-5311))), Integer(-107480)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_38(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (80577*skoS2/1280 + 16627/512 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (80577*skoS2/1280 - skoSM*(126*skoS2 + 61)/40 + 83647/2560 < skoX*(2560*skoSM + skoX*(161154*skoS2 - 64*skoSM*(126*skoS2 + 61) + 83647) + 61400)/2560) & (80577*skoS2/640 - skoSM*(126*skoS2 + 61)/20 + 83647/1280 < skoX*(2560*skoSM + skoX*(161154*skoS2 - 64*skoSM*(126*skoS2 + 61) - 20*skoX*(64*skoSM + 1535) + 83647) + 61400)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(80577, 1280), Symbol('skoS2')), Rational(16627, 512)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(80577, 1280), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(83647, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(161154), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(83647))), Integer(61400)))), StrictLessThan(Add(Mul(Rational(80577, 640), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(83647, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(161154), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Mul(Integer(-1), Integer(20), Symbol('skoX'), Add(Mul(Integer(64), Symbol('skoSM')), Integer(1535))), Integer(83647))), Integer(61400)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_39(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoS2 < 5567/126) & (skoX < 1) & (63*skoS2/1280 - 5567/2560 > skoX*(skoX*(126*skoS2 - 5567) - 112600)/2560) & (63*skoS2/640 - 5567/1280 > skoX*(skoX*(126*skoS2 + 56300*skoX - 5567) - 112600)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoS2'), Rational(5567, 126)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(63, 1280), Symbol('skoS2')), Rational(-5567, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(-5567))), Integer(-112600)))), StrictGreaterThan(Add(Mul(Rational(63, 640), Symbol('skoS2')), Rational(-5567, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Mul(Integer(56300), Symbol('skoX')), Integer(-5567))), Integer(-112600)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_40(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (84609*skoS2/1280 + 17459/512 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (84609*skoS2/1280 - skoSM*(126*skoS2 + 61)/40 + 87807/2560 < skoX*(2560*skoSM + skoX*(169218*skoS2 - 64*skoSM*(126*skoS2 + 61) + 87807) + 63960)/2560) & (84609*skoS2/640 - skoSM*(126*skoS2 + 61)/20 + 87807/1280 < skoX*(2560*skoSM + skoX*(169218*skoS2 - 64*skoSM*(126*skoS2 + 61) - 20*skoX*(64*skoSM + 1599) + 87807) + 63960)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(84609, 1280), Symbol('skoS2')), Rational(17459, 512)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(84609, 1280), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(87807, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(169218), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(87807))), Integer(63960)))), StrictLessThan(Add(Mul(Rational(84609, 640), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(87807, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(169218), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Mul(Integer(-1), Integer(20), Symbol('skoX'), Add(Mul(Integer(64), Symbol('skoSM')), Integer(1599))), Integer(87807))), Integer(63960)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_41(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoS2 < 647/14) & (skoX < 1) & (63*skoS2/1280 - 5823/2560 > 9*skoX*(skoX*(14*skoS2 - 647) - 13080)/2560) & (63*skoS2/640 - 5823/1280 > 9*skoX*(skoX*(14*skoS2 + 6540*skoX - 647) - 13080)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoS2'), Rational(647, 14)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(63, 1280), Symbol('skoS2')), Rational(-5823, 2560)), Mul(Rational(9, 2560), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(14), Symbol('skoS2')), Integer(-647))), Integer(-13080)))), StrictGreaterThan(Add(Mul(Rational(63, 640), Symbol('skoS2')), Rational(-5823, 1280)), Mul(Rational(9, 1280), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(14), Symbol('skoS2')), Mul(Integer(6540), Symbol('skoX')), Integer(-647))), Integer(-13080)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_42(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (88641*skoS2/1280 + 18291/512 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (88641*skoS2/1280 - skoSM*(126*skoS2 + 61)/40 + 91967/2560 < skoX*(2560*skoSM + skoX*(177282*skoS2 - 64*skoSM*(126*skoS2 + 61) + 91967) + 66520)/2560) & (88641*skoS2/640 - skoSM*(126*skoS2 + 61)/20 + 91967/1280 < skoX*(2560*skoSM + skoX*(177282*skoS2 - 64*skoSM*(126*skoS2 + 61) - 20*skoX*(64*skoSM + 1663) + 91967) + 66520)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(88641, 1280), Symbol('skoS2')), Rational(18291, 512)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(88641, 1280), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(91967, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(177282), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(91967))), Integer(66520)))), StrictLessThan(Add(Mul(Rational(88641, 640), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(91967, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(177282), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Mul(Integer(-1), Integer(20), Symbol('skoX'), Add(Mul(Integer(64), Symbol('skoSM')), Integer(1663))), Integer(91967))), Integer(66520)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_43(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoS2 < 6079/126) & (skoX < 1) & (63*skoS2/1280 - 6079/2560 > skoX*(skoX*(126*skoS2 - 6079) - 122840)/2560) & (63*skoS2/640 - 6079/1280 > skoX*(skoX*(126*skoS2 + 61420*skoX - 6079) - 122840)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoS2'), Rational(6079, 126)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(63, 1280), Symbol('skoS2')), Rational(-6079, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(-6079))), Integer(-122840)))), StrictGreaterThan(Add(Mul(Rational(63, 640), Symbol('skoS2')), Rational(-6079, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Mul(Integer(61420), Symbol('skoX')), Integer(-6079))), Integer(-122840)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_44(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (92673*skoS2/1280 + 19123/512 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (92673*skoS2/1280 - skoSM*(126*skoS2 + 61)/40 + 96127/2560 < skoX*(2560*skoSM + skoX*(185346*skoS2 - 64*skoSM*(126*skoS2 + 61) + 96127) + 69080)/2560) & (92673*skoS2/640 - skoSM*(126*skoS2 + 61)/20 + 96127/1280 < skoX*(2560*skoSM + skoX*(185346*skoS2 - 64*skoSM*(126*skoS2 + 61) - 20*skoX*(64*skoSM + 1727) + 96127) + 69080)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(92673, 1280), Symbol('skoS2')), Rational(19123, 512)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(92673, 1280), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(96127, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(185346), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(96127))), Integer(69080)))), StrictLessThan(Add(Mul(Rational(92673, 640), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(96127, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(185346), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Mul(Integer(-1), Integer(20), Symbol('skoX'), Add(Mul(Integer(64), Symbol('skoSM')), Integer(1727))), Integer(96127))), Integer(69080)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_45(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoS2 < 905/18) & (skoX < 1) & (63*skoS2/1280 - 1267/512 > 7*skoX*(skoX*(18*skoS2 - 905) - 18280)/2560) & (63*skoS2/640 - 1267/256 > 7*skoX*(skoX*(18*skoS2 + 9140*skoX - 905) - 18280)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoS2'), Rational(905, 18)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(63, 1280), Symbol('skoS2')), Rational(-1267, 512)), Mul(Rational(7, 2560), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(18), Symbol('skoS2')), Integer(-905))), Integer(-18280)))), StrictGreaterThan(Add(Mul(Rational(63, 640), Symbol('skoS2')), Rational(-1267, 256)), Mul(Rational(7, 1280), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(18), Symbol('skoS2')), Mul(Integer(9140), Symbol('skoX')), Integer(-905))), Integer(-18280)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_46(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (19341*skoS2/256 + 19955/512 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (19341*skoS2/256 - skoSM*(126*skoS2 + 61)/40 + 100287/2560 < skoX*(2560*skoSM + skoX*(193410*skoS2 - 64*skoSM*(126*skoS2 + 61) + 100287) + 71640)/2560) & (19341*skoS2/128 - skoSM*(126*skoS2 + 61)/20 + 100287/1280 < skoX*(2560*skoSM + skoX*(193410*skoS2 - 64*skoSM*(126*skoS2 + 61) - 20*skoX*(64*skoSM + 1791) + 100287) + 71640)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(19341, 256), Symbol('skoS2')), Rational(19955, 512)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(19341, 256), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(100287, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(193410), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(100287))), Integer(71640)))), StrictLessThan(Add(Mul(Rational(19341, 128), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(100287, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(193410), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Mul(Integer(-1), Integer(20), Symbol('skoX'), Add(Mul(Integer(64), Symbol('skoSM')), Integer(1791))), Integer(100287))), Integer(71640)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_47(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoS2 < 2197/42) & (skoX < 1) & (63*skoS2/1280 - 6591/2560 > 3*skoX*(skoX*(42*skoS2 - 2197) - 44360)/2560) & (63*skoS2/640 - 6591/1280 > 3*skoX*(skoX*(42*skoS2 + 22180*skoX - 2197) - 44360)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoS2'), Rational(2197, 42)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(63, 1280), Symbol('skoS2')), Rational(-6591, 2560)), Mul(Rational(3, 2560), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(42), Symbol('skoS2')), Integer(-2197))), Integer(-44360)))), StrictGreaterThan(Add(Mul(Rational(63, 640), Symbol('skoS2')), Rational(-6591, 1280)), Mul(Rational(3, 1280), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(42), Symbol('skoS2')), Mul(Integer(22180), Symbol('skoX')), Integer(-2197))), Integer(-44360)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_48(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (100737*skoS2/1280 + 20787/512 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (100737*skoS2/1280 - skoSM*(126*skoS2 + 61)/40 + 104447/2560 < skoX*(2560*skoSM + skoX*(201474*skoS2 - 64*skoSM*(126*skoS2 + 61) + 104447) + 74200)/2560) & (100737*skoS2/640 - skoSM*(126*skoS2 + 61)/20 + 104447/1280 < skoX*(2560*skoSM + skoX*(201474*skoS2 - 64*skoSM*(126*skoS2 + 61) - 20*skoX*(64*skoSM + 1855) + 104447) + 74200)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(100737, 1280), Symbol('skoS2')), Rational(20787, 512)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(100737, 1280), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(104447, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(201474), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(104447))), Integer(74200)))), StrictLessThan(Add(Mul(Rational(100737, 640), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(104447, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(201474), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Mul(Integer(-1), Integer(20), Symbol('skoX'), Add(Mul(Integer(64), Symbol('skoSM')), Integer(1855))), Integer(104447))), Integer(74200)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_49(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoS2 < 6847/126) & (skoX < 1) & (63*skoS2/1280 - 6847/2560 > skoX*(skoX*(126*skoS2 - 6847) - 138200)/2560) & (63*skoS2/640 - 6847/1280 > skoX*(skoX*(126*skoS2 + 69100*skoX - 6847) - 138200)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoS2'), Rational(6847, 126)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(63, 1280), Symbol('skoS2')), Rational(-6847, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(-6847))), Integer(-138200)))), StrictGreaterThan(Add(Mul(Rational(63, 640), Symbol('skoS2')), Rational(-6847, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Mul(Integer(69100), Symbol('skoX')), Integer(-6847))), Integer(-138200)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_50(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (104769*skoS2/1280 + 21619/512 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (104769*skoS2/1280 - skoSM*(126*skoS2 + 61)/40 + 108607/2560 < skoX*(2560*skoSM + skoX*(209538*skoS2 - 64*skoSM*(126*skoS2 + 61) + 108607) + 76760)/2560) & (104769*skoS2/640 - skoSM*(126*skoS2 + 61)/20 + 108607/1280 < skoX*(2560*skoSM + skoX*(209538*skoS2 - 64*skoSM*(126*skoS2 + 61) - 20*skoX*(64*skoSM + 1919) + 108607) + 76760)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(104769, 1280), Symbol('skoS2')), Rational(21619, 512)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(104769, 1280), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(108607, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(209538), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(108607))), Integer(76760)))), StrictLessThan(Add(Mul(Rational(104769, 640), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(108607, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(209538), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Mul(Integer(-1), Integer(20), Symbol('skoX'), Add(Mul(Integer(64), Symbol('skoSM')), Integer(1919))), Integer(108607))), Integer(76760)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_51(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoS2 < 7103/126) & (skoX < 1) & (63*skoS2/1280 - 7103/2560 > skoX*(skoX*(126*skoS2 - 7103) - 143320)/2560) & (63*skoS2/640 - 7103/1280 > skoX*(skoX*(126*skoS2 + 71660*skoX - 7103) - 143320)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoS2'), Rational(7103, 126)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(63, 1280), Symbol('skoS2')), Rational(-7103, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(-7103))), Integer(-143320)))), StrictGreaterThan(Add(Mul(Rational(63, 640), Symbol('skoS2')), Rational(-7103, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Mul(Integer(71660), Symbol('skoX')), Integer(-7103))), Integer(-143320)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_52(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (108801*skoS2/1280 + 22451/512 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (108801*skoS2/1280 - skoSM*(126*skoS2 + 61)/40 + 112767/2560 < skoX*(2560*skoSM + skoX*(217602*skoS2 - 64*skoSM*(126*skoS2 + 61) + 112767) + 79320)/2560) & (108801*skoS2/640 - skoSM*(126*skoS2 + 61)/20 + 112767/1280 < skoX*(2560*skoSM + skoX*(217602*skoS2 - 64*skoSM*(126*skoS2 + 61) - 20*skoX*(64*skoSM + 1983) + 112767) + 79320)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(108801, 1280), Symbol('skoS2')), Rational(22451, 512)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(108801, 1280), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(112767, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(217602), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(112767))), Integer(79320)))), StrictLessThan(Add(Mul(Rational(108801, 640), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(112767, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(217602), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Mul(Integer(-1), Integer(20), Symbol('skoX'), Add(Mul(Integer(64), Symbol('skoSM')), Integer(1983))), Integer(112767))), Integer(79320)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_53(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoS2 < 2453/42) & (skoX < 1) & (63*skoS2/1280 - 7359/2560 > 3*skoX*(skoX*(42*skoS2 - 2453) - 49480)/2560) & (63*skoS2/640 - 7359/1280 > 3*skoX*(skoX*(42*skoS2 + 24740*skoX - 2453) - 49480)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoS2'), Rational(2453, 42)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(63, 1280), Symbol('skoS2')), Rational(-7359, 2560)), Mul(Rational(3, 2560), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(42), Symbol('skoS2')), Integer(-2453))), Integer(-49480)))), StrictGreaterThan(Add(Mul(Rational(63, 640), Symbol('skoS2')), Rational(-7359, 1280)), Mul(Rational(3, 1280), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(42), Symbol('skoS2')), Mul(Integer(24740), Symbol('skoX')), Integer(-2453))), Integer(-49480)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_54(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (112833*skoS2/1280 + 23283/512 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (112833*skoS2/1280 - skoSM*(126*skoS2 + 61)/40 + 116927/2560 < skoX*(2560*skoSM + skoX*(225666*skoS2 - 64*skoSM*(126*skoS2 + 61) + 116927) + 81880)/2560) & (112833*skoS2/640 - skoSM*(126*skoS2 + 61)/20 + 116927/1280 < skoX*(2560*skoSM + skoX*(225666*skoS2 - 64*skoSM*(126*skoS2 + 61) - 20*skoX*(64*skoSM + 2047) + 116927) + 81880)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(112833, 1280), Symbol('skoS2')), Rational(23283, 512)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(112833, 1280), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(116927, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(225666), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(116927))), Integer(81880)))), StrictLessThan(Add(Mul(Rational(112833, 640), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(116927, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(225666), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Mul(Integer(-1), Integer(20), Symbol('skoX'), Add(Mul(Integer(64), Symbol('skoSM')), Integer(2047))), Integer(116927))), Integer(81880)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_55(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoS2 < 7615/126) & (skoX < 1) & (63*skoS2/1280 - 1523/512 > skoX*(skoX*(126*skoS2 - 7615) - 153560)/2560) & (63*skoS2/640 - 1523/256 > skoX*(skoX*(126*skoS2 + 76780*skoX - 7615) - 153560)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoS2'), Rational(7615, 126)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(63, 1280), Symbol('skoS2')), Rational(-1523, 512)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(-7615))), Integer(-153560)))), StrictGreaterThan(Add(Mul(Rational(63, 640), Symbol('skoS2')), Rational(-1523, 256)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Mul(Integer(76780), Symbol('skoX')), Integer(-7615))), Integer(-153560)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_56(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (23373*skoS2/256 + 24115/512 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (23373*skoS2/256 - skoSM*(126*skoS2 + 61)/40 + 121087/2560 < skoX*(2560*skoSM + skoX*(233730*skoS2 - 64*skoSM*(126*skoS2 + 61) + 121087) + 84440)/2560) & (23373*skoS2/128 - skoSM*(126*skoS2 + 61)/20 + 121087/1280 < skoX*(2560*skoSM + skoX*(233730*skoS2 - 64*skoSM*(126*skoS2 + 61) - 20*skoX*(64*skoSM + 2111) + 121087) + 84440)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(23373, 256), Symbol('skoS2')), Rational(24115, 512)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(23373, 256), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(121087, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(233730), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(121087))), Integer(84440)))), StrictLessThan(Add(Mul(Rational(23373, 128), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(121087, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(233730), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Mul(Integer(-1), Integer(20), Symbol('skoX'), Add(Mul(Integer(64), Symbol('skoSM')), Integer(2111))), Integer(121087))), Integer(84440)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_57(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoS2 < 7871/126) & (skoX < 1) & (63*skoS2/1280 - 7871/2560 > skoX*(skoX*(126*skoS2 - 7871) - 158680)/2560) & (63*skoS2/640 - 7871/1280 > skoX*(skoX*(126*skoS2 + 79340*skoX - 7871) - 158680)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoS2'), Rational(7871, 126)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(63, 1280), Symbol('skoS2')), Rational(-7871, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(-7871))), Integer(-158680)))), StrictGreaterThan(Add(Mul(Rational(63, 640), Symbol('skoS2')), Rational(-7871, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Mul(Integer(79340), Symbol('skoX')), Integer(-7871))), Integer(-158680)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_58(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (120897*skoS2/1280 + 24947/512 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (120897*skoS2/1280 - skoSM*(126*skoS2 + 61)/40 + 125247/2560 < skoX*(2560*skoSM + skoX*(241794*skoS2 - 64*skoSM*(126*skoS2 + 61) + 125247) + 87000)/2560) & (120897*skoS2/640 - skoSM*(126*skoS2 + 61)/20 + 125247/1280 < skoX*(2560*skoSM + skoX*(241794*skoS2 - 64*skoSM*(126*skoS2 + 61) - 20*skoX*(64*skoSM + 2175) + 125247) + 87000)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(120897, 1280), Symbol('skoS2')), Rational(24947, 512)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(120897, 1280), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(125247, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(241794), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(125247))), Integer(87000)))), StrictLessThan(Add(Mul(Rational(120897, 640), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(125247, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(241794), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Mul(Integer(-1), Integer(20), Symbol('skoX'), Add(Mul(Integer(64), Symbol('skoSM')), Integer(2175))), Integer(125247))), Integer(87000)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_59(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoS2 < 129/2) & (skoX < 1) & (63*skoS2/1280 - 8127/2560 > 63*skoX*(skoX*(2*skoS2 - 129) - 2600)/2560) & (63*skoS2/640 - 8127/1280 > 63*skoX*(skoX*(2*skoS2 + 1300*skoX - 129) - 2600)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoS2'), Rational(129, 2)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(63, 1280), Symbol('skoS2')), Rational(-8127, 2560)), Mul(Rational(63, 2560), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(2), Symbol('skoS2')), Integer(-129))), Integer(-2600)))), StrictGreaterThan(Add(Mul(Rational(63, 640), Symbol('skoS2')), Rational(-8127, 1280)), Mul(Rational(63, 1280), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(2), Symbol('skoS2')), Mul(Integer(1300), Symbol('skoX')), Integer(-129))), Integer(-2600)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_60(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (124929*skoS2/1280 + 25779/512 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (124929*skoS2/1280 - skoSM*(126*skoS2 + 61)/40 + 129407/2560 < skoX*(2560*skoSM + skoX*(249858*skoS2 - 64*skoSM*(126*skoS2 + 61) + 129407) + 89560)/2560) & (124929*skoS2/640 - skoSM*(126*skoS2 + 61)/20 + 129407/1280 < skoX*(2560*skoSM + skoX*(249858*skoS2 - 64*skoSM*(126*skoS2 + 61) - 20*skoX*(64*skoSM + 2239) + 129407) + 89560)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(124929, 1280), Symbol('skoS2')), Rational(25779, 512)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(124929, 1280), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(129407, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(249858), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(129407))), Integer(89560)))), StrictLessThan(Add(Mul(Rational(124929, 640), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(129407, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(249858), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Mul(Integer(-1), Integer(20), Symbol('skoX'), Add(Mul(Integer(64), Symbol('skoSM')), Integer(2239))), Integer(129407))), Integer(89560)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_61(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoS2 < 8383/126) & (skoX < 1) & (63*skoS2/1280 - 8383/2560 > skoX*(skoX*(126*skoS2 - 8383) - 168920)/2560) & (63*skoS2/640 - 8383/1280 > skoX*(skoX*(126*skoS2 + 84460*skoX - 8383) - 168920)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoS2'), Rational(8383, 126)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(63, 1280), Symbol('skoS2')), Rational(-8383, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(-8383))), Integer(-168920)))), StrictGreaterThan(Add(Mul(Rational(63, 640), Symbol('skoS2')), Rational(-8383, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Mul(Integer(84460), Symbol('skoX')), Integer(-8383))), Integer(-168920)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_62(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (128961*skoS2/1280 + 26611/512 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (128961*skoS2/1280 - skoSM*(126*skoS2 + 61)/40 + 133567/2560 < skoX*(2560*skoSM + skoX*(257922*skoS2 - 64*skoSM*(126*skoS2 + 61) + 133567) + 92120)/2560) & (128961*skoS2/640 - skoSM*(126*skoS2 + 61)/20 + 133567/1280 < skoX*(2560*skoSM + skoX*(257922*skoS2 - 64*skoSM*(126*skoS2 + 61) - 20*skoX*(64*skoSM + 2303) + 133567) + 92120)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(128961, 1280), Symbol('skoS2')), Rational(26611, 512)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(128961, 1280), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(133567, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(257922), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(133567))), Integer(92120)))), StrictLessThan(Add(Mul(Rational(128961, 640), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(133567, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(257922), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Mul(Integer(-1), Integer(20), Symbol('skoX'), Add(Mul(Integer(64), Symbol('skoSM')), Integer(2303))), Integer(133567))), Integer(92120)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_63(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoS2 < 8639/126) & (skoX < 1) & (63*skoS2/1280 - 8639/2560 > skoX*(skoX*(126*skoS2 - 8639) - 174040)/2560) & (63*skoS2/640 - 8639/1280 > skoX*(skoX*(126*skoS2 + 87020*skoX - 8639) - 174040)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoS2'), Rational(8639, 126)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(63, 1280), Symbol('skoS2')), Rational(-8639, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(-8639))), Integer(-174040)))), StrictGreaterThan(Add(Mul(Rational(63, 640), Symbol('skoS2')), Rational(-8639, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Mul(Integer(87020), Symbol('skoX')), Integer(-8639))), Integer(-174040)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_64(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (132993*skoS2/1280 + 27443/512 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (132993*skoS2/1280 - skoSM*(126*skoS2 + 61)/40 + 137727/2560 < skoX*(2560*skoSM + skoX*(265986*skoS2 - 64*skoSM*(126*skoS2 + 61) + 137727) + 94680)/2560) & (132993*skoS2/640 - skoSM*(126*skoS2 + 61)/20 + 137727/1280 < skoX*(2560*skoSM + skoX*(265986*skoS2 - 64*skoSM*(126*skoS2 + 61) - 20*skoX*(64*skoSM + 2367) + 137727) + 94680)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(132993, 1280), Symbol('skoS2')), Rational(27443, 512)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(132993, 1280), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(137727, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(265986), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(137727))), Integer(94680)))), StrictLessThan(Add(Mul(Rational(132993, 640), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(137727, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(265986), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Mul(Integer(-1), Integer(20), Symbol('skoX'), Add(Mul(Integer(64), Symbol('skoSM')), Integer(2367))), Integer(137727))), Integer(94680)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_65(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoS2 < 2965/42) & (skoX < 1) & (63*skoS2/1280 - 1779/512 > 3*skoX*(skoX*(42*skoS2 - 2965) - 59720)/2560) & (63*skoS2/640 - 1779/256 > 3*skoX*(skoX*(42*skoS2 + 29860*skoX - 2965) - 59720)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoS2'), Rational(2965, 42)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(63, 1280), Symbol('skoS2')), Rational(-1779, 512)), Mul(Rational(3, 2560), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(42), Symbol('skoS2')), Integer(-2965))), Integer(-59720)))), StrictGreaterThan(Add(Mul(Rational(63, 640), Symbol('skoS2')), Rational(-1779, 256)), Mul(Rational(3, 1280), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(42), Symbol('skoS2')), Mul(Integer(29860), Symbol('skoX')), Integer(-2965))), Integer(-59720)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_66(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (27405*skoS2/256 + 28275/512 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (27405*skoS2/256 - skoSM*(126*skoS2 + 61)/40 + 141887/2560 < skoX*(2560*skoSM + skoX*(274050*skoS2 - 64*skoSM*(126*skoS2 + 61) + 141887) + 97240)/2560) & (27405*skoS2/128 - skoSM*(126*skoS2 + 61)/20 + 141887/1280 < skoX*(2560*skoSM + skoX*(274050*skoS2 - 64*skoSM*(126*skoS2 + 61) - 20*skoX*(64*skoSM + 2431) + 141887) + 97240)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(27405, 256), Symbol('skoS2')), Rational(28275, 512)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(27405, 256), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(141887, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(274050), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(141887))), Integer(97240)))), StrictLessThan(Add(Mul(Rational(27405, 128), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(141887, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(274050), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Mul(Integer(-1), Integer(20), Symbol('skoX'), Add(Mul(Integer(64), Symbol('skoSM')), Integer(2431))), Integer(141887))), Integer(97240)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_67(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoS2 < 9151/126) & (skoX < 1) & (63*skoS2/1280 - 9151/2560 > skoX*(skoX*(126*skoS2 - 9151) - 184280)/2560) & (63*skoS2/640 - 9151/1280 > skoX*(skoX*(126*skoS2 + 92140*skoX - 9151) - 184280)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoS2'), Rational(9151, 126)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(63, 1280), Symbol('skoS2')), Rational(-9151, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(-9151))), Integer(-184280)))), StrictGreaterThan(Add(Mul(Rational(63, 640), Symbol('skoS2')), Rational(-9151, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Mul(Integer(92140), Symbol('skoX')), Integer(-9151))), Integer(-184280)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_68(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (141057*skoS2/1280 + 29107/512 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (141057*skoS2/1280 - skoSM*(126*skoS2 + 61)/40 + 146047/2560 < skoX*(2560*skoSM + skoX*(282114*skoS2 - 64*skoSM*(126*skoS2 + 61) + 146047) + 99800)/2560) & (141057*skoS2/640 - skoSM*(126*skoS2 + 61)/20 + 146047/1280 < skoX*(2560*skoSM + skoX*(282114*skoS2 - 64*skoSM*(126*skoS2 + 61) - 20*skoX*(64*skoSM + 2495) + 146047) + 99800)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(141057, 1280), Symbol('skoS2')), Rational(29107, 512)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(141057, 1280), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(146047, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(282114), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(146047))), Integer(99800)))), StrictLessThan(Add(Mul(Rational(141057, 640), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(146047, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(282114), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Mul(Integer(-1), Integer(20), Symbol('skoX'), Add(Mul(Integer(64), Symbol('skoSM')), Integer(2495))), Integer(146047))), Integer(99800)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_69(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoS2 < 9407/126) & (skoX < 1) & (63*skoS2/1280 - 9407/2560 > skoX*(skoX*(126*skoS2 - 9407) - 189400)/2560) & (63*skoS2/640 - 9407/1280 > skoX*(skoX*(126*skoS2 + 94700*skoX - 9407) - 189400)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoS2'), Rational(9407, 126)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(63, 1280), Symbol('skoS2')), Rational(-9407, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(-9407))), Integer(-189400)))), StrictGreaterThan(Add(Mul(Rational(63, 640), Symbol('skoS2')), Rational(-9407, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Mul(Integer(94700), Symbol('skoX')), Integer(-9407))), Integer(-189400)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_70(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (145089*skoS2/1280 + 29939/512 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (145089*skoS2/1280 - skoSM*(126*skoS2 + 61)/40 + 150207/2560 < skoX*(2560*skoSM + skoX*(290178*skoS2 - 64*skoSM*(126*skoS2 + 61) + 150207) + 102360)/2560) & (145089*skoS2/640 - skoSM*(126*skoS2 + 61)/20 + 150207/1280 < skoX*(2560*skoSM + skoX*(290178*skoS2 - 64*skoSM*(126*skoS2 + 61) - 20*skoX*(64*skoSM + 2559) + 150207) + 102360)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(145089, 1280), Symbol('skoS2')), Rational(29939, 512)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(145089, 1280), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(150207, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(290178), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(150207))), Integer(102360)))), StrictLessThan(Add(Mul(Rational(145089, 640), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(150207, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(290178), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Mul(Integer(-1), Integer(20), Symbol('skoX'), Add(Mul(Integer(64), Symbol('skoSM')), Integer(2559))), Integer(150207))), Integer(102360)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_71(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoS2 < 3221/42) & (skoX < 1) & (63*skoS2/1280 - 9663/2560 > 3*skoX*(skoX*(42*skoS2 - 3221) - 64840)/2560) & (63*skoS2/640 - 9663/1280 > 3*skoX*(skoX*(42*skoS2 + 32420*skoX - 3221) - 64840)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoS2'), Rational(3221, 42)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(63, 1280), Symbol('skoS2')), Rational(-9663, 2560)), Mul(Rational(3, 2560), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(42), Symbol('skoS2')), Integer(-3221))), Integer(-64840)))), StrictGreaterThan(Add(Mul(Rational(63, 640), Symbol('skoS2')), Rational(-9663, 1280)), Mul(Rational(3, 1280), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(42), Symbol('skoS2')), Mul(Integer(32420), Symbol('skoX')), Integer(-3221))), Integer(-64840)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_72(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (149121*skoS2/1280 + 30771/512 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (149121*skoS2/1280 - skoSM*(126*skoS2 + 61)/40 + 154367/2560 < skoX*(2560*skoSM + skoX*(298242*skoS2 - 64*skoSM*(126*skoS2 + 61) + 154367) + 104920)/2560) & (149121*skoS2/640 - skoSM*(126*skoS2 + 61)/20 + 154367/1280 < skoX*(2560*skoSM + skoX*(298242*skoS2 - 64*skoSM*(126*skoS2 + 61) - 20*skoX*(64*skoSM + 2623) + 154367) + 104920)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(149121, 1280), Symbol('skoS2')), Rational(30771, 512)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(149121, 1280), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(154367, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(298242), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(154367))), Integer(104920)))), StrictLessThan(Add(Mul(Rational(149121, 640), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(154367, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(298242), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Mul(Integer(-1), Integer(20), Symbol('skoX'), Add(Mul(Integer(64), Symbol('skoSM')), Integer(2623))), Integer(154367))), Integer(104920)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_73(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoS2 < 1417/18) & (skoX < 1) & (63*skoS2/1280 - 9919/2560 > 7*skoX*(skoX*(18*skoS2 - 1417) - 28520)/2560) & (63*skoS2/640 - 9919/1280 > 7*skoX*(skoX*(18*skoS2 + 14260*skoX - 1417) - 28520)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoS2'), Rational(1417, 18)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(63, 1280), Symbol('skoS2')), Rational(-9919, 2560)), Mul(Rational(7, 2560), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(18), Symbol('skoS2')), Integer(-1417))), Integer(-28520)))), StrictGreaterThan(Add(Mul(Rational(63, 640), Symbol('skoS2')), Rational(-9919, 1280)), Mul(Rational(7, 1280), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(18), Symbol('skoS2')), Mul(Integer(14260), Symbol('skoX')), Integer(-1417))), Integer(-28520)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_74(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (153153*skoS2/1280 + 31603/512 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (153153*skoS2/1280 - skoSM*(126*skoS2 + 61)/40 + 158527/2560 < skoX*(2560*skoSM + skoX*(306306*skoS2 - 64*skoSM*(126*skoS2 + 61) + 158527) + 107480)/2560) & (153153*skoS2/640 - skoSM*(126*skoS2 + 61)/20 + 158527/1280 < skoX*(2560*skoSM + skoX*(306306*skoS2 - 64*skoSM*(126*skoS2 + 61) - 20*skoX*(64*skoSM + 2687) + 158527) + 107480)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(153153, 1280), Symbol('skoS2')), Rational(31603, 512)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(153153, 1280), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(158527, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(306306), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(158527))), Integer(107480)))), StrictLessThan(Add(Mul(Rational(153153, 640), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(158527, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(306306), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Mul(Integer(-1), Integer(20), Symbol('skoX'), Add(Mul(Integer(64), Symbol('skoSM')), Integer(2687))), Integer(158527))), Integer(107480)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_75(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoS2 < 10175/126) & (skoX < 1) & (63*skoS2/1280 - 2035/512 > skoX*(skoX*(126*skoS2 - 10175) - 204760)/2560) & (63*skoS2/640 - 2035/256 > skoX*(skoX*(126*skoS2 + 102380*skoX - 10175) - 204760)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoS2'), Rational(10175, 126)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(63, 1280), Symbol('skoS2')), Rational(-2035, 512)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(-10175))), Integer(-204760)))), StrictGreaterThan(Add(Mul(Rational(63, 640), Symbol('skoS2')), Rational(-2035, 256)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Mul(Integer(102380), Symbol('skoX')), Integer(-10175))), Integer(-204760)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_76(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (31437*skoS2/256 + 32435/512 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (31437*skoS2/256 - skoSM*(126*skoS2 + 61)/40 + 162687/2560 < skoX*(2560*skoSM + skoX*(314370*skoS2 - 64*skoSM*(126*skoS2 + 61) + 162687) + 110040)/2560) & (31437*skoS2/128 - skoSM*(126*skoS2 + 61)/20 + 162687/1280 < skoX*(2560*skoSM + skoX*(314370*skoS2 - 64*skoSM*(126*skoS2 + 61) - 20*skoX*(64*skoSM + 2751) + 162687) + 110040)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(31437, 256), Symbol('skoS2')), Rational(32435, 512)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(31437, 256), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(162687, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(314370), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(162687))), Integer(110040)))), StrictLessThan(Add(Mul(Rational(31437, 128), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(162687, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(314370), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Mul(Integer(-1), Integer(20), Symbol('skoX'), Add(Mul(Integer(64), Symbol('skoSM')), Integer(2751))), Integer(162687))), Integer(110040)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_77(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoS2 < 1159/14) & (skoX < 1) & (63*skoS2/1280 - 10431/2560 > 9*skoX*(skoX*(14*skoS2 - 1159) - 23320)/2560) & (63*skoS2/640 - 10431/1280 > 9*skoX*(skoX*(14*skoS2 + 11660*skoX - 1159) - 23320)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoS2'), Rational(1159, 14)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(63, 1280), Symbol('skoS2')), Rational(-10431, 2560)), Mul(Rational(9, 2560), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(14), Symbol('skoS2')), Integer(-1159))), Integer(-23320)))), StrictGreaterThan(Add(Mul(Rational(63, 640), Symbol('skoS2')), Rational(-10431, 1280)), Mul(Rational(9, 1280), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(14), Symbol('skoS2')), Mul(Integer(11660), Symbol('skoX')), Integer(-1159))), Integer(-23320)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_78(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (161217*skoS2/1280 + 33267/512 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (161217*skoS2/1280 - skoSM*(126*skoS2 + 61)/40 + 166847/2560 < skoX*(2560*skoSM + skoX*(322434*skoS2 - 64*skoSM*(126*skoS2 + 61) + 166847) + 112600)/2560) & (161217*skoS2/640 - skoSM*(126*skoS2 + 61)/20 + 166847/1280 < skoX*(2560*skoSM + skoX*(322434*skoS2 - 64*skoSM*(126*skoS2 + 61) - 20*skoX*(64*skoSM + 2815) + 166847) + 112600)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(161217, 1280), Symbol('skoS2')), Rational(33267, 512)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(161217, 1280), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(166847, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(322434), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(166847))), Integer(112600)))), StrictLessThan(Add(Mul(Rational(161217, 640), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(166847, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(322434), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Mul(Integer(-1), Integer(20), Symbol('skoX'), Add(Mul(Integer(64), Symbol('skoSM')), Integer(2815))), Integer(166847))), Integer(112600)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_79(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoS2 < 10687/126) & (skoX < 1) & (63*skoS2/1280 - 10687/2560 > skoX*(skoX*(126*skoS2 - 10687) - 215000)/2560) & (63*skoS2/640 - 10687/1280 > skoX*(skoX*(126*skoS2 + 107500*skoX - 10687) - 215000)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoS2'), Rational(10687, 126)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(63, 1280), Symbol('skoS2')), Rational(-10687, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(-10687))), Integer(-215000)))), StrictGreaterThan(Add(Mul(Rational(63, 640), Symbol('skoS2')), Rational(-10687, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Mul(Integer(107500), Symbol('skoX')), Integer(-10687))), Integer(-215000)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_80(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (165249*skoS2/1280 + 34099/512 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (165249*skoS2/1280 - skoSM*(126*skoS2 + 61)/40 + 171007/2560 < skoX*(2560*skoSM + skoX*(330498*skoS2 - 64*skoSM*(126*skoS2 + 61) + 171007) + 115160)/2560) & (165249*skoS2/640 - skoSM*(126*skoS2 + 61)/20 + 171007/1280 < skoX*(2560*skoSM + skoX*(330498*skoS2 - 64*skoSM*(126*skoS2 + 61) - 20*skoX*(64*skoSM + 2879) + 171007) + 115160)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(165249, 1280), Symbol('skoS2')), Rational(34099, 512)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(165249, 1280), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(171007, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(330498), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(171007))), Integer(115160)))), StrictLessThan(Add(Mul(Rational(165249, 640), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(171007, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(330498), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Mul(Integer(-1), Integer(20), Symbol('skoX'), Add(Mul(Integer(64), Symbol('skoSM')), Integer(2879))), Integer(171007))), Integer(115160)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_81(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoS2 < 10943/126) & (skoX < 1) & (63*skoS2/1280 - 10943/2560 > skoX*(skoX*(126*skoS2 - 10943) - 220120)/2560) & (63*skoS2/640 - 10943/1280 > skoX*(skoX*(126*skoS2 + 110060*skoX - 10943) - 220120)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoS2'), Rational(10943, 126)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(63, 1280), Symbol('skoS2')), Rational(-10943, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(-10943))), Integer(-220120)))), StrictGreaterThan(Add(Mul(Rational(63, 640), Symbol('skoS2')), Rational(-10943, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Mul(Integer(110060), Symbol('skoX')), Integer(-10943))), Integer(-220120)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_82(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (169281*skoS2/1280 + 34931/512 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (169281*skoS2/1280 - skoSM*(126*skoS2 + 61)/40 + 175167/2560 < skoX*(2560*skoSM + skoX*(338562*skoS2 - 64*skoSM*(126*skoS2 + 61) + 175167) + 117720)/2560) & (169281*skoS2/640 - skoSM*(126*skoS2 + 61)/20 + 175167/1280 < skoX*(2560*skoSM + skoX*(338562*skoS2 - 64*skoSM*(126*skoS2 + 61) - 20*skoX*(64*skoSM + 2943) + 175167) + 117720)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(169281, 1280), Symbol('skoS2')), Rational(34931, 512)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(169281, 1280), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(175167, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(338562), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(175167))), Integer(117720)))), StrictLessThan(Add(Mul(Rational(169281, 640), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(175167, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(338562), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Mul(Integer(-1), Integer(20), Symbol('skoX'), Add(Mul(Integer(64), Symbol('skoSM')), Integer(2943))), Integer(175167))), Integer(117720)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_83(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoS2 < 3733/42) & (skoX < 1) & (63*skoS2/1280 - 11199/2560 > 3*skoX*(skoX*(42*skoS2 - 3733) - 75080)/2560) & (63*skoS2/640 - 11199/1280 > 3*skoX*(skoX*(42*skoS2 + 37540*skoX - 3733) - 75080)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoS2'), Rational(3733, 42)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(63, 1280), Symbol('skoS2')), Rational(-11199, 2560)), Mul(Rational(3, 2560), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(42), Symbol('skoS2')), Integer(-3733))), Integer(-75080)))), StrictGreaterThan(Add(Mul(Rational(63, 640), Symbol('skoS2')), Rational(-11199, 1280)), Mul(Rational(3, 1280), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(42), Symbol('skoS2')), Mul(Integer(37540), Symbol('skoX')), Integer(-3733))), Integer(-75080)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_84(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (173313*skoS2/1280 + 35763/512 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (173313*skoS2/1280 - skoSM*(126*skoS2 + 61)/40 + 179327/2560 < skoX*(2560*skoSM + skoX*(346626*skoS2 - 64*skoSM*(126*skoS2 + 61) + 179327) + 120280)/2560) & (173313*skoS2/640 - skoSM*(126*skoS2 + 61)/20 + 179327/1280 < skoX*(2560*skoSM + skoX*(346626*skoS2 - 64*skoSM*(126*skoS2 + 61) - 20*skoX*(64*skoSM + 3007) + 179327) + 120280)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(173313, 1280), Symbol('skoS2')), Rational(35763, 512)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(173313, 1280), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(179327, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(346626), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(179327))), Integer(120280)))), StrictLessThan(Add(Mul(Rational(173313, 640), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(179327, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(346626), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Mul(Integer(-1), Integer(20), Symbol('skoX'), Add(Mul(Integer(64), Symbol('skoSM')), Integer(3007))), Integer(179327))), Integer(120280)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_85(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoS2 < 11455/126) & (skoX < 1) & (63*skoS2/1280 - 2291/512 > skoX*(skoX*(126*skoS2 - 11455) - 230360)/2560) & (63*skoS2/640 - 2291/256 > skoX*(skoX*(126*skoS2 + 115180*skoX - 11455) - 230360)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoS2'), Rational(11455, 126)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(63, 1280), Symbol('skoS2')), Rational(-2291, 512)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(-11455))), Integer(-230360)))), StrictGreaterThan(Add(Mul(Rational(63, 640), Symbol('skoS2')), Rational(-2291, 256)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Mul(Integer(115180), Symbol('skoX')), Integer(-11455))), Integer(-230360)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_86(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (35469*skoS2/256 + 36595/512 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (35469*skoS2/256 - skoSM*(126*skoS2 + 61)/40 + 183487/2560 < skoX*(2560*skoSM + skoX*(354690*skoS2 - 64*skoSM*(126*skoS2 + 61) + 183487) + 122840)/2560) & (35469*skoS2/128 - skoSM*(126*skoS2 + 61)/20 + 183487/1280 < skoX*(2560*skoSM + skoX*(354690*skoS2 - 64*skoSM*(126*skoS2 + 61) - 20*skoX*(64*skoSM + 3071) + 183487) + 122840)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(35469, 256), Symbol('skoS2')), Rational(36595, 512)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(35469, 256), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(183487, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(354690), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(183487))), Integer(122840)))), StrictLessThan(Add(Mul(Rational(35469, 128), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(183487, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(354690), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Mul(Integer(-1), Integer(20), Symbol('skoX'), Add(Mul(Integer(64), Symbol('skoSM')), Integer(3071))), Integer(183487))), Integer(122840)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_87(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoS2 < 1673/18) & (skoX < 1) & (63*skoS2/1280 - 11711/2560 > 7*skoX*(skoX*(18*skoS2 - 1673) - 33640)/2560) & (63*skoS2/640 - 11711/1280 > 7*skoX*(skoX*(18*skoS2 + 16820*skoX - 1673) - 33640)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoS2'), Rational(1673, 18)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(63, 1280), Symbol('skoS2')), Rational(-11711, 2560)), Mul(Rational(7, 2560), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(18), Symbol('skoS2')), Integer(-1673))), Integer(-33640)))), StrictGreaterThan(Add(Mul(Rational(63, 640), Symbol('skoS2')), Rational(-11711, 1280)), Mul(Rational(7, 1280), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(18), Symbol('skoS2')), Mul(Integer(16820), Symbol('skoX')), Integer(-1673))), Integer(-33640)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_88(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (181377*skoS2/1280 + 37427/512 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (181377*skoS2/1280 - skoSM*(126*skoS2 + 61)/40 + 187647/2560 < skoX*(2560*skoSM + skoX*(362754*skoS2 - 64*skoSM*(126*skoS2 + 61) + 187647) + 125400)/2560) & (181377*skoS2/640 - skoSM*(126*skoS2 + 61)/20 + 187647/1280 < skoX*(2560*skoSM + skoX*(362754*skoS2 - 64*skoSM*(126*skoS2 + 61) - 20*skoX*(64*skoSM + 3135) + 187647) + 125400)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(181377, 1280), Symbol('skoS2')), Rational(37427, 512)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(181377, 1280), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(187647, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(362754), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(187647))), Integer(125400)))), StrictLessThan(Add(Mul(Rational(181377, 640), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(187647, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(362754), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Mul(Integer(-1), Integer(20), Symbol('skoX'), Add(Mul(Integer(64), Symbol('skoSM')), Integer(3135))), Integer(187647))), Integer(125400)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_89(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoS2 < 3989/42) & (skoX < 1) & (63*skoS2/1280 - 11967/2560 > 3*skoX*(skoX*(42*skoS2 - 3989) - 80200)/2560) & (63*skoS2/640 - 11967/1280 > 3*skoX*(skoX*(42*skoS2 + 40100*skoX - 3989) - 80200)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoS2'), Rational(3989, 42)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(63, 1280), Symbol('skoS2')), Rational(-11967, 2560)), Mul(Rational(3, 2560), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(42), Symbol('skoS2')), Integer(-3989))), Integer(-80200)))), StrictGreaterThan(Add(Mul(Rational(63, 640), Symbol('skoS2')), Rational(-11967, 1280)), Mul(Rational(3, 1280), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(42), Symbol('skoS2')), Mul(Integer(40100), Symbol('skoX')), Integer(-3989))), Integer(-80200)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_90(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (185409*skoS2/1280 + 38259/512 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (185409*skoS2/1280 - skoSM*(126*skoS2 + 61)/40 + 191807/2560 < skoX*(2560*skoSM + skoX*(370818*skoS2 - 64*skoSM*(126*skoS2 + 61) + 191807) + 127960)/2560) & (185409*skoS2/640 - skoSM*(126*skoS2 + 61)/20 + 191807/1280 < skoX*(2560*skoSM + skoX*(370818*skoS2 - 64*skoSM*(126*skoS2 + 61) - 20*skoX*(64*skoSM + 3199) + 191807) + 127960)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(185409, 1280), Symbol('skoS2')), Rational(38259, 512)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(185409, 1280), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(191807, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(370818), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(191807))), Integer(127960)))), StrictLessThan(Add(Mul(Rational(185409, 640), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(191807, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(370818), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Mul(Integer(-1), Integer(20), Symbol('skoX'), Add(Mul(Integer(64), Symbol('skoSM')), Integer(3199))), Integer(191807))), Integer(127960)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_91(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoS2 < 12223/126) & (skoX < 1) & (63*skoS2/1280 - 12223/2560 > skoX*(skoX*(126*skoS2 - 12223) - 245720)/2560) & (63*skoS2/640 - 12223/1280 > skoX*(skoX*(126*skoS2 + 122860*skoX - 12223) - 245720)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoS2'), Rational(12223, 126)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(63, 1280), Symbol('skoS2')), Rational(-12223, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(-12223))), Integer(-245720)))), StrictGreaterThan(Add(Mul(Rational(63, 640), Symbol('skoS2')), Rational(-12223, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Mul(Integer(122860), Symbol('skoX')), Integer(-12223))), Integer(-245720)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_92(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (189441*skoS2/1280 + 39091/512 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (189441*skoS2/1280 - skoSM*(126*skoS2 + 61)/40 + 195967/2560 < skoX*(2560*skoSM + skoX*(378882*skoS2 - 64*skoSM*(126*skoS2 + 61) + 195967) + 130520)/2560) & (189441*skoS2/640 - skoSM*(126*skoS2 + 61)/20 + 195967/1280 < skoX*(2560*skoSM + skoX*(378882*skoS2 - 64*skoSM*(126*skoS2 + 61) - 20*skoX*(64*skoSM + 3263) + 195967) + 130520)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(189441, 1280), Symbol('skoS2')), Rational(39091, 512)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(189441, 1280), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(195967, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(378882), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(195967))), Integer(130520)))), StrictLessThan(Add(Mul(Rational(189441, 640), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(195967, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(378882), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Mul(Integer(-1), Integer(20), Symbol('skoX'), Add(Mul(Integer(64), Symbol('skoSM')), Integer(3263))), Integer(195967))), Integer(130520)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_93(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoS2 < 12479/126) & (skoX < 1) & (63*skoS2/1280 - 12479/2560 > skoX*(skoX*(126*skoS2 - 12479) - 250840)/2560) & (63*skoS2/640 - 12479/1280 > skoX*(skoX*(126*skoS2 + 125420*skoX - 12479) - 250840)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoS2'), Rational(12479, 126)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(63, 1280), Symbol('skoS2')), Rational(-12479, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(-12479))), Integer(-250840)))), StrictGreaterThan(Add(Mul(Rational(63, 640), Symbol('skoS2')), Rational(-12479, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Mul(Integer(125420), Symbol('skoX')), Integer(-12479))), Integer(-250840)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_94(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (193473*skoS2/1280 + 39923/512 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (193473*skoS2/1280 - skoSM*(126*skoS2 + 61)/40 + 200127/2560 < skoX*(2560*skoSM + skoX*(386946*skoS2 - 64*skoSM*(126*skoS2 + 61) + 200127) + 133080)/2560) & (193473*skoS2/640 - skoSM*(126*skoS2 + 61)/20 + 200127/1280 < skoX*(2560*skoSM + skoX*(386946*skoS2 - 64*skoSM*(126*skoS2 + 61) - 20*skoX*(64*skoSM + 3327) + 200127) + 133080)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(193473, 1280), Symbol('skoS2')), Rational(39923, 512)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(193473, 1280), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(200127, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(386946), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(200127))), Integer(133080)))), StrictLessThan(Add(Mul(Rational(193473, 640), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(200127, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(386946), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Mul(Integer(-1), Integer(20), Symbol('skoX'), Add(Mul(Integer(64), Symbol('skoSM')), Integer(3327))), Integer(200127))), Integer(133080)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_95(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoS2 < 1415/14) & (skoX < 1) & (63*skoS2/1280 - 2547/512 > 9*skoX*(skoX*(14*skoS2 - 1415) - 28440)/2560) & (63*skoS2/640 - 2547/256 > 9*skoX*(skoX*(14*skoS2 + 14220*skoX - 1415) - 28440)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoS2'), Rational(1415, 14)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(63, 1280), Symbol('skoS2')), Rational(-2547, 512)), Mul(Rational(9, 2560), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(14), Symbol('skoS2')), Integer(-1415))), Integer(-28440)))), StrictGreaterThan(Add(Mul(Rational(63, 640), Symbol('skoS2')), Rational(-2547, 256)), Mul(Rational(9, 1280), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(14), Symbol('skoS2')), Mul(Integer(14220), Symbol('skoX')), Integer(-1415))), Integer(-28440)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_96(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (39501*skoS2/256 + 40755/512 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (39501*skoS2/256 - skoSM*(126*skoS2 + 61)/40 + 204287/2560 < skoX*(2560*skoSM + skoX*(395010*skoS2 - 64*skoSM*(126*skoS2 + 61) + 204287) + 135640)/2560) & (39501*skoS2/128 - skoSM*(126*skoS2 + 61)/20 + 204287/1280 < skoX*(2560*skoSM + skoX*(395010*skoS2 - 64*skoSM*(126*skoS2 + 61) - 20*skoX*(64*skoSM + 3391) + 204287) + 135640)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(39501, 256), Symbol('skoS2')), Rational(40755, 512)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(39501, 256), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(204287, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(395010), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(204287))), Integer(135640)))), StrictLessThan(Add(Mul(Rational(39501, 128), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(204287, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(395010), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Mul(Integer(-1), Integer(20), Symbol('skoX'), Add(Mul(Integer(64), Symbol('skoSM')), Integer(3391))), Integer(204287))), Integer(135640)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_97(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoS2 < 12991/126) & (skoX < 1) & (63*skoS2/1280 - 12991/2560 > skoX*(skoX*(126*skoS2 - 12991) - 261080)/2560) & (63*skoS2/640 - 12991/1280 > skoX*(skoX*(126*skoS2 + 130540*skoX - 12991) - 261080)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoS2'), Rational(12991, 126)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(63, 1280), Symbol('skoS2')), Rational(-12991, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(-12991))), Integer(-261080)))), StrictGreaterThan(Add(Mul(Rational(63, 640), Symbol('skoS2')), Rational(-12991, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Mul(Integer(130540), Symbol('skoX')), Integer(-12991))), Integer(-261080)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_98(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (201537*skoS2/1280 + 41587/512 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (201537*skoS2/1280 - skoSM*(126*skoS2 + 61)/40 + 208447/2560 < skoX*(2560*skoSM + skoX*(403074*skoS2 - 64*skoSM*(126*skoS2 + 61) + 208447) + 138200)/2560) & (201537*skoS2/640 - skoSM*(126*skoS2 + 61)/20 + 208447/1280 < skoX*(2560*skoSM + skoX*(403074*skoS2 - 64*skoSM*(126*skoS2 + 61) - 20*skoX*(64*skoSM + 3455) + 208447) + 138200)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(201537, 1280), Symbol('skoS2')), Rational(41587, 512)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(201537, 1280), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(208447, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(403074), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(208447))), Integer(138200)))), StrictLessThan(Add(Mul(Rational(201537, 640), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(208447, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(403074), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Mul(Integer(-1), Integer(20), Symbol('skoX'), Add(Mul(Integer(64), Symbol('skoSM')), Integer(3455))), Integer(208447))), Integer(138200)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_99(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoS2 < 13247/126) & (skoX < 1) & (63*skoS2/1280 - 13247/2560 > skoX*(skoX*(126*skoS2 - 13247) - 266200)/2560) & (63*skoS2/640 - 13247/1280 > skoX*(skoX*(126*skoS2 + 133100*skoX - 13247) - 266200)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoS2'), Rational(13247, 126)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(63, 1280), Symbol('skoS2')), Rational(-13247, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(-13247))), Integer(-266200)))), StrictGreaterThan(Add(Mul(Rational(63, 640), Symbol('skoS2')), Rational(-13247, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Mul(Integer(133100), Symbol('skoX')), Integer(-13247))), Integer(-266200)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_100(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (205569*skoS2/1280 + 42419/512 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (205569*skoS2/1280 - skoSM*(126*skoS2 + 61)/40 + 212607/2560 < skoX*(2560*skoSM + skoX*(411138*skoS2 - 64*skoSM*(126*skoS2 + 61) + 212607) + 140760)/2560) & (205569*skoS2/640 - skoSM*(126*skoS2 + 61)/20 + 212607/1280 < skoX*(2560*skoSM + skoX*(411138*skoS2 - 64*skoSM*(126*skoS2 + 61) - 20*skoX*(64*skoSM + 3519) + 212607) + 140760)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(205569, 1280), Symbol('skoS2')), Rational(42419, 512)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(205569, 1280), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(212607, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(411138), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(212607))), Integer(140760)))), StrictLessThan(Add(Mul(Rational(205569, 640), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(212607, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(411138), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Mul(Integer(-1), Integer(20), Symbol('skoX'), Add(Mul(Integer(64), Symbol('skoSM')), Integer(3519))), Integer(212607))), Integer(140760)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_101(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoS2 < 643/6) & (skoX < 1) & (63*skoS2/1280 - 13503/2560 > 21*skoX*(skoX*(6*skoS2 - 643) - 12920)/2560) & (63*skoS2/640 - 13503/1280 > 21*skoX*(skoX*(6*skoS2 + 6460*skoX - 643) - 12920)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoS2'), Rational(643, 6)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(63, 1280), Symbol('skoS2')), Rational(-13503, 2560)), Mul(Rational(21, 2560), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(6), Symbol('skoS2')), Integer(-643))), Integer(-12920)))), StrictGreaterThan(Add(Mul(Rational(63, 640), Symbol('skoS2')), Rational(-13503, 1280)), Mul(Rational(21, 1280), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(6), Symbol('skoS2')), Mul(Integer(6460), Symbol('skoX')), Integer(-643))), Integer(-12920)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_102(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (209601*skoS2/1280 + 43251/512 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (209601*skoS2/1280 - skoSM*(126*skoS2 + 61)/40 + 216767/2560 < skoX*(2560*skoSM + skoX*(419202*skoS2 - 64*skoSM*(126*skoS2 + 61) + 216767) + 143320)/2560) & (209601*skoS2/640 - skoSM*(126*skoS2 + 61)/20 + 216767/1280 < skoX*(2560*skoSM + skoX*(419202*skoS2 - 64*skoSM*(126*skoS2 + 61) - 20*skoX*(64*skoSM + 3583) + 216767) + 143320)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(209601, 1280), Symbol('skoS2')), Rational(43251, 512)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(209601, 1280), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(216767, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(419202), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(216767))), Integer(143320)))), StrictLessThan(Add(Mul(Rational(209601, 640), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(216767, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(419202), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Mul(Integer(-1), Integer(20), Symbol('skoX'), Add(Mul(Integer(64), Symbol('skoSM')), Integer(3583))), Integer(216767))), Integer(143320)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_103(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoS2 < 13759/126) & (skoX < 1) & (63*skoS2/1280 - 13759/2560 > skoX*(skoX*(126*skoS2 - 13759) - 276440)/2560) & (63*skoS2/640 - 13759/1280 > skoX*(skoX*(126*skoS2 + 138220*skoX - 13759) - 276440)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoS2'), Rational(13759, 126)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(63, 1280), Symbol('skoS2')), Rational(-13759, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(-13759))), Integer(-276440)))), StrictGreaterThan(Add(Mul(Rational(63, 640), Symbol('skoS2')), Rational(-13759, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Mul(Integer(138220), Symbol('skoX')), Integer(-13759))), Integer(-276440)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_104(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (213633*skoS2/1280 + 44083/512 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (213633*skoS2/1280 - skoSM*(126*skoS2 + 61)/40 + 220927/2560 < skoX*(2560*skoSM + skoX*(427266*skoS2 - 64*skoSM*(126*skoS2 + 61) + 220927) + 145880)/2560) & (213633*skoS2/640 - skoSM*(126*skoS2 + 61)/20 + 220927/1280 < skoX*(2560*skoSM + skoX*(427266*skoS2 - 64*skoSM*(126*skoS2 + 61) - 20*skoX*(64*skoSM + 3647) + 220927) + 145880)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(213633, 1280), Symbol('skoS2')), Rational(44083, 512)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(213633, 1280), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(220927, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(427266), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(220927))), Integer(145880)))), StrictLessThan(Add(Mul(Rational(213633, 640), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(220927, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(427266), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Mul(Integer(-1), Integer(20), Symbol('skoX'), Add(Mul(Integer(64), Symbol('skoSM')), Integer(3647))), Integer(220927))), Integer(145880)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_105(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoS2 < 14015/126) & (skoX < 1) & (63*skoS2/1280 - 2803/512 > skoX*(skoX*(126*skoS2 - 14015) - 281560)/2560) & (63*skoS2/640 - 2803/256 > skoX*(skoX*(126*skoS2 + 140780*skoX - 14015) - 281560)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoS2'), Rational(14015, 126)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(63, 1280), Symbol('skoS2')), Rational(-2803, 512)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(-14015))), Integer(-281560)))), StrictGreaterThan(Add(Mul(Rational(63, 640), Symbol('skoS2')), Rational(-2803, 256)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Mul(Integer(140780), Symbol('skoX')), Integer(-14015))), Integer(-281560)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_106(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (43533*skoS2/256 + 44915/512 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (43533*skoS2/256 - skoSM*(126*skoS2 + 61)/40 + 225087/2560 < skoX*(2560*skoSM + skoX*(435330*skoS2 - 64*skoSM*(126*skoS2 + 61) + 225087) + 148440)/2560) & (43533*skoS2/128 - skoSM*(126*skoS2 + 61)/20 + 225087/1280 < skoX*(2560*skoSM + skoX*(435330*skoS2 - 64*skoSM*(126*skoS2 + 61) - 20*skoX*(64*skoSM + 3711) + 225087) + 148440)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(43533, 256), Symbol('skoS2')), Rational(44915, 512)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(43533, 256), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(225087, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(435330), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(225087))), Integer(148440)))), StrictLessThan(Add(Mul(Rational(43533, 128), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(225087, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(435330), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Mul(Integer(-1), Integer(20), Symbol('skoX'), Add(Mul(Integer(64), Symbol('skoSM')), Integer(3711))), Integer(225087))), Integer(148440)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_107(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoS2 < 4757/42) & (skoX < 1) & (63*skoS2/1280 - 14271/2560 > 3*skoX*(skoX*(42*skoS2 - 4757) - 95560)/2560) & (63*skoS2/640 - 14271/1280 > 3*skoX*(skoX*(42*skoS2 + 47780*skoX - 4757) - 95560)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoS2'), Rational(4757, 42)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(63, 1280), Symbol('skoS2')), Rational(-14271, 2560)), Mul(Rational(3, 2560), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(42), Symbol('skoS2')), Integer(-4757))), Integer(-95560)))), StrictGreaterThan(Add(Mul(Rational(63, 640), Symbol('skoS2')), Rational(-14271, 1280)), Mul(Rational(3, 1280), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(42), Symbol('skoS2')), Mul(Integer(47780), Symbol('skoX')), Integer(-4757))), Integer(-95560)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_108(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (221697*skoS2/1280 + 45747/512 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (221697*skoS2/1280 - skoSM*(126*skoS2 + 61)/40 + 229247/2560 < skoX*(2560*skoSM + skoX*(443394*skoS2 - 64*skoSM*(126*skoS2 + 61) + 229247) + 151000)/2560) & (221697*skoS2/640 - skoSM*(126*skoS2 + 61)/20 + 229247/1280 < skoX*(2560*skoSM + skoX*(443394*skoS2 - 64*skoSM*(126*skoS2 + 61) - 20*skoX*(64*skoSM + 3775) + 229247) + 151000)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(221697, 1280), Symbol('skoS2')), Rational(45747, 512)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(221697, 1280), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(229247, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(443394), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(229247))), Integer(151000)))), StrictLessThan(Add(Mul(Rational(221697, 640), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(229247, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(443394), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Mul(Integer(-1), Integer(20), Symbol('skoX'), Add(Mul(Integer(64), Symbol('skoSM')), Integer(3775))), Integer(229247))), Integer(151000)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_109(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoS2 < 14527/126) & (skoX < 1) & (63*skoS2/1280 - 14527/2560 > skoX*(skoX*(126*skoS2 - 14527) - 291800)/2560) & (63*skoS2/640 - 14527/1280 > skoX*(skoX*(126*skoS2 + 145900*skoX - 14527) - 291800)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoS2'), Rational(14527, 126)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(63, 1280), Symbol('skoS2')), Rational(-14527, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(-14527))), Integer(-291800)))), StrictGreaterThan(Add(Mul(Rational(63, 640), Symbol('skoS2')), Rational(-14527, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Mul(Integer(145900), Symbol('skoX')), Integer(-14527))), Integer(-291800)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_110(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (225729*skoS2/1280 + 46579/512 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (225729*skoS2/1280 - skoSM*(126*skoS2 + 61)/40 + 233407/2560 < skoX*(2560*skoSM + skoX*(451458*skoS2 - 64*skoSM*(126*skoS2 + 61) + 233407) + 153560)/2560) & (225729*skoS2/640 - skoSM*(126*skoS2 + 61)/20 + 233407/1280 < skoX*(2560*skoSM + skoX*(451458*skoS2 - 64*skoSM*(126*skoS2 + 61) - 20*skoX*(64*skoSM + 3839) + 233407) + 153560)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(225729, 1280), Symbol('skoS2')), Rational(46579, 512)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(225729, 1280), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(233407, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(451458), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(233407))), Integer(153560)))), StrictLessThan(Add(Mul(Rational(225729, 640), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(233407, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(451458), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Mul(Integer(-1), Integer(20), Symbol('skoX'), Add(Mul(Integer(64), Symbol('skoSM')), Integer(3839))), Integer(233407))), Integer(153560)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_111(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoS2 < 14783/126) & (skoX < 1) & (63*skoS2/1280 - 14783/2560 > skoX*(skoX*(126*skoS2 - 14783) - 296920)/2560) & (63*skoS2/640 - 14783/1280 > skoX*(skoX*(126*skoS2 + 148460*skoX - 14783) - 296920)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoS2'), Rational(14783, 126)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(63, 1280), Symbol('skoS2')), Rational(-14783, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(-14783))), Integer(-296920)))), StrictGreaterThan(Add(Mul(Rational(63, 640), Symbol('skoS2')), Rational(-14783, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Mul(Integer(148460), Symbol('skoX')), Integer(-14783))), Integer(-296920)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_112(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (229761*skoS2/1280 + 47411/512 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (229761*skoS2/1280 - skoSM*(126*skoS2 + 61)/40 + 237567/2560 < skoX*(2560*skoSM + skoX*(459522*skoS2 - 64*skoSM*(126*skoS2 + 61) + 237567) + 156120)/2560) & (229761*skoS2/640 - skoSM*(126*skoS2 + 61)/20 + 237567/1280 < skoX*(2560*skoSM + skoX*(459522*skoS2 - 64*skoSM*(126*skoS2 + 61) - 20*skoX*(64*skoSM + 3903) + 237567) + 156120)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(229761, 1280), Symbol('skoS2')), Rational(47411, 512)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(229761, 1280), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(237567, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(459522), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(237567))), Integer(156120)))), StrictLessThan(Add(Mul(Rational(229761, 640), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(237567, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(459522), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Mul(Integer(-1), Integer(20), Symbol('skoX'), Add(Mul(Integer(64), Symbol('skoSM')), Integer(3903))), Integer(237567))), Integer(156120)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_113(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoS2 < 1671/14) & (skoX < 1) & (63*skoS2/1280 - 15039/2560 > 9*skoX*(skoX*(14*skoS2 - 1671) - 33560)/2560) & (63*skoS2/640 - 15039/1280 > 9*skoX*(skoX*(14*skoS2 + 16780*skoX - 1671) - 33560)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoS2'), Rational(1671, 14)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(63, 1280), Symbol('skoS2')), Rational(-15039, 2560)), Mul(Rational(9, 2560), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(14), Symbol('skoS2')), Integer(-1671))), Integer(-33560)))), StrictGreaterThan(Add(Mul(Rational(63, 640), Symbol('skoS2')), Rational(-15039, 1280)), Mul(Rational(9, 1280), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(14), Symbol('skoS2')), Mul(Integer(16780), Symbol('skoX')), Integer(-1671))), Integer(-33560)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_114(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (233793*skoS2/1280 + 48243/512 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (233793*skoS2/1280 - skoSM*(126*skoS2 + 61)/40 + 241727/2560 < skoX*(2560*skoSM + skoX*(467586*skoS2 - 64*skoSM*(126*skoS2 + 61) + 241727) + 158680)/2560) & (233793*skoS2/640 - skoSM*(126*skoS2 + 61)/20 + 241727/1280 < skoX*(2560*skoSM + skoX*(467586*skoS2 - 64*skoSM*(126*skoS2 + 61) - 20*skoX*(64*skoSM + 3967) + 241727) + 158680)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(233793, 1280), Symbol('skoS2')), Rational(48243, 512)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(233793, 1280), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(241727, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(467586), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(241727))), Integer(158680)))), StrictLessThan(Add(Mul(Rational(233793, 640), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(241727, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(467586), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Mul(Integer(-1), Integer(20), Symbol('skoX'), Add(Mul(Integer(64), Symbol('skoSM')), Integer(3967))), Integer(241727))), Integer(158680)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_115(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoS2 < 2185/18) & (skoX < 1) & (63*skoS2/1280 - 3059/512 > 7*skoX*(skoX*(18*skoS2 - 2185) - 43880)/2560) & (63*skoS2/640 - 3059/256 > 7*skoX*(skoX*(18*skoS2 + 21940*skoX - 2185) - 43880)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoS2'), Rational(2185, 18)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(63, 1280), Symbol('skoS2')), Rational(-3059, 512)), Mul(Rational(7, 2560), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(18), Symbol('skoS2')), Integer(-2185))), Integer(-43880)))), StrictGreaterThan(Add(Mul(Rational(63, 640), Symbol('skoS2')), Rational(-3059, 256)), Mul(Rational(7, 1280), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(18), Symbol('skoS2')), Mul(Integer(21940), Symbol('skoX')), Integer(-2185))), Integer(-43880)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_116(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (47565*skoS2/256 + 49075/512 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (47565*skoS2/256 - skoSM*(126*skoS2 + 61)/40 + 245887/2560 < skoX*(2560*skoSM + skoX*(475650*skoS2 - 64*skoSM*(126*skoS2 + 61) + 245887) + 161240)/2560) & (47565*skoS2/128 - skoSM*(126*skoS2 + 61)/20 + 245887/1280 < skoX*(2560*skoSM + skoX*(475650*skoS2 - 64*skoSM*(126*skoS2 + 61) - 20*skoX*(64*skoSM + 4031) + 245887) + 161240)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(47565, 256), Symbol('skoS2')), Rational(49075, 512)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(47565, 256), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(245887, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(475650), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(245887))), Integer(161240)))), StrictLessThan(Add(Mul(Rational(47565, 128), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(245887, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(475650), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Mul(Integer(-1), Integer(20), Symbol('skoX'), Add(Mul(Integer(64), Symbol('skoSM')), Integer(4031))), Integer(245887))), Integer(161240)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_117(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoS2 < 15551/126) & (skoX < 1) & (63*skoS2/1280 - 15551/2560 > skoX*(skoX*(126*skoS2 - 15551) - 312280)/2560) & (63*skoS2/640 - 15551/1280 > skoX*(skoX*(126*skoS2 + 156140*skoX - 15551) - 312280)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoS2'), Rational(15551, 126)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(63, 1280), Symbol('skoS2')), Rational(-15551, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(-15551))), Integer(-312280)))), StrictGreaterThan(Add(Mul(Rational(63, 640), Symbol('skoS2')), Rational(-15551, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Mul(Integer(156140), Symbol('skoX')), Integer(-15551))), Integer(-312280)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_118(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (241857*skoS2/1280 + 49907/512 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (241857*skoS2/1280 - skoSM*(126*skoS2 + 61)/40 + 250047/2560 < skoX*(2560*skoSM + skoX*(483714*skoS2 - 64*skoSM*(126*skoS2 + 61) + 250047) + 163800)/2560) & (241857*skoS2/640 - skoSM*(126*skoS2 + 61)/20 + 250047/1280 < skoX*(2560*skoSM + skoX*(483714*skoS2 - 64*skoSM*(126*skoS2 + 61) - 20*skoX*(64*skoSM + 4095) + 250047) + 163800)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(241857, 1280), Symbol('skoS2')), Rational(49907, 512)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(241857, 1280), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(250047, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(483714), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(250047))), Integer(163800)))), StrictLessThan(Add(Mul(Rational(241857, 640), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(250047, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(483714), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Mul(Integer(-1), Integer(20), Symbol('skoX'), Add(Mul(Integer(64), Symbol('skoSM')), Integer(4095))), Integer(250047))), Integer(163800)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_119(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoS2 < 5269/42) & (skoX < 1) & (63*skoS2/1280 - 15807/2560 > 3*skoX*(skoX*(42*skoS2 - 5269) - 105800)/2560) & (63*skoS2/640 - 15807/1280 > 3*skoX*(skoX*(42*skoS2 + 52900*skoX - 5269) - 105800)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoS2'), Rational(5269, 42)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(63, 1280), Symbol('skoS2')), Rational(-15807, 2560)), Mul(Rational(3, 2560), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(42), Symbol('skoS2')), Integer(-5269))), Integer(-105800)))), StrictGreaterThan(Add(Mul(Rational(63, 640), Symbol('skoS2')), Rational(-15807, 1280)), Mul(Rational(3, 1280), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(42), Symbol('skoS2')), Mul(Integer(52900), Symbol('skoX')), Integer(-5269))), Integer(-105800)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_120(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (245889*skoS2/1280 + 50739/512 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (245889*skoS2/1280 - skoSM*(126*skoS2 + 61)/40 + 254207/2560 < skoX*(2560*skoSM + skoX*(491778*skoS2 - 64*skoSM*(126*skoS2 + 61) + 254207) + 166360)/2560) & (245889*skoS2/640 - skoSM*(126*skoS2 + 61)/20 + 254207/1280 < skoX*(2560*skoSM + skoX*(491778*skoS2 - 64*skoSM*(126*skoS2 + 61) - 20*skoX*(64*skoSM + 4159) + 254207) + 166360)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(245889, 1280), Symbol('skoS2')), Rational(50739, 512)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(245889, 1280), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(254207, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(491778), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(254207))), Integer(166360)))), StrictLessThan(Add(Mul(Rational(245889, 640), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(254207, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(491778), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Mul(Integer(-1), Integer(20), Symbol('skoX'), Add(Mul(Integer(64), Symbol('skoSM')), Integer(4159))), Integer(254207))), Integer(166360)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_121(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoS2 < 16063/126) & (skoX < 1) & (63*skoS2/1280 - 16063/2560 > skoX*(skoX*(126*skoS2 - 16063) - 322520)/2560) & (63*skoS2/640 - 16063/1280 > skoX*(skoX*(126*skoS2 + 161260*skoX - 16063) - 322520)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoS2'), Rational(16063, 126)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(63, 1280), Symbol('skoS2')), Rational(-16063, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(-16063))), Integer(-322520)))), StrictGreaterThan(Add(Mul(Rational(63, 640), Symbol('skoS2')), Rational(-16063, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Mul(Integer(161260), Symbol('skoX')), Integer(-16063))), Integer(-322520)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_122(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (249921*skoS2/1280 + 51571/512 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (249921*skoS2/1280 - skoSM*(126*skoS2 + 61)/40 + 258367/2560 < skoX*(2560*skoSM + skoX*(499842*skoS2 - 64*skoSM*(126*skoS2 + 61) + 258367) + 168920)/2560) & (249921*skoS2/640 - skoSM*(126*skoS2 + 61)/20 + 258367/1280 < skoX*(2560*skoSM + skoX*(499842*skoS2 - 64*skoSM*(126*skoS2 + 61) - 20*skoX*(64*skoSM + 4223) + 258367) + 168920)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(249921, 1280), Symbol('skoS2')), Rational(51571, 512)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(249921, 1280), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(258367, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(499842), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(258367))), Integer(168920)))), StrictLessThan(Add(Mul(Rational(249921, 640), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(258367, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(499842), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Mul(Integer(-1), Integer(20), Symbol('skoX'), Add(Mul(Integer(64), Symbol('skoSM')), Integer(4223))), Integer(258367))), Integer(168920)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_123(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoS2 < 16319/126) & (skoX < 1) & (63*skoS2/1280 - 16319/2560 > skoX*(skoX*(126*skoS2 - 16319) - 327640)/2560) & (63*skoS2/640 - 16319/1280 > skoX*(skoX*(126*skoS2 + 163820*skoX - 16319) - 327640)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoS2'), Rational(16319, 126)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(63, 1280), Symbol('skoS2')), Rational(-16319, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(-16319))), Integer(-327640)))), StrictGreaterThan(Add(Mul(Rational(63, 640), Symbol('skoS2')), Rational(-16319, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Mul(Integer(163820), Symbol('skoX')), Integer(-16319))), Integer(-327640)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_124(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (253953*skoS2/1280 + 52403/512 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (253953*skoS2/1280 - skoSM*(126*skoS2 + 61)/40 + 262527/2560 < skoX*(2560*skoSM + skoX*(507906*skoS2 - 64*skoSM*(126*skoS2 + 61) + 262527) + 171480)/2560) & (253953*skoS2/640 - skoSM*(126*skoS2 + 61)/20 + 262527/1280 < skoX*(2560*skoSM + skoX*(507906*skoS2 - 64*skoSM*(126*skoS2 + 61) - 20*skoX*(64*skoSM + 4287) + 262527) + 171480)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(253953, 1280), Symbol('skoS2')), Rational(52403, 512)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(253953, 1280), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(262527, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(507906), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(262527))), Integer(171480)))), StrictLessThan(Add(Mul(Rational(253953, 640), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(262527, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(507906), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Mul(Integer(-1), Integer(20), Symbol('skoX'), Add(Mul(Integer(64), Symbol('skoSM')), Integer(4287))), Integer(262527))), Integer(171480)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_125(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoS2 < 5525/42) & (skoX < 1) & (63*skoS2/1280 - 3315/512 > 3*skoX*(skoX*(42*skoS2 - 5525) - 110920)/2560) & (63*skoS2/640 - 3315/256 > 3*skoX*(skoX*(42*skoS2 + 55460*skoX - 5525) - 110920)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoS2'), Rational(5525, 42)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(63, 1280), Symbol('skoS2')), Rational(-3315, 512)), Mul(Rational(3, 2560), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(42), Symbol('skoS2')), Integer(-5525))), Integer(-110920)))), StrictGreaterThan(Add(Mul(Rational(63, 640), Symbol('skoS2')), Rational(-3315, 256)), Mul(Rational(3, 1280), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(42), Symbol('skoS2')), Mul(Integer(55460), Symbol('skoX')), Integer(-5525))), Integer(-110920)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_126(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (51597*skoS2/256 + 53235/512 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (51597*skoS2/256 - skoSM*(126*skoS2 + 61)/40 + 266687/2560 < skoX*(2560*skoSM + skoX*(515970*skoS2 - 64*skoSM*(126*skoS2 + 61) + 266687) + 174040)/2560) & (51597*skoS2/128 - skoSM*(126*skoS2 + 61)/20 + 266687/1280 < skoX*(2560*skoSM + skoX*(515970*skoS2 - 64*skoSM*(126*skoS2 + 61) - 20*skoX*(64*skoSM + 4351) + 266687) + 174040)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(51597, 256), Symbol('skoS2')), Rational(53235, 512)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(51597, 256), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(266687, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(515970), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(266687))), Integer(174040)))), StrictLessThan(Add(Mul(Rational(51597, 128), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(266687, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(515970), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Mul(Integer(-1), Integer(20), Symbol('skoX'), Add(Mul(Integer(64), Symbol('skoSM')), Integer(4351))), Integer(266687))), Integer(174040)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_127(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoS2 < 16831/126) & (skoX < 1) & (63*skoS2/1280 - 16831/2560 > skoX*(skoX*(126*skoS2 - 16831) - 337880)/2560) & (63*skoS2/640 - 16831/1280 > skoX*(skoX*(126*skoS2 + 168940*skoX - 16831) - 337880)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoS2'), Rational(16831, 126)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(63, 1280), Symbol('skoS2')), Rational(-16831, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(-16831))), Integer(-337880)))), StrictGreaterThan(Add(Mul(Rational(63, 640), Symbol('skoS2')), Rational(-16831, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Mul(Integer(168940), Symbol('skoX')), Integer(-16831))), Integer(-337880)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_128(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (262017*skoS2/1280 + 54067/512 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (262017*skoS2/1280 - skoSM*(126*skoS2 + 61)/40 + 270847/2560 < skoX*(2560*skoSM + skoX*(524034*skoS2 - 64*skoSM*(126*skoS2 + 61) + 270847) + 176600)/2560) & (262017*skoS2/640 - skoSM*(126*skoS2 + 61)/20 + 270847/1280 < skoX*(2560*skoSM + skoX*(524034*skoS2 - 64*skoSM*(126*skoS2 + 61) - 20*skoX*(64*skoSM + 4415) + 270847) + 176600)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(262017, 1280), Symbol('skoS2')), Rational(54067, 512)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(262017, 1280), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(270847, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(524034), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(270847))), Integer(176600)))), StrictLessThan(Add(Mul(Rational(262017, 640), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(270847, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(524034), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Mul(Integer(-1), Integer(20), Symbol('skoX'), Add(Mul(Integer(64), Symbol('skoSM')), Integer(4415))), Integer(270847))), Integer(176600)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_129(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoS2 < 2441/18) & (skoX < 1) & (63*skoS2/1280 - 17087/2560 > 7*skoX*(skoX*(18*skoS2 - 2441) - 49000)/2560) & (63*skoS2/640 - 17087/1280 > 7*skoX*(skoX*(18*skoS2 + 24500*skoX - 2441) - 49000)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoS2'), Rational(2441, 18)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(63, 1280), Symbol('skoS2')), Rational(-17087, 2560)), Mul(Rational(7, 2560), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(18), Symbol('skoS2')), Integer(-2441))), Integer(-49000)))), StrictGreaterThan(Add(Mul(Rational(63, 640), Symbol('skoS2')), Rational(-17087, 1280)), Mul(Rational(7, 1280), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(18), Symbol('skoS2')), Mul(Integer(24500), Symbol('skoX')), Integer(-2441))), Integer(-49000)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_130(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (266049*skoS2/1280 + 54899/512 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (266049*skoS2/1280 - skoSM*(126*skoS2 + 61)/40 + 275007/2560 < skoX*(2560*skoSM + skoX*(532098*skoS2 - 64*skoSM*(126*skoS2 + 61) + 275007) + 179160)/2560) & (266049*skoS2/640 - skoSM*(126*skoS2 + 61)/20 + 275007/1280 < skoX*(2560*skoSM + skoX*(532098*skoS2 - 64*skoSM*(126*skoS2 + 61) - 20*skoX*(64*skoSM + 4479) + 275007) + 179160)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(266049, 1280), Symbol('skoS2')), Rational(54899, 512)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(266049, 1280), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(275007, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(532098), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(275007))), Integer(179160)))), StrictLessThan(Add(Mul(Rational(266049, 640), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(275007, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(532098), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Mul(Integer(-1), Integer(20), Symbol('skoX'), Add(Mul(Integer(64), Symbol('skoSM')), Integer(4479))), Integer(275007))), Integer(179160)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_131(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoS2 < 1927/14) & (skoX < 1) & (63*skoS2/1280 - 17343/2560 > 9*skoX*(skoX*(14*skoS2 - 1927) - 38680)/2560) & (63*skoS2/640 - 17343/1280 > 9*skoX*(skoX*(14*skoS2 + 19340*skoX - 1927) - 38680)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoS2'), Rational(1927, 14)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(63, 1280), Symbol('skoS2')), Rational(-17343, 2560)), Mul(Rational(9, 2560), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(14), Symbol('skoS2')), Integer(-1927))), Integer(-38680)))), StrictGreaterThan(Add(Mul(Rational(63, 640), Symbol('skoS2')), Rational(-17343, 1280)), Mul(Rational(9, 1280), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(14), Symbol('skoS2')), Mul(Integer(19340), Symbol('skoX')), Integer(-1927))), Integer(-38680)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_132(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (270081*skoS2/1280 + 55731/512 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (270081*skoS2/1280 - skoSM*(126*skoS2 + 61)/40 + 279167/2560 < skoX*(2560*skoSM + skoX*(540162*skoS2 - 64*skoSM*(126*skoS2 + 61) + 279167) + 181720)/2560) & (270081*skoS2/640 - skoSM*(126*skoS2 + 61)/20 + 279167/1280 < skoX*(2560*skoSM + skoX*(540162*skoS2 - 64*skoSM*(126*skoS2 + 61) - 20*skoX*(64*skoSM + 4543) + 279167) + 181720)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(270081, 1280), Symbol('skoS2')), Rational(55731, 512)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(270081, 1280), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(279167, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(540162), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(279167))), Integer(181720)))), StrictLessThan(Add(Mul(Rational(270081, 640), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(279167, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(540162), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Mul(Integer(-1), Integer(20), Symbol('skoX'), Add(Mul(Integer(64), Symbol('skoSM')), Integer(4543))), Integer(279167))), Integer(181720)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_133(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoS2 < 17599/126) & (skoX < 1) & (63*skoS2/1280 - 17599/2560 > skoX*(skoX*(126*skoS2 - 17599) - 353240)/2560) & (63*skoS2/640 - 17599/1280 > skoX*(skoX*(126*skoS2 + 176620*skoX - 17599) - 353240)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoS2'), Rational(17599, 126)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(63, 1280), Symbol('skoS2')), Rational(-17599, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(-17599))), Integer(-353240)))), StrictGreaterThan(Add(Mul(Rational(63, 640), Symbol('skoS2')), Rational(-17599, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Mul(Integer(176620), Symbol('skoX')), Integer(-17599))), Integer(-353240)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_134(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (274113*skoS2/1280 + 56563/512 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (274113*skoS2/1280 - skoSM*(126*skoS2 + 61)/40 + 283327/2560 < skoX*(2560*skoSM + skoX*(548226*skoS2 - 64*skoSM*(126*skoS2 + 61) + 283327) + 184280)/2560) & (274113*skoS2/640 - skoSM*(126*skoS2 + 61)/20 + 283327/1280 < skoX*(2560*skoSM + skoX*(548226*skoS2 - 64*skoSM*(126*skoS2 + 61) - 20*skoX*(64*skoSM + 4607) + 283327) + 184280)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(274113, 1280), Symbol('skoS2')), Rational(56563, 512)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(274113, 1280), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(283327, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(548226), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(283327))), Integer(184280)))), StrictLessThan(Add(Mul(Rational(274113, 640), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(283327, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(548226), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Mul(Integer(-1), Integer(20), Symbol('skoX'), Add(Mul(Integer(64), Symbol('skoSM')), Integer(4607))), Integer(283327))), Integer(184280)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_135(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoS2 < 17855/126) & (skoX < 1) & (63*skoS2/1280 - 3571/512 > skoX*(skoX*(126*skoS2 - 17855) - 358360)/2560) & (63*skoS2/640 - 3571/256 > skoX*(skoX*(126*skoS2 + 179180*skoX - 17855) - 358360)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoS2'), Rational(17855, 126)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(63, 1280), Symbol('skoS2')), Rational(-3571, 512)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(-17855))), Integer(-358360)))), StrictGreaterThan(Add(Mul(Rational(63, 640), Symbol('skoS2')), Rational(-3571, 256)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Mul(Integer(179180), Symbol('skoX')), Integer(-17855))), Integer(-358360)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_136(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (55629*skoS2/256 + 57395/512 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (55629*skoS2/256 - skoSM*(126*skoS2 + 61)/40 + 287487/2560 < skoX*(2560*skoSM + skoX*(556290*skoS2 - 64*skoSM*(126*skoS2 + 61) + 287487) + 186840)/2560) & (55629*skoS2/128 - skoSM*(126*skoS2 + 61)/20 + 287487/1280 < skoX*(2560*skoSM + skoX*(556290*skoS2 - 64*skoSM*(126*skoS2 + 61) - 20*skoX*(64*skoSM + 4671) + 287487) + 186840)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(55629, 256), Symbol('skoS2')), Rational(57395, 512)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(55629, 256), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(287487, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(556290), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(287487))), Integer(186840)))), StrictLessThan(Add(Mul(Rational(55629, 128), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(287487, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(556290), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Mul(Integer(-1), Integer(20), Symbol('skoX'), Add(Mul(Integer(64), Symbol('skoSM')), Integer(4671))), Integer(287487))), Integer(186840)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_137(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoS2 < 6037/42) & (skoX < 1) & (63*skoS2/1280 - 18111/2560 > 3*skoX*(skoX*(42*skoS2 - 6037) - 121160)/2560) & (63*skoS2/640 - 18111/1280 > 3*skoX*(skoX*(42*skoS2 + 60580*skoX - 6037) - 121160)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoS2'), Rational(6037, 42)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(63, 1280), Symbol('skoS2')), Rational(-18111, 2560)), Mul(Rational(3, 2560), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(42), Symbol('skoS2')), Integer(-6037))), Integer(-121160)))), StrictGreaterThan(Add(Mul(Rational(63, 640), Symbol('skoS2')), Rational(-18111, 1280)), Mul(Rational(3, 1280), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(42), Symbol('skoS2')), Mul(Integer(60580), Symbol('skoX')), Integer(-6037))), Integer(-121160)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_138(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (282177*skoS2/1280 + 58227/512 > skoSM*(126*skoS2 + 61)/40 - 1/5) & (282177*skoS2/1280 - skoSM*(126*skoS2 + 61)/40 + 291647/2560 < skoX*(2560*skoSM + skoX*(564354*skoS2 - 64*skoSM*(126*skoS2 + 61) + 291647) + 189400)/2560) & (282177*skoS2/640 - skoSM*(126*skoS2 + 61)/20 + 291647/1280 < skoX*(2560*skoSM + skoX*(564354*skoS2 - 64*skoSM*(126*skoS2 + 61) - 20*skoX*(64*skoSM + 4735) + 291647) + 189400)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(282177, 1280), Symbol('skoS2')), Rational(58227, 512)), Add(Mul(Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(-1, 5))), StrictLessThan(Add(Mul(Rational(282177, 1280), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(291647, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(564354), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(291647))), Integer(189400)))), StrictLessThan(Add(Mul(Rational(282177, 640), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(291647, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(564354), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Mul(Integer(-1), Integer(20), Symbol('skoX'), Add(Mul(Integer(64), Symbol('skoSM')), Integer(4735))), Integer(291647))), Integer(189400)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_139(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoS2 < 18367/126) & (skoX < 1) & (63*skoS2/1280 - 18367/2560 > skoX*(skoX*(126*skoS2 - 18367) - 368600)/2560) & (63*skoS2/640 - 18367/1280 > skoX*(skoX*(126*skoS2 + 184300*skoX - 18367) - 368600)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoS2'), Rational(18367, 126)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(63, 1280), Symbol('skoS2')), Rational(-18367, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(-18367))), Integer(-368600)))), StrictGreaterThan(Add(Mul(Rational(63, 640), Symbol('skoS2')), Rational(-18367, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Mul(Integer(184300), Symbol('skoX')), Integer(-18367))), Integer(-368600)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(delta:sympy.Rational, skoX:sympy.Rational, skoS2:sympy.Rational, skoSP:sympy.Rational, skoSM:sympy.Rational):
	# (0 <= delta) & (1 > skoX) & (skoS2 > 0) & (skoSM > 0) & (skoSP > 0) & (skoX > 0) & (skoSP*(63*skoS2/20 + 13/8) > skoSM*(63*skoS2/20 + 61/40) - 1/5) & (skoX*(skoSM + skoSP + skoX*(skoSM*(-63*skoS2/20 - 61/40) + skoSP*(63*skoS2/20 + 13/8) + 1/5) + 4) > skoSM*(-63*skoS2/20 - 61/40) + skoSP*(63*skoS2/20 + 13/8) + 1/5) & (skoX*(2*skoSM + 2*skoSP + skoX*(skoSM*(-63*skoS2/10 - 61/20) + skoSP*(63*skoS2/10 + 13/4) + skoX*(-skoSM - skoSP - 4) + 2/5) + 8) > skoSM*(-63*skoS2/10 - 61/20) + skoSP*(63*skoS2/10 + 13/4) + 2/5)

	post_cond =  And(LessThan(Integer(0), Symbol('delta')), StrictGreaterThan(Integer(1), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoSP'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictGreaterThan(Mul(Symbol('skoSP'), Add(Mul(Rational(63, 20), Symbol('skoS2')), Rational(13, 8))), Add(Mul(Symbol('skoSM'), Add(Mul(Rational(63, 20), Symbol('skoS2')), Rational(61, 40))), Rational(-1, 5))), StrictGreaterThan(Mul(Symbol('skoX'), Add(Symbol('skoSM'), Symbol('skoSP'), Mul(Symbol('skoX'), Add(Mul(Symbol('skoSM'), Add(Mul(Integer(-1), Rational(63, 20), Symbol('skoS2')), Rational(-61, 40))), Mul(Symbol('skoSP'), Add(Mul(Rational(63, 20), Symbol('skoS2')), Rational(13, 8))), Rational(1, 5))), Integer(4))), Add(Mul(Symbol('skoSM'), Add(Mul(Integer(-1), Rational(63, 20), Symbol('skoS2')), Rational(-61, 40))), Mul(Symbol('skoSP'), Add(Mul(Rational(63, 20), Symbol('skoS2')), Rational(13, 8))), Rational(1, 5))), StrictGreaterThan(Mul(Symbol('skoX'), Add(Mul(Integer(2), Symbol('skoSM')), Mul(Integer(2), Symbol('skoSP')), Mul(Symbol('skoX'), Add(Mul(Symbol('skoSM'), Add(Mul(Integer(-1), Rational(63, 10), Symbol('skoS2')), Rational(-61, 20))), Mul(Symbol('skoSP'), Add(Mul(Rational(63, 10), Symbol('skoS2')), Rational(13, 4))), Mul(Symbol('skoX'), Add(Mul(Integer(-1), Symbol('skoSM')), Mul(Integer(-1), Symbol('skoSP')), Integer(-4))), Rational(2, 5))), Integer(8))), Add(Mul(Symbol('skoSM'), Add(Mul(Integer(-1), Rational(63, 10), Symbol('skoS2')), Rational(-61, 20))), Mul(Symbol('skoSP'), Add(Mul(Rational(63, 10), Symbol('skoS2')), Rational(13, 4))), Rational(2, 5))))

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
		print('delta = 0')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 1')
		exit(0)
	
	
	if pre_condition_1(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_1 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 1')
		exit(0)
	
	
	if pre_condition_2(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_2 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 1/4')
		print('skoSM = 2')
		print('skoSP = 15/8')
		exit(0)
	
	
	if pre_condition_3(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_3 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 1/4')
		print('skoSM = 2')
		print('skoSP = 15/8')
		exit(0)
	
	
	if pre_condition_4(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_4 SAT")
		print('delta = 0')
		print('skoX = 26149/524288')
		print('skoS2 = 4/3')
		print('skoSM = 3')
		print('skoSP = 47/16')
		exit(0)
	
	
	if pre_condition_5(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_5 SAT")
		print('delta = 0')
		print('skoX = 26149/524288')
		print('skoS2 = 4/3')
		print('skoSM = 3')
		print('skoSP = 47/16')
		exit(0)
	
	
	if pre_condition_6(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_6 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 4')
		print('skoSM = 4')
		print('skoSP = 127/32')
		exit(0)
	
	
	if pre_condition_7(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_7 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 4')
		print('skoSM = 4')
		print('skoSP = 127/32')
		exit(0)
	
	
	if pre_condition_8(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_8 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 7')
		print('skoSM = 5')
		print('skoSP = 319/64')
		exit(0)
	
	
	if pre_condition_9(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_9 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 7')
		print('skoSM = 5')
		print('skoSP = 319/64')
		exit(0)
	
	
	if pre_condition_10(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_10 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 15')
		print('skoSM = 6')
		print('skoSP = 383/64')
		exit(0)
	
	
	if pre_condition_11(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_11 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 15')
		print('skoSM = 6')
		print('skoSP = 383/64')
		exit(0)
	
	
	if pre_condition_12(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_12 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 17')
		print('skoSM = 7')
		print('skoSP = 447/64')
		exit(0)
	
	
	if pre_condition_13(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_13 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 17')
		print('skoSM = 7')
		print('skoSP = 447/64')
		exit(0)
	
	
	if pre_condition_14(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_14 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 19')
		print('skoSM = 8')
		print('skoSP = 511/64')
		exit(0)
	
	
	if pre_condition_15(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_15 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 19')
		print('skoSM = 8')
		print('skoSP = 511/64')
		exit(0)
	
	
	if pre_condition_16(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_16 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 21')
		print('skoSM = 9')
		print('skoSP = 575/64')
		exit(0)
	
	
	if pre_condition_17(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_17 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 21')
		print('skoSM = 9')
		print('skoSP = 575/64')
		exit(0)
	
	
	if pre_condition_18(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_18 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 23')
		print('skoSM = 10')
		print('skoSP = 639/64')
		exit(0)
	
	
	if pre_condition_19(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_19 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 23')
		print('skoSM = 10')
		print('skoSP = 639/64')
		exit(0)
	
	
	if pre_condition_20(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_20 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 25')
		print('skoSM = 11')
		print('skoSP = 703/64')
		exit(0)
	
	
	if pre_condition_21(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_21 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 25')
		print('skoSM = 11')
		print('skoSP = 703/64')
		exit(0)
	
	
	if pre_condition_22(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_22 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 27')
		print('skoSM = 12')
		print('skoSP = 767/64')
		exit(0)
	
	
	if pre_condition_23(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_23 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 27')
		print('skoSM = 12')
		print('skoSP = 767/64')
		exit(0)
	
	
	if pre_condition_24(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_24 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 29')
		print('skoSM = 13')
		print('skoSP = 831/64')
		exit(0)
	
	
	if pre_condition_25(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_25 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 29')
		print('skoSM = 13')
		print('skoSP = 831/64')
		exit(0)
	
	
	if pre_condition_26(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_26 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 31')
		print('skoSM = 14')
		print('skoSP = 895/64')
		exit(0)
	
	
	if pre_condition_27(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_27 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 31')
		print('skoSM = 14')
		print('skoSP = 895/64')
		exit(0)
	
	
	if pre_condition_28(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_28 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 33')
		print('skoSM = 15')
		print('skoSP = 959/64')
		exit(0)
	
	
	if pre_condition_29(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_29 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 33')
		print('skoSM = 15')
		print('skoSP = 959/64')
		exit(0)
	
	
	if pre_condition_30(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_30 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 36')
		print('skoSM = 16')
		print('skoSP = 1023/64')
		exit(0)
	
	
	if pre_condition_31(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_31 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 36')
		print('skoSM = 16')
		print('skoSP = 1023/64')
		exit(0)
	
	
	if pre_condition_32(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_32 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 38')
		print('skoSM = 17')
		print('skoSP = 1087/64')
		exit(0)
	
	
	if pre_condition_33(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_33 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 38')
		print('skoSM = 17')
		print('skoSP = 1087/64')
		exit(0)
	
	
	if pre_condition_34(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_34 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 40')
		print('skoSM = 18')
		print('skoSP = 1151/64')
		exit(0)
	
	
	if pre_condition_35(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_35 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 40')
		print('skoSM = 18')
		print('skoSP = 1151/64')
		exit(0)
	
	
	if pre_condition_36(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_36 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 42')
		print('skoSM = 19')
		print('skoSP = 1215/64')
		exit(0)
	
	
	if pre_condition_37(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_37 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 42')
		print('skoSM = 19')
		print('skoSP = 1215/64')
		exit(0)
	
	
	if pre_condition_38(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_38 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 44')
		print('skoSM = 20')
		print('skoSP = 1279/64')
		exit(0)
	
	
	if pre_condition_39(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_39 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 44')
		print('skoSM = 20')
		print('skoSP = 1279/64')
		exit(0)
	
	
	if pre_condition_40(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_40 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 46')
		print('skoSM = 21')
		print('skoSP = 1343/64')
		exit(0)
	
	
	if pre_condition_41(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_41 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 46')
		print('skoSM = 21')
		print('skoSP = 1343/64')
		exit(0)
	
	
	if pre_condition_42(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_42 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 48')
		print('skoSM = 22')
		print('skoSP = 1407/64')
		exit(0)
	
	
	if pre_condition_43(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_43 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 48')
		print('skoSM = 22')
		print('skoSP = 1407/64')
		exit(0)
	
	
	if pre_condition_44(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_44 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 50')
		print('skoSM = 23')
		print('skoSP = 1471/64')
		exit(0)
	
	
	if pre_condition_45(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_45 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 50')
		print('skoSM = 23')
		print('skoSP = 1471/64')
		exit(0)
	
	
	if pre_condition_46(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_46 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 52')
		print('skoSM = 24')
		print('skoSP = 1535/64')
		exit(0)
	
	
	if pre_condition_47(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_47 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 52')
		print('skoSM = 24')
		print('skoSP = 1535/64')
		exit(0)
	
	
	if pre_condition_48(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_48 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 54')
		print('skoSM = 25')
		print('skoSP = 1599/64')
		exit(0)
	
	
	if pre_condition_49(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_49 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 54')
		print('skoSM = 25')
		print('skoSP = 1599/64')
		exit(0)
	
	
	if pre_condition_50(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_50 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 56')
		print('skoSM = 26')
		print('skoSP = 1663/64')
		exit(0)
	
	
	if pre_condition_51(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_51 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 56')
		print('skoSM = 26')
		print('skoSP = 1663/64')
		exit(0)
	
	
	if pre_condition_52(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_52 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 58')
		print('skoSM = 27')
		print('skoSP = 1727/64')
		exit(0)
	
	
	if pre_condition_53(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_53 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 58')
		print('skoSM = 27')
		print('skoSP = 1727/64')
		exit(0)
	
	
	if pre_condition_54(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_54 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 60')
		print('skoSM = 28')
		print('skoSP = 1791/64')
		exit(0)
	
	
	if pre_condition_55(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_55 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 60')
		print('skoSM = 28')
		print('skoSP = 1791/64')
		exit(0)
	
	
	if pre_condition_56(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_56 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 62')
		print('skoSM = 29')
		print('skoSP = 1855/64')
		exit(0)
	
	
	if pre_condition_57(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_57 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 62')
		print('skoSM = 29')
		print('skoSP = 1855/64')
		exit(0)
	
	
	if pre_condition_58(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_58 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 64')
		print('skoSM = 30')
		print('skoSP = 1919/64')
		exit(0)
	
	
	if pre_condition_59(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_59 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 64')
		print('skoSM = 30')
		print('skoSP = 1919/64')
		exit(0)
	
	
	if pre_condition_60(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_60 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 66')
		print('skoSM = 31')
		print('skoSP = 1983/64')
		exit(0)
	
	
	if pre_condition_61(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_61 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 66')
		print('skoSM = 31')
		print('skoSP = 1983/64')
		exit(0)
	
	
	if pre_condition_62(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_62 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 68')
		print('skoSM = 32')
		print('skoSP = 2047/64')
		exit(0)
	
	
	if pre_condition_63(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_63 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 68')
		print('skoSM = 32')
		print('skoSP = 2047/64')
		exit(0)
	
	
	if pre_condition_64(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_64 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 70')
		print('skoSM = 33')
		print('skoSP = 2111/64')
		exit(0)
	
	
	if pre_condition_65(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_65 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 70')
		print('skoSM = 33')
		print('skoSP = 2111/64')
		exit(0)
	
	
	if pre_condition_66(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_66 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 72')
		print('skoSM = 34')
		print('skoSP = 2175/64')
		exit(0)
	
	
	if pre_condition_67(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_67 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 72')
		print('skoSM = 34')
		print('skoSP = 2175/64')
		exit(0)
	
	
	if pre_condition_68(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_68 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 74')
		print('skoSM = 35')
		print('skoSP = 2239/64')
		exit(0)
	
	
	if pre_condition_69(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_69 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 74')
		print('skoSM = 35')
		print('skoSP = 2239/64')
		exit(0)
	
	
	if pre_condition_70(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_70 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 76')
		print('skoSM = 36')
		print('skoSP = 2303/64')
		exit(0)
	
	
	if pre_condition_71(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_71 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 76')
		print('skoSM = 36')
		print('skoSP = 2303/64')
		exit(0)
	
	
	if pre_condition_72(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_72 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 78')
		print('skoSM = 37')
		print('skoSP = 2367/64')
		exit(0)
	
	
	if pre_condition_73(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_73 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 78')
		print('skoSM = 37')
		print('skoSP = 2367/64')
		exit(0)
	
	
	if pre_condition_74(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_74 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 80')
		print('skoSM = 38')
		print('skoSP = 2431/64')
		exit(0)
	
	
	if pre_condition_75(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_75 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 80')
		print('skoSM = 38')
		print('skoSP = 2431/64')
		exit(0)
	
	
	if pre_condition_76(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_76 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 82')
		print('skoSM = 39')
		print('skoSP = 2495/64')
		exit(0)
	
	
	if pre_condition_77(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_77 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 82')
		print('skoSM = 39')
		print('skoSP = 2495/64')
		exit(0)
	
	
	if pre_condition_78(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_78 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 84')
		print('skoSM = 40')
		print('skoSP = 2559/64')
		exit(0)
	
	
	if pre_condition_79(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_79 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 84')
		print('skoSM = 40')
		print('skoSP = 2559/64')
		exit(0)
	
	
	if pre_condition_80(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_80 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 86')
		print('skoSM = 41')
		print('skoSP = 2623/64')
		exit(0)
	
	
	if pre_condition_81(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_81 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 86')
		print('skoSM = 41')
		print('skoSP = 2623/64')
		exit(0)
	
	
	if pre_condition_82(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_82 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 88')
		print('skoSM = 42')
		print('skoSP = 2687/64')
		exit(0)
	
	
	if pre_condition_83(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_83 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 88')
		print('skoSM = 42')
		print('skoSP = 2687/64')
		exit(0)
	
	
	if pre_condition_84(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_84 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 90')
		print('skoSM = 43')
		print('skoSP = 2751/64')
		exit(0)
	
	
	if pre_condition_85(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_85 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 90')
		print('skoSM = 43')
		print('skoSP = 2751/64')
		exit(0)
	
	
	if pre_condition_86(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_86 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 92')
		print('skoSM = 44')
		print('skoSP = 2815/64')
		exit(0)
	
	
	if pre_condition_87(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_87 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 92')
		print('skoSM = 44')
		print('skoSP = 2815/64')
		exit(0)
	
	
	if pre_condition_88(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_88 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 94')
		print('skoSM = 45')
		print('skoSP = 2879/64')
		exit(0)
	
	
	if pre_condition_89(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_89 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 94')
		print('skoSM = 45')
		print('skoSP = 2879/64')
		exit(0)
	
	
	if pre_condition_90(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_90 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 96')
		print('skoSM = 46')
		print('skoSP = 2943/64')
		exit(0)
	
	
	if pre_condition_91(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_91 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 96')
		print('skoSM = 46')
		print('skoSP = 2943/64')
		exit(0)
	
	
	if pre_condition_92(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_92 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 99')
		print('skoSM = 47')
		print('skoSP = 3007/64')
		exit(0)
	
	
	if pre_condition_93(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_93 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 99')
		print('skoSM = 47')
		print('skoSP = 3007/64')
		exit(0)
	
	
	if pre_condition_94(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_94 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 101')
		print('skoSM = 48')
		print('skoSP = 3071/64')
		exit(0)
	
	
	if pre_condition_95(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_95 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 101')
		print('skoSM = 48')
		print('skoSP = 3071/64')
		exit(0)
	
	
	if pre_condition_96(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_96 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 103')
		print('skoSM = 49')
		print('skoSP = 3135/64')
		exit(0)
	
	
	if pre_condition_97(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_97 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 103')
		print('skoSM = 49')
		print('skoSP = 3135/64')
		exit(0)
	
	
	if pre_condition_98(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_98 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 105')
		print('skoSM = 50')
		print('skoSP = 3199/64')
		exit(0)
	
	
	if pre_condition_99(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_99 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 105')
		print('skoSM = 50')
		print('skoSP = 3199/64')
		exit(0)
	
	
	if pre_condition_100(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_100 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 107')
		print('skoSM = 51')
		print('skoSP = 3263/64')
		exit(0)
	
	
	if pre_condition_101(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_101 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 107')
		print('skoSM = 51')
		print('skoSP = 3263/64')
		exit(0)
	
	
	if pre_condition_102(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_102 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 109')
		print('skoSM = 52')
		print('skoSP = 3327/64')
		exit(0)
	
	
	if pre_condition_103(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_103 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 109')
		print('skoSM = 52')
		print('skoSP = 3327/64')
		exit(0)
	
	
	if pre_condition_104(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_104 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 111')
		print('skoSM = 53')
		print('skoSP = 3391/64')
		exit(0)
	
	
	if pre_condition_105(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_105 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 111')
		print('skoSM = 53')
		print('skoSP = 3391/64')
		exit(0)
	
	
	if pre_condition_106(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_106 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 113')
		print('skoSM = 54')
		print('skoSP = 3455/64')
		exit(0)
	
	
	if pre_condition_107(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_107 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 113')
		print('skoSM = 54')
		print('skoSP = 3455/64')
		exit(0)
	
	
	if pre_condition_108(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_108 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 115')
		print('skoSM = 55')
		print('skoSP = 3519/64')
		exit(0)
	
	
	if pre_condition_109(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_109 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 115')
		print('skoSM = 55')
		print('skoSP = 3519/64')
		exit(0)
	
	
	if pre_condition_110(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_110 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 117')
		print('skoSM = 56')
		print('skoSP = 3583/64')
		exit(0)
	
	
	if pre_condition_111(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_111 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 117')
		print('skoSM = 56')
		print('skoSP = 3583/64')
		exit(0)
	
	
	if pre_condition_112(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_112 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 119')
		print('skoSM = 57')
		print('skoSP = 3647/64')
		exit(0)
	
	
	if pre_condition_113(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_113 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 119')
		print('skoSM = 57')
		print('skoSP = 3647/64')
		exit(0)
	
	
	if pre_condition_114(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_114 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 121')
		print('skoSM = 58')
		print('skoSP = 3711/64')
		exit(0)
	
	
	if pre_condition_115(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_115 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 121')
		print('skoSM = 58')
		print('skoSP = 3711/64')
		exit(0)
	
	
	if pre_condition_116(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_116 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 123')
		print('skoSM = 59')
		print('skoSP = 3775/64')
		exit(0)
	
	
	if pre_condition_117(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_117 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 123')
		print('skoSM = 59')
		print('skoSP = 3775/64')
		exit(0)
	
	
	if pre_condition_118(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_118 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 125')
		print('skoSM = 60')
		print('skoSP = 3839/64')
		exit(0)
	
	
	if pre_condition_119(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_119 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 125')
		print('skoSM = 60')
		print('skoSP = 3839/64')
		exit(0)
	
	
	if pre_condition_120(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_120 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 127')
		print('skoSM = 61')
		print('skoSP = 3903/64')
		exit(0)
	
	
	if pre_condition_121(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_121 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 127')
		print('skoSM = 61')
		print('skoSP = 3903/64')
		exit(0)
	
	
	if pre_condition_122(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_122 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 129')
		print('skoSM = 62')
		print('skoSP = 3967/64')
		exit(0)
	
	
	if pre_condition_123(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_123 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 129')
		print('skoSM = 62')
		print('skoSP = 3967/64')
		exit(0)
	
	
	if pre_condition_124(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_124 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 131')
		print('skoSM = 63')
		print('skoSP = 4031/64')
		exit(0)
	
	
	if pre_condition_125(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_125 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 131')
		print('skoSM = 63')
		print('skoSP = 4031/64')
		exit(0)
	
	
	if pre_condition_126(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_126 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 133')
		print('skoSM = 64')
		print('skoSP = 4095/64')
		exit(0)
	
	
	if pre_condition_127(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_127 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 133')
		print('skoSM = 64')
		print('skoSP = 4095/64')
		exit(0)
	
	
	if pre_condition_128(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_128 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 135')
		print('skoSM = 65')
		print('skoSP = 4159/64')
		exit(0)
	
	
	if pre_condition_129(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_129 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 135')
		print('skoSM = 65')
		print('skoSP = 4159/64')
		exit(0)
	
	
	if pre_condition_130(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_130 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 137')
		print('skoSM = 66')
		print('skoSP = 4223/64')
		exit(0)
	
	
	if pre_condition_131(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_131 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 137')
		print('skoSM = 66')
		print('skoSP = 4223/64')
		exit(0)
	
	
	if pre_condition_132(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_132 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 139')
		print('skoSM = 67')
		print('skoSP = 4287/64')
		exit(0)
	
	
	if pre_condition_133(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_133 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 139')
		print('skoSM = 67')
		print('skoSP = 4287/64')
		exit(0)
	
	
	if pre_condition_134(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_134 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 141')
		print('skoSM = 68')
		print('skoSP = 4351/64')
		exit(0)
	
	
	if pre_condition_135(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_135 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 141')
		print('skoSM = 68')
		print('skoSP = 4351/64')
		exit(0)
	
	
	if pre_condition_136(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_136 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 143')
		print('skoSM = 69')
		print('skoSP = 4415/64')
		exit(0)
	
	
	if pre_condition_137(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_137 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 143')
		print('skoSM = 69')
		print('skoSP = 4415/64')
		exit(0)
	
	
	if pre_condition_138(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_138 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 145')
		print('skoSM = 70')
		print('skoSP = 4479/64')
		exit(0)
	
	
	if pre_condition_139(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_139 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 145')
		print('skoSM = 70')
		print('skoSP = 4479/64')
		exit(0)


	print("UNKNOWN")
	exit(0)
